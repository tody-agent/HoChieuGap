// HoChieuGap Blog — Global constants

export const SITE_TITLE = 'HoChieuGap — Blog Hộ Chiếu & Thủ Tục Xuất Nhập Cảnh';
export const SITE_DESCRIPTION =
	'Hướng dẫn chi tiết thủ tục hộ chiếu, tình huống gấp, mẹo tiết kiệm thời gian. Cập nhật 2026.';

export const BRAND = {
	name: 'HoChieuGap',
	hotline: '0909 123 456',
	zaloLink: 'https://zalo.me/0909123456',
	email: 'info@hochieugap.vn',
	siteUrl: 'https://hochieugap.vn',
	landingPage: 'https://hochieugap.vn',
};

// Content cluster definitions for internal linking
export const CLUSTERS = {
	'gap-khan-cap': { name: 'Hộ Chiếu Gấp — Khẩn Cấp', icon: '🔥', pillarSlug: 'lam-ho-chieu-gap-24h' },
	'cap-moi': { name: 'Cấp Mới Hộ Chiếu', icon: '🆕', pillarSlug: 'thu-tuc-lam-ho-chieu-lan-dau-2026' },
	'tre-em': { name: 'HC Trẻ Em & Gia Đình', icon: '👶', pillarSlug: 'ho-chieu-cho-tre-em-duoi-14-tuoi' },
	'gia-han': { name: 'Gia Hạn / Đổi / Cấp Lại', icon: '🔄', pillarSlug: 'gia-han-ho-chieu-2026' },
	'mat-hc': { name: 'HC Bị Mất', icon: '🔍', pillarSlug: 'mat-ho-chieu-phai-lam-sao' },
	'du-lich': { name: 'HC & Du Lịch', icon: '✈️', pillarSlug: 'checklist-ho-chieu-du-lich' },
	'chi-phi': { name: 'Chi Phí & Bảng Giá', icon: '💰', pillarSlug: 'chi-phi-lam-ho-chieu-2026' },
	'phap-ly': { name: 'Thủ Tục & Pháp Lý', icon: '📋', pillarSlug: 'thong-tu-31-ho-chieu' },
	'nghe-nghiep': { name: 'HC Theo Nghề Nghiệp', icon: '🎓', pillarSlug: 'ho-chieu-gap-du-hoc' },
	'meo': { name: 'Mẹo & Kinh Nghiệm', icon: '💡', pillarSlug: '10-sai-lam-lam-ho-chieu' },
} as const;

export type ClusterKey = keyof typeof CLUSTERS;
