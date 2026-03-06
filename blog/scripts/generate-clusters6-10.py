#!/usr/bin/env python3
"""Generate Clusters 6-10 for HoChieuGap blog (50 articles)."""
import os, json

DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'content', 'blog')

TOPICS = [
# ── CLUSTER 6: Du Lịch & Mùa Vụ ──
("du-lich-he-can-ho-chieu-gi","Du Lịch Hè: Chuẩn Bị HC Bao Lâu Trước Chuyến Đi?","Timeline chuẩn bị HC cho mùa du lịch hè. Tránh quá tải, mẹo nhanh.","du-lich",["hộ chiếu du lịch hè"],True,6),
("quoc-gia-mien-visa-ho-chieu-viet-nam","Danh Sách Nước Miễn Visa Cho Hộ Chiếu Việt Nam 2026","Cập nhật danh sách quốc gia miễn visa cho HCVN. Điều kiện, thời gian lưu trú.","du-lich",["nước miễn visa hộ chiếu việt nam"],False,7),
("lam-ho-chieu-truoc-tet","Làm Hộ Chiếu Trước Tết: Vì Sao Nên Làm Từ Tháng 11?","Gợi ý chuẩn bị HC trước Tết cho du lịch xuân. Lịch nghỉ cơ quan XNC.","du-lich",["làm hộ chiếu trước tết"],False,5),
("ho-chieu-di-thai-lan","Đi Thái Lan Cần Gì? Hộ Chiếu, Visa, Checklist Du Lịch","Checklist đầy đủ đi Thái Lan: HC, visa (miễn visa), bảo hiểm.","du-lich",["hộ chiếu đi thái lan"],False,5),
("ho-chieu-di-han-quoc","Đi Hàn Quốc: Yêu Cầu HC, Visa, Giấy Tờ Tài Chính","Hộ chiếu đi Hàn Quốc: thời hạn, visa, chứng minh tài chính.","du-lich",["hộ chiếu đi hàn quốc"],False,5),
("ho-chieu-di-nhat-ban","Đi Nhật Bản 2026: HC Cần Bao Lâu, Visa Tự Xin Hay Qua DV?","Hướng dẫn HC + visa Nhật Bản. Yêu cầu, timeline, mẹo xin visa.","du-lich",["hộ chiếu đi nhật bản"],False,5),
("ho-chieu-du-lich-chau-au","Du Lịch Châu Âu (Schengen): HC + Visa Cần Chuẩn Bị Gì?","Checklist HC + visa Schengen cho du lịch châu Âu. Timeline chi tiết.","du-lich",["hộ chiếu du lịch châu âu"],False,6),
("ho-chieu-di-my","Hộ Chiếu Đi Mỹ: Yêu Cầu, Visa B1/B2, Phỏng Vấn ĐSQ","Chuẩn bị HC + visa Mỹ. Yêu cầu HC, lịch phỏng vấn, mẹo pass.","du-lich",["hộ chiếu đi mỹ"],False,6),
("ho-chieu-mua-le-hoi","Làm HC Mùa Lễ Hội — Thời Gian Chờ Lâu Hơn Bình Thường?","Cảnh báo thời gian chờ HC dài hơn vào mùa lễ hội, Tết, hè.","du-lich",["hộ chiếu mùa lễ hội"],False,4),
("checklist-ho-chieu-truoc-chuyen-di","Checklist Kiểm Tra Hộ Chiếu Trước Mỗi Chuyến Đi","Danh sách kiểm tra HC trước khi bay: hạn, trang, visa, ảnh...","du-lich",["checklist hộ chiếu trước chuyến đi"],False,4),

# ── CLUSTER 7: Chi Phí & So Sánh ──
("chi-phi-lam-ho-chieu-2026","Bảng Giá Làm Hộ Chiếu 2026: Từ 200K Đến Trọn Gói 5.5 Triệu","Tổng hợp chi phí HC 2026: lệ phí, phí dịch vụ, phí gia hạn, cấp mới.","chi-phi",["chi phí làm hộ chiếu 2026","bảng giá hộ chiếu"],True,6),
("ho-chieu-dich-vu-uy-tin","Dịch Vụ Hộ Chiếu Gấp Uy Tín: Cách Chọn Đúng, Tránh Lừa","Tiêu chí chọn DV HC uy tín. Dấu hiệu nhận biết DV không đáng tin.","chi-phi",["dịch vụ hộ chiếu uy tín"],False,5),
("ho-chieu-tu-di-hay-thue-dv","Làm HC Tự Đi Hay Thuê Dịch Vụ? So Sánh Chi Tiết","So sánh tự đi vs dịch vụ: thời gian, chi phí, rủi ro, phù hợp ai.","chi-phi",["làm hộ chiếu tự đi hay thuê dịch vụ"],False,5),
("le-phi-ho-chieu-theo-loai","Lệ Phí HC Theo Loại: Phổ Thông, Chip, Trẻ Em, Mất, Đổi","Bảng lệ phí nhà nước cho từng loại HC. Cập nhật mới nhất 2026.","chi-phi",["lệ phí hộ chiếu theo loại"],False,4),
("dich-vu-ho-chieu-tai-nha","Dịch Vụ HC Tại Nhà: Tiện Lợi, Nhưng Chi Phí Bao Nhiêu?","Dịch vụ trọn gói tại nhà: quy trình, chi phí, ai nên dùng.","chi-phi",["dịch vụ hộ chiếu tại nhà"],False,4),
("ho-chieu-cho-doanh-nghiep","Gói Dịch Vụ HC Cho Doanh Nghiệp: Nhiều Nhân Viên, Giá Ưu Đãi","Chính sách HC cho DN: số lượng lớn, ưu đãi, thanh toán linh hoạt.","chi-phi",["hộ chiếu cho doanh nghiệp"],False,4),
("phu-phi-ho-chieu","Các Khoản Phụ Phí Khi Làm HC Mà Ít Ai Biết","Phụ phí ảnh, photocopy, đi lại... Cách tính tổng chi phí thực tế.","chi-phi",["phụ phí hộ chiếu"],False,3),
("ho-chieu-gia-re-nhat","Cách Làm HC Giá Rẻ Nhất: Tiết Kiệm Tối Đa Chi Phí","Mẹo tiết kiệm khi làm HC: chụp ảnh online, nộp online, tự điền TK01.","chi-phi",["làm hộ chiếu giá rẻ nhất"],False,4),
("tra-gop-ho-chieu","Trả Góp Phí Dịch Vụ HC Gấp — Có Được Không?","Chính sách thanh toán: chuyển khoản, trả góp, COD, thanh toán công ty.","chi-phi",["trả góp hộ chiếu"],False,3),
("hoan-tien-ho-chieu","Chính Sách Hoàn Tiền 100% Nếu Trễ Hẹn — Cam Kết HoChieuGap","Chi tiết chính sách hoàn tiền cam kết của HoChieuGap khi trễ hẹn.","chi-phi",["hoàn tiền hộ chiếu trễ hẹn"],False,3),

# ── CLUSTER 8: Thủ Tục & Pháp Lý ──
("quy-dinh-ho-chieu-2026","Quy Định Mới Về Hộ Chiếu 2026 — Những Thay Đổi Cần Biết","Tổng hợp thay đổi pháp lý về HC 2026. Chip, mẫu mới, quy trình.","phap-ly",["quy định hộ chiếu 2026"],True,6),
("cccd-gan-chip-ho-chieu","CCCD Gắn Chip Có Ảnh Hưởng Gì Đến Thủ Tục Làm HC?","Mối liên hệ CCCD chip vs HC. Ưu điểm khi có CCCD chip.","phap-ly",["CCCD gắn chip hộ chiếu"],False,4),
("cam-xuat-canh-ho-chieu","Ai Bị Cấm Xuất Cảnh? Có Trường Hợp Nào Không Được Cấp HC?","Danh sách trường hợp bị cấm xuất cảnh, không cấp HC. Cách kiểm tra.","phap-ly",["cấm xuất cảnh hộ chiếu"],False,5),
("to-khai-tk01a-tre-em","Tờ Khai TK01a Cho Trẻ Em: Khác Gì TK01? Cách Điền Đúng","So sánh TK01 vs TK01a. Hướng dẫn điền TK01a cho trẻ em.","phap-ly",["tờ khai TK01a trẻ em"],False,4),
("ho-chieu-cong-vu","Hộ Chiếu Công Vụ: Ai Được Cấp? Khác HC Phổ Thông Thế Nào?","Phân biệt HC công vụ vs phổ thông. Điều kiện, quyền lợi.","phap-ly",["hộ chiếu công vụ"],False,4),
("ho-chieu-ngoai-giao","Hộ Chiếu Ngoại Giao: Dành Cho Ai? Đặc Quyền Gì?","HC ngoại giao: đối tượng, đặc quyền, khác biệt với HC phổ thông.","phap-ly",["hộ chiếu ngoại giao"],False,4),
("luat-xuat-nhap-canh-2019","Luật Xuất Nhập Cảnh 2019 (Sửa Đổi): Điểm Chính Cần Biết","Tóm tắt Luật XNC 2019 ảnh hưởng đến thủ tục HC. Quyền, nghĩa vụ.","phap-ly",["luật xuất nhập cảnh 2019"],False,5),
("ho-chieu-cho-nguoi-nuoc-ngoai","Người Nước Ngoài Tại VN Cần Gia Hạn Visa/HC — Hướng Dẫn","Hướng dẫn cho người nước ngoài sống tại VN cần gia hạn giấy tờ.","phap-ly",["hộ chiếu cho người nước ngoài tại việt nam"],False,5),
("giay-thong-hanh","Giấy Thông Hành Là Gì? Khi Nào Cần? Khác HC Thế Nào?","Phân biệt giấy thông hành vs hộ chiếu. Trường hợp cấp giấy thông hành.","phap-ly",["giấy thông hành"],False,4),
("kinh-nghiem-nop-ho-chieu-online","Kinh Nghiệm Nộp Hồ Sơ HC Online: Tránh Lỗi Phổ Biến","Mẹo nộp HC online thành công. Lỗi thường gặp và cách xử lý.","phap-ly",["kinh nghiệm nộp hộ chiếu online"],False,4),

# ── CLUSTER 9: Theo Nghề Nghiệp / Đối Tượng ──
("ho-chieu-cho-lao-dong-xuat-khau","Hộ Chiếu Cho Lao Động Xuất Khẩu: Thủ Tục, Yêu Cầu Đặc Biệt","HC cho LĐXK: hồ sơ, yêu cầu sức khoẻ, phối hợp với công ty phái cử.","nghe-nghiep",["hộ chiếu lao động xuất khẩu"],True,6),
("ho-chieu-du-hoc","Hộ Chiếu Cho Du Học Sinh: Timeline Chuẩn Bị Tối Ưu","Timeline làm HC + visa du học. Khi nào bắt đầu, deadline quan trọng.","nghe-nghiep",["hộ chiếu du học sinh"],False,5),
("ho-chieu-cho-phi-cong","HC Cho Phi Công & Tiếp Viên: Hết Trang Visa Xử Lý Sao?","HC nghề hàng không: hết trang nhanh, cấp đổi gấp, traveler program.","nghe-nghiep",["hộ chiếu cho phi công"],False,4),
("ho-chieu-cho-thuyen-vien","HC Cho Thuyền Viên/Hải Quân: Giấy Tờ Đặc Biệt Cần Biết","Thuyền viên cần HC + sổ thuyền viên. Thủ tục khác biệt.","nghe-nghiep",["hộ chiếu cho thuyền viên"],False,4),
("ho-chieu-cho-tu-do","Freelancer / Tự Do Làm HC: Không Có Xác Nhận Công Ty","Người tự do, freelancer làm HC: không cần xác nhận cơ quan.","nghe-nghiep",["freelancer làm hộ chiếu"],False,4),
("ho-chieu-cho-huu-tri","Người Hưu Trí Làm HC Đi Du Lịch: Đơn Giản Hơn Bạn Nghĩ","Người hưu trí làm HC: hồ sơ, dịch vụ tại nhà, mẹo cho người lớn tuổi.","nghe-nghiep",["người hưu trí làm hộ chiếu"],False,4),
("ho-chieu-cho-quan-nhan","Quân Nhân Làm Hộ Chiếu Phổ Thông: Thủ Tục Khác Gì?","Quân nhân, công an muốn làm HC phổ thông: thủ tục xin phép đơn vị.","nghe-nghiep",["quân nhân làm hộ chiếu"],False,4),
("viet-kieu-lam-ho-chieu-vn","Việt Kiều Về VN Cần HC VN Hay HC Nước Ngoài? Quy Định 2026","Việt kiều: dùng HC nước ngoài hay đăng ký HC VN. Quy định mới nhất.","nghe-nghiep",["việt kiều làm hộ chiếu"],False,5),
("ho-chieu-cho-nguoi-khuyet-tat","Người Khuyết Tật Làm HC: Quy Trình Ưu Tiên & Hỗ Trợ","Quy trình ưu tiên cho người khuyết tật. Hỗ trợ tại nhà.","nghe-nghiep",["người khuyết tật làm hộ chiếu"],False,4),
("ho-chieu-cho-bac-si","Bác Sĩ / Y Tá Đi Hội Nghị Y Khoa Quốc Tế: Chuẩn Bị HC & Visa","HC cho nhân viên y tế đi hội nghị quốc tế. Timeline tối ưu.","nghe-nghiep",["bác sĩ làm hộ chiếu"],False,4),

# ── CLUSTER 10: Mẹo & Kinh Nghiệm ──
("meo-chup-anh-ho-chieu","10 Mẹo Chụp Ảnh Hộ Chiếu Đẹp Tại Nhà — AI Tự Crop","Mẹo chụp ảnh HC đẹp tại nhà. Dùng tool AI crop ảnh chuẩn 4×6.","meo",["mẹo chụp ảnh hộ chiếu đẹp"],True,5),
("sai-lam-pho-bien-lam-ho-chieu","7 Sai Lầm Phổ Biến Khi Làm HC — Tránh Để Khỏi Mất Công","Những sai lầm hay gặp: thiếu giấy tờ, ảnh sai, sai thông tin...","meo",["sai lầm khi làm hộ chiếu"],False,5),
("bao-quan-ho-chieu","Cách Bảo Quản Hộ Chiếu: Bao, Túi, Nơi Cất, Chống Mất","Mẹo giữ HC an toàn: bao HC, nơi cất, chụp backup, chống mất.","meo",["cách bảo quản hộ chiếu"],False,4),
("xep-hang-lam-ho-chieu-nhanh","Xếp Hàng Làm HC: Mẹo Tránh Đông, Không Chờ Quá 30 Phút","Mẹo chọn thời điểm, đăng ký online, tối ưu thời gian xếp hàng.","meo",["xếp hàng làm hộ chiếu nhanh"],False,4),
("app-ho-chieu-can-biet","Top 3 App Cần Có Khi Làm Hộ Chiếu: VNeID, DVCQG, HoChieuGap","Danh sách app hỗ trợ: VNeID, Cổng DVCQG, HoChieuGap. Công dụng.","meo",["app làm hộ chiếu"],False,4),
("kinh-nghiem-lam-ho-chieu-lan-dau","Kinh Nghiệm Thực Tế: Tôi Đã Làm HC Lần Đầu Thế Nào?","Chia sẻ kinh nghiệm HC lần đầu, từ chuẩn bị đến nhận kết quả.","meo",["kinh nghiệm làm hộ chiếu lần đầu"],False,5),
("ho-chieu-va-cmnd-cccd","Phân Biệt: CMND, CCCD, Hộ Chiếu — Khi Nào Dùng Giấy Nào?","So sánh CMND vs CCCD vs HC. Mục đích sử dụng, khi nào cần cái nào.","meo",["phân biệt CMND CCCD hộ chiếu"],False,4),
("lam-ho-chieu-trong-1-ngay","Có Thể Làm HC Trong 1 Ngày? Thực Tế vs Quảng Cáo","Sự thật về 'HC trong 1 ngày'. Khi nào khả thi, khi nào không.","meo",["làm hộ chiếu trong 1 ngày"],False,4),
("sao-chep-ho-chieu","Nên Photocopy/Scan Hộ Chiếu Không? Lưu Trữ Digital Thế Nào?","Mẹo backup HC: scan, photo, lưu Cloud. Phòng trường hợp mất.","meo",["scan hộ chiếu lưu điện thoại"],False,3),
("mang-theo-ho-chieu-khi-nao","Ngoài Đi Nước Ngoài, Khi Nào Nên Mang HC Theo Người?","Các tình huống cần HC ngoài bay: nhận visa, đổi tiền, khách sạn...","meo",["khi nào cần mang hộ chiếu"],False,3),
]

