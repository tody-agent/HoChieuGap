#!/usr/bin/env python3
"""Generate topics-200.json with 200 article topic definitions for HoChieuGap."""
import json, os

PROVINCES = [
    "da-nang", "can-tho", "hai-phong", "binh-duong", "dong-nai",
    "khanh-hoa", "quang-ninh", "thua-thien-hue", "nghe-an", "thanh-hoa",
    "bac-ninh", "vinh-phuc", "hung-yen", "thai-nguyen", "lam-dong",
    "ba-ria-vung-tau", "long-an", "tien-giang", "an-giang", "kien-giang",
    "quang-nam", "binh-thuan", "phu-tho", "nam-dinh", "hai-duong",
    "gia-lai", "dak-lak", "binh-dinh", "quang-ngai", "thai-binh"
]
PROVINCE_NAMES = [
    "Đà Nẵng", "Cần Thơ", "Hải Phòng", "Bình Dương", "Đồng Nai",
    "Khánh Hòa", "Quảng Ninh", "Thừa Thiên Huế", "Nghệ An", "Thanh Hóa",
    "Bắc Ninh", "Vĩnh Phúc", "Hưng Yên", "Thái Nguyên", "Lâm Đồng",
    "Bà Rịa - Vũng Tàu", "Long An", "Tiền Giang", "An Giang", "Kiên Giang",
    "Quảng Nam", "Bình Thuận", "Phú Thọ", "Nam Định", "Hải Dương",
    "Gia Lai", "Đắk Lắk", "Bình Định", "Quảng Ngãi", "Thái Bình"
]

COUNTRIES = [
    ("singapore", "Singapore", "miễn visa 30 ngày"),
    ("uc", "Úc", "visa du lịch subclass 600"),
    ("canada", "Canada", "visa du lịch TRV"),
    ("duc", "Đức", "visa Schengen"),
    ("anh-quoc", "Anh Quốc", "visa Standard Visitor"),
    ("phap", "Pháp", "visa Schengen"),
    ("y", "Ý", "visa Schengen"),
    ("tay-ban-nha", "Tây Ban Nha", "visa Schengen"),
    ("new-zealand", "New Zealand", "visa Visitor"),
    ("dai-loan", "Đài Loan", "visa du lịch"),
    ("trung-quoc", "Trung Quốc", "visa du lịch L"),
    ("an-do", "Ấn Độ", "e-Visa"),
    ("campuchia", "Campuchia", "visa on arrival"),
    ("lao", "Lào", "miễn visa 30 ngày"),
    ("myanmar", "Myanmar", "e-Visa"),
    ("philippines", "Philippines", "miễn visa 21 ngày"),
    ("indonesia", "Indonesia", "miễn visa 30 ngày"),
    ("malaysia", "Malaysia", "miễn visa 30 ngày"),
    ("uae", "UAE", "miễn visa 90 ngày"),
    ("qatar", "Qatar", "visa on arrival"),
    ("saudi-arabia", "Saudi Arabia", "e-Visa"),
    ("bo-dao-nha", "Bồ Đào Nha", "visa Schengen"),
    ("ha-lan", "Hà Lan", "visa Schengen"),
    ("thuy-si", "Thụy Sĩ", "visa Schengen"),
    ("thuy-dien", "Thụy Điển", "visa Schengen"),
    ("ba-lan", "Ba Lan", "visa Schengen"),
    ("sec", "Séc", "visa Schengen"),
    ("hungary", "Hungary", "visa Schengen"),
    ("tho-nhi-ky", "Thổ Nhĩ Kỳ", "e-Visa"),
    ("israel", "Israel", "visa du lịch B/2"),
]

topics = []

# --- GROUP 1: Địa phương (30 bài) - P0 ---
for slug, name in zip(PROVINCES, PROVINCE_NAMES):
    topics.append({
        "slug": f"lam-ho-chieu-gap-tai-{slug}",
        "title": f"Làm Hộ Chiếu Gấp Tại {name} — Địa Chỉ, Thủ Tục, Chi Phí 2026",
        "description": f"Hướng dẫn làm hộ chiếu gấp tại {name}. Địa chỉ cơ quan XNC, giờ làm việc, dịch vụ gấp 24h.",
        "cluster": "dia-phuong",
        "keywords": [f"làm hộ chiếu gấp {name}", f"hộ chiếu {name}"],
        "isPillar": slug == "da-nang",
        "readingTime": 6,
        "priority": "P0",
        "prompt_context": f"Viết bài hướng dẫn làm hộ chiếu gấp tại {name}. Bao gồm: địa chỉ Phòng Quản lý Xuất nhập cảnh {name}, giờ làm việc, cách đến (giao thông), thủ tục cụ thể, chi phí, và lý do nên dùng dịch vụ HoChieuGap tại {name}. Nếu là thành phố lớn (Đà Nẵng, Cần Thơ, Hải Phòng) thì thêm nhiều chi tiết hơn."
    })

