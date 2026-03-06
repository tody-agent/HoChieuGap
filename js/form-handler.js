/**
 * Form Submission Handler — Google Sheet Integration
 * Auto Retry + Toast UI + Fallback Contact
 * 
 * Shared across: passport-photo register form + landing page contact form
 */

// ═══════════════════════════════════════
// CONFIGURATION
// ═══════════════════════════════════════
const FORM_CONFIG = {
    URLS: {
        // Deploy Apps Script → paste URL here per form type
        // passport: 'https://script.google.com/macros/s/AKfycbz1EfVGj6a10iwdIUTgs1JOynCcnXfpcYW-y1EeG5h2IMFHQuhobyooHhex44NYXOve/exec',
        // contact:  'https://script.google.com/macros/s/AKfycbz1EfVGj6a10iwdIUTgs1JOynCcnXfpcYW-y1EeG5h2IMFHQuhobyooHhex44NYXOve/exec',
    },
    FALLBACK_CONTACT: {
        url: 'https://zalo.me/0909123456',
        phone: 'tel:0909123456',
        label: '💬 Nhắn Zalo ngay',
    },
    MAX_RETRIES: 3,
    PHONE_REGEX: /^0\d{8,10}$/,
    MESSAGES: {
        sending: 'Đang gửi...',
        retrying: (attempt, max) => `Đang thử lại (${attempt}/${max})...`,
        phoneInvalid: {
            title: 'Số điện thoại không hợp lệ',
            msg: 'Vui lòng nhập số điện thoại bắt đầu bằng 0, từ 9–11 chữ số.',
        },
        success: {
            title: 'Gửi yêu cầu thành công! 🎉',
            msg: 'Chuyên viên sẽ liên hệ bạn trong 5 phút. Nhắn Zalo để được tư vấn nhanh hơn!',
        },
        retryNotice: {
            title: 'Đang thử lại...',
            msg: (attempt, max) => `Lần ${attempt}/${max} — Vui lòng chờ trong giây lát.`,
        },
        error: {
            title: 'Gửi không thành công',
            msg: 'Hệ thống đang bận. Vui lòng nhắn Zalo hoặc gọi hotline để được hỗ trợ ngay!',
        },
    },
};

// ═══════════════════════════════════════
// TOAST NOTIFICATION SYSTEM
// ═══════════════════════════════════════

function getToastContainer() {
    let c = document.querySelector('.form-toast-container');
    if (!c) {
        c = document.createElement('div');
        c.className = 'form-toast-container';
        document.body.appendChild(c);
    }
    return c;
}

function showFormToast(type, title, msg, options = {}) {
    const container = getToastContainer();
    container.querySelectorAll('.form-toast').forEach(t => hideFormToast(t));

    const icons = { success: '✅', error: '❌', retrying: '⏳' };
    const toast = document.createElement('div');
    toast.className = `form-toast form-toast--${type}`;

    const fallback = FORM_CONFIG.FALLBACK_CONTACT;
    toast.innerHTML = `
        <span class="form-toast-icon">${icons[type] || '📋'}</span>
        <div class="form-toast-body">
            <div class="form-toast-title">${title}</div>
            <div class="form-toast-msg">${msg}</div>
            ${options.showFallback ? `
                <div class="form-toast-actions">
                    <a href="${fallback.url}" target="_blank" class="form-toast-zalo">${fallback.label}</a>
                    <a href="${fallback.phone}" class="form-toast-call">📞 Gọi ngay</a>
                </div>
            ` : ''}
        </div>
        <button class="form-toast-close" aria-label="Đóng">✕</button>
    `;

    toast.querySelector('.form-toast-close').addEventListener('click', () => hideFormToast(toast));
    container.appendChild(toast);

    const dismissMs = { success: 6000, error: 15000, retrying: 10000 };
    setTimeout(() => hideFormToast(toast), dismissMs[type] || 8000);

    return toast;
}

function hideFormToast(toast) {
    if (!toast || !toast.parentNode) return;
    toast.classList.add('hiding');
    setTimeout(() => toast.remove(), 300);
}

// ═══════════════════════════════════════
// FETCH WITH RETRY (Exponential Backoff)
// ═══════════════════════════════════════

