// --- Passport Photo Tool ---
// MediaPipe Face Detection — lag-free, GPU-accelerated
// Vietnam passport 4x6cm standard overlay guide
// Supports: auto-capture (self) + friend-capture mode

// ==========================================
// DOM REFERENCES (all in one place)
// ==========================================
const videoElement = document.getElementById('videoElement');
const canvasElement = document.getElementById('canvasElement');
const statusText = document.getElementById('status-text');
const guideFrame = document.getElementById('guide-frame');
const guideOval = document.getElementById('guide-oval');
const countdownElement = document.getElementById('countdown-overlay');
const countdownNumber = document.getElementById('countdown-number');
const btnCapture = document.getElementById('btn-capture');
const captureHint = document.getElementById('capture-hint');
const previewImage = document.getElementById('preview-image');
const confirmationImage = document.getElementById('confirmation-image');

// Views
const onboardingView = document.getElementById('onboarding-view');
const cameraView = document.getElementById('camera-view');
const previewView = document.getElementById('preview-view');
const confirmationView = document.getElementById('confirmation-view');
const registerView = document.getElementById('register-view');
const successView = document.getElementById('success-view');

// Buttons
const btnStart = document.getElementById('btn-start');
const modeSelf = document.getElementById('mode-self');
const modeFriend = document.getElementById('mode-friend');
const btnBackOnboarding = document.getElementById('btn-back-onboarding');
const btnRetake = document.getElementById('btn-retake');
const btnAccept = document.getElementById('btn-accept');
const btnDownload = document.getElementById('btn-download');
const btnDownloadFinal = document.getElementById('btn-download-final');
const btnGoRegister = document.getElementById('btn-go-register');
const btnBackRegister = document.getElementById('btn-back-register');

// ==========================================
// STATE
// ==========================================
let faceDetector = null;
let isModelLoaded = false;
let stream = null;
let animationFrameId = null;
let lastDetectionTime = 0;
const DETECTION_INTERVAL_MS = 200;

let consecutivePerfectFrames = 0;
const PERFECT_FRAMES_THRESHOLD = 8;

let cameraMode = 'self'; // 'self' or 'friend'
let countdownTimer = null;
let isCapturing = false;
let finalImageDataUrl = null;

// ==========================================
// LOAD MEDIAPIPE (dynamic, non-blocking)
// ==========================================
async function loadModels() {
    statusText.textContent = "Khởi động Trí tuệ AI...";
    try {
        const visionModule = await import(
            'https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.22/vision_bundle.mjs'
        );
        const { FilesetResolver, FaceDetector } = visionModule;

        const vision = await FilesetResolver.forVisionTasks(
            'https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.22/wasm'
        );
        faceDetector = await FaceDetector.createFromOptions(vision, {
            baseOptions: {
                modelAssetPath: 'https://storage.googleapis.com/mediapipe-models/face_detector/blaze_face_short_range/float16/1/blaze_face_short_range.tflite',
                delegate: 'GPU'
            },
            runningMode: 'VIDEO',
            minDetectionConfidence: 0.5
        });

        isModelLoaded = true;
        statusText.textContent = "AI Đã Sẵn Sàng";
        console.log("✅ MediaPipe Face Detector loaded");
    } catch (err) {
        console.error("❌ Error loading MediaPipe:", err);
        statusText.textContent = "Khởi động AI thất bại. Bạn có thể tự bấm nút chụp.";
        btnCapture.disabled = false;
    }
}

// ==========================================
// VIEW NAVIGATION
// ==========================================
function switchView(fromView, toView) {
    if (!fromView || !toView) return;

    // Fade out current view
    fromView.style.opacity = '0';
    fromView.style.pointerEvents = 'none';

    setTimeout(() => {
        // Hide old view
        fromView.classList.add('hidden');
        fromView.style.opacity = '';
        fromView.style.pointerEvents = '';

        // Show new view
        toView.style.opacity = '0';
        toView.classList.remove('hidden');
        // Force reflow for transition
        void toView.offsetWidth;
        toView.style.opacity = '1';
    }, 300);
}

// ==========================================
// CAMERA LOGIC
// ==========================================
async function startCamera() {
    try {
        stream = await navigator.mediaDevices.getUserMedia({
            video: {
                facingMode: "user",
                width: { ideal: 720 },
                height: { ideal: 1280 }
            },
            audio: false
        });
        videoElement.srcObject = stream;
        return new Promise((resolve) => {
            videoElement.onloadedmetadata = () => resolve();
        });
    } catch (err) {
        console.error("Camera error:", err);
        alert("Vui lòng cấp quyền Camera trong cài đặt trình duyệt để sử dụng tính năng này.");
        switchView(cameraView, onboardingView);
        throw err;
    }
}

function stopCamera() {
    if (stream) {
        stream.getTracks().forEach(track => track.stop());
        stream = null;
    }
    if (animationFrameId) {
        cancelAnimationFrame(animationFrameId);
        animationFrameId = null;
    }
    if (countdownTimer) {
        clearInterval(countdownTimer);
        countdownTimer = null;
    }
    videoElement.srcObject = null;
}

