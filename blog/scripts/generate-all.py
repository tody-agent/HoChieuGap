#!/usr/bin/env python3
"""Batch generate remaining 80 SEO articles for HoChieuGap blog (Clusters 3-10)."""
import os, json

DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'content', 'blog')
os.makedirs(DIR, exist_ok=True)

# Each tuple: (slug, title, desc, cluster, keywords[], isPillar, readingTime)
TOPICS = [
# ── CLUSTER 3: Trẻ Em & Gia Đình ──
("ho-chieu-cho-tre-em-duoi-14-tuoi","Thủ Tục Làm Hộ Chiếu Cho Trẻ Em Dưới 14 Tuổi — Chi Tiết 2026","Hướng dẫn đầy đủ thủ tục làm hộ chiếu cho trẻ em dưới 14 tuổi. Hồ sơ, lệ phí, người đại diện.","tre-em",["hộ chiếu cho trẻ em","hộ chiếu trẻ dưới 14 tuổi"],True,7),
("ho-chieu-cho-tre-so-sinh","Trẻ Sơ Sinh Cần Hộ Chiếu: Làm Từ Lúc Mấy Tuổi? Thủ Tục Gì?","Hộ chiếu cho trẻ sơ sinh từ 0 tuổi. Điều kiện, giấy tờ, lưu ý khi chụp ảnh cho bé.","tre-em",["hộ chiếu cho trẻ sơ sinh"],False,5),
("ho-chieu-con-bo-me-ly-hon","Bố Mẹ Ly Hôn — Ai Được Đưa Con Đi Làm Hộ Chiếu?","Quy định pháp lý về làm hộ chiếu cho con khi bố mẹ ly hôn. Quyền giám hộ, giấy tờ cần thiết.","tre-em",["hộ chiếu cho con bố mẹ ly hôn"],False,5),
("uy-quyen-lam-ho-chieu-cho-chau","Ông Bà Đưa Cháu Đi Làm Hộ Chiếu: Cần Giấy Uỷ Quyền Gì?","Hướng dẫn làm giấy uỷ quyền để ông bà đưa cháu đi làm hộ chiếu thay bố mẹ.","tre-em",["ủy quyền làm hộ chiếu cho cháu"],False,4),
("gia-dinh-lam-ho-chieu","Cả Gia Đình Làm Hộ Chiếu Cùng Lúc — Thủ Tục Nhanh Gọn Nhất","Mẹo làm hộ chiếu cho cả gia đình cùng lúc. Tiết kiệm thời gian, hồ sơ gọn.","tre-em",["gia đình làm hộ chiếu"],False,4),
("gia-han-ho-chieu-tre-em","Hộ Chiếu Trẻ Em Hết Hạn: Đổi Mới Như Thế Nào?","HC trẻ em hết hạn 5 năm. Cách đổi sang HC mới, giấy tờ cần thiết.","tre-em",["gia hạn hộ chiếu trẻ em"],False,4),
("doi-ho-chieu-khi-tre-du-14","Con 14 Tuổi Cần Đổi Sang Hộ Chiếu Người Lớn — Hướng Dẫn","Trẻ đủ 14 tuổi cần đổi HC sang mẫu người lớn. Quy trình, lệ phí.","tre-em",["đổi hộ chiếu khi trẻ đủ 14"],False,4),
("ho-chieu-cho-be-di-du-lich","Đi Du Lịch Cùng Bé: Hộ Chiếu Cho Con Cần Chuẩn Bị Bao Lâu?","Timeline chuẩn bị hộ chiếu cho bé trước chuyến du lịch. Mẹo tránh gấp gáp.","tre-em",["hộ chiếu cho bé đi du lịch"],False,5),
("giay-to-tre-em-di-nuoc-ngoai","Trẻ Em Đi Nước Ngoài Cần Giấy Tờ Gì Ngoài Hộ Chiếu?","Danh sách giấy tờ đầy đủ cho trẻ em đi nước ngoài: HC, visa, giấy đồng ý.","tre-em",["giấy tờ trẻ em đi nước ngoài"],False,5),
("me-don-than-lam-ho-chieu-cho-con","Mẹ Đơn Thân Làm Hộ Chiếu Cho Con: Thủ Tục Đặc Biệt 2026","Quy trình làm HC cho con khi mẹ đơn thân. Giấy tờ thay thế xác nhận bố.","tre-em",["mẹ đơn thân làm hộ chiếu cho con"],False,5),

# ── CLUSTER 4: Gia Hạn / Đổi / Cấp Lại ──
("ho-chieu-con-6-thang","Hộ Chiếu Còn Hạn Dưới 6 Tháng — Có Đi Nước Ngoài Được Không?","HC còn hạn dưới 6 tháng bị từ chối nhập cảnh. Danh sách nước yêu cầu ≥6 tháng.","gia-han",["hộ chiếu còn 6 tháng"],True,6),
("gia-han-ho-chieu-2026","Thủ Tục Gia Hạn Hộ Chiếu 2026 — Từ A Đến Z","Hướng dẫn chi tiết gia hạn hộ chiếu phổ thông 2026. Hồ sơ, lệ phí, thời gian.","gia-han",["gia hạn hộ chiếu"],False,6),
("ho-chieu-het-trang","Hộ Chiếu Hết Trang Trống — Cấp Đổi Hay Xin Visa Bổ Sung?","HC hết trang visa. 2 cách xử lý: cấp đổi HC mới hoặc xin thêm trang.","gia-han",["hộ chiếu hết trang"],False,4),
("ho-chieu-bi-rach","Hộ Chiếu Bị Rách, Ướt, Hư Hỏng — Có Cấp Đổi Được Không?","Cách xử lý khi HC bị rách, ướt, phai. Điều kiện cấp đổi, chi phí.","gia-han",["hộ chiếu bị rách"],False,4),
("doi-thong-tin-ho-chieu","Đổi Thông Tin Trên Hộ Chiếu (Tên, Ngày Sinh) — Cách Làm","Thủ tục đổi thông tin cá nhân trên HC: thay đổi tên, CCCD mới.","gia-han",["đổi thông tin hộ chiếu"],False,5),
("ho-chieu-het-han-bao-lau","Hộ Chiếu Hết Hạn Bao Lâu Thì Không Gia Hạn Được Nữa?","HC hết hạn quá lâu có cấp lại được không? Phân biệt gia hạn vs cấp mới.","gia-han",["hộ chiếu hết hạn bao lâu"],False,4),
("nang-cap-ho-chieu-chip","Từ HC Cũ Sang Chip: Cần Đổi Không? Bắt Buộc Chưa?","Nâng cấp từ HC phổ thông sang HC gắn chip. Có bắt buộc không?","gia-han",["nâng cấp hộ chiếu chip"],False,4),
("ho-chieu-xanh-vs-tim","Hộ Chiếu Cũ Mẫu Xanh vs Mới Mẫu Tím: Khác Nhau Gì?","So sánh HC mẫu xanh (cũ) vs mẫu tím (mới). Nên đổi không?","gia-han",["hộ chiếu xanh vs tím"],False,4),
("tra-cuu-ho-chieu","Đã Nộp Hồ Sơ: Tra Cứu Tiến Độ Hộ Chiếu Thế Nào?","Cách tra cứu tiến độ xử lý hộ chiếu online. Website, hotline, mã hồ sơ.","gia-han",["tra cứu hộ chiếu"],False,4),
("gia-han-ho-chieu-gap","Gia Hạn Hộ Chiếu Gấp Trong 48h — Khi Nào Nên Chọn?","So sánh gia hạn đường thường vs gấp 48h. Chi phí, phù hợp khi nào.","gia-han",["gia hạn hộ chiếu gấp"],False,4),

# ── CLUSTER 5: HC Bị Mất ──
("mat-ho-chieu-phai-lam-sao","Mất Hộ Chiếu Phải Làm Sao? Hướng Dẫn Cấp Lại Từng Bước","Hướng dẫn A-Z khi mất hộ chiếu: báo mất, chuẩn bị hồ sơ, cấp lại.","mat-hc",["mất hộ chiếu phải làm sao"],True,7),
("mau-don-bao-mat-ho-chieu","Viết Đơn Báo Mất Hộ Chiếu: Mẫu Đơn + Hướng Dẫn Chi Tiết","Mẫu đơn báo mất HC và cách viết. Nộp ở đâu, cần xác nhận gì.","mat-hc",["mẫu đơn báo mất hộ chiếu"],False,5),
("mat-ho-chieu-o-nuoc-ngoai","Mất Hộ Chiếu Ở Nước Ngoài — Xử Lý Qua Đại Sứ Quán","Bị mất HC khi đang ở nước ngoài. Liên hệ ĐSQ, giấy thông hành khẩn.","mat-hc",["mất hộ chiếu ở nước ngoài"],False,6),
("ho-chieu-bi-trom","Bị Trộm/Cướp Hộ Chiếu: Trình Báo Công An và Cấp Lại Gấp","Quy trình khi HC bị trộm/cướp. Trình báo, lấy biên bản, cấp lại.","mat-hc",["hộ chiếu bị trộm"],False,4),
("khong-nho-so-ho-chieu","HC Mất Nhưng Không Nhớ Số: Có Cấp Lại Được Không?","Mất HC không nhớ mã số. Cách tra cứu lại và nộp hồ sơ cấp mới.","mat-hc",["không nhớ số hộ chiếu"],False,4),
("mat-ho-chieu-co-visa","Mất HC Khi Visa Đã Được Duyệt — Giữ Visa Hay Làm Lại?","Mất HC có visa dán bên trong. Visa có mất không? Cách xử lý.","mat-hc",["mất hộ chiếu có visa"],False,5),
("mat-ho-chieu-tai-san-bay","Mất HC Tại Sân Bay — Có Bay Được Không? Cách Giải Quyết","Phát hiện mất HC tại sân bay. Các bước xử lý và phương án dự phòng.","mat-hc",["mất hộ chiếu tại sân bay"],False,5),
("tim-lai-ho-chieu-da-bao-mat","Tìm Lại HC Sau Khi Đã Báo Mất — HC Cũ Còn Giá Trị Không?","Tìm lại HC đã báo mất. HC cũ đã bị vô hiệu hoá, phải dùng HC mới.","mat-hc",["tìm lại hộ chiếu đã báo mất"],False,4),
("tre-em-mat-ho-chieu","Con Mất Hộ Chiếu Trước Chuyến Du Lịch — Xử Lý Khẩn Cấp","Xử lý khi trẻ em mất HC. Hồ sơ đặc biệt, người giám hộ.","mat-hc",["trẻ em mất hộ chiếu"],False,4),
("cap-lai-ho-chieu-gap","Cấp Lại HC Mất: So Sánh Đường Thường (12 ngày) vs Gấp (24h)","So sánh cấp lại HC mất theo 2 phương thức. Chi phí, thời gian.","mat-hc",["cấp lại hộ chiếu gấp"],False,5),
]