CLUSTER_CONTENT = {
    "du-lich": ("Chuẩn bị hộ chiếu đúng cách là bước đầu tiên cho mọi chuyến đi nước ngoài. Bài viết giúp bạn lên kế hoạch phù hợp theo mùa và điểm đến.", "- Du khách chuẩn bị chuyến đi nước ngoài\n- Gia đình du lịch mùa hè, Tết\n- Người đi công tác theo mùa", "| Vé máy bay/booking | Để chứng minh chuyến đi | ❗ Nếu cần |"),
    "chi-phi": ("Chi phí làm hộ chiếu phụ thuộc vào loại HC, dịch vụ gấp, và các phụ phí kèm theo. Bài viết giúp bạn tính đúng và chọn phương án tối ưu.", "- Người muốn biết chi phí chính xác\n- So sánh tự đi vs dịch vụ\n- Doanh nghiệp cần báo giá", ""),
    "phap-ly": ("Quy định về hộ chiếu thay đổi theo từng năm. Cập nhật đúng giúp bạn tránh rủi ro bị trả hồ sơ hoặc từ chối xuất cảnh.", "- Mọi công dân cần cập nhật quy định mới\n- Người gặp vấn đề pháp lý\n- Cán bộ nhà nước, quân nhân", ""),
    "nghe-nghiep": ("Từng nhóm đối tượng có yêu cầu và quy trình HC khác nhau. Bài viết hướng dẫn cụ thể theo nghề nghiệp và hoàn cảnh.", "- Lao động xuất khẩu\n- Du học sinh, freelancer\n- Quân nhân, Việt kiều, người khuyết tật", "| Giấy tờ nghề nghiệp | Tuỳ đối tượng | ❗ Nếu cần |"),
    "meo": ("Kinh nghiệm thực tế giúp bạn làm HC nhanh hơn, tránh sai sót, tiết kiệm thời gian và chi phí.", "- Người làm HC lần đầu\n- Muốn tiết kiệm thời gian\n- Cần mẹo thực tế, đã kiểm chứng", ""),
}