# --- GROUP 2: Visa theo quốc gia (30 bài) - P0 ---
for slug, name, visa_info in COUNTRIES:
    topics.append({
        "slug": f"ho-chieu-di-{slug}",
        "title": f"Đi {name}: Yêu Cầu Hộ Chiếu, Visa & Checklist Đầy Đủ 2026",
        "description": f"Hướng dẫn chuẩn bị HC + visa đi {name}. Yêu cầu HC, loại visa ({visa_info}), checklist giấy tờ.",
        "cluster": "visa",
        "keywords": [f"hộ chiếu đi {name}", f"visa {name} cho người Việt"],
        "isPillar": slug == "singapore",
        "readingTime": 7,
        "priority": "P0",
        "prompt_context": f"Viết bài hướng dẫn chuẩn bị hộ chiếu và visa đi {name} cho công dân Việt Nam. Thông tin visa: {visa_info}. Bao gồm: yêu cầu hộ chiếu (thời hạn, loại), thủ tục xin visa, hồ sơ cần thiết, thời gian xử lý, chi phí visa, mẹo phỏng vấn (nếu có), và lưu ý quan trọng."
    })

# --- GROUP 3: Tình huống gấp long-tail (25 bài) - P0 ---
URGENT_TOPICS = [
    ("ho-chieu-het-han-khi-dang-o-nuoc-ngoai", "Hộ Chiếu Hết Hạn Khi Đang Ở Nước Ngoài — Xử Lý Khẩn Cấp", "HC hết hạn khi ở nước ngoài. Liên hệ ĐSQ, gia hạn tạm, giấy thông hành.", "hộ chiếu hết hạn ở nước ngoài"),
    ("lam-ho-chieu-khi-cccd-bi-mat", "Làm HC Khi CCCD Bị Mất — Có Cách Nào Không?", "Mất CCCD nhưng cần làm HC gấp. Giải pháp thay thế, giấy tờ bổ sung.", "làm hộ chiếu khi mất CCCD"),
    ("ho-chieu-bi-tu-choi-tai-san-bay", "Bị Từ Chối Lên Máy Bay Vì Hộ Chiếu — Nguyên Nhân & Cách Xử Lý", "Các lý do bị từ chối boarding: HC hết hạn, sai tên, thiếu visa. Cách khắc phục.", "bị từ chối lên máy bay vì hộ chiếu"),
    ("ho-chieu-sai-ten-phai-lam-sao", "Hộ Chiếu Sai Tên So Với Vé Máy Bay — Phải Làm Sao?", "HC sai tên, sai dấu so với vé bay. Cách xử lý nhanh nhất.", "hộ chiếu sai tên"),
    ("ho-chieu-gap-cho-nguoi-benh-nang", "Hộ Chiếu Gấp Cho Người Bệnh Nặng Cần Ra Nước Ngoài", "Xử lý HC khẩn cấp cho bệnh nhân cần chữa bệnh ở nước ngoài.", "hộ chiếu gấp bệnh nặng"),
    ("bay-quoc-te-qua-canh-can-ho-chieu-gi", "Quá Cảnh (Transit) Cần Hộ Chiếu Gì? Visa Transit Là Gì?", "Quy định HC khi transit, quá cảnh qua nước thứ 3. Khi nào cần visa transit.", "quá cảnh cần hộ chiếu gì"),
    ("tre-em-bi-giu-lai-cua-khau-vi-ho-chieu", "Trẻ Em Bị Giữ Lại Cửa Khẩu Vì Hộ Chiếu — Giải Quyết Thế Nào?", "Trẻ bị chặn tại biên giới/sân bay vì HC: thiếu giấy tờ, HC hết hạn.", "trẻ em bị giữ tại cửa khẩu"),
    ("ho-chieu-bi-tich-thu-phai-lam-sao", "Hộ Chiếu Bị Tịch Thu — Khi Nào Xảy Ra & Cách Lấy Lại", "Trường hợp HC bị tịch thu: nợ thuế, vi phạm. Quy trình lấy lại.", "hộ chiếu bị tịch thu"),
    ("ho-chieu-bi-tu-choi-cap", "Bị Từ Chối Cấp Hộ Chiếu — Nguyên Nhân & Cách Khiếu Nại", "5 lý do bị từ chối cấp HC và quy trình khiếu nại.", "bị từ chối cấp hộ chiếu"),
    ("huy-chuyen-bay-vi-ho-chieu-claim-bao-hiem", "Hủy Chuyến Bay Vì HC: Claim Bảo Hiểm Du Lịch Được Không?", "Mất chuyến bay do HC vấn đề. Cách claim bảo hiểm du lịch.", "hủy chuyến bay vì hộ chiếu"),
    ("lam-ho-chieu-khi-mang-thai", "Mang Thai Có Làm Hộ Chiếu Được Không? Có Gì Cần Lưu Ý?", "Phụ nữ mang thai làm HC: quy định, chụp ảnh bụng bầu, di chuyển.", "mang thai làm hộ chiếu"),
    ("ho-chieu-cho-nguoi-dang-nam-vien", "Người Đang Nằm Viện Cần Hộ Chiếu — Dịch Vụ Tại Giường Bệnh", "Làm HC cho người nằm viện: uỷ quyền, chụp ảnh tại viện.", "hộ chiếu cho người nằm viện"),
    ("ho-chieu-cho-nguoi-bi-tam-than", "Người Tâm Thần / Mất Năng Lực Hành Vi — Ai Làm HC Thay?", "Giám hộ làm HC cho người mất năng lực. Giấy tờ pháp lý cần thiết.", "hộ chiếu cho người tâm thần"),
    ("giam-ho-lam-ho-chieu-cho-tre-mo-coi", "Giám Hộ Làm HC Cho Trẻ Mồ Côi — Thủ Tục Đặc Biệt", "Trẻ mồ côi cần HC: người giám hộ hợp pháp, giấy tờ toà án.", "giám hộ làm hộ chiếu cho trẻ mồ côi"),
    ("ho-chieu-sau-ket-hon-doi-ten", "Đổi Tên Trên HC Sau Kết Hôn — Bắt Buộc Không?", "Thay đổi tên/họ trên HC sau kết hôn. Quy trình, chi phí.", "đổi tên hộ chiếu sau kết hôn"),
    ("ho-chieu-sau-ly-hon-doi-ho-con", "Sau Ly Hôn: Đổi Họ Con Trên HC — Quy Trình Pháp Lý", "Đổi họ con trên HC sau ly hôn. Cần quyết định toà, giấy khai sinh mới.", "đổi họ con trên hộ chiếu sau ly hôn"),
    ("bo-me-gia-lan-dau-ra-nuoc-ngoai", "Bố Mẹ Già Lần Đầu Ra Nước Ngoài — Hướng Dẫn HC Toàn Tập", "Hỗ trợ người lớn tuổi lần đầu làm HC: dịch vụ tại nhà, chụp ảnh.", "bố mẹ già lần đầu ra nước ngoài"),
    ("couple-du-lich-honeymoon-can-gi", "Du Lịch Honeymoon: Cặp Đôi Cần Chuẩn Bị HC & Visa Gì?", "Checklist HC + visa honeymoon cho cặp đôi mới cưới.", "hộ chiếu du lịch honeymoon"),
    ("gia-dinh-3-the-he-du-lich-can-biet", "Cả Nhà 3 Thế Hệ Du Lịch — HC Cho Ông Bà, Bố Mẹ, Cháu", "Làm HC cho cả gia đình: ông bà (người cao tuổi), bố mẹ, trẻ em cùng lúc.", "gia đình 3 thế hệ du lịch"),
    ("ho-chieu-cho-3-4-nguoi-cung-luc", "Làm HC Cho 3-4 Người Cùng Lúc — Có Ưu Đãi Giá Tốt Hơn?", "Dịch vụ HC nhóm: giá ưu đãi, tiết kiệm thời gian.", "làm hộ chiếu cho nhóm 3-4 người"),
    ("lam-ho-chieu-khi-dang-co-lenh-cam-xuat-canh", "Đang Có Lệnh Cấm Xuất Cảnh — Có Làm HC Được Không?", "Bị cấm xuất cảnh: có đăng ký HC được không? Cách gỡ lệnh cấm.", "làm hộ chiếu khi cấm xuất cảnh"),
    ("ho-chieu-gap-ngay-le-tet", "Cần HC Gấp Đúng Ngày Lễ/Tết — Cơ Quan Nghỉ, Làm Sao?", "Xử lý HC khẩn cấp khi cơ quan XNC nghỉ lễ. Phương án dự phòng.", "hộ chiếu gấp ngày lễ tết"),
    ("ho-chieu-bi-dinh-nuoc-muc-mo-hong", "HC Bị Dính Nước/Mực/Mờ Hỏng Ở 1 Trang — Còn Dùng Được Không?", "HC bị dính nước, mực lan, mờ 1-2 trang. Đánh giá còn hợp lệ không.", "hộ chiếu bị dính nước mực"),
    ("lam-2-ho-chieu-cung-luc-duoc-khong", "Có Được Làm 2 Hộ Chiếu Cùng Lúc Không? (HC Phổ Thông + Công Vụ)", "Quy định sở hữu nhiều HC: phổ thông + công vụ, hoặc HC cũ + mới.", "làm 2 hộ chiếu cùng lúc"),
    ("ho-chieu-gap-cho-doan-cong-tac-nhieu-nguoi", "HC Gấp Cho Đoàn Công Tác 10-20 Người — Dịch Vụ Doanh Nghiệp", "Xử lý HC hàng loạt cho đoàn công tác doanh nghiệp.", "hộ chiếu gấp đoàn công tác"),
]

