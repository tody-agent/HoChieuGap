#!/usr/bin/env python3
"""Generate all 100 SEO content articles for HoChieuGap blog."""

import os
from datetime import datetime

CONTENT_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'content', 'blog')

ARTICLES = [
    # ── CLUSTER 2: Cấp Mới Lần Đầu (10 bài) ──
    {
        "slug": "thu-tuc-lam-ho-chieu-lan-dau-2026",
        "title": "Thủ Tục Làm Hộ Chiếu Lần Đầu 2026 — Hướng Dẫn A-Z",
        "description": "Hướng dẫn đầy đủ thủ tục làm hộ chiếu phổ thông lần đầu năm 2026. Hồ sơ, lệ phí, địa điểm, thời gian.",
        "cluster": "cap-moi",
        "keywords": ["thủ tục làm hộ chiếu lần đầu", "làm hộ chiếu lần đầu 2026", "hồ sơ làm hộ chiếu"],
        "isPillar": True,
        "readingTime": 8,
        "relatedSlugs": ["le-phi-lam-ho-chieu", "cach-dien-to-khai-ho-chieu", "dia-chi-lam-ho-chieu-tphcm"],
        "content": """Làm hộ chiếu lần đầu tiên? Bài viết này hướng dẫn bạn **từ A đến Z** — từ chuẩn bị hồ sơ, nộp đơn, đến nhận hộ chiếu.

## Ai cần làm hộ chiếu lần đầu?

- Công dân Việt Nam **chưa từng có hộ chiếu**
- Người từ 14 tuổi trở lên (trẻ em dưới 14 tuổi dùng mẫu TK01a)
- Muốn đi du lịch, công tác, du học, hoặc định cư

## Hồ sơ cần chuẩn bị

| STT | Giấy tờ | Yêu cầu | Bắt buộc |
|-----|---------|---------|---------|
| 1 | Tờ khai TK01 | Bản chính, điền đủ thông tin | ✅ |
| 2 | CCCD / CMND | Bản chính, còn hiệu lực | ✅ |
| 3 | Ảnh 4×6cm nền trắng | Chụp không quá 6 tháng | ✅ |
| 4 | Giấy khai sinh | Cho trẻ chưa có mã định danh | ❗ Nếu cần |

## Quy trình nộp hồ sơ

### Cách 1: Nộp trực tiếp
1. Đến Phòng Quản lý Xuất nhập cảnh (Công an tỉnh/thành phố)
2. Lấy số thứ tự, nộp hồ sơ
3. Chụp ảnh, lấy dấu vân tay tại chỗ
4. Nhận giấy hẹn — trả kết quả sau **12 ngày làm việc**

### Cách 2: Đăng ký online qua Cổng DVCQG
1. Truy cập [dichvucong.gov.vn](https://dichvucong.gov.vn)
2. Đăng nhập bằng tài khoản VNeID hoặc CCCD gắn chip
3. Điền tờ khai online, chọn ngày hẹn
4. Đến đúng ngày hẹn → nộp bản chính, chụp ảnh, lấy vân tay

### Cách 3: Sử dụng dịch vụ
1. Liên hệ HoChieuGap — tư vấn miễn phí
2. Chuẩn bị giấy tờ theo hướng dẫn
3. Dịch vụ nộp hộ + theo dõi tiến độ
4. Nhận HC gấp từ **24h đến 72h**

## Lệ phí nhà nước

| Loại HC | Lệ phí |
|---------|--------|
| Hộ chiếu phổ thông (không chip) | 200.000 VND |
| Hộ chiếu gắn chip | 400.000 VND |

> Đây là lệ phí nhà nước. Nếu dùng dịch vụ gấp, phí dịch vụ sẽ cộng thêm.

## Thời gian nhận kết quả

| Phương thức | Thời gian |
|------------|----------|
| Đường thường | 12 ngày làm việc (~2-3 tuần) |
| Dịch vụ gấp 72h | 3 ngày |
| Dịch vụ gấp 48h | 2 ngày |
| Dịch vụ gấp 24h | 1 ngày |

## Lưu ý quan trọng

1. **CCCD phải còn hiệu lực** — nếu hết hạn, đổi CCCD trước
2. **Ảnh phải đúng quy chuẩn** — mặt nhìn thẳng, không đeo kính, nền trắng
3. **Mang theo bản gốc** — không chấp nhận bản photo
4. Từ 2023, **không cần hộ khẩu** — chỉ cần CCCD
5. Có thể nộp tại **bất kỳ tỉnh/thành** nào, không phụ thuộc hộ khẩu

## Câu hỏi thường gặp

### Làm HC lần đầu có cần hộ khẩu không?
Từ năm 2023, **không cần** hộ khẩu. Chỉ cần CCCD còn hiệu lực.

### Bao lâu thì nhận được HC?
Đường thường: 12 ngày làm việc. Dịch vụ gấp: từ 24h.

### Có nộp online hoàn toàn được không?
Nộp tờ khai online được, nhưng vẫn phải đến **trực tiếp** để chụp ảnh và lấy dấu vân tay.

## Kết luận

Thủ tục làm hộ chiếu lần đầu năm 2026 đơn giản hơn so với trước đây nhờ bỏ yêu cầu hộ khẩu và hỗ trợ đăng ký online. Nếu cần nhanh hơn 12 ngày, dịch vụ hộ chiếu gấp giúp bạn có HC trong 24-72h."""
    },
    {
        "slug": "sinh-vien-lam-ho-chieu",
        "title": "Sinh Viên Làm Hộ Chiếu: Cần Gì? Bao Lâu? Chi Phí?",
        "description": "Hướng dẫn sinh viên làm hộ chiếu lần đầu: hồ sơ, chi phí, địa điểm, thời gian. Mẹo tiết kiệm thời gian.",
        "cluster": "cap-moi",
        "keywords": ["sinh viên làm hộ chiếu", "hộ chiếu cho sinh viên", "thủ tục hộ chiếu sinh viên"],
        "readingTime": 5,
        "relatedSlugs": ["thu-tuc-lam-ho-chieu-lan-dau-2026", "le-phi-lam-ho-chieu", "dang-ky-ho-chieu-online"],
        "content": """Sinh viên chuẩn bị đi du lịch, exchange, hoặc thực tập nước ngoài? Đây là hướng dẫn **đầy đủ nhất** để làm hộ chiếu khi bạn đang là sinh viên.

## Sinh viên cần giấy tờ gì để làm HC?

Tin vui: **không khác gì** công dân bình thường! Bạn cần:

1. **CCCD bản chính** (còn hiệu lực)
2. **Ảnh 4×6cm nền trắng**
3. **Tờ khai TK01** (tải và điền trước hoặc điền tại cơ quan XNC)

> **Không cần** giấy xác nhận sinh viên, thẻ sinh viên, hay bất kỳ giấy tờ nào liên quan đến trường.

## Mẹo cho sinh viên

### 1. Chọn thời điểm nộp
- **Tránh** đầu tuần (T2-T3) và mùa hè — đông nhất
- **Nên** nộp giữa tuần (T4-T5), đầu giờ sáng

### 2. Nộp online trước
- Đăng ký trên Cổng DVCQG → chọn ngày hẹn → đến đúng giờ
- Không phải chờ đợi lâu

### 3. Chụp ảnh sẵn
- Dùng công cụ [Chụp ảnh HC online](/passport-photo/) — miễn phí
- Hoặc chụp tại tiệm với giá 20.000 - 50.000 VND

## Chi phí

| Hạng mục | Chi phí |
|----------|--------|
| Lệ phí HC phổ thông | 200.000 VND |
| Lệ phí HC gắn chip | 400.000 VND |
| Ảnh tại tiệm | 20.000 - 50.000 VND |
| **Tổng (tự đi)** | **220.000 - 450.000 VND** |

> Nếu cần gấp: dịch vụ gấp 72h từ 3.100.000 VND.

## Sinh viên ngoại tỉnh

Nếu bạn đang học xa nhà:
- ✅ Nộp hồ sơ tại **bất kỳ tỉnh/thành** nào
- ✅ Không cần về quê để làm
- ✅ Chỉ cần mang CCCD bản chính

## Timeline gợi ý

| Thời điểm | Hành động |
|----------|-----------|
| 3 tháng trước chuyến đi | Kiểm tra HC, bắt đầu làm nếu chưa có |
| 1 tháng trước | Đã nộp HC + bắt đầu xin visa (nếu cần) |
| 2 tuần trước | HC + visa OK → chuẩn bị hành lý |

## Kết luận

Làm hộ chiếu cho sinh viên **cực kỳ đơn giản** — chỉ cần CCCD, ảnh, tờ khai. Chi phí chỉ từ 200.000 VND. Nên làm sớm để tránh gấp gáp khi có cơ hội đi nước ngoài."""
    },
    {
        "slug": "le-phi-lam-ho-chieu",
        "title": "Làm Hộ Chiếu Lần Đầu Bao Nhiêu Tiền? Bảng Phí Chi Tiết 2026",
        "description": "Bảng lệ phí làm hộ chiếu 2026: phổ thông, gắn chip, trẻ em, gấp. Chi phí thực tế từ A đến Z.",
        "cluster": "cap-moi",
        "keywords": ["lệ phí làm hộ chiếu", "làm hộ chiếu bao nhiêu tiền", "chi phí hộ chiếu 2026"],
        "readingTime": 5,
        "relatedSlugs": ["thu-tuc-lam-ho-chieu-lan-dau-2026", "chi-phi-lam-ho-chieu-2026", "ho-chieu-gan-chip"],
        "content": """Một trong những câu hỏi phổ biến nhất: **"Làm hộ chiếu bao nhiêu tiền?"** Bài viết này tổng hợp **tất cả chi phí** bạn cần biết.

## Lệ phí nhà nước (bắt buộc)

| Loại hộ chiếu | Lệ phí |
|---------------|--------|
| HC phổ thông (không chip) | **200.000 VND** |
| HC phổ thông gắn chip | **400.000 VND** |
| HC cho trẻ em dưới 14 tuổi | **100.000 VND** |
| Cấp đổi HC (gia hạn/hư hỏng) | **200.000 VND** |
| Cấp lại HC do mất | **400.000 VND** |

> Đây là lệ phí do **Bộ Tài chính quy định**, áp dụng thống nhất trên toàn quốc.

## Chi phí phụ (tuỳ chọn)

| Hạng mục | Chi phí ước tính |
|----------|-----------------|
| Ảnh 4×6 tại tiệm | 20.000 - 50.000 VND |
| Chụp ảnh online (HoChieuGap) | **Miễn phí** |
| Photocopy giấy tờ | 5.000 - 10.000 VND |
| Đi lại (xe, xăng, taxi) | 50.000 - 200.000 VND |

## Tổng chi phí thực tế

| Phương thức | Chi phí tổng |
|------------|-------------|
| Tự đi, HC thường | **~250.000 VND** |
| Tự đi, HC chip | **~450.000 VND** |
| Dịch vụ gấp 72h | Từ **1.100.000 VND** |
| Dịch vụ gấp 48h | Từ **1.600.000 VND** |
| Dịch vụ gấp 24h | Từ **2.300.000 VND** |
| Trọn gói tại nhà | Từ **4.000.000 VND** |

## So sánh: Tự đi vs Thuê dịch vụ

| | Tự đi | Dịch vụ |
|--|------|---------|
| Chi phí | 250-450K | 1.1M - 5.5M |
| Thời gian | 12 ngày | 1-3 ngày |
| Công sức | Tự xếp hàng, nộp | Không cần đi đâu |
| Rủi ro sai sót | Có | Gần 0% |
| Phù hợp | Không gấp, có thời gian | Gấp, bận rộn |

> **Khi nào nên dùng dịch vụ?** Khi thời gian của bạn **đáng giá hơn** chi phí dịch vụ, hoặc khi bạn cần HC **gấp**.

## Câu hỏi thường gặp

### HC gắn chip có bắt buộc không?
Hiện tại **chưa bắt buộc**. Bạn có thể chọn HC thường (200K) hoặc HC chip (400K).

### Trẻ em phải đóng bao nhiêu?
Lệ phí HC cho trẻ em dưới 14 tuổi: **100.000 VND**.

### Phí dịch vụ gấp có bao gồm lệ phí nhà nước không?
**Có.** Giá dịch vụ HoChieuGap đã bao gồm toàn bộ, không phát sinh thêm.

## Kết luận

Làm hộ chiếu lần đầu chỉ tốn **200.000 - 400.000 VND** lệ phí nhà nước. Nếu cần gấp, dịch vụ từ 1.100.000 VND (72h) đến 5.500.000 VND (trọn gói tại nhà 24h)."""
    },
    {
        "slug": "cach-dien-to-khai-ho-chieu",
        "title": "Hướng Dẫn Điền Tờ Khai TK01 Làm Hộ Chiếu — Từng Ô Một",
        "description": "Hướng dẫn chi tiết cách điền tờ khai TK01 làm hộ chiếu từng ô. Kèm mẫu đã điền để tham khảo.",
        "cluster": "cap-moi",
        "keywords": ["cách điền tờ khai hộ chiếu", "mẫu TK01", "tờ khai hộ chiếu TK01"],
        "readingTime": 6,
        "relatedSlugs": ["thu-tuc-lam-ho-chieu-lan-dau-2026", "quy-dinh-anh-ho-chieu", "to-khai-tk01a-tre-em"],
        "content": """Tờ khai TK01 là mẫu **bắt buộc** khi làm hộ chiếu. Không ít người điền sai, dẫn đến **hồ sơ bị trả lại**. Bài viết này hướng dẫn bạn điền đúng từng ô.

## Tờ khai TK01 là gì?

- Mẫu đơn xin cấp hộ chiếu phổ thông cho **người từ 14 tuổi trở lên**
- Trẻ em dưới 14 tuổi dùng **TK01a** (xem bài riêng)
- Ban hành theo Thông tư 31/2023/TT-BCA

## Hướng dẫn điền từng phần

### Phần 1: Thông tin cá nhân
| Ô | Cách điền | Ví dụ |
|---|----------|-------|
| Họ và tên | Viết IN HOA, đúng CCCD | NGUYỄN VĂN AN |
| Giới tính | Đánh dấu Nam/Nữ | ☑ Nam |
| Ngày tháng năm sinh | dd/mm/yyyy | 15/06/1990 |
| Nơi sinh | Tỉnh/TP | TP. Hồ Chí Minh |
| Số CCCD | 12 chữ số | 079190123456 |
| Dân tộc | Kinh, Hoa, Tày... | Kinh |
| Tôn giáo | Không/Phật giáo/Công giáo... | Không |

### Phần 2: Nơi thường trú
- Ghi **đúng theo CCCD mới nhất**
- Gồm: Số nhà, đường, phường/xã, quận/huyện, tỉnh/TP
- Nếu khác nơi tạm trú → ghi thêm nơi tạm trú

### Phần 3: Mục đích
- Đánh dấu: Du lịch / Thăm thân / Công tác / Khác
- Chọn **1 mục đích chính** (không ảnh hưởng đến HC)

### Phần 4: Ảnh
- Dán ảnh 4×6 vào ô
- **Không ghim, không kẹp** — dùng keo dán
- Ảnh [chụp online chuẩn](/passport-photo/) hoặc tại tiệm

### Phần 5: Ký tên
- Ký bằng **bút bi đen hoặc xanh**
- Ký giống nhau ở tất cả chỗ yêu cầu
- Trẻ em 14-17: tự ký hoặc người đại diện ký

## Lỗi phổ biến khi điền TK01

| STT | Lỗi | Cách tránh |
|-----|------|-----------|
| 1 | Viết chữ thường thay vì IN HOA | Luôn viết IN HOA |
| 2 | Sai ngày sinh so với CCCD | Đối chiếu kỹ với CCCD |
| 3 | Ghi sai nơi thường trú | Copy đúng từ CCCD |
| 4 | Tẩy xoá, sửa trên đơn | Điền đơn mới nếu sai |
| 5 | Dán ảnh sai quy cách | Ảnh 4×6, nền trắng, không đeo kính |

## Tải mẫu TK01 ở đâu?

- [Cổng DVCQG](https://dichvucong.gov.vn) — tải PDF + điền online
- Nhận trực tiếp tại Phòng XNC các tỉnh/thành
- Dịch vụ HoChieuGap — chúng tôi điền giúp bạn

## Kết luận

Điền tờ khai TK01 đúng cách giúp hồ sơ **được chấp nhận ngay lần đầu**, tránh mất thời gian đi lại. Nếu không chắc chắn, hãy sử dụng dịch vụ để được hỗ trợ điền đơn chuyên nghiệp."""
    },
    {
        "slug": "quy-dinh-anh-ho-chieu",
        "title": "Ảnh Hộ Chiếu Chuẩn: Kích Thước, Quy Định, Mẹo Chụp Đẹp",
        "description": "Quy định ảnh hộ chiếu Việt Nam 2026: kích thước 4x6cm, nền trắng, quy cách. Mẹo chụp ảnh đẹp tại nhà.",
        "cluster": "cap-moi",
        "keywords": ["quy định ảnh hộ chiếu", "ảnh hộ chiếu 4x6", "chụp ảnh hộ chiếu tại nhà"],
        "readingTime": 5,
        "relatedSlugs": ["thu-tuc-lam-ho-chieu-lan-dau-2026", "meo-chup-anh-ho-chieu", "cach-dien-to-khai-ho-chieu"],
        "content": """Ảnh hộ chiếu là thành phần **không thể thiếu** và có quy định khá nghiêm ngặt. Ảnh không chuẩn = hồ sơ bị trả lại. Dưới đây là hướng dẫn chi tiết.

## Quy định ảnh hộ chiếu Việt Nam

| Tiêu chí | Yêu cầu |
|----------|---------|
| Kích thước | 4×6 cm |
| Nền | **Trắng** |
| Mặt | Nhìn thẳng chính diện |
| Biểu cảm | Tự nhiên, miệng khép |
| Đầu | Để trần (không đội mũ, khăn) |
| Kính | **Không đeo kính** (kể cả kính cận) |
| Thời hạn | Chụp trong **6 tháng gần nhất** |
| Số lượng | 2 tấm (1 dán tờ khai, 1 nộp kèm) |

## Ảnh bị từ chối khi nào?

❌ Nền không phải trắng (xanh, xám)
❌ Đeo kính (bất kỳ loại nào)
❌ Đội mũ, khăn (trừ tôn giáo)
❌ Mặt nghiêng, nhìn sang bên
❌ Ảnh mờ, tối, quá sáng
❌ Ảnh chụp quá 6 tháng
❌ Ảnh selfie (thường bị lệch)

## Tự chụp ảnh HC tại nhà

### Dùng công cụ online miễn phí

**HoChieuGap** cung cấp công cụ [Chụp ảnh HC online](/passport-photo/):
- ✅ AI nhận diện khuôn mặt tự động
- ✅ Khung hướng dẫn chuẩn 4×6
- ✅ Nền trắng tự động
- ✅ Tải ảnh ngay, không cần đăng nhập

### Mẹo chụp đẹp

1. **Ánh sáng** — Đứng gần cửa sổ, ánh sáng tự nhiên chiếu đều
2. **Nền** — Đứng trước tường trắng hoặc dùng vải trắng
3. **Khoảng cách** — Nhờ người khác chụp cách 1.5-2m
4. **Biểu cảm** — Mặt bình thường, không cười, không nhăn
5. **Trang phục** — Mặc áo tối màu (đậm) để nổi trên nền trắng

## Chụp tại tiệm

- Chi phí: **20.000 - 50.000 VND**
- Ưu điểm: chuyên nghiệp, đảm bảo chuẩn
- Nhược điểm: phải đi ra tiệm

## Ảnh HC cho trẻ em

- Quy cách giống người lớn
- **Trẻ sơ sinh**: bế ngang, chụp mặt thẳng
- Nền trắng, không đeo mũ
- Khó hơn vì trẻ khó hợp tác → nên chụp tại tiệm hoặc dùng tool AI

## Kết luận

Ảnh hộ chiếu chuẩn không khó — quan trọng là **4×6, nền trắng, nhìn thẳng, không đeo kính**. Sử dụng công cụ chụp ảnh online của HoChieuGap để có ảnh chuẩn ngay tại nhà, miễn phí."""
    },
    {
        "slug": "dia-chi-lam-ho-chieu-tphcm",
        "title": "Làm Hộ Chiếu Ở Đâu Tại TP.HCM? Danh Sách Địa Chỉ 2026",
        "description": "Danh sách đầy đủ các phòng quản lý xuất nhập cảnh tại TP.HCM. Địa chỉ, giờ làm việc, hotline.",
        "cluster": "cap-moi",
        "keywords": ["địa chỉ làm hộ chiếu tphcm", "phòng XNC tphcm", "nơi làm hộ chiếu tại hồ chí minh"],
        "readingTime": 4,
        "relatedSlugs": ["thu-tuc-lam-ho-chieu-lan-dau-2026", "dia-chi-lam-ho-chieu-ha-noi", "dang-ky-ho-chieu-online"],
        "content": """Tại TP.HCM có nhiều địa điểm tiếp nhận hồ sơ HC. Bài viết tổng hợp **đầy đủ** địa chỉ, giờ làm việc, và mẹo tránh đông.

## Danh sách cơ quan cấp HC tại TP.HCM

### 1. Phòng Quản lý XNC — Công an TP.HCM
- **Địa chỉ:** 161 Nguyễn Du, Phường Bến Thành, Quận 1
- **Giờ làm việc:** T2-T6, 7:30-11:30 và 13:30-16:30
- **Lưu ý:** Đông nhất vào sáng T2 và T3

### 2. Chi nhánh quận/huyện (một số quận)
Từ năm 2023, một số quận đã có **điểm tiếp nhận hồ sơ HC**:
- Công an Quận Bình Thạnh
- Công an Quận Tân Bình
- Công an huyện Bình Chánh
- *(Danh sách có thể thay đổi — liên hệ xác nhận)*

### 3. Cục Quản lý XNC — Bộ Công an (Chi nhánh phía Nam)
- **Địa chỉ:** 254 Nguyễn Trãi, Phường Nguyễn Cư Trinh, Quận 1
- **Giờ làm việc:** T2-T6, 8:00-11:30 và 13:30-16:30

## Mẹo tránh đông, xếp hàng nhanh

1. 🕐 **Đi giữa tuần** (T4-T5) — ít đông nhất
2. ☀️ **Đi sớm** — có mặt trước 7:00 để lấy số đầu tiên
3. 📱 **Đăng ký online** trước → đến đúng giờ hẹn
4. 📋 **Hồ sơ đầy đủ** — tránh bị trả về vì thiếu giấy tờ
5. 💡 **Tránh đầu tháng** — nhiều người nộp vào đầu tháng

## Không muốn đi xếp hàng?

Sử dụng **dịch vụ HoChieuGap**:
- 🏠 Đến nhận hồ sơ tận nhà/văn phòng
- 📝 Nộp hồ sơ thay bạn
- ⚡ Xử lý gấp 24h-72h
- 📞 Hotline: **0909 123 456**

## Kết luận

Tại TP.HCM, bạn có nhiều lựa chọn để nộp hồ sơ HC. Đi giữa tuần + đăng ký online = tiết kiệm thời gian nhất. Hoặc sử dụng dịch vụ để không cần đi đâu cả."""
    },
    {
        "slug": "dia-chi-lam-ho-chieu-ha-noi",
        "title": "Làm Hộ Chiếu Ở Đâu Tại Hà Nội? Danh Sách Phòng XNC 2026",
        "description": "Danh sách phòng quản lý xuất nhập cảnh tại Hà Nội. Địa chỉ, giờ mở cửa, cách đến, mẹo tiết kiệm thời gian.",
        "cluster": "cap-moi",
        "keywords": ["địa chỉ làm hộ chiếu hà nội", "phòng XNC hà nội", "nơi làm hộ chiếu tại hà nội"],
        "readingTime": 4,
        "relatedSlugs": ["thu-tuc-lam-ho-chieu-lan-dau-2026", "dia-chi-lam-ho-chieu-tphcm", "dang-ky-ho-chieu-online"],
        "content": """Tìm địa chỉ làm hộ chiếu tại Hà Nội? Bài viết tổng hợp tất cả điểm tiếp nhận hồ sơ, giờ làm việc, và cách tối ưu thời gian.

## Danh sách cơ quan cấp HC tại Hà Nội

### 1. Cục Quản lý XNC — Bộ Công an
- **Địa chỉ:** 44-46 Phố Trần Phú, Quận Ba Đình
- **Giờ làm việc:** T2-T6, 8:00-11:30 và 13:30-16:30
- **Lưu ý:** Cơ quan cấp trung ương, xử lý nhanh

### 2. Phòng QLXNC — Công an TP. Hà Nội
- **Địa chỉ:** 89 Trần Hưng Đạo, Quận Hoàn Kiếm
- **Giờ làm việc:** T2-T6, 7:30-11:30 và 13:30-16:30
- **Lưu ý:** Rất đông, nên đăng ký online trước

### 3. Điểm tiếp nhận cấp quận (mở rộng từ 2023)
- Công an quận Cầu Giấy
- Công an quận Thanh Xuân
- Công an quận Long Biên
- *(Liên hệ xác nhận lịch tiếp nhận cụ thể)*

## Cách đến nhanh nhất

| Phương tiện | Gợi ý |
|------------|-------|
| Xe máy | Gửi xe tại bãi gần, đi bộ vào |
| Ô tô | Tìm bãi đỗ trước — khu vực thường kẹt xe |
| Xe bus | Tuyến 01, 34, 23 (tuỳ điểm) |
| Grab/Taxi | Tiện nhất nếu không quen đường |

## Mẹo giảm thời gian chờ

1. 📱 **Đăng ký hẹn online** qua Cổng DVCQG
2. 🕐 **Tránh T2-T3** — đông nhất trong tuần
3. ❄️ **Tránh mùa hè** — mùa du lịch, đông hơn bình thường
4. 📋 **Chuẩn bị đầy đủ** — CCCD, ảnh, tờ khai đã điền

## Dịch vụ HC gấp tại Hà Nội

HoChieuGap hoạt động tại **cả Hà Nội**:
- 🏠 Đến nhận hồ sơ trong nội thành
- ⚡ Gấp 24h-72h
- 📞 Hotline: **0909 123 456**

## Kết luận

Hà Nội có nhiều điểm tiếp nhận hồ sơ HC, đặc biệt sau khi mở rộng đến cấp quận. Đăng ký online + đi giữa tuần = tiết kiệm nhất."""
    },
    {
        "slug": "dang-ky-ho-chieu-online",
        "title": "Đăng Ký Làm Hộ Chiếu Online Qua Cổng Dịch Vụ Công — Hướng Dẫn",
        "description": "Hướng dẫn step-by-step đăng ký làm hộ chiếu online qua Cổng DVCQG. CCCD gắn chip, VNeID, chọn ngày hẹn.",
        "cluster": "cap-moi",
        "keywords": ["đăng ký hộ chiếu online", "làm hộ chiếu qua mạng", "cổng dịch vụ công hộ chiếu"],
        "readingTime": 6,
        "relatedSlugs": ["thu-tuc-lam-ho-chieu-lan-dau-2026", "cccd-gan-chip-ho-chieu", "kinh-nghiem-nop-ho-chieu-online"],
        "content": """Từ năm 2023, bạn có thể đăng ký làm hộ chiếu **online** qua Cổng dịch vụ công quốc gia. Tiết kiệm thời gian xếp hàng, chọn ngày giờ hẹn phù hợp.

## Điều kiện đăng ký online

- ✅ Có **CCCD gắn chip** (loại mới)
- ✅ Có tài khoản **VNeID** hoặc tài khoản Cổng DVCQG
- ✅ Điện thoại/máy tính có kết nối internet

> **Lưu ý:** Đăng ký online chỉ giúp **đặt lịch hẹn** và điền tờ khai trước. Bạn vẫn phải đến **trực tiếp** để chụp ảnh và lấy dấu vân tay.

## Hướng dẫn step-by-step

### Bước 1: Truy cập Cổng DVCQG
- Vào [dichvucong.gov.vn](https://dichvucong.gov.vn)
- Đăng nhập bằng tài khoản VNeID

### Bước 2: Tìm dịch vụ
- Tìm kiếm: "Cấp hộ chiếu phổ thông"
- Chọn loại: Cấp mới / Cấp đổi / Cấp lại

### Bước 3: Điền tờ khai online
- Hệ thống tự điền một phần từ CCCD chip
- Bổ sung thông tin còn thiếu
- Upload ảnh 4×6 nền trắng (nếu yêu cầu)

### Bước 4: Chọn điểm nộp & ngày hẹn
- Chọn Phòng XNC gần nhất
- Chọn ngày giờ phù hợp
- Nhận mã hồ sơ + giấy hẹn điện tử

### Bước 5: Đến nộp trực tiếp
- Mang CCCD bản chính
- Đến đúng ngày giờ đã hẹn
- Chụp ảnh, lấy vân tay, xác nhận thông tin

## Ưu điểm vs nhược điểm

| ✅ Ưu điểm | ❌ Nhược điểm |
|-----------|-------------|
| Không xếp hàng lấy số | Cần CCCD gắn chip |
| Chọn giờ hẹn phù hợp | Vẫn phải đến trực tiếp |
| Điền tờ khai trước, không vội | Hệ thống đôi khi lỗi |
| Tiết kiệm 1-2h | Không giúp rút ngắn 12 ngày chờ |

## Online có giúp lấy HC nhanh hơn không?

**Không.** Đăng ký online chỉ giúp tiết kiệm thời gian **xếp hàng**, nhưng thời gian xử lý vẫn là **12 ngày làm việc**. Muốn nhanh hơn → cần dùng **dịch vụ gấp**.

## Lỗi thường gặp khi nộp online

1. Hệ thống **quá tải** → thử lại ngoài giờ cao điểm
2. CCCD **chưa kích hoạt chip** → đến công an phường kích hoạt
3. **Upload ảnh sai** → dùng ảnh 4×6 nền trắng đúng quy cách
4. **Quên mật khẩu VNeID** → reset qua app VNeID

## Kết luận

Đăng ký online giúp tiết kiệm thời gian xếp hàng, nhưng **không rút ngắn 12 ngày chờ**. Nếu cần nhanh hơn, kết hợp đăng ký online + dịch vụ gấp."""
    },
    {
        "slug": "nguoi-gia-lam-ho-chieu",
        "title": "Người Lớn Tuổi Làm Hộ Chiếu: Quy Trình Đơn Giản, Không Phiền Hà",
        "description": "Hướng dẫn làm hộ chiếu cho ông bà, bố mẹ lớn tuổi. Quy trình đơn giản, dịch vụ tại nhà, con cháu hỗ trợ.",
        "cluster": "cap-moi",
        "keywords": ["người già làm hộ chiếu", "hộ chiếu cho người lớn tuổi", "làm hộ chiếu cho bố mẹ"],
        "readingTime": 4,
        "relatedSlugs": ["thu-tuc-lam-ho-chieu-lan-dau-2026", "dich-vu-ho-chieu-tai-nha", "gia-dinh-lam-ho-chieu"],
        "content": """Muốn đưa bố mẹ, ông bà đi du lịch nước ngoài nhưng lo thủ tục hộ chiếu rắc rối? Bài viết này giúp bạn hỗ trợ người thân lớn tuổi làm HC **dễ dàng nhất**.

## Người lớn tuổi có làm HC được không?

**Hoàn toàn được**, không có giới hạn tuổi. Tuy nhiên cần lưu ý:
- CCCD phải **còn hiệu lực**
- Phải **tự đến trực tiếp** để chụp ảnh, lấy vân tay
- Nếu không tự đi được → cần giấy uỷ quyền + giấy xác nhận y tế

## Hồ sơ — Giống người bình thường

1. CCCD bản chính
2. Ảnh 4×6 nền trắng
3. Tờ khai TK01

> Không cần giấy tờ đặc biệt nào khác. Con cháu có thể giúp điền tờ khai.

## Tình huống đặc biệt

### Người không tự đi được
Nếu ông bà **bệnh, không thể di chuyển**:
- Một số Phòng XNC có thể **cử cán bộ đến nhà** (trường hợp đặc biệt)
- Dịch vụ trọn gói HoChieuGap: đến tận nhà hỗ trợ

### Người không biết chữ
- Con cháu hoặc nhân viên dịch vụ **điền tờ khai thay**
- Người đứng đơn **điểm chỉ** thay chữ ký

## Mẹo giúp ông bà làm HC dễ dàng

1. 📅 **Chọn ngày ít đông** — T4-T5, tránh đầu tuần
2. 🚗 **Đưa đón tận nơi** — tránh để ông bà tự đi
3. 📋 **Chuẩn bị hồ sơ sẵn** — ông bà chỉ cần đến ký tên
4. ⏰ **Đăng ký online** — giảm thời gian chờ
5. 🏠 **Dịch vụ tại nhà** — tốt nhất nếu ngại di chuyển

## Dịch vụ trọn gói tại nhà

HoChieuGap đến **tận nhà**:
- 📸 Hỗ trợ chụp ảnh chuẩn
- 📝 Điền tờ khai
- 🚗 Đưa đón đến cơ quan XNC (nếu cần)
- 📦 Giao HC tận tay

Chi phí từ **4.000.000 VND** (72h) — bao gồm mọi chi phí.

## Kết luận

Làm hộ chiếu cho người lớn tuổi không khó — chỉ cần con cháu hỗ trợ chuẩn bị hồ sơ. Dịch vụ tại nhà là giải pháp tốt nhất để ông bà không phải vất vả."""
    },
    {
        "slug": "ho-chieu-gan-chip",
        "title": "Hộ Chiếu Phổ Thông vs Hộ Chiếu Gắn Chip: Khác Nhau Thế Nào?",
        "description": "So sánh chi tiết hộ chiếu phổ thông và hộ chiếu gắn chip 2026. Khác nhau gì? Nên làm loại nào?",
        "cluster": "cap-moi",
        "keywords": ["hộ chiếu gắn chip", "so sánh hộ chiếu chip", "hộ chiếu chip có gì khác"],
        "readingTime": 5,
        "relatedSlugs": ["thu-tuc-lam-ho-chieu-lan-dau-2026", "le-phi-lam-ho-chieu", "ho-chieu-xanh-vs-tim"],
        "content": """Từ 2023, Việt Nam bắt đầu cấp **hộ chiếu gắn chip điện tử**. Nhiều người băn khoăn: nên làm loại nào? Khác nhau ra sao? Bài viết so sánh chi tiết.

## Hộ chiếu gắn chip là gì?

Hộ chiếu gắn chip (HC ePassport) có **vi mạch điện tử** nhúng trong trang bìa, lưu trữ:
- Thông tin cá nhân (tên, ngày sinh, số HC)
- Ảnh khuôn mặt số hoá
- Dấu vân tay số hoá

Biểu tượng chip: 🔌 trên bìa HC

## So sánh chi tiết

| Tiêu chí | HC Phổ thông | HC Gắn chip |
|----------|-------------|-------------|
| **Lệ phí** | 200.000 VND | 400.000 VND |
| **Trang bìa** | Xanh lá cũ / Tím mới | Tím + biểu tượng chip |
| **Bảo mật** | Tiêu chuẩn | Cao hơn (dữ liệu mã hoá) |
| **Cổng tự động sân bay** | ❌ | ✅ (một số nước) |
| **Thời gian cấp** | 12 ngày | 12 ngày |
| **Thời hạn** | 10 năm | 10 năm |
| **Xin visa dễ hơn?** | Không ảnh hưởng | Một số nước ưu tiên |

## HC chip có bắt buộc không?

**Chưa bắt buộc** (tính đến 2026). Bạn có thể chọn:
- HC thường: phí thấp hơn, đủ dùng cho mọi mục đích
- HC chip: phí cao hơn, nhiều ưu điểm về bảo mật

## Ai nên làm HC chip?

- ✅ Đi **Nhật, Hàn, EU** thường xuyên (cổng tự động)
- ✅ Muốn **bảo mật** cao hơn
- ✅ Hay đi nước ngoài (ưu tiên nhập cảnh)
- ❌ Chỉ đi 1-2 lần → HC thường là đủ

## Nâng cấp từ HC thường sang chip

- **Không** nâng cấp được — phải **cấp đổi** HC mới
- Nộp HC cũ, nhận HC chip mới
- Phí: 400.000 VND

## Kết luận

HC gắn chip có nhiều ưu điểm về bảo mật và tiện lợi, nhưng **chưa bắt buộc**. Nếu ngân sách cho phép và bạn đi nước ngoài thường xuyên, nên chọn HC chip. Ngược lại, HC thường hoàn toàn đủ dùng."""
    },
]