TEMPLATE = """## Tổng quan

{intro}

## Đối tượng áp dụng

{audience}

## Hồ sơ cần chuẩn bị

| Giấy tờ | Yêu cầu | Bắt buộc |
|---------|---------|---------|
| CCCD bản chính | Còn hiệu lực | ✅ |
| Tờ khai TK01 | Bản chính, đầy đủ | ✅ |
| Ảnh 4×6 nền trắng | Chụp trong 6 tháng | ✅ |
{extra}

## Quy trình thực hiện

### Bước 1: Tư vấn miễn phí
Gọi **0909 123 456** hoặc nhắn Zalo để tư vấn tình huống cụ thể.

### Bước 2: Chuẩn bị hồ sơ
Chuẩn bị giấy tờ theo hướng dẫn — dịch vụ hỗ trợ điền tờ khai.

### Bước 3: Nộp & xử lý
Chúng tôi nộp tại cơ quan XNC, theo dõi tiến độ real-time.

### Bước 4: Nhận kết quả
Giao tận tay hoặc nhận tại văn phòng. Cam kết đúng hẹn.

## Chi phí

| Gói | Thời gian | Chi phí |
|-----|----------|---------|
| Gấp 24h | 1 ngày | Từ 2.300.000 VND |
| Gấp 48h | 2 ngày | Từ 1.600.000 VND |
| Gấp 72h | 3 ngày | Từ 1.100.000 VND |

> Giá trọn gói, không phát sinh. Cam kết hoàn 100% phí dịch vụ nếu trễ hẹn.

## Kết luận

Liên hệ **HoChieuGap** để được tư vấn và hỗ trợ nhanh nhất:
- 📞 **0909 123 456** | 💬 [Zalo](https://zalo.me/0909123456) | 📝 [Gửi yêu cầu](https://hochieugap.vn/#contact)"""

def gen(slug, title, desc, cluster, kws, pillar, rt):
    path = os.path.join(DIR, f"{slug}.md")
    if os.path.exists(path):
        return False
    intro, audience, extra = CLUSTER_CONTENT.get(cluster, ("","",""))
    body = TEMPLATE.format(intro=intro, audience=audience, extra=extra)
    fm = f"""---
title: '{title}'
description: '{desc}'
pubDate: 2026-03-02
cluster: '{cluster}'
keywords: {json.dumps(kws, ensure_ascii=False)}
isPillar: {'true' if pillar else 'false'}
readingTime: {rt}
relatedSlugs: []
---

{body}
"""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(fm)
    return True

created = 0
for t in TOPICS:
    if gen(*t):
        created += 1
        print(f"  ✅ {t[0]}")
    else:
        print(f"  ⏭ {t[0]} (exists)")

print(f"\n✅ Done! Created: {created}/{len(TOPICS)}")