for slug, title, desc, kw in URGENT_TOPICS:
    topics.append({
        "slug": slug,
        "title": title,
        "description": desc,
        "cluster": "gap-khan-cap" if "gấp" in title.lower() or "khẩn" in desc.lower() else "gia-dinh",
        "keywords": [kw],
        "isPillar": False,
        "readingTime": 5,
        "priority": "P0",
        "prompt_context": f"Viết bài SEO cho HoChieuGap về: {title}. Mô tả: {desc}. Bao gồm phần FAQ (3+ câu hỏi), bảng chi phí dịch vụ, và CTA liên hệ HoChieuGap."
    })

# --- GROUP 4: FAQ featured snippets (20 bài) - P1 ---
FAQ_TOPICS = [
    ("ho-chieu-co-may-loai", "Hộ Chiếu Có Mấy Loại? Phân Biệt Phổ Thông, Công Vụ, Ngoại Giao", "Phân biệt 3 loại HC chính ở VN: phổ thông, công vụ, ngoại giao.", "hộ chiếu có mấy loại"),
    ("ho-chieu-va-passport-khac-nhau-khong", "Hộ Chiếu Và Passport Có Khác Nhau Không?", "Giải đáp: hộ chiếu = passport. Nguồn gốc từ, cách gọi.", "hộ chiếu và passport khác nhau không"),
    ("ho-chieu-pho-thong-la-gi", "Hộ Chiếu Phổ Thông Là Gì? Ai Được Cấp?", "Giải thích HC phổ thông: đối tượng, phân biệt với HC khác.", "hộ chiếu phổ thông là gì"),
    ("bao-lau-thi-nhan-duoc-ho-chieu", "Bao Lâu Thì Nhận Được Hộ Chiếu? Thời Gian Xử Lý Thực Tế", "Thời gian xử lý HC: đường thường 12 ngày, gấp 24h-72h.", "bao lâu nhận được hộ chiếu"),
    ("co-can-ho-khau-de-lam-ho-chieu-khong", "Có Cần Hộ Khẩu Để Làm HC Không? Quy Định Mới 2026", "Từ 2023 không cần hộ khẩu, chỉ cần CCCD. Quy định mới.", "có cần hộ khẩu làm hộ chiếu"),
    ("ho-chieu-dien-tu-la-gi", "Hộ Chiếu Điện Tử (ePassport) Là Gì? VN Đã Có Chưa?", "ePassport: chip điện tử, sinh trắc học. VN triển khai từ 2023.", "hộ chiếu điện tử là gì"),
    ("kich-thuoc-anh-ho-chieu-bao-nhieu", "Kích Thước Ảnh Hộ Chiếu Chuẩn: Bao Nhiêu cm? Nền Gì?", "Ảnh HC: 4×6cm, nền trắng, không đeo kính. Quy cách chi tiết.", "kích thước ảnh hộ chiếu"),
    ("ho-chieu-viet-nam-di-duoc-bao-nhieu-nuoc", "Hộ Chiếu VN Đi Được Bao Nhiêu Nước Không Cần Visa?", "Passport Index VN 2026: số nước miễn visa, visa on arrival.", "hộ chiếu Việt Nam đi được bao nhiêu nước"),
    ("ho-chieu-va-visa-khac-nhau-the-nao", "Hộ Chiếu Và Visa Khác Nhau Thế Nào? Giải Thích Dễ Hiểu", "Phân biệt HC (giấy tờ tùy thân) vs visa (giấy phép nhập cảnh).", "hộ chiếu và visa khác nhau"),
    ("tai-sao-ho-chieu-co-mau-khac-nhau", "Tại Sao Hộ Chiếu Có Màu Khác Nhau? Ý Nghĩa Từng Màu", "Ý nghĩa màu HC: xanh (phổ thông), đỏ (ngoại giao), xanh lá (công vụ).", "tại sao hộ chiếu có màu khác nhau"),
    ("so-ho-chieu-co-bao-nhieu-so", "Số Hộ Chiếu Có Bao Nhiêu Số? Cách Đọc Mã Số HC", "Mã số HC: 8 ký tự (1 chữ + 7 số). Cách đọc, ý nghĩa.", "số hộ chiếu có bao nhiêu số"),
    ("lam-ho-chieu-co-can-suc-khoe-khong", "Làm HC Có Cần Khám Sức Khỏe Không?", "Không cần khám sức khỏe khi làm HC phổ thông. Chỉ cần cho LĐXK.", "làm hộ chiếu có cần khám sức khỏe"),
    ("ho-chieu-co-the-thay-cmnd-khong", "HC Có Thể Thay Thế CMND/CCCD Trong Nước Không?", "HC vs CCCD: khi nào dùng HC thay CCCD, khi nào không.", "hộ chiếu thay thế CMND"),
    ("lam-ho-chieu-o-dau-nhanh-nhat", "Làm HC Ở Đâu Nhanh Nhất? So Sánh Cơ Quan XNC Cả Nước", "So sánh thời gian xử lý HC giữa các phòng XNC.", "làm hộ chiếu ở đâu nhanh nhất"),
    ("ho-chieu-bi-danh-dau-la-gi", "HC Bị Đánh Dấu Là Gì? Khi Nào Bị Đánh Dấu Cảnh Báo?", "Hệ thống cảnh báo trên HC: nguyên nhân, hậu quả, cách gỡ.", "hộ chiếu bị đánh dấu"),
    ("mat-ho-chieu-co-bi-phat-khong", "Mất HC Có Bị Phạt Tiền Không? Mức Phạt Bao Nhiêu?", "Không phạt hành chính khi mất HC. Chỉ tốn phí cấp lại.", "mất hộ chiếu có bị phạt không"),
    ("ho-chieu-con-trang-nhung-het-han-lam-sao", "HC Còn Nhiều Trang Nhưng Hết Hạn — Xử Lý Thế Nào?", "HC hết hạn dù còn trang: phải cấp mới, không gia hạn.", "hộ chiếu hết hạn còn trang"),
    ("dang-ky-ho-chieu-online-qua-dich-vu-cong", "Đăng Ký HC Online Qua Dịch Vụ Công Quốc Gia — Hướng Dẫn", "Đăng ký HC online tại dichvucong.gov.vn. Từng bước chi tiết.", "đăng ký hộ chiếu online dịch vụ công"),
    ("ho-chieu-cu-con-gia-tri-khong", "HC Cũ (Mẫu Cũ, Đã Cắt Góc) Còn Giá Trị Gì Không?", "HC cũ bị cắt góc: dùng chứng minh lịch sử visa, nhưng không có giá trị pháp lý.", "hộ chiếu cũ còn giá trị không"),
    ("lam-ho-chieu-mat-bao-nhieu-ngay-cong", "Làm HC Mất Bao Nhiêu Ngày Công? Có Cần Nghỉ Làm Không?", "Tự đi: mất 1-2 ngày công. Dịch vụ: chỉ 30 phút giao nhận.", "làm hộ chiếu mất bao nhiêu ngày công"),
]

