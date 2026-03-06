// --- Passport Photo Tool ---
// MediaPipe Face Detection — lag-free, GPU-accelerated
// Vietnam passport 4x6cm standard overlay guide
// Supports: auto-capture (self) + friend-capture mode

// --- Configurations & State ---
let faceDetector = null;
let isModelLoaded = false;
let stream = null;
let animationFrameId = null;
let lastDetectionTime = 0;
const DETECTION_INTERVAL_MS = 200;

let consecutivePerfectFrames = 0;
const PERFECT_FRAMES_THRESHOLD = 8;

let captureMode = 'self';
let countdownTimer = null;
let countdownValue = 0;
let isCapturing = false;
let finalImageDataUrl = null; // Lưu ảnh cuối cùng

// --- Load MediaPipe (dynamic import, non-blocking) ---
async function loadModels() {
    statusText.textContent = "Đang tải công cụ AI...";
    // Assuming aiLoader is replaced by statusText or a new element
    // UI.aiLoader.classList.add('active'); // Removed as aiLoader is not in new UI
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
        statusText.textContent = "Sẵn sàng";
        // UI.aiLoader.classList.remove('active'); // Removed
        console.log("✅ MediaPipe Face Detector loaded");
    } catch (err) {
        console.error("❌ Error loading MediaPipe:", err);
        statusText.textContent = "Lỗi tải AI. Bạn vẫn có thể chụp bằng tay.";
        // UI.aiLoader.classList.remove('active'); // Removed
        btnCapture.disabled = false;
    }
}

// --- View Navigation ---
// Đổi view helper mượt mà hơn với GSAP (ưu tiên CSS transitions, fallback bằng DOM manipulation)
function switchView(fromView, toViewAction) {
    // Animation CSS thông qua classes (ẩn dần)
    fromView.style.opacity = '0';

    setTimeout(() => {
        fromView.classList.add('hidden');

        // Xử lý custom actions cho view mới trước khi hiển thị
        if (typeof toViewAction === 'function') {
            toViewAction();
        } else if (toViewAction instanceof HTMLElement) {
            // Nếu chỉ truyền node
            toViewAction.classList.remove('hidden');
            // Force reflow
            void toViewAction.offsetWidth;
            toViewAction.style.opacity = '1';
        }
    }, 300); // 300ms khớp CSS transition (nếu có)
}

// --- Camera Logic ---
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
        alert("Không thể truy cập camera. Vui lòng cấp quyền trong cài đặt trình duyệt.");
        switchView(cameraView, onboardingView); // Adjusted to new switchView
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