// ==========================================
// FACE DETECTION LOOP (rAF + Throttle)
// ==========================================
function startFaceDetection() {
    if (!isModelLoaded || !faceDetector) {
        btnCapture.disabled = false;
        statusText.textContent = "AI chưa sẵn sàng — Vui lòng tự bấm nút chụp";
        return;
    }

    statusText.textContent = "Đang quét tìm khuôn mặt...";
    if (cameraMode === 'self') {
        btnCapture.disabled = true;
    }

    function detectLoop() {
        if (videoElement.paused || videoElement.ended || !stream) return;

        const now = performance.now();
        if (now - lastDetectionTime >= DETECTION_INTERVAL_MS) {
            lastDetectionTime = now;
            try {
                const result = faceDetector.detectForVideo(videoElement, now);
                processDetectionResult(result);
            } catch (err) {
                // skip frame
            }
        }

        animationFrameId = requestAnimationFrame(detectLoop);
    }

    animationFrameId = requestAnimationFrame(detectLoop);
}

// ==========================================
// PROCESS DETECTION RESULTS
// ==========================================
function processDetectionResult(result) {
    if (!result || !result.detections || result.detections.length === 0) {
        setGuideState('error', 'Chưa nhận diện được khuôn mặt');
        if (cameraMode === 'self') btnCapture.disabled = true;
        consecutivePerfectFrames = 0;
        btnCapture.classList.remove('shutter-auto-taking');
        return;
    }

    const detection = result.detections[0];
    const bbox = detection.boundingBox;
    if (cameraMode === 'self') btnCapture.disabled = false;

    const videoWidth = videoElement.videoWidth;
    const videoHeight = videoElement.videoHeight;

    const faceWidthRatio = bbox.width / videoWidth;
    const isRightSize = faceWidthRatio > 0.22 && faceWidthRatio < 0.70;

    const faceCenterX = videoWidth - (bbox.originX + bbox.width / 2);
    const isCenteredX = Math.abs(faceCenterX - videoWidth / 2) < videoWidth * 0.15;

    const faceCenterY = bbox.originY + bbox.height / 2;
    const targetCenterY = videoHeight * 0.40;
    const isCenteredY = Math.abs(faceCenterY - targetCenterY) < videoHeight * 0.15;

    if (!isRightSize) {
        const hint = faceWidthRatio < 0.22 ? '🔍 Di chuyển lại gần camera hơn' : '🔍 Lùi ra xa camera một chút';
        setGuideState('warning', hint);
        consecutivePerfectFrames = 0;
        btnCapture.classList.remove('shutter-auto-taking');
    } else if (!isCenteredX || !isCenteredY) {
        let hint = '↔️ Hãy di chuyển mặt nhẹ ';
        if (!isCenteredY && faceCenterY < targetCenterY) hint += 'xuống dưới';
        else if (!isCenteredY) hint += 'lên trên';
        else if (!isCenteredX && faceCenterX < videoWidth / 2) hint += 'sang phải';
        else hint += 'sang trái';
        setGuideState('warning', hint);
        consecutivePerfectFrames = 0;
        btnCapture.classList.remove('shutter-auto-taking');
    } else {
        setGuideState('success', '✨ Hoàn hảo! Xin giữ nguyên tư thế...');
        consecutivePerfectFrames++;

        if (cameraMode === 'self' && consecutivePerfectFrames > PERFECT_FRAMES_THRESHOLD) {
            btnCapture.classList.add('shutter-auto-taking');
            if (animationFrameId) {
                cancelAnimationFrame(animationFrameId);
                animationFrameId = null;
            }
            setTimeout(() => takePhoto(), 500);
        }
    }
}

function setGuideState(stateClass, message) {
    guideFrame.className = 'guide-frame state-' + stateClass;
    guideOval.className = 'guide-oval state-' + stateClass;
    statusText.textContent = message;
}

// ==========================================
// COUNTDOWN (Friend Mode)
// ==========================================
function startCountdown() {
    let cdValue = 3;
    countdownElement.classList.add('active');
    countdownNumber.textContent = cdValue;

    countdownTimer = setInterval(() => {
        cdValue--;
        if (cdValue > 0) {
            countdownNumber.textContent = cdValue;
            countdownNumber.classList.add('pulse');
            setTimeout(() => countdownNumber.classList.remove('pulse'), 200);
        } else {
            clearInterval(countdownTimer);
            countdownTimer = null;
            countdownElement.classList.remove('active');
            takePhoto();
        }
    }, 1000);
}

