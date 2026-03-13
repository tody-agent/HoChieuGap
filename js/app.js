// ══════════════════════════════════════════════
// HoChieuGap — Interactive App Logic
// ══════════════════════════════════════════════

document.addEventListener('DOMContentLoaded', () => {
  initNavbar();
  initWizard();
  initServices();
  initPricing();
  initProcess();
  initDocuments();
  initFAQ();
  initTestimonials();
  initContactForm();
  initAnimations();
  initCountUp();
  initStickyMobileCTA();
});

// ═══ NAVBAR ═══
function initNavbar() {
  const navbar = document.getElementById('navbar');
  const toggle = document.getElementById('navToggle');
  const links = document.getElementById('navLinks');

  // Scroll effect
  window.addEventListener('scroll', () => {
    navbar.classList.toggle('navbar--scrolled', window.scrollY > 50);
  });

  // Mobile toggle
  toggle.addEventListener('click', () => {
    links.classList.toggle('navbar__links--open');
    toggle.classList.toggle('active');
  });

  // Close on link click
  links.querySelectorAll('a').forEach(a => {
    a.addEventListener('click', () => {
      links.classList.remove('navbar__links--open');
      toggle.classList.remove('active');
    });
  });

  // UX: Close mobile nav on scroll for cleaner experience
  let lastScrollY = 0;
  window.addEventListener('scroll', () => {
    if (Math.abs(window.scrollY - lastScrollY) > 60) {
      links.classList.remove('navbar__links--open');
      toggle.classList.remove('active');
      lastScrollY = window.scrollY;
    }
  }, { passive: true });
}

// ═══ WIZARD ENGINE ═══
let wizardState = {
  currentStep: 0,
  selections: {}
};

function initWizard() {
  renderStepIndicators();
  renderWizardStep(0);
  updateProgress();

  document.getElementById('wizardBack').addEventListener('click', wizardGoBack);
}

function renderStepIndicators() {
  const container = document.getElementById('wizardStepsIndicator');
  const allSteps = [...WIZARD_STEPS, { id: 'result', title: 'Kết quả' }];
  container.innerHTML = allSteps.map((step, i) => `
    <div class="wizard__step-dot ${i === 0 ? 'wizard__step-dot--active' : ''}" data-step="${i}">
      <div class="wizard__step-dot-circle">${i < WIZARD_STEPS.length ? i + 1 : '✓'}</div>
      <span class="wizard__step-dot-label">${step.title}</span>
    </div>
  `).join('');
}

function updateStepIndicators() {
  const dots = document.querySelectorAll('.wizard__step-dot');
  dots.forEach((dot, i) => {
    dot.classList.remove('wizard__step-dot--active', 'wizard__step-dot--done');
    if (i < wizardState.currentStep) dot.classList.add('wizard__step-dot--done');
    if (i === wizardState.currentStep) dot.classList.add('wizard__step-dot--active');
  });
}

function updateProgress() {
  const total = WIZARD_STEPS.length + 1; // +1 for result
  const pct = (wizardState.currentStep / total) * 100;
  document.getElementById('wizardProgressBar').style.width = pct + '%';

  const backBtn = document.getElementById('wizardBack');
  backBtn.disabled = wizardState.currentStep === 0;

  const countEl = document.getElementById('wizardStepCount');
  if (wizardState.currentStep < WIZARD_STEPS.length) {
    countEl.textContent = `Bước ${wizardState.currentStep + 1} / ${WIZARD_STEPS.length}`;
  } else {
    countEl.textContent = 'Kết quả';
  }

  updateStepIndicators();
}

function renderWizardStep(stepIndex) {
  const body = document.getElementById('wizardBody');

  if (stepIndex >= WIZARD_STEPS.length) {
    renderWizardResult();
    return;
  }

  const step = WIZARD_STEPS[stepIndex];
  body.innerHTML = `
    <div class="wizard__step">
      <div class="wizard__step-header">
        <div class="wizard__step-icon">${step.icon}</div>
        <h3 class="wizard__step-title">${step.title}</h3>
        <p class="wizard__step-subtitle">${step.subtitle}</p>
      </div>
      <div class="wizard__options">
        ${step.options.map(opt => `
          <button class="wizard__option ${wizardState.selections[step.id] === opt.id ? 'wizard__option--selected' : ''}"
                  data-value="${opt.id}" data-step="${step.id}">
            <span class="wizard__option-icon">${opt.icon}</span>
            <div class="wizard__option-content">
              <div class="wizard__option-label">${opt.label}</div>
              <div class="wizard__option-desc">${opt.desc}</div>
            </div>
            ${opt.tag ? `<span class="wizard__option-tag" style="background:${opt.tagColor || 'var(--c-primary)'}">${opt.tag}</span>` : ''}
          </button>
        `).join('')}
      </div>
    </div>
  `;

  // Bind option clicks
  body.querySelectorAll('.wizard__option').forEach(btn => {
    btn.addEventListener('click', () => {
      const stepId = btn.dataset.step;
      const value = btn.dataset.value;
      wizardState.selections[stepId] = value;

      // Visual feedback
      body.querySelectorAll('.wizard__option').forEach(b => b.classList.remove('wizard__option--selected'));
      btn.classList.add('wizard__option--selected');

      // Auto-advance after short delay
      setTimeout(() => {
        wizardState.currentStep++;
        updateProgress();
        renderWizardStep(wizardState.currentStep);
      }, 300);
    });
  });
}

