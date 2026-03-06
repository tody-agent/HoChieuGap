// HoChieuGap — Data Module
// All content, pricing, wizard config, FAQ

const SITE_CONFIG = {
    brand: 'HoChieuGap',
    tagline: 'Bạn lo chuyến đi — Chúng tôi lo hộ chiếu.',
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
        title: 'Cho chúng tôi biết về bạn',
        subtitle: 'Để tư vấn chính xác nhất — bạn chỉ cần chọn 1 lần',
        icon: '👤',
        options: [
            { id: 'individual', label: 'Tôi làm cho bản thân', icon: '🧑', desc: 'Tôi hoặc người thân cần hộ chiếu — không biết bắt đầu từ đâu cũng được' },
            { id: 'travel', label: 'Công ty Du lịch', icon: '✈️', desc: 'Cần xử lý hộ chiếu cho khách tour — số lượng lớn, deadline gấp' },
            { id: 'education', label: 'Agency Giáo dục', icon: '🎓', desc: 'Hộ chiếu cho du học sinh — cần đúng hẹn để kịp visa' },
            { id: 'labor', label: 'Xuất khẩu Lao động', icon: '🏗️', desc: 'Hộ chiếu cho lao động nước ngoài — ổn định, giá tốt theo lô' },
            { id: 'other', label: 'Tổ chức / Doanh nghiệp', icon: '🏢', desc: 'Công ty cần làm HC cho nhân viên hoặc đối tác' }
        ]
    },
    {
        id: 'service-type',
        title: 'Tình huống của bạn là gì?',
        subtitle: 'Đừng lo — dù tình huống nào, chúng tôi đều có giải pháp',
        icon: '📋',
        options: [
            { id: 'new-first', label: 'Chưa có hộ chiếu', icon: '🆕', desc: 'Lần đầu làm hộ chiếu — chúng tôi hướng dẫn từ A đến Z' },
            { id: 'renew-expired', label: 'HC đã hết hạn', icon: '🔄', desc: 'Hết hạn rồi, cần cấp lại gấp cho chuyến đi sắp tới' },
            { id: 'extend', label: 'HC sắp hết hạn / hư', icon: '📝', desc: 'Còn hạn < 6 tháng, hết trang, rách — không đủ để xin visa' },
            { id: 'lost', label: 'Mất hộ chiếu!', icon: '🔍', desc: 'Mất HC rồi — bình tĩnh, chúng tôi xử lý khẩn cấp trong 24h' },
            { id: 'early-pickup', label: 'Đã nộp, cần nhận sớm', icon: '⚡', desc: 'Đã có giấy hẹn nhưng chuyến bay không chờ — cần lấy trước' },
            { id: 'full-package', label: 'Làm hết cho tôi', icon: '🏠', desc: 'Không muốn đi đâu — chúng tôi đến tận nhà, xử lý toàn bộ' },
            { id: 'other', label: 'Tình huống khác', icon: '❓', desc: 'Kể cho chúng tôi — chưa biết gì cũng không sao' }
        ]
    },
    {
        id: 'urgency',
        title: 'Bạn cần gấp thế nào?',
        subtitle: 'Chọn thời gian phù hợp — chúng tôi cam kết đúng hẹn hoặc hoàn tiền',
        icon: '⏰',
        options: [
            { id: '1-day', label: 'Ngày mai phải có!', icon: '🔥', desc: 'Bay ngày kia? Chúng tôi xử lý trong 24h', tag: 'Gấp nhất', tagColor: '#D4A853' },
            { id: '2-day', label: 'Cần trong 2 ngày', icon: '🕐', desc: 'Còn 2 ngày — đủ thời gian, yên tâm' },
            { id: '3-day', label: 'Khoảng 3 ngày', icon: '📅', desc: 'Không quá gấp — tiết kiệm chi phí hơn' },
            { id: 'consult', label: 'Chưa biết — tư vấn giúp', icon: '💬', desc: 'Không chắc cần bao lâu? Gọi cho chúng tôi, tư vấn miễn phí' }
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
        shortDesc: 'Đã nộp hồ sơ rồi nhưng chuyến bay không chờ? Chúng tôi lấy sớm cho bạn.',
        details: [
            'Có giấy hẹn rồi — không cần chờ đủ 12 ngày',
            'Bay gấp? Nhận HC sớm nhất trong 24h',
            'Bạn không cần đi lại — chúng tôi xử lý'
        ],
        docs: ['Giấy hẹn trả kết quả', 'CMND/CCCD bản chính']
    },
    {
        id: 'extend',
        title: 'HC sắp hết hạn / hư hỏng',
        icon: '📝',
        shortDesc: 'Còn dưới 6 tháng? Hết trang? Rách? Đổi ngay kẻo lỡ visa.',
        details: [
            'HC còn hạn dưới 6 tháng — nhiều nước từ chối visa',
            'Hết trang, rách, ướt — cần đổi mới gấp',
            'Thay đổi thông tin cá nhân — chúng tôi lo thủ tục'
        ],
        docs: ['Hộ chiếu cũ bản chính', 'CMND/CCCD bản chính', 'Sao chụp hộ khẩu']
    },
    {
        id: 'lost',
        title: 'Mất hộ chiếu — Đừng hoảng',
        icon: '🔍',
        shortDesc: 'Mất HC đúng lúc cần đi? Bình tĩnh — 24h có HC mới.',
        details: [
            'Hộ khẩu TP.HCM hay ngoại tỉnh đều làm được',
            'Chỉ cần CMND/CCCD — không cần công chứng',
            'Chúng tôi hỗ trợ viết đơn báo mất luôn'
        ],
        docs: ['CMND/CCCD bản chính', 'Sao chụp hộ khẩu', 'Đơn báo mất (hỗ trợ làm)']
    },
    {
        id: 'new-first',
        title: 'Làm HC lần đầu / Cấp lại',
        icon: '🆕',
        shortDesc: 'Chưa từng có HC? HC hết hạn? Không biết thủ tục? Chúng tôi lo từ A-Z.',
        details: [
            'Lần đầu làm hộ chiếu — chúng tôi hướng dẫn mọi bước',
            'HC hết hạn cần cấp lại — nhanh nhất 24h',
            'Người lớn tuổi, bận rộn — chúng tôi xử lý thay'
        ],
        docs: ['Tờ khai TK01/TK01a', 'CMND/CCCD bản chính', 'Ảnh 4x6 nền trắng', 'Sao chụp hộ khẩu']
    },
    {
        id: 'full-package',
        title: 'Ngồi nhà — Chúng tôi đến tận nơi',
        icon: '🏠',
        shortDesc: 'Không muốn đi đâu? Chúng tôi đến nhà, làm hết, giao HC tận tay.',
        details: [
            'Đến tận nhà hoặc văn phòng — bạn không cần đi đâu',
            'Điền đơn, chuẩn bị hồ sơ, nộp hồ sơ thay bạn',
            'Đặc biệt phù hợp cho người lớn tuổi hoặc bận rộn'
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
        title: 'Gọi cho chúng tôi — Không cần chuẩn bị gì',
        desc: 'Bấm gọi, nhắn Zalo, hoặc điền form. Kể tình huống của bạn — chúng tôi tư vấn miễn phí, hướng dẫn từng bước.',
        icon: '📞',
        duration: '5 phút'
    },
    {
        step: 2,
        title: 'Chuẩn bị giấy tờ — Có người hướng dẫn',
        desc: 'Chúng tôi gửi checklist rõ ràng. Thiếu gì bổ sung nấy. Dịch vụ trọn gói — đến tận nhà nhận giấy tờ.',
        icon: '📁',
        duration: '30 phút'
    },
    {
        step: 3,
        title: 'Ngồi chờ — Chúng tôi lo hết',
        desc: 'Nộp hồ sơ, theo dõi tiến độ, xử lý mọi vấn đề phát sinh. Bạn không cần đi đâu, không cần lo gì.',
        icon: '⚙️',
        duration: '1-3 ngày'
    },
    {
        step: 4,
        title: 'Cầm hộ chiếu — Sẵn sàng lên đường ✈️',
        desc: 'Nhận hộ chiếu đúng hẹn — giao tận tay hoặc nhận tại văn phòng. Trễ hẹn? Hoàn tiền 100%.',
        icon: '✅',
        duration: 'Đúng hẹn'
    }
];

// ── FAQ ──────────────────────
const FAQ_ITEMS = [
    {
        q: 'Tôi lớn tuổi, không biết thủ tục gì cả — có được hỗ trợ tận nơi không?',
        a: '<strong>Hoàn toàn được!</strong> Chúng tôi có dịch vụ <strong>trọn gói tại nhà</strong> — đến tận nơi nhận giấy tờ, điền đơn thay bạn, nộp hồ sơ và giao HC tận tay. Bạn không cần biết gì về thủ tục. Chỉ cần gọi một cuộc điện thoại.'
    },
    {
        q: 'Mai bay rồi, hôm nay làm có kịp không?',
        a: 'Tuỳ tình huống cụ thể — nhưng chúng tôi đã xử lý thành công hàng trăm ca gấp trong <strong>24h</strong>. Gọi ngay hotline <strong>0909 123 456</strong> để được tư vấn phương án nhanh nhất, kể cả ngoài giờ hành chính.'
    },
    {
        q: 'Thời gian cấp hộ chiếu nhanh nhất là bao lâu?',
        a: 'Nhanh nhất là <strong>24h</strong> — cam kết đúng hẹn hoặc hoàn tiền 100%. Ngoài ra có gói 48h và 72h tuỳ ngân sách.'
    },
    {
        q: 'Tôi ở ngoại tỉnh, có làm được hộ chiếu gấp tại TP.HCM không?',
        a: '<strong>Được!</strong> Bất kể hộ khẩu đâu, chúng tôi đều hỗ trợ. Chỉ cần <strong>CMND/CCCD bản chính</strong> và <strong>sao chụp hộ khẩu</strong> (không cần công chứng). Nhiều khách ngoại tỉnh đã hoàn thành trong 24-48h.'
    },
    {
        q: 'Hộ chiếu bị mất thì phải làm sao?',
        a: '<strong>Đừng hoảng.</strong> Bạn chỉ cần gọi cho chúng tôi — chúng tôi sẽ hỗ trợ viết <strong>đơn báo mất</strong>, nộp hồ sơ cấp lại, và có thể có HC mới trong 24h. Chỉ cần CMND/CCCD bản chính.'
    },
    {
        q: 'Phí dịch vụ đã bao gồm lệ phí nhà nước chưa?',
        a: '<strong>Đã bao gồm tất cả</strong> — lệ phí nhà nước + phí dịch vụ xử lý gấp. Bạn trả 1 lần duy nhất, không phát sinh, không bất ngờ. Cam kết bằng văn bản.'
    },
    {
        q: 'Công ty chúng tôi cần làm hàng chục hồ sơ mỗi tháng — có ưu đãi không?',
        a: '<strong>Có!</strong> Chúng tôi có chính sách riêng cho doanh nghiệp: giá <strong>ưu đãi 20-35%</strong> theo số lượng, account manager riêng, hotline ưu tiên, hợp đồng SLA, xuất VAT. Liên hệ để nhận báo giá.'
    },
    {
        q: 'Có cam kết hoàn tiền nếu làm trễ hẹn không?',
        a: '<strong>Cam kết 100%!</strong> Nếu không giao hộ chiếu đúng hẹn đã thoả thuận — hoàn lại toàn bộ phí dịch vụ. Cam kết bằng văn bản, rõ ràng, minh bạch.'
    },
    {
        q: 'CMND/CCCD hết hạn có làm được hộ chiếu không?',
        a: 'CMND/CCCD là giấy tờ bắt buộc. Nếu hết hạn, bạn cần làm lại CCCD trước. <strong>Đừng lo</strong> — chúng tôi sẽ tư vấn phương án nhanh nhất, kể cả hỗ trợ làm CCCD gấp.'
    },
    {
        q: 'Có thể làm hộ chiếu online không?',
        a: 'Công dân VN có <strong>CCCD gắn chip</strong> có thể nộp hồ sơ online qua Cổng dịch vụ công. Tuy nhiên vẫn cần đến trực tiếp để chụp ảnh và lấy dấu vân tay. Chúng tôi hỗ trợ toàn bộ — bạn chỉ cần đi 1 lần.'
    }
];

// ── Testimonials ──────────────────────
const TESTIMONIALS = [
    {
        name: 'Cô Thanh Lan, 58 tuổi',
        role: 'Cá nhân, Q. Bình Thạnh',
        text: 'Tôi không biết gì về thủ tục, con cháu thì bận. Gọi điện xong, họ đến tận nhà làm hết cho tôi. Giờ tôi đã có hộ chiếu đi thăm con ở Úc rồi!',
        rating: 5
    },
    {
        name: 'Tuấn, 26 tuổi',
        role: 'Nhân viên văn phòng, Q.1',
        text: 'Lười xếp hàng, sợ mất ngày nghỉ. Nhắn Zalo buổi sáng, chiều đã có người liên hệ, 2 ngày sau nhận HC. Nhanh gọn lẹ, đi Bali kịp!',
        rating: 5
    },
    {
        name: 'Anh Minh Tuấn',
        role: 'Quản lý, Cty Du lịch Vietravel',
        text: 'Xử lý 15 hồ sơ HC cho đoàn khách trong 2 ngày. Rất chuyên nghiệp, đúng hẹn 100%. Giờ hợp tác cố định hàng tháng rồi.',
        rating: 5
    },
    {
        name: 'Chị Thu Hà',
        role: 'Cá nhân, TP.HCM',
        text: 'Mất hộ chiếu đúng lúc sắp bay — hoảng lắm! Gọi lúc 7h tối, họ vẫn nhận xử lý. 24h sau có HC mới. Cứu cả chuyến đi của gia đình!',
        rating: 5
    },
    {
        name: 'Chị Phương Anh',
        role: 'Trưởng phòng HR, Cty ABC Corp',
        text: 'Mỗi tháng 30+ hồ sơ HC cho nhân viên đi công tác. Có account manager riêng, báo tiến độ qua Zalo. Ổn định, uy tín, không phải lo lắng gì.',
        rating: 5
    },
    {
        name: 'Anh Đức Anh',
        role: 'Giám đốc, Agency Du học Úc',
        text: 'Đối tác tin cậy cho tất cả hồ sơ HC du học sinh. Giá tốt theo lô, quy trình rõ ràng. Các em kịp deadline visa 100%.',
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
