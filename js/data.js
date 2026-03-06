// HoChieuGap — Data Module
// All content, pricing, wizard config, FAQ

const SITE_CONFIG = {
    brand: 'HoChieuGap',
    tagline: 'Dịch vụ Hộ Chiếu Gấp — Nhanh · Uy Tín · Mọi Tình Huống',
    hotline: '0909 123 456',
    zaloLink: 'https://zalo.me/0909123456',
    email: 'info@hochieugap.vn',
    address: {
        hcm: '123 Nguyễn Huệ, Quận 1, TP. Hồ Chí Minh',
        hn: '45 Tràng Tiền, Quận Hoàn Kiếm, Hà Nội'
    },
    stats: {
        served: 5000,
        monthly: 500,
        years: 10,
        successRate: 100
    }
};

// ── Wizard Steps ──────────────────────────────
const WIZARD_STEPS = [
    {
        id: 'customer-type',
        title: 'Bạn là ai?',
        subtitle: 'Chọn loại khách hàng phù hợp',
        icon: '👤',
        options: [
            { id: 'individual', label: 'Cá nhân', icon: '🧑', desc: 'Tôi cần làm hộ chiếu cho bản thân / gia đình' },
            { id: 'travel', label: 'Công ty Du lịch', icon: '✈️', desc: 'Tôi cần xử lý hộ chiếu cho khách tour' },
            { id: 'education', label: 'Agency Giáo dục', icon: '🎓', desc: 'Tôi cần làm hộ chiếu cho du học sinh' },
            { id: 'labor', label: 'Xuất khẩu Lao động', icon: '🏗️', desc: 'Tôi cần hộ chiếu cho lao động đi nước ngoài' },
            { id: 'other', label: 'Tổ chức khác', icon: '🏢', desc: 'Doanh nghiệp, tổ chức có nhu cầu khác' }
        ]
    },
    {
        id: 'service-type',
        title: 'Bạn cần gì?',
        subtitle: 'Chọn dịch vụ phù hợp với tình huống của bạn',
        icon: '📋',
        options: [
            { id: 'new-first', label: 'Cấp mới lần đầu', icon: '🆕', desc: 'Chưa từng có hộ chiếu, cần làm mới' },
            { id: 'renew-expired', label: 'Làm lại HC hết hạn', icon: '🔄', desc: 'Hộ chiếu đã hết hạn, cần cấp lại' },
            { id: 'extend', label: 'Gia hạn / Đổi HC', icon: '📝', desc: 'HC còn hạn < 6 tháng, hết trang, hư hỏng' },
            { id: 'lost', label: 'HC bị mất', icon: '🔍', desc: 'Mất hộ chiếu, cần làm lại gấp' },
            { id: 'early-pickup', label: 'Lấy trước ngày hẹn', icon: '⚡', desc: 'Đã nộp hồ sơ, cần nhận sớm hơn' },
            { id: 'full-package', label: 'Trọn gói tại nhà / VP', icon: '🏠', desc: 'Không cần đi đâu, chúng tôi xử lý toàn bộ' },
            { id: 'other', label: 'Tình huống khác', icon: '❓', desc: 'Mô tả tình huống, chúng tôi tư vấn' }
        ]
    },
    {
        id: 'urgency',
        title: 'Bạn cần trong bao lâu?',
        subtitle: 'Thời gian càng gấp, phí dịch vụ càng cao',
        icon: '⏰',
        options: [
            { id: '1-day', label: 'Hoàn tất trong 24h', icon: '🔥', desc: 'Xử lý nhanh nhất', tag: 'Gấp nhất', tagColor: '#E74C3C' },
            { id: '2-day', label: 'Hoàn tất trong 48h', icon: '🕐', desc: 'Nhận kết quả sau 2 ngày' },
            { id: '3-day', label: 'Hoàn tất trong 72h', icon: '📅', desc: 'Tối ưu chi phí' },
            { id: 'consult', label: 'Chưa rõ, tư vấn thêm', icon: '💬', desc: 'Chúng tôi sẽ liên hệ tư vấn' }
        ]
    }
];

// ── Pricing Matrix (VND) ──────────────────────
// Rows: service-type, Cols: urgency
const PRICING = {
    'early-pickup': {
        '1-day': 4000000,
        '2-day': 3000000,
        '3-day': 2000000,
        'consult': null
    },
    'extend': {
        '1-day': 2300000,
        '2-day': 1600000,
        '3-day': 1100000,
        'consult': null
    },
    'lost': {
        '1-day': 3000000,
        '2-day': 2200000,
        '3-day': 1600000,
        'consult': null
    },
    'new-first': {
        '1-day': 4500000,
        '2-day': 3500000,
        '3-day': 3100000,
        'consult': null
    },
    'renew-expired': {
        '1-day': 4500000,
        '2-day': 3500000,
        '3-day': 3100000,
        'consult': null
    },
    'full-package': {
        '1-day': 5500000,
        '2-day': 4500000,
        '3-day': 4000000,
        'consult': null
    },
    'other': {
        '1-day': null,
        '2-day': null,
        '3-day': null,
        'consult': null
    }
};