function renderWizardResult() {
  const body = document.getElementById('wizardBody');
  const serviceId = wizardState.selections['service-type'];
  const urgencyId = wizardState.selections['urgency'];
  const service = getServiceById(serviceId);
  const price = getPrice(serviceId, urgencyId);

  const urgencyLabels = {
    '1-day': 'Hoàn tất trong 24h',
    '2-day': 'Hoàn tất trong 48h',
    '3-day': 'Hoàn tất trong 72h',
    'consult': 'Tư vấn thêm'
  };

  if (!service) {
    body.innerHTML = `
      <div class="wizard__result">
        <div class="wizard__result-header">
          <div class="wizard__result-icon">💬</div>
          <h3 class="wizard__result-title">Chúng tôi sẽ tư vấn cho bạn!</h3>
        </div>
        <div class="wizard__result-card">
          <p style="text-align:center;color:var(--c-text-muted);font-size:16px;">
            Tình huống của bạn cần tư vấn trực tiếp. Liên hệ ngay để được hỗ trợ nhanh nhất!
          </p>
        </div>
        <div class="wizard__result-actions">
          <a href="tel:${SITE_CONFIG.hotline.replace(/\s/g, '')}" class="btn btn--accent btn--lg">📞 Gọi ${SITE_CONFIG.hotline}</a>
          <a href="${SITE_CONFIG.zaloLink}" target="_blank" class="btn btn--outline btn--lg">💬 Nhắn Zalo</a>
          <a href="#contact" class="btn btn--ghost btn--lg">📝 Điền form</a>
        </div>
      </div>
    `;
    return;
  }

  body.innerHTML = `
    <div class="wizard__result">
      <div class="wizard__result-header">
        <div class="wizard__result-icon">🎯</div>
        <h3 class="wizard__result-title">Tìm thấy dịch vụ phù hợp!</h3>
      </div>
      <div class="wizard__result-card">
        <div class="wizard__result-service">${service.icon} ${service.title}</div>
        <p style="color:var(--c-text-muted);margin-bottom:8px;">${service.shortDesc}</p>
        <div style="font-size:14px;color:var(--c-primary);font-weight:600;">
          ⏰ Thời gian: ${urgencyLabels[urgencyId] || 'Liên hệ'}
        </div>
        <div class="wizard__result-price">
          ${formatVND(price)}
          ${price ? '<small> / hồ sơ</small>' : ''}
        </div>
        <div class="wizard__result-docs">
          <h4>📋 Hồ sơ cần chuẩn bị:</h4>
          <ul>
            ${service.docs.map(d => `<li>${d}</li>`).join('')}
          </ul>
        </div>
      </div>
      <div class="wizard__result-actions">
        <a href="#contact" class="btn btn--accent btn--lg" onclick="prefillForm('${serviceId}','${urgencyId}')">📝 Đăng ký ngay</a>
        <a href="tel:${SITE_CONFIG.hotline.replace(/\s/g, '')}" class="btn btn--outline btn--lg">📞 Gọi ${SITE_CONFIG.hotline}</a>
        <a href="${SITE_CONFIG.zaloLink}" target="_blank" class="btn btn--ghost btn--lg">💬 Nhắn Zalo</a>
      </div>
    </div>
  `;
}

function wizardGoBack() {
  if (wizardState.currentStep > 0) {
    wizardState.currentStep--;
    updateProgress();
    renderWizardStep(wizardState.currentStep);
  }
}

function prefillForm(serviceId, urgencyId) {
  const serviceSelect = document.getElementById('formService');
  const urgencySelect = document.getElementById('formUrgency');
  if (serviceSelect) serviceSelect.value = serviceId;
  if (urgencySelect) urgencySelect.value = urgencyId;
  updateFormEstimate();
}