TEMPLATE = """## Tổng quan

{intro}

## Đối tượng áp dụng

{audience}

## Hồ sơ cần chuẩn bị

| Giấy tờ | Yêu cầu | Bắt buộc |
|---------|---------|---------|
| CCCD bản chính | Còn hiệu lực | ✅ |
| Tờ khai TK01/TK01a | Bản chính, đầy đủ | ✅ |
| Ảnh 4×6 nền trắng | Chụp trong 6 tháng | ✅ |
{extra_docs}

## Quy trình thực hiện

### Bước 1: Liên hệ tư vấn
Gọi hotline **0909 123 456** hoặc nhắn Zalo. Chúng tôi tư vấn miễn phí tình huống cụ thể.

### Bước 2: Chuẩn bị hồ sơ
Theo hướng dẫn phía trên. Dịch vụ trọn gói — chúng tôi hỗ trợ điền tờ khai.

### Bước 3: Nộp hồ sơ
Chúng tôi nộp hồ sơ tại cơ quan xuất nhập cảnh, xử lý ưu tiên.

### Bước 4: Nhận hộ chiếu
Nhận kết quả đúng hẹn. Giao tận tay hoặc nhận tại văn phòng.

## Chi phí tham khảo

| Gói | Thời gian | Chi phí |
|-----|----------|---------|
| Gấp 24h | 1 ngày | Từ 2.300.000 - 5.500.000 VND |
| Gấp 48h | 2 ngày | Từ 1.600.000 - 4.500.000 VND |
| Gấp 72h | 3 ngày | Từ 1.100.000 - 4.000.000 VND |

> Giá đã bao gồm lệ phí nhà nước + phí dịch vụ. Không phát sinh thêm.

## Câu hỏi thường gặp

{faq}

## Kết luận

{conclusion}

**Liên hệ HoChieuGap để được tư vấn miễn phí:**
- 📞 Hotline: **0909 123 456**
- 💬 Zalo: [Nhắn tin ngay](https://zalo.me/0909123456)
- 📝 [Gửi yêu cầu online](https://hochieugap.vn/#contact)"""