// --- Face Detection Loop (rAF + Throttle) ---
function startFaceDetection() {
    if (!isModelLoaded || !faceDetector) {
        // AI not loaded yet — enable manual capture
        btnCapture.disabled = false;
        statusText.textContent = "AI chưa sẵn sàng — chụp bằng tay";
        return;
    }

    statusText.textContent = "Đang tìm khuôn mặt...";
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

// --- Process Detection Results ---
function processDetectionResult(result) {
    if (!result || !result.detections || result.detections.length === 0) {
        setGuideState('error', 'Chưa tìm thấy khuôn mặt');
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
        const hint = faceWidthRatio < 0.22 ? '📏 Lại gần hơn' : '📏 Lùi xa hơn';
        setGuideState('warning', hint);
        consecutivePerfectFrames = 0;
        btnCapture.classList.remove('shutter-auto-taking');
    } else if (!isCenteredX || !isCenteredY) {
        let hint = '↔️ Đưa mặt ';
        if (!isCenteredY && faceCenterY < targetCenterY) hint += 'xuống thấp hơn';
        else if (!isCenteredY) hint += 'lên cao hơn';
        else if (!isCenteredX && faceCenterX < videoWidth / 2) hint += 'sang phải';
        else hint += 'sang trái';
        setGuideState('warning', hint);
        consecutivePerfectFrames = 0;
        btnCapture.classList.remove('shutter-auto-taking');
    } else {
        setGuideState('success', '✅ Tuyệt vời! Giữ yên...');
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

// --- Countdown (Friend Mode) ---
function startCountdown() {
    let countdownValue = 3; // Renamed to avoid conflict with global countdownValue
    countdownElement.classList.add('active');
    countdownNumber.textContent = countdownValue;

    countdownTimer = setInterval(() => {
        countdownValue--;
        if (countdownValue > 0) {
            countdownNumber.textContent = countdownValue;
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

// --- Capture & Crop ---
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

    finalImageDataUrl = canvasElement.toDataURL('image/jpeg', 0.92); // Store in finalImageDataUrl
    previewImage.src = finalImageDataUrl;

    stopCamera();
    switchView(cameraView, previewView); // Adjusted to new switchView
}

// --- Mode Toggle ---
function setMode(mode) {
    cameraMode = mode; // Renamed captureMode to cameraMode
    btnStartCamera.classList.toggle('active', mode === 'self'); // Assuming btnStartCamera is 'mode-self'
    btnStartFriendCamera.classList.toggle('active', mode === 'friend'); // Assuming btnStartFriendCamera is 'mode-friend'

    if (mode === 'friend') {
        btnCapture.disabled = false;
        instructionOverlay.textContent = 'Nhờ người khác bấm nút chụp giùm';
    } else {
        instructionOverlay.textContent = 'Hệ thống sẽ tự chụp khi hoàn hảo';
    }
}

// ==========================================
// EVENT LISTENERS (always attached, never blocked)
// ==========================================

// Replaced UI.btnStart with btnStartCamera and btnStartFriendCamera
btnStartCamera.addEventListener('click', async () => {
    setMode('self'); // Set mode explicitly
    switchView(onboardingView, cameraView); // Adjusted to new switchView
    await startCamera();
    startFaceDetection();
});

btnStartFriendCamera.addEventListener('click', async () => {
    setMode('friend'); // Set mode explicitly
    switchView(onboardingView, cameraView); // Adjusted to new switchView
    await startCamera();
    startFaceDetection();
});

// Replaced UI.btnBackOnboarding with a new back button if needed, or removed if flow changed.
// Assuming the new flow doesn't have a direct "back to onboarding" from camera view.
// If needed, a new button would be required.

btnCapture.addEventListener('click', () => {
    if (cameraMode === 'friend') { // Renamed captureMode to cameraMode
        startCountdown();
    } else {
        if (animationFrameId) {
            cancelAnimationFrame(animationFrameId);
            animationFrameId = null;
        }
        takePhoto();
    }
});

UI.btnRetake.addEventListener('click', async () => {
    switchView('camera');
    consecutivePerfectFrames = 0;
    UI.guideFrame.className = 'guide-frame state-default';
    UI.guideOval.className = 'guide-oval state-default';
    UI.statusText.textContent = 'Đang tải Camera...';
    await startCamera();
    startFaceDetection();
});

UI.btnAccept.addEventListener('click', () => {
    // Transfer image to confirmation view
    UI.confirmationImage.src = UI.previewImage.src;
    switchView('confirmation');
});

UI.btnDownload.addEventListener('click', () => {
    const link = document.createElement('a');
    link.download = 'passport-photo.jpg';
    link.href = UI.previewImage.src;
    link.click();
});

UI.btnDownloadFinal.addEventListener('click', () => {
    const link = document.createElement('a');
    link.download = 'passport-photo.jpg';
    link.href = UI.confirmationImage.src;
    link.click();
});

UI.modeSelf.addEventListener('click', () => setMode('self'));
UI.modeFriend.addEventListener('click', () => setMode('friend'));

// --- Register Form Wiring ---
const btnGoRegister = document.getElementById('btn-go-register');
const registerView = document.getElementById('register-view');
const confirmationView = document.getElementById('confirmation-view');
const passportForm = document.getElementById('passportRegisterForm');
const successView = document.getElementById('success-view');

if (btnGoRegister) {
    btnGoRegister.addEventListener('click', () => {
        // Transfer photo data to hidden inputs
        const regImageData = document.getElementById('regImageData');
        const regHasPhoto = document.getElementById('regHasPhoto');
        if (regImageData && finalImageDataUrl) {
            // Don't send base64 to Google Sheet (too large), just flag
            regImageData.value = ''; // Clear — photo stays local
            if (regHasPhoto) regHasPhoto.value = 'Có';
        }

        // Switch: confirmation → register
        confirmationView.classList.add('hidden');
        registerView.classList.remove('hidden');
        registerView.style.opacity = '1';

        // Scroll to top of register view
        const regContent = registerView.querySelector('.register-content');
        if (regContent) regContent.scrollTop = 0;
    });
}

// Back from register → confirmation
const btnBackRegister = document.getElementById('btn-back-register');
if (btnBackRegister) {
    btnBackRegister.addEventListener('click', () => {
        registerView.classList.add('hidden');
        confirmationView.classList.remove('hidden');
        confirmationView.style.opacity = '1';
    });
}

// Form submission success → show success view
if (passportForm) {
    passportForm.addEventListener('form:success', () => {
        // Hide register view, show success view
        registerView.classList.add('hidden');
        if (successView) {
            // Populate success ticket info from form data
            const name = document.getElementById('regName')?.value || '';
            const service = document.getElementById('regService')?.selectedOptions[0]?.text || '';
            const urgency = document.getElementById('regUrgency')?.selectedOptions[0]?.text || '';
            const phone = document.getElementById('regPhone')?.value || '';

            // Generate ticket ID (timestamp-based)
            const ticketId = 'HCG-' + Date.now().toString(36).toUpperCase();

            // Fill ticket rows if they exist
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

            successView.classList.remove('hidden');
            successView.style.opacity = '1';
        }
    });
}

// --- Init (non-blocking) ---
loadModels();