// ═══ SERVICES GRID ═══
function initServices() {
  const grid = document.getElementById('servicesGrid');
  grid.innerHTML = SERVICES.map(svc => {
    const minPrice = Math.min(...Object.values(PRICING[svc.id]).filter(Boolean));
    const maxPrice = Math.max(...Object.values(PRICING[svc.id]).filter(Boolean));

    return `
      <div class="service-card animate-on-scroll">
        <div class="service-card__icon">${svc.icon}</div>
        <h3 class="service-card__title">${svc.title}</h3>
        <p class="service-card__desc">${svc.shortDesc}</p>
        <ul class="service-card__details">
          ${svc.details.map(d => `<li>${d}</li>`).join('')}
        </ul>
        <div class="service-card__price-range">
          Từ ${formatVND(minPrice)} — ${formatVND(maxPrice)}
        </div>
      </div>
    `;
  }).join('');

  // Dual tabs
  const tabs = document.querySelectorAll('.dual-tab');
  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      tabs.forEach(t => t.classList.remove('dual-tab--active'));
      tab.classList.add('dual-tab--active');

      document.querySelectorAll('.dual-content').forEach(c => c.classList.add('dual-content--hidden'));
      document.getElementById('content-' + tab.dataset.tab).classList.remove('dual-content--hidden');
    });
  });
}

// ═══ PRICING TABLE ═══
function initPricing() {
  const tbody = document.getElementById('pricingBody');
  const rows = SERVICES.map(svc => {
    const prices = PRICING[svc.id];
    
    const renderPrice = (price) => {
        if (!price) return 'Liên hệ';
        const anchor = price * 1.2;
        return `<del style="color:var(--c-text-muted); font-size: 0.85em; display:block; margin-bottom: 2px;">${formatVND(anchor)}</del>${formatVND(price)}`;
    };

    return `
      <tr>
        <td>${svc.icon} ${svc.title}</td>
        <td class="price-cell" data-label="72h">${renderPrice(prices['3-day'])}</td>
        <td class="price-cell" data-label="48h">${renderPrice(prices['2-day'])}</td>
        <td class="price-cell price-cell--hot" data-label="24h ⚡">${renderPrice(prices['1-day'])}</td>
      </tr>
    `;
  }).join('');
  tbody.innerHTML = rows;
}

// ═══ PROCESS TIMELINE ═══
function initProcess() {
  const container = document.getElementById('processTimeline');
  container.innerHTML = PROCESS_STEPS.map(step => `
    <div class="process-step animate-on-scroll">
      <div class="process-step__icon">${step.icon}</div>
      <div class="process-step__content">
        <div class="process-step__num">Bước ${step.step}</div>
        <h3 class="process-step__title">${step.title}</h3>
        <p class="process-step__desc">${step.desc}</p>
        <span class="process-step__duration">${step.duration}</span>
      </div>
    </div>
  `).join('');
}

// ═══ DOCUMENTS CHECKLIST ═══
function initDocuments() {
  const grid = document.getElementById('docsGrid');
  grid.innerHTML = DOCUMENTS.map(doc => `
    <div class="doc-item ${doc.required ? 'doc-item--required' : ''} animate-on-scroll">
      <div class="doc-item__check">${doc.required ? '★' : '○'}</div>
      <div class="doc-item__content">
        <div class="doc-item__name">${doc.name}</div>
        <div class="doc-item__note">${doc.note}</div>
        <div class="doc-item__qty">${doc.quantity}</div>
      </div>
    </div>
  `).join('');
}

// ═══ FAQ ACCORDION ═══
function initFAQ() {
  const list = document.getElementById('faqList');
  list.innerHTML = FAQ_ITEMS.map((item, i) => `
    <div class="faq-item animate-on-scroll" id="faq-${i}">
      <button class="faq-item__question" onclick="toggleFAQ(${i})">
        <span>${item.q}</span>
        <span class="faq-item__arrow">▼</span>
      </button>
      <div class="faq-item__answer">${item.a}</div>
    </div>
  `).join('');
}

function toggleFAQ(index) {
  const item = document.getElementById(`faq-${index}`);
  const wasOpen = item.classList.contains('faq-item--open');

  // Close all
  document.querySelectorAll('.faq-item').forEach(el => el.classList.remove('faq-item--open'));

  // Toggle current
  if (!wasOpen) {
    item.classList.add('faq-item--open');
  }
}

