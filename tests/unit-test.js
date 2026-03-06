// ══════════════════════════════════════════════
// HoChieuGap — Unit Test Suite
// Pure logic tests • TDD • Zero dependencies
// ══════════════════════════════════════════════

(function () {
    'use strict';

    // --- Mini Test Framework (reuse pattern from test.js) ---
    const results = [];
    let currentGroup = '';

    function group(name) { currentGroup = name; }

    function assert(name, fn) {
        try {
            const result = fn();
            if (result === true) {
                results.push({ group: currentGroup, name, status: 'pass' });
            } else {
                results.push({ group: currentGroup, name, status: 'fail', detail: String(result || 'Assertion failed') });
            }
        } catch (err) {
            results.push({ group: currentGroup, name, status: 'fail', detail: err.message });
        }
    }

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
                const icon = t.status === 'pass' ? '✅' : '❌';
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
    // GROUP 1: formatVND()
    // ══════════════════════════════════════════════
    group('formatVND()');

    assert('Formats standard price (4,000,000)', () => {
        const result = formatVND(4000000);
        return result === '4.000.000 VND' ? true : `Got: "${result}"`;
    });

    assert('Formats smaller price (1,100,000)', () => {
        const result = formatVND(1100000);
        return result === '1.100.000 VND' ? true : `Got: "${result}"`;
    });

    assert('Returns "Liên hệ" for null', () => {
        return formatVND(null) === 'Liên hệ' ? true : `Got: "${formatVND(null)}"`;
    });

    assert('Returns "Liên hệ" for 0', () => {
        return formatVND(0) === 'Liên hệ' ? true : `Got: "${formatVND(0)}"`;
    });

    assert('Returns "Liên hệ" for undefined', () => {
        return formatVND(undefined) === 'Liên hệ' ? true : `Got: "${formatVND(undefined)}"`;
    });

    assert('Formats smallest valid price (1)', () => {
        const result = formatVND(1);
        return result === '1 VND' ? true : `Got: "${result}"`;
    });

    // ══════════════════════════════════════════════
    // GROUP 2: getPrice()
    // ══════════════════════════════════════════════
    group('getPrice()');

    assert('Returns price for new-first + 1-day', () => {
        const price = getPrice('new-first', '1-day');
        return price === 4500000 ? true : `Got: ${price}`;
    });

    assert('Returns price for early-pickup + 3-day', () => {
        const price = getPrice('early-pickup', '3-day');
        return price === 2000000 ? true : `Got: ${price}`;
    });

    assert('Returns null for consult urgency', () => {
        const price = getPrice('extend', 'consult');
        return price === null ? true : `Got: ${price}`;
    });

    assert('Returns null for "other" service', () => {
        const price = getPrice('other', '1-day');
        return price === null ? true : `Got: ${price}`;
    });

    assert('Returns null for invalid service ID', () => {
        const price = getPrice('nonexistent', '1-day');
        return price === null ? true : `Got: ${price}`;
    });

    assert('Returns null for invalid urgency ID', () => {
        const price = getPrice('new-first', 'invalid');
        return price === null ? true : `Got: ${price}`;
    });

    assert('Returns null for both invalid', () => {
        const price = getPrice('xxx', 'yyy');
        return price === null ? true : `Got: ${price}`;
    });

    // ══════════════════════════════════════════════
    // GROUP 3: getServiceById()
    // ══════════════════════════════════════════════
    group('getServiceById()');

    assert('Finds "early-pickup" service', () => {
        const svc = getServiceById('early-pickup');
        return svc && svc.title === 'Lấy HC trước ngày hẹn' ? true : `Got: ${JSON.stringify(svc)}`;
    });

    assert('Finds "full-package" service with correct icon', () => {
        const svc = getServiceById('full-package');
        return svc && svc.icon === '🏠' ? true : `Got icon: ${svc?.icon}`;
    });

    assert('Returns undefined for invalid ID', () => {
        const svc = getServiceById('nonexistent');
        return svc === undefined ? true : `Got: ${svc}`;
    });

    assert('Returns undefined for empty string', () => {
        const svc = getServiceById('');
        return svc === undefined ? true : `Got: ${svc}`;
    });

    assert('Returns undefined for null', () => {
        const svc = getServiceById(null);
        return svc === undefined ? true : `Got: ${svc}`;
    });

    // ══════════════════════════════════════════════
    // GROUP 4: Data Integrity — PRICING
    // ══════════════════════════════════════════════
    group('Data Integrity — PRICING');

    assert('Every SERVICES ID has a PRICING entry', () => {
        const missing = SERVICES.filter(s => !PRICING[s.id]);
        return missing.length === 0 ? true : `Missing: ${missing.map(s => s.id).join(', ')}`;
    });

    assert('Each pricing entry has 4 urgency levels', () => {
        const expected = ['1-day', '2-day', '3-day', 'consult'];
        const invalid = Object.keys(PRICING).filter(id => {
            const keys = Object.keys(PRICING[id]);
            return expected.some(k => !keys.includes(k));
        });
        return invalid.length === 0 ? true : `Invalid entries: ${invalid.join(', ')}`;
    });

    assert('1-day price >= 2-day >= 3-day (when not null)', () => {
        const violations = [];
        Object.entries(PRICING).forEach(([id, prices]) => {
            const p1 = prices['1-day'];
            const p2 = prices['2-day'];
            const p3 = prices['3-day'];
            if (p1 !== null && p2 !== null && p1 < p2) violations.push(`${id}: 1-day < 2-day`);
            if (p2 !== null && p3 !== null && p2 < p3) violations.push(`${id}: 2-day < 3-day`);
        });
        return violations.length === 0 ? true : violations.join('; ');
    });

    assert('All non-null prices are positive', () => {
        const negatives = [];
        Object.entries(PRICING).forEach(([id, prices]) => {
            Object.entries(prices).forEach(([urgency, price]) => {
                if (price !== null && price <= 0) negatives.push(`${id}/${urgency}: ${price}`);
            });
        });
        return negatives.length === 0 ? true : negatives.join('; ');
    });

    assert('"other" service has all null prices', () => {
        const prices = PRICING['other'];
        if (!prices) return 'No "other" pricing entry';
        const nonNull = Object.entries(prices).filter(([, v]) => v !== null);
        return nonNull.length === 0 ? true : `Non-null: ${nonNull.map(([k]) => k).join(', ')}`;
    });

    // ══════════════════════════════════════════════
    // GROUP 5: Data Integrity — SERVICES
    // ══════════════════════════════════════════════
    group('Data Integrity — SERVICES');

    assert('Has exactly 5 services', () => {
        return SERVICES.length === 5 ? true : `Got: ${SERVICES.length}`;
    });

    assert('Each service has required fields', () => {
        const requiredFields = ['id', 'title', 'icon', 'shortDesc', 'details', 'docs'];
        const invalid = SERVICES.filter(s => requiredFields.some(f => !s[f]));
        return invalid.length === 0 ? true : `Missing fields in: ${invalid.map(s => s.id).join(', ')}`;
    });

    assert('No duplicate service IDs', () => {
        const ids = SERVICES.map(s => s.id);
        const dupes = ids.filter((id, i) => ids.indexOf(id) !== i);
        return dupes.length === 0 ? true : `Duplicates: ${dupes.join(', ')}`;
    });

    assert('Each service has non-empty docs array', () => {
        const empty = SERVICES.filter(s => !Array.isArray(s.docs) || s.docs.length === 0);
        return empty.length === 0 ? true : `Empty docs: ${empty.map(s => s.id).join(', ')}`;
    });

    // ══════════════════════════════════════════════
    // GROUP 6: Data Integrity — WIZARD_STEPS
    // ══════════════════════════════════════════════
    group('Data Integrity — WIZARD_STEPS');

    assert('Has exactly 3 wizard steps', () => {
        return WIZARD_STEPS.length === 3 ? true : `Got: ${WIZARD_STEPS.length}`;
    });

    assert('Each step has required fields', () => {
        const requiredFields = ['id', 'title', 'subtitle', 'icon', 'options'];
        const invalid = WIZARD_STEPS.filter(s => requiredFields.some(f => !s[f]));
        return invalid.length === 0 ? true : `Missing fields in: ${invalid.map(s => s.id).join(', ')}`;
    });

    assert('Each step has at least 1 option', () => {
        const empty = WIZARD_STEPS.filter(s => !Array.isArray(s.options) || s.options.length === 0);
        return empty.length === 0 ? true : `Empty options: ${empty.map(s => s.id).join(', ')}`;
    });

    assert('Step IDs are unique', () => {
        const ids = WIZARD_STEPS.map(s => s.id);
        const dupes = ids.filter((id, i) => ids.indexOf(id) !== i);
        return dupes.length === 0 ? true : `Duplicates: ${dupes.join(', ')}`;
    });

    // ══════════════════════════════════════════════
    // GROUP 7: Data Integrity — Other Data
    // ══════════════════════════════════════════════
    group('Data Integrity — Other');

    assert('SITE_CONFIG has non-empty hotline', () => {
        return SITE_CONFIG.hotline && SITE_CONFIG.hotline.length > 0 ? true : 'Missing hotline';
    });

    assert('FAQ_ITEMS has at least 1 item', () => {
        return FAQ_ITEMS.length > 0 ? true : 'Empty FAQ_ITEMS';
    });

    assert('Each FAQ has non-empty q and a', () => {
        const invalid = FAQ_ITEMS.filter((item, i) => !item.q || !item.a);
        return invalid.length === 0 ? true : `${invalid.length} FAQ items missing q or a`;
    });

    assert('All TESTIMONIALS have rating 1-5', () => {
        const invalid = TESTIMONIALS.filter(t => !t.rating || t.rating < 1 || t.rating > 5);
        return invalid.length === 0 ? true : `${invalid.length} testimonials with invalid rating`;
    });

    // ══════════════════════════════════════════════
    // RENDER
    // ══════════════════════════════════════════════
    render();

    // Console summary
    const pass = results.filter(r => r.status === 'pass').length;
    const fail = results.filter(r => r.status === 'fail').length;
    console.log(`\n🧪 Unit Tests: ${pass}/${results.length} passed${fail > 0 ? ` (${fail} FAILED)` : ' ✅ ALL PASS'}`);
    if (fail > 0) {
        results.filter(r => r.status === 'fail').forEach(r => {
            console.error(`  ❌ [${r.group}] ${r.name}: ${r.detail}`);
        });
    }
})();
