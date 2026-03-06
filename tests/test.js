// ══════════════════════════════════════════════
// HoChieuGap — Pre-Deployment Test Suite
// Browser-based, zero dependencies
// ══════════════════════════════════════════════

(function () {
    'use strict';

    // --- Test Framework ---
    const results = [];
    let currentGroup = '';

    function group(name) {
        currentGroup = name;
    }

    function assert(name, fn) {
        try {
            const result = fn();
            if (result === 'skip') {
                results.push({ group: currentGroup, name, status: 'skip', detail: 'Skipped' });
            } else if (result === true) {
                results.push({ group: currentGroup, name, status: 'pass' });
            } else {
                results.push({ group: currentGroup, name, status: 'fail', detail: String(result || 'Assertion failed') });
            }
        } catch (err) {
            results.push({ group: currentGroup, name, status: 'fail', detail: err.message });
        }
    }

    async function assertAsync(name, fn) {
        try {
            const result = await fn();
            if (result === true) {
                results.push({ group: currentGroup, name, status: 'pass' });
            } else {
                results.push({ group: currentGroup, name, status: 'fail', detail: String(result || 'Assertion failed') });
            }
        } catch (err) {
            results.push({ group: currentGroup, name, status: 'fail', detail: err.message });
        }
    }

    // --- Utility: Fetch HTML and parse ---
    async function fetchPage(url) {
        const response = await fetch(url);
        if (!response.ok) throw new Error(`HTTP ${response.status} for ${url}`);
        const html = await response.text();
        const parser = new DOMParser();
        return parser.parseFromString(html, 'text/html');
    }

    // --- Utility: Check if file is accessible ---
    async function fileExists(url) {
        try {
            const res = await fetch(url, { method: 'HEAD' });
            return res.ok;
        } catch {
            return false;
        }
    }

    // --- Render Results ---
    function render() {
        const container = document.getElementById('test-results');
        const groups = {};

        results.forEach(r => {
            if (!groups[r.group]) groups[r.group] = [];
            groups[r.group].push(r);
        });

        let html = '';
        for (const [groupName, tests] of Object.entries(groups)) {
            const groupFailed = tests.some(t => t.status === 'fail');
            html += `<div class="test-group">`;
            html += `<div class="test-group__header">${groupFailed ? '❌' : '✅'} ${groupName}</div>`;
            tests.forEach(t => {
                const icon = t.status === 'pass' ? '✅' : t.status === 'fail' ? '❌' : '⏭️';
                const detailClass = t.status === 'fail' ? 'error' : '';
                html += `<div class="test-row">
                    <span class="test-status">${icon}</span>
                    <span class="test-name">${t.name}</span>
                    ${t.detail ? `<span class="test-detail ${detailClass}">${t.detail}</span>` : ''}
                </div>`;
            });
            html += `</div>`;
        }

        container.innerHTML = html;

        const pass = results.filter(r => r.status === 'pass').length;
        const fail = results.filter(r => r.status === 'fail').length;
        const skip = results.filter(r => r.status === 'skip').length;

        document.getElementById('pass-count').textContent = pass;
        document.getElementById('fail-count').textContent = fail;
        document.getElementById('skip-count').textContent = skip;
        document.getElementById('total-count').textContent = results.length;

        const pct = results.length > 0 ? (pass / results.length) * 100 : 0;
        document.getElementById('progress-fill').style.width = pct + '%';
        document.getElementById('progress-fill').style.background = fail > 0 ? '#ef4444' : '#10b981';
    }

    // ══════════════════════════════════════════════
    // TEST SUITES
    // ══════════════════════════════════════════════

    async function runAll() {
        const BASE = window.location.origin;

        // ── 1. HOME PAGE: DOM Structure ──
        group('Home Page — DOM Structure');
        let homePage;
        try {
            homePage = await fetchPage(BASE + '/index.html');
        } catch (err) {
            assert('Can load index.html', () => 'Cannot fetch: ' + err.message);
            render();
            return;
        }

        assert('Has <title> tag', () => {
            const title = homePage.querySelector('title');
            return title && title.textContent.length > 0 ? true : 'Missing or empty title';
        });

        assert('Has <meta description>', () => {
            const meta = homePage.querySelector('meta[name="description"]');
            return meta && meta.content.length > 20 ? true : 'Missing or too short meta description';
        });

        assert('Has #navbar', () => !!homePage.querySelector('#navbar') || 'Missing #navbar');
        assert('Has #hero', () => !!homePage.querySelector('#hero') || 'Missing #hero');
        assert('Has #wizard', () => !!homePage.querySelector('#wizard') || 'Missing #wizard');
        assert('Has #services', () => !!homePage.querySelector('#services') || 'Missing #services');
        assert('Has #pricing', () => !!homePage.querySelector('#pricing') || 'Missing #pricing');
        assert('Has #process', () => !!homePage.querySelector('#process') || 'Missing #process');
        assert('Has #documents', () => !!homePage.querySelector('#documents') || 'Missing #documents');
        assert('Has #faq', () => !!homePage.querySelector('#faq') || 'Missing #faq');
        assert('Has #contact', () => !!homePage.querySelector('#contact') || 'Missing #contact');
        assert('Has #tools section', () => !!homePage.querySelector('#tools') || 'Missing #tools CTA section');

        assert('Has single <h1>', () => {
            const h1s = homePage.querySelectorAll('h1');
            return h1s.length === 1 ? true : `Found ${h1s.length} h1 tags (expected 1)`;
        });

        // ── 2. HOME PAGE: Navigation Links ──
        group('Home Page — Navigation Links');

        assert('Navbar has link to passport-photo/', () => {
            const links = homePage.querySelectorAll('.navbar__links a');
            const found = Array.from(links).some(a => a.href && a.getAttribute('href').includes('passport-photo'));
            return found ? true : 'Missing passport-photo link in navbar';
        });

        assert('Footer has link to passport-photo/', () => {
            const footerLinks = homePage.querySelectorAll('.footer__links a');
            const found = Array.from(footerLinks).some(a => a.getAttribute('href')?.includes('passport-photo'));
            return found ? true : 'Missing passport-photo link in footer';
        });

        assert('#tools section has CTA link to passport-photo/', () => {
            const toolLink = homePage.querySelector('#tools a[href*="passport-photo"]');
            return toolLink ? true : 'Missing CTA link in #tools section';
        });

        assert('Navbar has #wizard link', () => {
            const found = Array.from(homePage.querySelectorAll('.navbar__links a')).some(a => a.getAttribute('href') === '#wizard');
            return found ? true : 'Missing #wizard link';
        });

        assert('Navbar has #services link', () => {
            const found = Array.from(homePage.querySelectorAll('.navbar__links a')).some(a => a.getAttribute('href') === '#services');
            return found ? true : 'Missing #services link';
        });

        assert('Navbar has #contact link', () => {
            const found = Array.from(homePage.querySelectorAll('.navbar__links a')).some(a => a.getAttribute('href')?.includes('#contact'));
            return found ? true : 'Missing #contact link';
        });

        // ── 3. HOME PAGE: Contact Form ──
        group('Home Page — Contact Form');

        assert('Form has required name field', () => {
            const input = homePage.querySelector('#formName[required]');
            return input ? true : 'Missing required name field';
        });

        assert('Form has required phone field', () => {
            const input = homePage.querySelector('#formPhone[required]');
            return input ? true : 'Missing required phone field';
        });

        assert('Form has customerType select', () => {
            const sel = homePage.querySelector('#formCustomerType[required]');
            return sel ? true : 'Missing required customerType field';
        });

        assert('Form has service select', () => {
            const sel = homePage.querySelector('#formService[required]');
            return sel ? true : 'Missing required service field';
        });

        assert('Form has urgency select', () => {
            const sel = homePage.querySelector('#formUrgency[required]');
            return sel ? true : 'Missing required urgency field';
        });

        assert('Form has submit button', () => {
            const btn = homePage.querySelector('#contactForm button[type="submit"]');
            return btn ? true : 'Missing submit button';
        });

        // ── 4. PASSPORT PHOTO: DOM Structure ──
        group('Passport Photo — DOM Structure');
        let photoPage;
        try {
            photoPage = await fetchPage(BASE + '/passport-photo/index.html');
        } catch (err) {
            assert('Can load passport-photo/index.html', () => 'Cannot fetch: ' + err.message);
            render();
            return;
        }

        assert('Has #onboarding-view', () => !!photoPage.querySelector('#onboarding-view') || 'Missing #onboarding-view');
        assert('Has #camera-view', () => !!photoPage.querySelector('#camera-view') || 'Missing #camera-view');
        assert('Has #preview-view', () => !!photoPage.querySelector('#preview-view') || 'Missing #preview-view');
        assert('Has #confirmation-view', () => !!photoPage.querySelector('#confirmation-view') || 'Missing #confirmation-view');

        assert('Has #btn-start', () => !!photoPage.querySelector('#btn-start') || 'Missing start button');
        assert('Has #btn-capture', () => !!photoPage.querySelector('#btn-capture') || 'Missing capture button');
        assert('Has #btn-retake', () => !!photoPage.querySelector('#btn-retake') || 'Missing retake button');
        assert('Has #btn-accept', () => !!photoPage.querySelector('#btn-accept') || 'Missing accept button');
        assert('Has #btn-download', () => !!photoPage.querySelector('#btn-download') || 'Missing download button');
        assert('Has #btn-download-final', () => !!photoPage.querySelector('#btn-download-final') || 'Missing final download button');
        assert('Has #confirmation-image', () => !!photoPage.querySelector('#confirmation-image') || 'Missing confirmation image');

        assert('Has videoElement', () => !!photoPage.querySelector('#videoElement') || 'Missing video element');
        assert('Has canvasElement', () => !!photoPage.querySelector('#canvasElement') || 'Missing canvas element');
        assert('Has guide-frame', () => !!photoPage.querySelector('.guide-frame') || 'Missing guide frame');

        // ── 5. PASSPORT PHOTO: Navigation Links ──
        group('Passport Photo — Navigation Links');

        assert('Onboarding has back-link to home', () => {
            const link = photoPage.querySelector('#onboarding-view .back-link');
            return link && link.getAttribute('href') === '../' ? true : 'Missing or incorrect back-link in onboarding';
        });

        assert('Preview has back-link to home', () => {
            const link = photoPage.querySelector('#preview-view .back-link');
            return link && link.getAttribute('href') === '../' ? true : 'Missing or incorrect back-link in preview';
        });

        assert('Confirmation has "Tiếp tục đăng ký" button', () => {
            const btn = photoPage.querySelector('#confirmation-view #btn-go-register');
            return btn ? true : 'Missing register button in confirmation';
        });

        assert('Confirmation has "Quay về trang chủ" link', () => {
            const link = photoPage.querySelector('#confirmation-view a[href="../"]');
            return link ? true : 'Missing home link in confirmation';
        });

        // ── 6. ASSET REFERENCES ──
        group('Asset References');

        await assertAsync('Home CSS (css/style.css) exists', async () => {
            return await fileExists(BASE + '/css/style.css') ? true : 'css/style.css not found';
        });

        await assertAsync('Home JS (js/data.js) exists', async () => {
            return await fileExists(BASE + '/js/data.js') ? true : 'js/data.js not found';
        });

        await assertAsync('Home JS (js/app.js) exists', async () => {
            return await fileExists(BASE + '/js/app.js') ? true : 'js/app.js not found';
        });

        await assertAsync('Passport-photo CSS (style.css) exists', async () => {
            return await fileExists(BASE + '/passport-photo/style.css') ? true : 'passport-photo/style.css not found';
        });

        await assertAsync('Passport-photo JS (app.js) exists', async () => {
            return await fileExists(BASE + '/passport-photo/app.js') ? true : 'passport-photo/app.js not found';
        });

        // ── 7. JS SYNTAX CHECK ──
        group('JS Syntax Validation');

        await assertAsync('js/data.js loads without syntax error', async () => {
            try {
                const res = await fetch(BASE + '/js/data.js');
                const code = await res.text();
                new Function(code);
                return true;
            } catch (err) {
                return 'Syntax error: ' + err.message;
            }
        });

        await assertAsync('js/app.js loads without syntax error', async () => {
            try {
                const res = await fetch(BASE + '/js/app.js');
                const code = await res.text();
                new Function(code);
                return true;
            } catch (err) {
                return 'Syntax error: ' + err.message;
            }
        });

        await assertAsync('passport-photo/app.js loads without syntax error', async () => {
            try {
                const res = await fetch(BASE + '/passport-photo/app.js');
                const code = await res.text();
                new Function(code);
                return true;
            } catch (err) {
                return 'Syntax error: ' + err.message;
            }
        });

        // ── 8. SEO & ACCESSIBILITY ──
        group('SEO & Accessibility');

        assert('Home page has lang attribute', () => {
            const html = homePage.querySelector('html');
            return html && html.getAttribute('lang') ? true : 'Missing lang attribute';
        });

        assert('Home page has og:title', () => {
            const meta = homePage.querySelector('meta[property="og:title"]');
            return meta ? true : 'Missing og:title';
        });

        assert('Home page has og:description', () => {
            const meta = homePage.querySelector('meta[property="og:description"]');
            return meta ? true : 'Missing og:description';
        });

        assert('Passport photo page has lang attribute', () => {
            const html = photoPage.querySelector('html');
            return html && html.getAttribute('lang') ? true : 'Missing lang attribute';
        });

        assert('All form inputs have labels', () => {
            const inputs = homePage.querySelectorAll('#contactForm input, #contactForm select, #contactForm textarea');
            const withoutLabel = Array.from(inputs).filter(input => {
                const id = input.id;
                if (!id) return true;
                return !homePage.querySelector(`label[for="${id}"]`);
            });
            return withoutLabel.length === 0 ? true : `${withoutLabel.length} inputs missing labels`;
        });

        assert('Interactive elements have unique IDs', () => {
            const elements = homePage.querySelectorAll('button[id], a[id], input[id], select[id]');
            const ids = Array.from(elements).map(el => el.id).filter(Boolean);
            const dupes = ids.filter((id, i) => ids.indexOf(id) !== i);
            return dupes.length === 0 ? true : `Duplicate IDs: ${dupes.join(', ')}`;
        });

        // ── 9. CROSS-PAGE CONSISTENCY ──
        group('Cross-Page Consistency');

        assert('Both pages use Vietnamese language', () => {
            const homeLang = homePage.querySelector('html').getAttribute('lang');
            const photoLang = photoPage.querySelector('html').getAttribute('lang');
            return homeLang === 'vi' && photoLang === 'vi' ? true : `Home: ${homeLang}, Photo: ${photoLang}`;
        });

        assert('Home page footer copyright is current year', () => {
            const footer = homePage.querySelector('.footer__bottom');
            return footer && footer.textContent.includes('2026') ? true : 'Copyright year might be outdated';
        });

        assert('Confirmation view has all 3 action types', () => {
            const confirmView = photoPage.querySelector('#confirmation-view');
            if (!confirmView) return 'No confirmation view';
            const hasRegister = !!confirmView.querySelector('#btn-go-register');
            const hasDownload = !!confirmView.querySelector('#btn-download-final');
            const hasHome = !!confirmView.querySelector('a[href="../"]');
            if (!hasRegister) return 'Missing register button';
            if (!hasDownload) return 'Missing download button';
            if (!hasHome) return 'Missing home link';
            return true;
        });

        // ── DONE ──
        render();
    }

    // Run on load
    runAll();
})();