// ═══ TESTIMONIALS ═══
function initTestimonials() {
  const grid = document.getElementById('testimonialsGrid');
  grid.innerHTML = TESTIMONIALS.map(t => `
    <div class="testimonial-card animate-on-scroll">
      <div class="testimonial-card__stars">${'★'.repeat(t.rating)}</div>
      <p class="testimonial-card__text">${t.text}</p>
      <div class="testimonial-card__author">${t.name}</div>
      <div class="testimonial-card__role">${t.role}</div>
    </div>
  `).join('');
}

// ═══ CONTACT FORM ═══
function initContactForm() {
  const form = document.getElementById('contactForm');
  const serviceSelect = document.getElementById('formService');
  const urgencySelect = document.getElementById('formUrgency');

  // Real-time price estimate
  serviceSelect.addEventListener('change', updateFormEstimate);
  urgencySelect.addEventListener('change', updateFormEstimate);

  // Listen for form:success event from form-handler.js
  form.addEventListener('form:success', () => {
    const serviceId = serviceSelect.value;
    const urgencyId = urgencySelect.value;
    const price = getPrice(serviceId, urgencyId);

    // Show success modal
    const modal = document.getElementById('successModal');
    const estimate = document.getElementById('modalEstimate');

    if (price) {
      estimate.innerHTML = `Giá ước tính: <strong>${formatVND(price)}</strong>`;
    } else {
      estimate.innerHTML = 'Chúng tôi sẽ báo giá chính xác khi liên hệ';
    }

    modal.classList.add('modal-overlay--open');
    document.getElementById('formEstimate').style.display = 'none';
  });

  // Modal close
  document.getElementById('modalClose').addEventListener('click', closeModal);
  document.getElementById('modalCloseBtn').addEventListener('click', closeModal);
  document.getElementById('successModal').addEventListener('click', (e) => {
    if (e.target === e.currentTarget) closeModal();
  });
}

function updateFormEstimate() {
  const serviceId = document.getElementById('formService').value;
  const urgencyId = document.getElementById('formUrgency').value;
  const estimateEl = document.getElementById('formEstimate');
  const priceEl = document.getElementById('formEstimatePrice');

  if (serviceId && urgencyId) {
    const price = getPrice(serviceId, urgencyId);
    if (price) {
      priceEl.textContent = formatVND(price);
      estimateEl.style.display = 'flex';
    } else {
      priceEl.textContent = 'Liên hệ báo giá';
      estimateEl.style.display = 'flex';
    }
  } else {
    estimateEl.style.display = 'none';
  }
}

function closeModal() {
  document.getElementById('successModal').classList.remove('modal-overlay--open');
}

// Floating CTA removed — tập trung form tự động hoá

// ═══ SCROLL ANIMATIONS ═══
function initAnimations() {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('animate-on-scroll--visible');
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  });

  // Observe all animated elements
  setTimeout(() => {
    document.querySelectorAll('.animate-on-scroll').forEach(el => {
      observer.observe(el);
    });
  }, 100);
}

// ═══ COUNT-UP ANIMATION ═══
function initCountUp() {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        const target = parseInt(el.dataset.count);
        animateCount(el, target);
        observer.unobserve(el);
      }
    });
  }, { threshold: 0.5 });

  document.querySelectorAll('[data-count]').forEach(el => {
    observer.observe(el);
  });
}

function animateCount(el, target) {
  const duration = 2000;
  const start = performance.now();

  function update(now) {
    const elapsed = now - start;
    const progress = Math.min(elapsed / duration, 1);
    // Ease out
    const eased = 1 - Math.pow(1 - progress, 3);
    const current = Math.round(eased * target);
    el.textContent = current.toLocaleString();

    if (progress < 1) {
      requestAnimationFrame(update);
    }
  }

  requestAnimationFrame(update);
}

// ═══ STICKY MOBILE CTA ═══
// UX: Fitts's Law — Keep primary actions in thumb zone
// UX: Auto-hide when contact section is visible to avoid redundancy
function initStickyMobileCTA() {
  const bar = document.getElementById('mobileStickyBar');
  if (!bar) return;

  const contactSection = document.getElementById('contact');
  if (!contactSection) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      bar.classList.toggle('mobile-sticky-cta--hidden', entry.isIntersecting);
    });
  }, {
    threshold: 0.15
  });

  observer.observe(contactSection);

  // Also hide when footer is visible
  const footer = document.querySelector('.footer');
  if (footer) {
    const footerObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          bar.classList.add('mobile-sticky-cta--hidden');
        }
      });
    }, { threshold: 0.3 });
    footerObserver.observe(footer);
  }
}