for slug, title, desc, kw in FAQ_TOPICS:
    topics.append({
        "slug": slug, "title": title, "description": desc,
        "cluster": "faq", "keywords": [kw], "isPillar": False,
        "readingTime": 4, "priority": "P1",
        "prompt_context": f"Viết bài dạng FAQ chi tiết cho HoChieuGap: {title}. Mô tả: {desc}. Tối ưu featured snippet Google. Trả lời ngắn gọn ở đầu bài rồi giải thích chi tiết."
    })

# --- GROUP 5: Doanh nghiệp (15 bài) - P1 ---
BIZ_TOPICS = [
    ("ho-chieu-hang-loat-cho-nhan-vien", "HC Hàng Loạt Cho Nhân Viên: Gói Doanh Nghiệp HoChieuGap"),
    ("hr-guide-lam-ho-chieu-cho-nhan-vien", "HR Guide: Quy Trình Làm HC Cho Nhân Viên Đi Công Tác"),
    ("ho-chieu-cho-startup-founder", "Startup Founder Cần HC Gấp Đi Gọi Vốn — Xử Lý Nhanh"),
    ("ho-chieu-cho-giao-vien-di-tap-huan", "Giáo Viên Đi Tập Huấn Nước Ngoài — HC & Visa A-Z"),
    ("ho-chieu-cho-ky-su-xuat-khau", "Kỹ Sư Xuất Khẩu Nhật/Hàn — Thủ Tục HC Đặc Biệt"),
    ("ho-chieu-cho-nhan-vien-ngan-hang", "Nhân Viên Ngân Hàng Đi Đào Tạo Nước Ngoài — HC & Visa"),
    ("ho-chieu-cho-van-dong-vien", "Vận Động Viên Thi Đấu Quốc Tế — HC & Visa Thể Thao"),
    ("ho-chieu-cho-nghe-si-ca-si", "Nghệ Sĩ/Ca Sĩ Đi Biểu Diễn Nước Ngoài — Work Permit & HC"),
    ("ho-chieu-cho-phong-vien-nha-bao", "Phóng Viên/Nhà Báo Tác Nghiệp Quốc Tế — HC & Visa Báo Chí"),
    ("ho-chieu-cho-truong-doan-du-lich", "Trưởng Đoàn Du Lịch (Tour Leader) — HC Nhiều Lần, Visa Nhiều Nước"),
    ("thanh-toan-ho-chieu-bang-chuyen-khoan-cong-ty", "Thanh Toán HC Bằng Chuyển Khoản Công Ty — Xuất Hoá Đơn VAT"),
    ("ho-chieu-cho-tinh-nguyen-vien-ngo", "Tình Nguyện Viên NGO Đi Nước Ngoài — HC & Giấy Tờ Cần Thiết"),
    ("ho-chieu-cho-tu-nghiep-sinh", "Tu Nghiệp Sinh / Thực Tập Sinh Quốc Tế — Thủ Tục HC"),
    ("ho-chieu-cho-dieu-duong-xkld", "Điều Dưỡng XKLĐ Nhật Bản/Đức — HC + Visa Đặc Biệt"),
    ("ho-chieu-cho-thuyen-truong", "Thuyền Trưởng & Sỹ Quan Tàu Biển — HC Đặc Thù Hàng Hải"),
]
for slug, title in BIZ_TOPICS:
    topics.append({
        "slug": slug, "title": title,
        "description": f"{title}. Hướng dẫn chi tiết từ HoChieuGap.",
        "cluster": "doanh-nghiep", "keywords": [title.split("—")[0].strip() if "—" in title else slug.replace("-", " ")],
        "isPillar": slug == "ho-chieu-hang-loat-cho-nhan-vien",
        "readingTime": 5, "priority": "P1",
        "prompt_context": f"Viết bài cho HoChieuGap: {title}. Hướng dẫn chi tiết cho đối tượng doanh nghiệp/chuyên nghiệp. Bao gồm FAQ, bảng chi phí, CTA."
    })