// ── Services Detail ──────────────────────
const SERVICES = [
    {
        id: 'early-pickup',
        title: 'Lấy HC trước ngày hẹn',
        icon: '⚡',
        shortDesc: 'Đã nộp hồ sơ, cần nhận sớm hơn 12 ngày chờ',
        details: [
            'Bạn đã hoàn tất nộp hồ sơ và có giấy hẹn',
            'Cần nhận hộ chiếu sớm cho chuyến đi gấp',
            'Xử lý nhanh nhất: có kết quả trong 24h'
        ],
        docs: ['Giấy hẹn trả kết quả', 'CMND/CCCD bản chính']
    },
    {
        id: 'extend',
        title: 'Gia hạn / Đổi HC',
        icon: '📝',
        shortDesc: 'HC còn hạn < 6 tháng, hết trang, hư hỏng, sai thông tin',
        details: [
            'Hộ chiếu còn hạn dưới 6 tháng — không đủ xin visa',
            'Hộ chiếu hết trang, rách, ướt, hư hỏng',
            'Cần thay đổi thông tin cá nhân trên HC'
        ],
        docs: ['Hộ chiếu cũ bản chính', 'CMND/CCCD bản chính', 'Sao chụp hộ khẩu']
    },
    {
        id: 'lost',
        title: 'Làm lại HC bị mất',
        icon: '🔍',
        shortDesc: 'Mất hộ chiếu — xử lý khẩn cấp trong 24h',
        details: [
            'Bất kể hộ khẩu TP.HCM hay ngoại tỉnh',
            'Chỉ cần CMND/CCCD bản chính + sao chụp hộ khẩu',
            'Không cần công chứng'
        ],
        docs: ['CMND/CCCD bản chính', 'Sao chụp hộ khẩu', 'Đơn báo mất (hỗ trợ làm)']
    },
    {
        id: 'new-first',
        title: 'Cấp mới / Cấp lại hết hạn',
        icon: '🆕',
        shortDesc: 'Chưa từng có HC hoặc HC đã hết hạn cần cấp lại',
        details: [
            'Làm hộ chiếu lần đầu tiên',
            'Hộ chiếu hết hạn cần cấp lại mới',
            'Hỗ trợ đầy đủ thủ tục từ A-Z'
        ],
        docs: ['Tờ khai TK01/TK01a', 'CMND/CCCD bản chính', 'Ảnh 4x6 nền trắng', 'Sao chụp hộ khẩu']
    },
    {
        id: 'full-package',
        title: 'Trọn gói tại nhà / VP',
        icon: '🏠',
        shortDesc: 'Không cần đi đâu — nhận tài liệu tận nơi, xử lý toàn bộ',
        details: [
            'Đến tận nhà/văn phòng nhận thông tin & tài liệu',
            'Điền đơn, chuẩn bị hồ sơ thay bạn',
            'Nộp hồ sơ và giao HC tận tay'
        ],
        docs: ['CMND/CCCD bản chính', 'Sao chụp hộ khẩu', 'HC cũ (nếu có)']
    }
];

// ── Document Checklist ──────────────────────
const DOCUMENTS = [
    {
        name: 'Tờ khai TK01 (≥14 tuổi) hoặc TK01a (<14 tuổi)',
        note: 'Theo Thông tư 31/2023/TT-BCA',
        quantity: '1 bản chính',
        downloadUrl: 'https://hochieu.xuatnhapcanh.gov.vn/docs/TK01.pdf',
        required: true
    },
    {
        name: 'Ảnh 4x6cm, nền trắng',
        note: 'Chụp không quá 6 tháng, mặt nhìn thẳng, đầu để trần, không đeo kính',
        quantity: '1 bản chính',
        required: true
    },
    {
        name: 'CMND / Căn cước công dân',
        note: 'Bản chính — xuất trình khi nộp',
        quantity: '1 bản chính',
        required: true
    },
    {
        name: 'Hộ chiếu cũ còn giá trị (nếu có)',
        note: 'Đối với người đã được cấp hộ chiếu',
        quantity: '1 bản chính',
        required: false
    },
    {
        name: 'Đơn báo mất (nếu HC mất)',
        note: 'Chúng tôi hỗ trợ viết đơn báo mất',
        quantity: '1 bản chính',
        required: false
    },
    {
        name: 'Giấy khai sinh (trẻ < 14 tuổi)',
        note: 'Chưa có mã số định danh cá nhân',
        quantity: '1 bản chính + 1 bản sao',
        required: false
    },
    {
        name: 'Giấy tờ người đại diện hợp pháp',
        note: 'Cho người mất năng lực hành vi / trẻ em',
        quantity: '1 bản chính + 1 bản sao',
        required: false
    }
];