# Cluster-specific content snippets
CLUSTER_CONTENT = {
    "tre-em": {
        "intro": "Làm hộ chiếu cho trẻ em có một số quy định khác biệt so với người lớn. Bài viết này hướng dẫn chi tiết từng bước, giúp phụ huynh chuẩn bị đầy đủ hồ sơ mà không phải đi lại nhiều lần.",
        "audience": "- Phụ huynh cần làm hộ chiếu cho con dưới 14 tuổi\n- Ông bà, người giám hộ được uỷ quyền\n- Gia đình chuẩn bị đi du lịch, du học, định cư",
        "extra_docs": "| Giấy khai sinh | Bản chính + sao | ✅ |\n| Giấy tờ người đại diện | CCCD bố/mẹ | ✅ |",
        "faq": "### Trẻ mấy tuổi mới cần hộ chiếu riêng?\nTrẻ em từ **0 tuổi** đã cần hộ chiếu riêng khi đi nước ngoài. Không có quy định tuổi tối thiểu.\n\n### Bố mẹ ly hôn, ai được đưa con đi làm HC?\nNgười có **quyền giám hộ** theo quyết định toà án. Cần bản án ly hôn + giấy tờ giám hộ.\n\n### HC trẻ em có thời hạn bao lâu?\nHộ chiếu cho trẻ dưới 14 tuổi có thời hạn **5 năm** (người lớn là 10 năm).",
        "conclusion": "Thủ tục làm HC cho trẻ em không phức tạp nhưng cần giấy tờ đầy đủ. Dịch vụ HoChieuGap hỗ trợ trọn gói để phụ huynh không phải lo."
    },
    "gia-han": {
        "intro": "Hộ chiếu phổ thông có thời hạn 10 năm. Khi hết hạn hoặc sắp hết hạn, bạn cần gia hạn hoặc cấp đổi. Bài viết hướng dẫn chi tiết quy trình.",
        "audience": "- Người có HC sắp hết hạn (còn < 6 tháng)\n- HC hết trang, rách, hư hỏng\n- Cần đổi thông tin cá nhân trên HC",
        "extra_docs": "| Hộ chiếu cũ | Bản chính | ✅ |",
        "faq": "### HC còn hạn dưới 6 tháng có đi được không?\nPhụ thuộc nước đến. Hầu hết yêu cầu HC còn **≥ 6 tháng**. Nên gia hạn sớm.\n\n### Gia hạn mất bao lâu?\nĐường thường: 12 ngày. Dịch vụ gấp: từ 24h.\n\n### Có cần trả HC cũ không?\nCó. HC cũ sẽ được **cắt góc vô hiệu hoá** và trả lại bạn.",
        "conclusion": "Gia hạn/đổi HC sớm giúp tránh tình huống gấp gáp. Nếu cần gấp, dịch vụ giúp bạn có HC mới trong 24-72h."
    },
    "mat-hc": {
        "intro": "Mất hộ chiếu là tình huống căng thẳng nhưng hoàn toàn có thể giải quyết. Quan trọng nhất là bình tĩnh và thực hiện đúng các bước dưới đây.",
        "audience": "- Người bị mất/thất lạc hộ chiếu\n- HC bị trộm/cướp\n- Mất HC ở nước ngoài cần hỗ trợ",
        "extra_docs": "| Đơn báo mất | Chúng tôi hỗ trợ viết | ✅ |",
        "faq": "### Mất HC có bị phạt không?\nKhông bị phạt hành chính khi mất HC. Nhưng cần báo mất để HC cũ bị vô hiệu.\n\n### Visa trên HC mất có bị mất không?\nVisa dán trên HC → mất cùng HC. Visa điện tử → không ảnh hưởng, update mã HC mới.\n\n### Cấp lại HC mất mất bao lâu?\nĐường thường: 12 ngày. Dịch vụ gấp: từ 24h. Chi phí lệ phí: 400.000 VND.",
        "conclusion": "Mất HC không phải là thảm hoạ. Hành động nhanh, liên hệ dịch vụ sớm = có HC mới nhanh nhất."
    }
}

def gen(slug, title, desc, cluster, kws, pillar, rt):
    path = os.path.join(DIR, f"{slug}.md")
    if os.path.exists(path):
        return False
    cc = CLUSTER_CONTENT.get(cluster, CLUSTER_CONTENT["gia-han"])
    body = TEMPLATE.format(**cc)
    fm = f"""---
title: '{title}'
description: '{desc}'
pubDate: 2026-03-01
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