# --- GROUP 6: Seasonal (15 bài) - P1 ---
SEASONAL = [
    ("ho-chieu-truoc-tet-nguyen-dan-2027", "Làm HC Trước Tết Nguyên Đán 2027 — Deadline & Mẹo"),
    ("ho-chieu-mua-he-2026", "HC Mùa Hè 2026: Cẩn Thận Quá Tải, Làm Sớm Từ Tháng 4"),
    ("ho-chieu-cho-sea-games-2027", "HC Cho SEA Games 2027 — VĐV, HLV & CĐV Cần Biết"),
    ("ho-chieu-nghi-le-30-4-1-5", "Nghỉ Lễ 30/4 - 1/5: Làm HC Kịp Không? Timeline Chi Tiết"),
    ("ho-chieu-mua-giang-sinh-nam-moi", "Du Lịch Giáng Sinh & Năm Mới — Chuẩn Bị HC Từ Bao Giờ?"),
    ("ho-chieu-tet-trung-thu-cho-be", "Tết Trung Thu Đưa Bé Đi Nước Ngoài — HC Cho Bé Chuẩn Bị Sao?"),
    ("ho-chieu-mua-xuat-khau-lao-dong", "Mùa XKLĐ (Tháng 3-6): Làm HC Số Lượng Lớn"),
    ("ho-chieu-mua-tuyen-sinh-du-hoc", "Mùa Tuyển Sinh Du Học (Tháng 8-10): Timeline HC & Visa"),
    ("ho-chieu-truoc-black-friday-du-lich", "Du Lịch Black Friday/11.11 — Đặt Tour Giá Rẻ, HC Có Kịp?"),
    ("ho-chieu-mua-cuoi", "Mùa Cưới (Tháng 10-12): Honeymoon Cần HC & Visa Gì?"),
    ("ho-chieu-cho-fdi-worker", "Nhân Viên FDI Cần HC Gấp Đi Training — Dịch Vụ Express"),
    ("ho-chieu-mua-le-hoi-hoa-da-lat", "Du Lịch Lễ Hội Hoa Đà Lạt — Cần HC Nếu Kết Hợp Tour Nước Ngoài"),
    ("ho-chieu-cho-runner-marathon-quoc-te", "Runner Chạy Marathon Quốc Tế — HC & Visa Chuẩn Bị Sớm"),
    ("ho-chieu-mua-dong-chau-au", "Du Lịch Mùa Đông Châu Âu — HC + Visa Schengen Timeline"),
    ("ho-chieu-cho-tet-duong-lich", "Tết Dương Lịch Du Lịch Ngắn Ngày — HC Cần Bao Lâu?"),
]
for slug, title in SEASONAL:
    topics.append({
        "slug": slug, "title": title,
        "description": f"{title}. Hướng dẫn và timeline từ HoChieuGap.",
        "cluster": "seasonal", "keywords": [slug.replace("-", " ")],
        "isPillar": False, "readingTime": 5, "priority": "P1",
        "prompt_context": f"Viết bài seasonal cho HoChieuGap: {title}. Tập trung vào timeline, deadline, mẹo chuẩn bị sớm. Bao gồm FAQ, CTA."
    })