// ── Process Steps ──────────────────────
const PROCESS_STEPS = [
    {
        step: 1,
        title: 'Liên hệ & Tư vấn',
        desc: 'Gọi hotline, nhắn Zalo, hoặc điền form. Chúng tôi tư vấn miễn phí tình huống của bạn.',
        icon: '📞',
        duration: '5 phút'
    },
    {
        step: 2,
        title: 'Chuẩn bị Hồ sơ',
        desc: 'Chuẩn bị giấy tờ theo hướng dẫn. Dịch vụ trọn gói — chúng tôi đến nhận tận nơi.',
        icon: '📁',
        duration: '30 phút'
    },
    {
        step: 3,
        title: 'Nộp & Xử lý',
        desc: 'Chúng tôi nộp hồ sơ, theo dõi tiến độ và xử lý mọi vấn đề phát sinh.',
        icon: '⚙️',
        duration: '1-3 ngày'
    },
    {
        step: 4,
        title: 'Nhận Hộ chiếu',
        desc: 'Nhận hộ chiếu đúng hẹn. Giao tận tay hoặc nhận tại văn phòng.',
        icon: '✅',
        duration: 'Đúng hẹn'
    }
];

// ── FAQ ──────────────────────
const FAQ_ITEMS = [
    {
        q: 'Thời gian cấp hộ chiếu nhanh nhất là bao lâu?',
        a: 'Nhanh nhất là <strong>24h</strong> — cam kết đúng hẹn. Ngoài ra có các gói xử lý 48h và 72h làm việc tuỳ nhu cầu và ngân sách của bạn.'
    },
    {
        q: 'Tôi ở ngoại tỉnh, có làm được hộ chiếu gấp tại TP.HCM không?',
        a: 'Được! Bất kể hộ khẩu TP.HCM hay ngoại tỉnh, chúng tôi đều hỗ trợ xử lý. Chỉ cần mang theo <strong>CMND/CCCD bản chính</strong> và <strong>sao chụp hộ khẩu</strong> (không cần công chứng).'
    },
    {
        q: 'CMND/CCCD hết hạn có làm được hộ chiếu không?',
        a: 'CMND/CCCD là giấy tờ bắt buộc khi làm hộ chiếu. Nếu hết hạn, bạn cần làm lại CCCD trước. Chúng tôi sẽ tư vấn phương án nhanh nhất cho bạn.'
    },
    {
        q: 'Có thể làm hộ chiếu online không?',
        a: 'Có! Công dân VN có <strong>CCCD gắn chip</strong> có thể nộp hồ sơ online qua Cổng dịch vụ công. Tuy nhiên vẫn cần đến trực tiếp để chụp ảnh và lấy dấu vân tay. Chúng tôi hỗ trợ toàn bộ quy trình.'
    },
    {
        q: 'Hộ chiếu bị mất thì phải làm sao?',
        a: 'Bạn cần làm <strong>đơn báo mất</strong> (chúng tôi hỗ trợ viết), sau đó nộp hồ sơ cấp lại. Dịch vụ khẩn cấp có kết quả trong 24h. Chỉ cần CMND/CCCD bản chính.'
    },
    {
        q: 'Phí dịch vụ đã bao gồm lệ phí nhà nước chưa?',
        a: 'Phí dịch vụ đã bao gồm toàn bộ chi phí: lệ phí nhà nước + phí dịch vụ xử lý gấp. <strong>Không phát sinh thêm chi phí.</strong>'
    },
    {
        q: 'Công ty du lịch / agency có được giá ưu đãi không?',
        a: 'Có! Chúng tôi có chính sách ưu đãi riêng cho <strong>đối tác doanh nghiệp</strong>: giá ưu đãi theo số lượng, hotline ưu tiên, và hợp đồng dịch vụ. Liên hệ để nhận báo giá.'
    },
    {
        q: 'Có cam kết hoàn tiền không?',
        a: 'Có! Chúng tôi cam kết <strong>hoàn 100% phí dịch vụ</strong> nếu không giao hộ chiếu đúng hẹn đã thoả thuận. Cam kết bằng văn bản.'
    }
];

// ── Testimonials ──────────────────────
const TESTIMONIALS = [
    {
        name: 'Anh Minh Tuấn',
        role: 'Quản lý, Cty Du lịch Vietravel',
        text: 'Xử lý 15 hồ sơ HC cho đoàn khách trong 2 ngày. Rất chuyên nghiệp, đúng hẹn 100%.',
        rating: 5
    },
    {
        name: 'Chị Thu Hà',
        role: 'Cá nhân, TP.HCM',
        text: 'Mất hộ chiếu khi sắp bay, nhờ dịch vụ gấp xử lý thần tốc trong 24h. Cứu cả chuyến đi!',
        rating: 5
    },
    {
        name: 'Anh Đức Anh',
        role: 'Agency Du học Úc',
        text: 'Đối tác tin cậy cho tất cả hồ sơ HC du học sinh. Giá hợp lý, quy trình rõ ràng.',
        rating: 5
    }
];

// ── Utility: Format VND ──────────────────────
function formatVND(amount) {
    if (!amount) return 'Liên hệ';
    return new Intl.NumberFormat('vi-VN').format(amount) + ' VND';
}

function getPrice(serviceId, urgencyId) {
    if (PRICING[serviceId] && PRICING[serviceId][urgencyId] !== undefined) {
        return PRICING[serviceId][urgencyId];
    }
    return null;
}

function getServiceById(id) {
    return SERVICES.find(s => s.id === id);
}