// ==========================================
// CAPTURE & CROP
// ==========================================
function takePhoto() {
    btnCapture.classList.remove('shutter-auto-taking');

    const ctx = canvasElement.getContext('2d');
    const cw = 400;
    const ch = 600;
    canvasElement.width = cw;
    canvasElement.height = ch;

    const vw = videoElement.videoWidth;
    const vh = videoElement.videoHeight;

    ctx.translate(cw, 0);
    ctx.scale(-1, 1);

    const scale = ch / vh;
    const drawW = vw * scale;
    const offsetX = (drawW - cw) / 2;

    ctx.drawImage(videoElement, -offsetX, 0, drawW, ch);

    finalImageDataUrl = canvasElement.toDataURL('image/jpeg', 0.92);
    previewImage.src = finalImageDataUrl;

    stopCamera();
    switchView(cameraView, previewView);
}

// ==========================================
// MODE TOGGLE
// ==========================================
function setMode(mode) {
    cameraMode = mode;
    modeSelf.classList.toggle('active', mode === 'self');
    modeFriend.classList.toggle('active', mode === 'friend');

    if (mode === 'friend') {
        btnCapture.disabled = false;
        captureHint.textContent = 'Nhờ người thân bấm nút chụp giúp bạn';
    } else {
        captureHint.textContent = '✨ Trí tuệ AI sẽ tự động chụp khi góc mặt chuẩn xác nhất';
    }
}

// ==========================================
// EVENT LISTENERS
// ==========================================

// Start camera (from onboarding)
btnStart.addEventListener('click', async () => {
    switchView(onboardingView, cameraView);
    await startCamera();
    startFaceDetection();
});

// Mode toggles (within camera view)
modeSelf.addEventListener('click', () => setMode('self'));
modeFriend.addEventListener('click', () => setMode('friend'));

// Back to onboarding from camera
btnBackOnboarding.addEventListener('click', () => {
    stopCamera();
    switchView(cameraView, onboardingView);
});

// Capture button
btnCapture.addEventListener('click', () => {
    if (cameraMode === 'friend') {
        startCountdown();
    } else {
        if (animationFrameId) {
            cancelAnimationFrame(animationFrameId);
            animationFrameId = null;
        }
        takePhoto();
    }
});

// Retake — go back to camera
btnRetake.addEventListener('click', async () => {
    switchView(previewView, cameraView);
    consecutivePerfectFrames = 0;
    guideFrame.className = 'guide-frame state-default';
    guideOval.className = 'guide-oval state-default';
    statusText.textContent = 'Đang kết nối Camera...';
    await startCamera();
    startFaceDetection();
});

// Accept photo → confirmation
btnAccept.addEventListener('click', () => {
    confirmationImage.src = previewImage.src;
    switchView(previewView, confirmationView);
});

// Download from preview
btnDownload.addEventListener('click', () => {
    const link = document.createElement('a');
    link.download = 'passport-photo.jpg';
    link.href = previewImage.src;
    link.click();
});

// Download from confirmation
btnDownloadFinal.addEventListener('click', () => {
    const link = document.createElement('a');
    link.download = 'passport-photo.jpg';
    link.href = confirmationImage.src;
    link.click();
});

// --- Register Form Wiring ---
const passportForm = document.getElementById('passportRegisterForm');

if (btnGoRegister) {
    btnGoRegister.addEventListener('click', () => {
        // Transfer photo data to hidden inputs
        const regImageData = document.getElementById('regImageData');
        const regHasPhoto = document.getElementById('regHasPhoto');
        if (regImageData && finalImageDataUrl) {
            regImageData.value = '';
            if (regHasPhoto) regHasPhoto.value = 'Có';
        }

        switchView(confirmationView, registerView);

        // Scroll to top of register view
        const regContent = registerView.querySelector('.register-content');
        if (regContent) regContent.scrollTop = 0;
    });
}

// Back from register → confirmation
if (btnBackRegister) {
    btnBackRegister.addEventListener('click', () => {
        switchView(registerView, confirmationView);
    });
}

// Form submission success → show success view
if (passportForm) {
    passportForm.addEventListener('form:success', () => {
        const name = document.getElementById('regName')?.value || '';
        const service = document.getElementById('regService')?.selectedOptions[0]?.text || '';
        const urgency = document.getElementById('regUrgency')?.selectedOptions[0]?.text || '';
        const phone = document.getElementById('regPhone')?.value || '';

        const ticketId = 'HCG-' + Date.now().toString(36).toUpperCase();

        const ticketContainer = successView.querySelector('.success-ticket');
        if (ticketContainer) {
            ticketContainer.innerHTML = `
                <div class="ticket-row"><span class="label">Mã đơn:</span><strong>${ticketId}</strong></div>
                <div class="ticket-row"><span class="label">Họ tên:</span><span>${name}</span></div>
                <div class="ticket-row"><span class="label">SĐT:</span><span>${phone}</span></div>
                <div class="ticket-row"><span class="label">Dịch vụ:</span><span>${service}</span></div>
                <div class="ticket-row"><span class="label">Mức độ gấp:</span><span class="color-success">${urgency}</span></div>
                <div class="ticket-row"><span class="label">Có ảnh:</span><span class="color-success">✅ Có</span></div>
            `;
        }

        switchView(registerView, successView);
    });
}

// --- Init (non-blocking) ---
loadModels();