# --- GROUP 7: So sánh & Review (15 bài) - P1 ---
COMPARE = [
    ("so-sanh-dich-vu-ho-chieu-gap-2026", "So Sánh 5 Dịch Vụ HC Gấp Uy Tín Nhất 2026", "chi-phi"),
    ("ho-chieu-gap-24h-vs-48h-vs-72h", "HC Gấp 24h vs 48h vs 72h — Chọn Gói Nào Phù Hợp?", "chi-phi"),
    ("tu-lam-ho-chieu-online-vs-dich-vu", "Tự Làm HC Online vs Thuê Dịch Vụ — So Sánh Chi Tiết 2026", "chi-phi"),
    ("ho-chieu-gap-ha-noi-vs-tphcm", "HC Gấp Hà Nội vs TP.HCM: Nơi Nào Nhanh Hơn?", "chi-phi"),
    ("chi-phi-an-ho-chieu-it-ai-biet", "5 Chi Phí Ẩn Khi Làm HC Mà Ít Ai Biết", "chi-phi"),
    ("ho-chieu-chip-vs-thuong-khac-gi", "HC Chip vs HC Thường: Khác Gì? Nên Đổi Không?", "chi-phi"),
    ("review-dich-vu-hochieugap-co-tot-khong", "Review Dịch Vụ HoChieuGap: Có Tốt Không? Khách Hàng Nói Gì?", "chi-phi"),
    ("lam-ho-chieu-tai-cuc-vs-phong-xnc", "Nộp Tại Cục XNC vs Phòng XNC Công An Tỉnh — Khác Gì?", "chi-phi"),
    ("ho-chieu-viet-nam-xep-hang-the-gioi", "HC Việt Nam Xếp Hạng Bao Nhiêu Thế Giới? Passport Index 2026", "chi-phi"),
    ("ho-chieu-viet-nam-vs-asean-so-sanh", "HC Việt Nam vs ASEAN: Nước Nào Đi Được Nhiều Nước Nhất?", "chi-phi"),
    ("ho-chieu-truoc-va-sau-2023", "HC Cấp Trước vs Sau 7/2023: Khác Nhau Nhiều Không?", "phap-ly"),
    ("so-sanh-phi-ho-chieu-viet-nam-vs-the-gioi", "Phí Làm HC VN vs Thế Giới: VN Rẻ Hay Đắt?", "chi-phi"),
    ("app-chup-anh-ho-chieu-nao-tot-nhat", "5 App Chụp Ảnh HC Tốt Nhất 2026 — Miễn Phí & Chuẩn Quy Cách", "meo"),
    ("sai-lam-chon-dich-vu-ho-chieu-gia-re", "5 Sai Lầm Khi Chọn DV HC Giá Rẻ — Tiền Mất Tật Mang", "chi-phi"),
    ("dich-vu-ho-chieu-online-co-an-toan-khong", "DV HC Online Có An Toàn Không? Cách Nhận Biết Lừa Đảo", "an-ninh"),
]
for slug, title, cluster in COMPARE:
    topics.append({
        "slug": slug, "title": title,
        "description": f"{title}. Phân tích chi tiết từ HoChieuGap.",
        "cluster": cluster, "keywords": [slug.replace("-", " ")],
        "isPillar": False, "readingTime": 6, "priority": "P1",
        "prompt_context": f"Viết bài so sánh/review cho HoChieuGap: {title}. Dùng bảng so sánh. Bao gồm FAQ, CTA. Tone khách quan nhưng highlight ưu điểm HoChieuGap."
    })

