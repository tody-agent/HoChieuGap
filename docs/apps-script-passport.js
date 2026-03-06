/**
 * Google Apps Script — HoChieuGap Form → Sheet Handler
 * 
 * HƯỚNG DẪN SETUP:
 * ─────────────────────────────────────────────
 * 1. Tạo Google Sheet mới
 * 2. Đặt tên tab sheet: "Data"
 * 3. Tạo header row (dòng 1) theo đúng thứ tự:
 *    A: Thời gian | B: Họ tên | C: Giới tính | D: Ngày sinh | E: Số CCCD 
 *    F: SĐT | G: Dịch vụ | H: Mức độ gấp | I: Nơi sinh | J: Dân tộc 
 *    K: Tôn giáo | L: Địa chỉ TT | M: Địa chỉ tạm trú | N: Nghề nghiệp 
 *    O: Số HC cũ | P: Ghi chú | Q: Có ảnh | R: Nguồn trang
 * 4. Extensions → Apps Script → paste code này
 * 5. Deploy → New deployment → Web app
 *    - Execute as: Me
 *    - Who has access: Anyone
 * 6. Copy URL → paste vào FORM_CONFIG.URLS.passport trong form-handler.js
 */

const SHEET_NAME = 'Data';

function doPost(e) {
    try {
        const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(SHEET_NAME);
        if (!e || !e.parameter) {
            return ContentService.createTextOutput(
                JSON.stringify({ status: 'error', message: 'No data received' })
            ).setMimeType(ContentService.MimeType.JSON);
        }

        const p = e.parameter;

        sheet.appendRow([
            new Date(),               // A: Thời gian (auto)
            p.name || '',             // B: Họ tên
            p.gender || '',           // C: Giới tính
            p.dob || '',              // D: Ngày sinh
            p.idNumber || '',         // E: Số CCCD
            p.phone || '',            // F: SĐT
            p.service || '',          // G: Dịch vụ
            p.urgency || '',          // H: Mức độ gấp
            p.birthPlace || '',       // I: Nơi sinh
            p.ethnicity || '',        // J: Dân tộc
            p.religion || '',         // K: Tôn giáo
            p.permanentAddress || '', // L: Địa chỉ TT
            p.tempAddress || '',      // M: Địa chỉ tạm trú
            p.occupation || '',       // N: Nghề nghiệp
            p.oldPassport || '',      // O: Số HC cũ
            p.note || '',             // P: Ghi chú
            p.hasPhoto || 'Không',    // Q: Có ảnh
            p.url || ''               // R: Nguồn trang
        ]);

        return ContentService.createTextOutput(
            JSON.stringify({ status: 'success' })
        ).setMimeType(ContentService.MimeType.JSON);

    } catch (err) {
        return ContentService.createTextOutput(
            JSON.stringify({ status: 'error', message: err.toString() })
        ).setMimeType(ContentService.MimeType.JSON);
    }
}