async function fetchWithRetry(url, options, maxRetries, onRetry) {
    let lastError;
    for (let attempt = 1; attempt <= maxRetries; attempt++) {
        try {
            const res = await fetch(url, options);
            if (res.type === 'opaque' || res.ok) return res;
            try {
                const data = await res.json();
                if (data.status === 'success') return res;
                throw new Error(data.message || 'Server error');
            } catch {
                if (res.type === 'opaque') return res;
                throw new Error(`HTTP ${res.status}`);
            }
        } catch (err) {
            lastError = err;
            if (attempt < maxRetries) {
                const delay = Math.pow(2, attempt - 1) * 1000;
                if (onRetry) onRetry(attempt, maxRetries);
                await new Promise(r => setTimeout(r, delay));
            }
        }
    }
    throw lastError;
}

// ═══════════════════════════════════════
// EXPANDABLE SECTION TOGGLE
// ═══════════════════════════════════════

function initExpandableSections() {
    document.querySelectorAll('.expand-toggle').forEach(btn => {
        btn.addEventListener('click', () => {
            const target = document.getElementById(btn.dataset.target);
            if (!target) return;

            const isOpen = target.classList.contains('expanded');
            target.classList.toggle('expanded');
            btn.classList.toggle('active');

            const icon = btn.querySelector('.expand-icon');
            if (icon) icon.textContent = isOpen ? '➕' : '➖';

            const label = btn.querySelector('.expand-label');
            if (label) {
                label.textContent = isOpen
                    ? 'Điền thêm thông tin (nhanh hơn khi tư vấn)'
                    : 'Ẩn phần mở rộng';
            }
        });
    });
}

// ═══════════════════════════════════════
// FORM SUBMISSION HANDLER
// ═══════════════════════════════════════

window.submitToGoogleSheet = function (event) {
    event.preventDefault();
    const form = event.target;
    const btn = form.querySelector('button[type="submit"]');
    if (!btn || btn.disabled) return;

    const originalHTML = btn.innerHTML;
    const cfg = FORM_CONFIG;
    const msgs = cfg.MESSAGES;

    // Phone validation
    const phoneInput = form.querySelector('input[name="phone"]');
    if (phoneInput) {
        const phone = phoneInput.value.replace(/\s+/g, '');
        if (!cfg.PHONE_REGEX.test(phone)) {
            showFormToast('error', msgs.phoneInvalid.title, msgs.phoneInvalid.msg);
            phoneInput.focus();
            return;
        }
    }

    // Auto-fill source URL
    const urlInput = form.querySelector('input[name="url"]');
    if (urlInput) urlInput.value = window.location.href;

    const formType = form.getAttribute('data-form-type') || Object.keys(cfg.URLS)[0];
    const scriptURL = cfg.URLS[formType] || Object.values(cfg.URLS)[0];

    if (!scriptURL) {
        // No URL configured — show success anyway for demo/testing
        console.warn('[form-handler] No Apps Script URL configured for type:', formType);
        showFormToast('error', 'Chưa cấu hình', 'Vui lòng cấu hình Google Sheet URL trong form-handler.js', { showFallback: true });
        return;
    }

    // Disable button + show loading
    const submitText = btn.querySelector('.submit-text');
    const submitLoader = btn.querySelector('.loader');
    if (submitText) submitText.textContent = msgs.sending;
    if (submitLoader) submitLoader.classList.remove('hidden');
    btn.disabled = true;

    fetchWithRetry(
        scriptURL,
        { method: 'POST', body: new FormData(form) },
        cfg.MAX_RETRIES,
        (attempt, max) => {
            if (submitText) submitText.textContent = msgs.retrying(attempt, max);
            showFormToast('retrying', msgs.retryNotice.title, msgs.retryNotice.msg(attempt, max));
        }
    )
        .then(() => {
            showFormToast('success', msgs.success.title, msgs.success.msg, { showFallback: true });

            // Dispatch custom event for app-specific success handling
            form.dispatchEvent(new CustomEvent('form:success', { bubbles: true }));

            form.reset();
        })
        .catch(() => {
            showFormToast('error', msgs.error.title, msgs.error.msg, { showFallback: true });

            // Dispatch custom event for app-specific error handling
            form.dispatchEvent(new CustomEvent('form:error', { bubbles: true }));
        })
        .finally(() => {
            btn.innerHTML = originalHTML;
            btn.disabled = false;
        });
};

// Init expandable sections on DOM ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initExpandableSections);
} else {
    initExpandableSections();
}