# --- GROUP 8: Digital & ePassport (10 bài) - P2 ---
DIGITAL = [
    ("epassport-viet-nam-tong-quan", "ePassport Việt Nam: Tổng Quan Công Nghệ & Lợi Ích"),
    ("cong-dich-vu-cong-quoc-gia-lam-ho-chieu", "Cổng Dịch Vụ Công Quốc Gia: Đăng Ký HC Online Từng Bước"),
    ("vneid-va-ho-chieu-lien-quan-gi", "VNeID Và Hộ Chiếu: Liên Quan Gì? Có Thay Thế HC Không?"),
    ("ho-chieu-sinh-trac-hoc-la-gi", "HC Sinh Trắc Học Là Gì? Vân Tay & Khuôn Mặt Trên HC"),
    ("xu-huong-ho-chieu-so-2030", "Xu Hướng Hộ Chiếu Số 2030: Digital Travel Credential"),
    ("quet-ho-chieu-bang-nfc-dien-thoai", "Quét HC Bằng NFC Điện Thoại — App Nào Đọc Được Chip HC?"),
    ("tu-dong-hoa-xet-duyet-ho-chieu", "AI & Tự Động Hoá Xét Duyệt HC: Tương Lai Ngành XNC"),
    ("bao-mat-thong-tin-ho-chieu-dien-tu", "Bảo Mật Thông Tin Trên HC Điện Tử: An Toàn Đến Đâu?"),
    ("so-sanh-epassport-cac-nuoc-asean", "So Sánh ePassport ASEAN: Nước Nào Tiên Tiến Nhất?"),
    ("blockchain-ho-chieu-tuong-lai", "Blockchain & Hộ Chiếu: Có Thay Thế HC Giấy Được Không?"),
]
for slug, title in DIGITAL:
    topics.append({
        "slug": slug, "title": title,
        "description": f"{title}. Phân tích chuyên sâu.",
        "cluster": "cong-nghe", "keywords": [slug.replace("-", " ")],
        "isPillar": slug == "epassport-viet-nam-tong-quan",
        "readingTime": 6, "priority": "P2",
        "prompt_context": f"Viết bài công nghệ cho HoChieuGap: {title}. Tone chuyên gia nhưng dễ hiểu. Bao gồm FAQ, CTA."
    })