def generate_article(article):
    """Generate a single article markdown file."""
    slug = article["slug"]
    filepath = os.path.join(CONTENT_DIR, f"{slug}.md")

    if os.path.exists(filepath):
        print(f"  ⏭ Skipped (exists): {slug}")
        return False

    is_pillar = article.get("isPillar", False)
    reading_time = article.get("readingTime", 5)
    related = article.get("relatedSlugs", [])

    frontmatter = f"""---
title: '{article["title"]}'
description: '{article["description"]}'
pubDate: 2026-03-01
cluster: '{article["cluster"]}'
keywords: {article["keywords"]}
isPillar: {"true" if is_pillar else "false"}
readingTime: {reading_time}
relatedSlugs: {related}
---"""

    content = f"{frontmatter}\n\n{article['content'].strip()}\n"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"  ✅ Created: {slug}")
    return True

def main():
    os.makedirs(CONTENT_DIR, exist_ok=True)

    created = 0
    skipped = 0

    print(f"\n🏭 Generating {len(ARTICLES)} articles...\n")

    for article in ARTICLES:
        if generate_article(article):
            created += 1
        else:
            skipped += 1

    print(f"\n✅ Done! Created: {created}, Skipped: {skipped}")
    print(f"📁 Output: {CONTENT_DIR}")

if __name__ == "__main__":
    main()
