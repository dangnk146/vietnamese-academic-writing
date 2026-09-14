# Danh mục từ ngữ cấm trong Luận văn Thạc sĩ, Tiến sĩ và Paper IEEE / Q1

Văn phong học thuật quốc tế và luận văn sau đại học đòi hỏi tính khách quan, khiêm tốn khoa học và lập luận dựa trên bằng chứng định lượng. Các từ ngữ dưới đây bị nghiêm cấm hoặc hạn chế tối đa trong quá trình viết và biên tập.

---

## 1. Từ ngữ so sánh nhất và khẳng định tuyệt đối (Superlatives & Absolute Claims)

Trong khoa học thực nghiệm, không có mô hình hay phương pháp nào là tối ưu tuyệt đối trong mọi tình huống. Sử dụng từ so sánh nhất khi chưa có chứng minh toán học tổng quát là lỗi học thuật nghiêm trọng.

<!-- machine-readable: superlatives -->

| Cụm từ cấm (Regex / Pattern) | Nguy cơ học thuật | Cách diễn đạt chuẩn mực thay thế |
|---|---|---|
| `(?:tốt\|cao\|giỏi\|nhanh\|chính xác\|tối ưu\|hiệu quả\|đột phá\|vượt trội\|mới\|hiện đại\|toàn diện)\s+nhất` | Khẳng định chủ quan, vi phạm tính khiêm tốn khoa học | Nêu rõ số liệu cụ thể: *"đạt độ chính xác $94{,}18\%$, cao hơn so với..."*, hoặc *"mang lại hiệu quả ổn định"*. |
| `duy nhất` | Bác bỏ không có căn cứ các nghiên cứu khác | *"là một trong số ít các nghiên cứu"*, *"hướng tiếp cận đặc thù"*. |
| `số\s*(?:một\|1)\b` | Khẩu hiệu tiếp thị thương mại | Bỏ hoàn toàn; trình bày vị trí trên bảng xếp hạng thực nghiệm (Benchmark). |
| `hoàn hảo` | Bất khả thi trong hệ thống kỹ thuật thực tế | *"đáp ứng tốt các tiêu chí đề ra"*, *"đạt độ tin cậy cao"*. |
| `tuyệt đối` | Bỏ qua sai số đo lường và nhiễu dữ liệu | *"với độ tin cậy cao ($p < 0{,}001$)"*, *"tiệm cận mức kỳ vọng"*. |
| `triệt để` | Cường điệu hóa khả năng xử lý | *"giải quyết hiệu quả"*, *"suy giảm đáng kể"*. |
| `hàng đầu` | Nhận định mơ hồ, thiếu tiêu chí định lượng | *"các nghiên cứu tiêu biểu"*, *"phương pháp tiên tiến"*. |

---

## 2. Từ ngữ kịch tính hóa và quá nghiêm trọng hóa (Hyperbole & Sensationalism)

Văn phong học thuật cấm dùng từ giật gân, hoang mang, cảm thán như báo chí lá cải. Tác động của bệnh lý hoặc sai lệch kỹ thuật phải được mô tả bằng thuật ngữ khoa học và số liệu thống kê.

<!-- machine-readable: hyperbole -->

| Cụm từ cấm (Pattern) | Lý do loại bỏ | Cách diễn đạt chuẩn mực thay thế |
|---|---|---|
| `vô cùng nghiêm trọng` | Cảm tính hóa, thiếu định lượng | *"thách thức to lớn đối với hệ thống y tế công cộng"*, *"nguy cơ sai lệch đáng kể"*. |
| `cực kỳ nguy hiểm` | Giọng điệu cảnh báo giật gân | *"tiềm ẩn rủi ro lâm sàng cao"*, *"ảnh hưởng bất lợi đến tiên lượng"*. |
| `thảm họa` | Văn phong văn học/báo chí | *"gánh nặng bệnh tật to lớn"*, *"suy giảm nghiêm trọng chức năng nhận thức"*. |
| `đe dọa nghiêm trọng tới sự sống còn` | Khẩu ngữ cường điệu | *"làm suy giảm chất lượng cuộc sống và tăng tỷ lệ tử vong"*. |
| `hoàn toàn bế tắc` | Phủ nhận nỗ lực y học tiền nhiệm | *"gặp nhiều thách thức lớn trong việc chẩn đoán phân biệt sớm"*. |
| `vấn nạn nhức nhối` | Ngôn ngữ báo chí xã hội | *"khoảng trống nghiên cứu cấp thiết cần được giải quyết"*. |
| `sai lầm chết người` | Kịch tính hóa lỗi kỹ thuật | *"hạn chế phương pháp luận dẫn đến kết quả bị thổi phồng"*. |

---

## 3. Đại từ nhân xưng không phù hợp (Inappropriate Pronouns)

Văn bản khoa học (đặc biệt là luận văn tiếng Việt) sử dụng phong cách khách quan (Impersonal register).

| Từ cấm | Lý do | Cách thay thế chuẩn |
|---|---|---|
| `tôi` | Vi phạm tính khách quan của công trình nghiên cứu | Dùng: `luận văn`, `nghiên cứu này`, `tác giả đề tài`. |
| `chúng tôi` | Hạn chế tối đa trong luận văn Thạc sĩ tiếng Việt (vốn là công trình cá nhân của học viên) | Dùng: `đề tài đề xuất`, `nghiên cứu tiến hành`, `mô hình được thiết kế`. |
| `bạn` | Ngôn ngữ giao tiếp thân mật, hướng dẫn sử dụng phần mềm | Dùng: `người thao tác`, `người làm chuyên môn`, `bác sĩ lâm sàng`. |
| `quý vị` / `anh/chị` | Ngôn từ thuyết trình hội thảo hoặc bán hàng | Dùng ngôi thứ ba mô tả chức danh: `hội đồng`, `độc giả`, `các nhà nghiên cứu`. |

---

## 4. Dịch máy thô thiển (Academic Translationese & Clichés)

| Cụm dịch máy thô (❌) | Dạng tiếng Việt chuẩn học thuật (✅) | Ghi chú |
|---|---|---|
| `được thiết kế bởi tác giả` | `do tác giả thiết kế` / `mô hình được thiết kế nhằm` | Tránh lạm dụng bị động tiếng Anh (*is designed by*). |
| `đóng một vai trò quan trọng trong` | `đóng vai trò quan trọng đối với` / `giữ vai trò then chốt trong` | Bỏ chữ "một" thừa thãi từ *play an important role*. |
| `thực hiện một cuộc điều tra` | `tiến hành khảo sát` / `khảo sát` | Bỏ *conduct an investigation*. |
| `trong một cách thức hiệu quả` | `một cách hiệu quả` / `đạt hiệu quả cao` | Dịch thô từ *in an effective manner*. |
| `được dựa trên` | `dựa trên` / `được xây dựng dựa trên` | Tránh bị động kép không tự nhiên. |
| `cho thấy rằng` (dày đặc) | `cho thấy` / `chứng minh` / `kết quả chỉ ra` | Đa dạng hóa liên từ báo cáo kết quả. |