# --- GROUP 9: Pháp lý cập nhật (10 bài) - P2 ---
LEGAL = [
    ("nghi-dinh-ho-chieu-moi-nhat-2026", "Nghị Định Mới Nhất Về HC 2026 — Thay Đổi Gì?"),
    ("quyen-cong-dan-ve-ho-chieu", "Quyền Công Dân Về HC: Ai Cũng Được Cấp? Trường Hợp Ngoại Lệ?"),
    ("ho-chieu-va-luat-bao-ve-du-lieu-ca-nhan", "HC & Luật Bảo Vệ Dữ Liệu Cá Nhân: Quyền Riêng Tư"),
    ("ho-chieu-cho-nguoi-co-tien-an", "Người Có Tiền Án Có Được Cấp HC Không? Quy Định Chi Tiết"),
    ("ho-chieu-cho-nguoi-bi-truy-na", "Người Bị Truy Nã Có Được Cấp HC? Cấm Xuất Cảnh"),
    ("thu-tuc-huy-ho-chieu-cu", "Thủ Tục Huỷ HC Cũ Đã Không Còn Sử Dụng"),
    ("ho-chieu-cho-tre-bi-bo-roi", "HC Cho Trẻ Bị Bỏ Rơi / Không Rõ Cha Mẹ — Ai Đứng Đơn?"),
    ("quyen-khieu-nai-khi-bi-tu-choi-cap-hc", "Quyền Khiếu Nại Khi Bị Từ Chối Cấp HC — Tìm Hiểu Pháp Luật"),
    ("thoi-han-ho-chieu-viet-nam-5-nam-vs-10-nam", "Thời Hạn HC VN: 5 Năm vs 10 Năm — Ai Được Loại Nào?"),
    ("quoc-tich-kep-va-ho-chieu-viet-nam", "Quốc Tịch Kép & HC Việt Nam: Quy Định Hiện Hành 2026"),
]
for slug, title in LEGAL:
    topics.append({
        "slug": slug, "title": title,
        "description": f"{title}. Cập nhật pháp lý mới nhất.",
        "cluster": "phap-ly", "keywords": [slug.replace("-", " ")],
        "isPillar": False, "readingTime": 5, "priority": "P2",
        "prompt_context": f"Viết bài pháp lý cho HoChieuGap: {title}. Trích dẫn luật/nghị định khi có thể. Tone chuyên nghiệp, chính xác. Bao gồm FAQ, CTA."
    })

# --- GROUP 10: An ninh & Scam (10 bài) - P2 ---
SECURITY = [
    ("nhan-biet-dich-vu-ho-chieu-lua-dao", "Nhận Biết DV HC Lừa Đảo: 7 Dấu Hiệu Cảnh Báo"),
    ("ho-chieu-gia-phat-hien-the-nao", "HC Giả Phát Hiện Thế Nào? Công Nghệ Chống Giả Mạo"),
    ("bao-mat-thong-tin-khi-gui-ho-chieu", "Bảo Mật Khi Gửi HC Qua Dịch Vụ: Checklist An Toàn"),
    ("scam-ho-chieu-online-canh-giac", "Cảnh Giác Lừa Đảo HC Online: FB, Zalo, Website Giả"),
    ("an-toan-ho-chieu-khi-du-lich", "An Toàn HC Khi Du Lịch: Mẹo Chống Mất, Trộm, Sao Chép"),
    ("ho-chieu-va-identity-theft", "HC & Identity Theft: Rủi Ro Khi Bị Lộ Thông Tin HC"),
    ("xu-ly-khi-bi-lua-tien-dich-vu-hc", "Bị Lừa Tiền DV HC: Cách Tố Cáo & Lấy Lại Tiền"),
    ("dich-vu-ho-chieu-co-giay-phep-khong", "DV HC Có Cần Giấy Phép Kinh Doanh? Cách Kiểm Tra Uy Tín"),
    ("cam-nang-chong-gia-mao-ho-chieu", "Cẩm Nang Chống Giả Mạo HC Cho Doanh Nghiệp & Cá Nhân"),
    ("ho-chieu-va-rfid-skimming", "HC Chip & RFID Skimming: Có Bị Đọc Trộm Không?"),
]
for slug, title in SECURITY:
    topics.append({
        "slug": slug, "title": title,
        "description": f"{title}. Hướng dẫn bảo vệ an toàn từ HoChieuGap.",
        "cluster": "an-ninh", "keywords": [slug.replace("-", " ")],
        "isPillar": slug == "nhan-biet-dich-vu-ho-chieu-lua-dao",
        "readingTime": 5, "priority": "P2",
        "prompt_context": f"Viết bài an ninh/cảnh giác cho HoChieuGap: {title}. Tone cảnh báo nhưng không gây hoang mang. Bao gồm checklist, FAQ, CTA."
    })

# --- Check for duplicates with existing posts ---
EXISTING_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'content', 'blog')
existing = set()
if os.path.isdir(EXISTING_DIR):
    existing = {f.replace('.md','') for f in os.listdir(EXISTING_DIR) if f.endswith('.md')}

# Filter out duplicates
new_slugs = set()
unique_topics = []
dupes = []
for t in topics:
    if t["slug"] in existing:
        dupes.append(t["slug"])
    elif t["slug"] in new_slugs:
        dupes.append(f"{t['slug']} (internal dupe)")
    else:
        new_slugs.add(t["slug"])
        unique_topics.append(t)

# Write output
OUT = os.path.join(os.path.dirname(__file__), '..', '..', 'topics-queue', 'topics-200.json')
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(unique_topics, f, ensure_ascii=False, indent=2)

print(f"✅ Generated {len(unique_topics)} unique topics → topics-queue/topics-200.json")
if dupes:
    print(f"⏭ Skipped {len(dupes)} duplicates: {', '.join(dupes[:10])}...")

# Stats
from collections import Counter
clusters = Counter(t["cluster"] for t in unique_topics)
priorities = Counter(t["priority"] for t in unique_topics)
print(f"\n📊 By cluster:")
for c, n in clusters.most_common():
    print(f"   {c}: {n}")
print(f"\n🎯 By priority:")
for p, n in priorities.most_common():
    print(f"   {p}: {n}")
