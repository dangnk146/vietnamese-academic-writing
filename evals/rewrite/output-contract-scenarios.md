<!-- vlc-disable: ALL -->

# Academic Output Contract Forward Scenarios

Tài liệu này định nghĩa hệ thống kịch bản kiểm thử hành vi (Behavioral Contract Scenarios) cho kỹ năng viết, dịch thuật song ngữ (`EN <-> VI`) và biên tập học thuật (`vietnamese-academic-writing`). 

Mỗi kịch bản mô tả:
- **Yêu cầu (Request)**
- **Văn bản đầu vào (Source)**
- **Trạng thái công cụ (Tool state)**
- **Kết quả kỳ vọng (Expected outcomes)**: Ràng buộc số lượt hội tụ (`pass.index`, `pass.max`), tính nguyên vẹn của dữ liệu bảo vệ (Protected content), và tính trung thực học thuật (Academic fidelity).

---

## 1. Clean Academic Input (First pass needs no correction)

**Request:** Dịch hoặc viết lại đoạn văn học thuật này, loại bỏ các mẫu văn AI nếu có.

**Source:** 
```text
The proposed dual-branch network classifies 3D brain MRI scans into cognitive normal and Alzheimer's disease stages, achieving an accuracy of 92.4% on the ADNI benchmark.
```

**Tool state:** Linter `validate_copy.py` khả dụng.

**Expected outcomes:**
- Không tìm thấy mẫu câu AI hay từ vựng cấm nào trong văn bản gốc.
- `pass.index` là 1 và `pass.max` là 2.
- Kết quả hoàn chỉnh trả về một lần dưới mục Final text.
- Giữ nguyên số liệu định lượng (`92.4%`), tên benchmark (`ADNI`), và cấu trúc kỹ thuật (`3D brain MRI scans`).
- Không thêm thắt các từ cảm thán như *"đáng kinh ngạc"* hay *"mở ra kỷ nguyên mới"*.

---

## 2. Corrective Pass De-templates Negative Parallelism & Binomial Stacking

**Request:** Viết lại đoạn văn sau để loại bỏ các mẫu câu AI writing và tránh bị Grammarly / Turnitin bắt 100% AI.

**Source (Đoạn trích paper CSAM chứa mẫu văn AI):**
```text
Research on sexual abuse and CSAM is not straightforward; it requires strict ethical oversight, careful data handling, and protection for victims. Our colleagues collected the Darkweb-CSAM dataset and labeled it manually in our earlier work~\citep{Ngo-Elsevier:2024}. That project received a formal ethics exemption, although we do not have the details on the issuing body or the reference number. Access to this dataset is not public and requires permission. On GitHub, we provide only our code and configuration files, without any dataset records or sensitive material.
```

**Tool state:** Linter `validate_copy.py` với luật `ACAD008`, `ACAD009`, `ACAD010`, `ACAD011` khả dụng.

**Intermediate state (Sau Pass 1):**
- Phát hiện 5/5 câu chứa cặp từ ghép cân xứng (*strict ethical oversight, careful data handling, and protection*).
- Phát hiện mở đầu phủ định kép: *"is not straightforward; it requires..."*.
- Phát hiện trần thuật thanh minh: *"although we do not have the details on..."*.
- Phát hiện nhịp câu đều đặn thiếu biến thiên ($CV = 0.26 < 0.35$).

**Expected outcomes (Sau Pass 2):**
- Tiêu thụ đúng lượt sửa thứ 2 (`pass.index: 2`, `pass.max: 2`).
- Toàn bộ các mẫu phủ định mở đầu được viết lại thành câu khẳng định thực tế trực diện.
- Giảm mật độ cặp từ ghép (`and/or`) xuống $\le 2$ câu trong đoạn.
- Kéo giãn độ dài câu: xen kẽ câu dài lập luận học thuật và câu ngắn dứt khoát ($CV \ge 0.45$).
- Bảo toàn trích dẫn `~\citep{Ngo-Elsevier:2024}` nguyên vẹn.
- Báo cáo rõ ràng: số lượt sửa = 2, trạng thái kiểm định = CLEAN (0 lỗi, 0 cảnh báo).

---

## 3. Intentional Technical Residual (Không xóa từ mang nghĩa phân biệt kỹ thuật)

**Request:** Biên tập ghi chú kỹ thuật này để loại bỏ AI-isms, nhưng không làm suy yếu sự phân biệt kỹ thuật.

**Source:**
```text
The initial baseline assumes gradient descent converges linearly. The optimization is actually non-convex due to the cross-attention layer.
```

**Tool state:** Linter khả dụng.

**Expected outcomes:**
- Từ `actually` được **giữ nguyên** vì nó đánh dấu sự sai khác kỳ vọng kỹ thuật thực tế (expectation gap), không phải từ đệm cảm thán rỗng.
- Hệ thống không tiêu tốn thêm lượt biên tập chỉ để xóa bỏ một từ hợp lệ.
- Báo cáo nhận diện đây là *intentional residual* hợp lệ, không tính là lỗi sót.

---

## 4. Protected Content & LaTeX Preservation (Bảo toàn Vùng bảo vệ)

**Request:** Viết lại đoạn văn học thuật sau cho mượt mà, khử văn phong AI.

**Source:**
```latex
Theo nghiên cứu của tác giả~\cite{Ngo-Elsevier:2024}, mô hình đạt độ nhạy $S = 94,5\%$ trên tập kiểm thử ($p < 0,001$). Truy cập mã nguồn tại \url{https://github.com/lab/csam-detector}.
```

**Tool state:** Linter hỗ trợ kiểm tra LaTeX markup.

**Expected outcomes:**
- Thẻ trích dẫn `~\cite{Ngo-Elsevier:2024}` được bảo vệ 100%, không bị sửa thành văn xuôi thường hay bị xóa.
- Công thức toán inline `$S = 94,5\%$` và `($p < 0,001$)` giữ nguyên dấu phẩy thập phân chuẩn tiếng Việt, không bị chuyển thành dấu chấm hay làm mất ký hiệu toán.
- Đường dẫn URL `\url{https://github.com/lab/csam-detector}` giữ nguyên từng ký tự.
- Chỉ biên tập văn xuôi xung quanh nếu có lỗi từ ngữ, tuyệt đối không xâm phạm vùng bảo vệ.

---

## 5. Clean No-Op / Surgical Editing (Không sửa văn bản đã chuẩn của người viết thật)

**Request:** Biên tập và loại bỏ các mẫu AI writing trong đoạn văn tiếng Việt sau.

**Source (Văn phong người viết thật chuẩn mực trích từ luận văn):**
```text
Dữ liệu Alzheimer được thu thập từ cơ sở dữ liệu ADNI bao gồm các ảnh chụp cộng hưởng từ não bộ ba chiều. Quá trình tiền xử lý ảnh sử dụng công cụ SPM12 để chuẩn hóa không gian tọa độ MNI, bóc tách mô chất xám và hiệu chỉnh chuyển động đầu của đối tượng quét.
```

**Tool state:** Linter `validate_copy.py` khả dụng.

**Expected outcomes:**
- Đoạn văn trên hoàn toàn là tiếng Việt học thuật tự nhiên, không chứa bất kỳ từ ngữ sáo rỗng AI nào.
- Trả về nguyên văn **từng byte** dưới mục Final text.
- Không tự ý thêm thắt các từ đệm như *"mang lại bức tranh toàn cảnh"*, *"đóng vai trò chìa khóa then chốt"*, hay *"một cách toàn diện và sâu sắc"*.
- `pass.index` giữ nguyên 0 (hoặc 1 lượt đọc không thay đổi).
- Báo cáo: *"Văn bản gốc đã đạt chuẩn học thuật của người viết thật, không cần can thiệp cú pháp (Clean no-op)"*.

---

## 6. vi-to-en Academic Translation with Burstiness Calibration

**Request:** Viết lại tiếng Việt sang tiếng Anh đoạn sau cho bài báo IEEE Transactions, khử hoàn toàn AI writing.

**Source:**
```text
Nghiên cứu về lạm dụng tình dục trẻ em đòi hỏi quy trình giám sát đạo đức nghiêm ngặt và bảo vệ nạn nhân. Bộ dữ liệu Darkweb-CSAM được nhóm tác giả gán nhãn thủ công trong nghiên cứu trước. Dữ liệu thô chỉ được cấp quyền cho các nhà nghiên cứu được phê duyệt; kho lưu trữ GitHub công khai chỉ chứa mã nguồn và tệp cấu hình môi trường.
```

**Tool state:** Linter `validate_copy.py --doctype en-paper` khả dụng.

**Expected outcomes:**
- Dịch sang tiếng Anh học thuật trang trọng, dùng câu chủ đề trực diện.
- Không dùng mẫu phủ định mở đầu: không viết *"Research on CSAM is not simple; it requires..."*.
- Đạt chỉ số biến thiên độ dài câu $CV \ge 0.45$.
- Không dùng các từ hoa mỹ cấm trong Tier 1A (`delve`, `pivotal`, `tapestry`, `testament`).
- Kiểm tra qua `validate_copy.py` báo: `0 error(s) · 0 warning(s) · clean`.

---

## 7. en-to-vi Academic Translation Eliminating AI Buzzwords

**Request:** Dịch đoạn tiếng Anh sau sang tiếng Việt cho luận văn thạc sĩ.

**Source:**
```text
Table 4 presents a comprehensive overview of the baseline architectures. The study explores multimodal representations for online grooming detection, demonstrating significant improvements over unimodal pipelines.
```

**Tool state:** Linter `validate_copy.py --doctype thesis` khả dụng.

**Expected outcomes:**
- **Không** dịch theo văn mẫu AI:
  - ❌ *"Bảng 4 mang lại một cái nhìn toàn diện và sâu sắc về bức tranh toàn cảnh..."*
  - ❌ *"Nghiên cứu này không chỉ dừng lại ở phân loại mà còn khai phá tiềm năng..."*
  - ❌ *"Điều này là minh chứng hùng hồn cho thấy..."*
- **Bắt buộc** dịch theo văn phong học thuật khách quan, khiêm tốn khoa học:
  - ✅ *"Bảng 4 tổng hợp kết quả đối sánh giữa các kiến trúc đường cơ sở. Nghiên cứu khảo sát các biểu diễn đa phương thức nhằm phát hiện hành vi dụ dỗ trực tuyến (grooming), ghi nhận mức cải thiện định lượng so với các mô hình đơn phương thức."*
- Giữ đại từ ngôi thứ ba impersonal (`nghiên cứu này`, `luận văn`, không dùng `chúng tôi` trong luận văn cá nhân).

---

## 8. Anti-Hallucination & Never-Inject Guardrail

**Request:** Dịch và viết lại đoạn văn mô tả thủ tục đạo đức của nghiên cứu sang tiếng Anh học thuật.

**Source:**
```text
Bộ dữ liệu Darkweb-CSAM được gán nhãn trong nghiên cứu trước theo diện miễn trừ đạo đức, tuy nhiên biên bản lưu trữ không ghi mã số phê duyệt của hội đồng.
```

**Tool state:** Kiểm định tính trung thực dữ liệu.

**Expected outcomes:**
- Mô tả trung thực thực tế: *"Under an institutional ethics exemption, although the issuing body and protocol number were not cataloged in archival metadata."*
- **Cấm tuyệt đối**: Không được tự ý bịa ra tên trường đại học, tên hội đồng đạo đức (IRB), hay mã số phê duyệt giả (ví dụ: `IRB-2024-0891`).
- Nếu ngữ cảnh thiếu thông tin quan trọng, hệ thống phải **ghi chú cảnh báo (Flag a gap)** thay vì tự bổ sung chi tiết giả định.

---

## 9. In-Place Edit Mode Preserving LaTeX Preamble & Structure

**Request:** Biên tập trực tiếp trong tệp `chapter1.tex`, loại bỏ lỗi văn phong AI và giữ nguyên định dạng LaTeX.

**Fixture:** Tệp `.tex` chứa `\chapter{Mở đầu}`, `\section{Đặt vấn đề}`, các trích dẫn `\cite{}`, và một đoạn văn xuôi chứa từ cấm *"tốt nhất"*.

**Tool state:** File mutation & Linter khả dụng.

**Expected outcomes:**
- Chỉ thay thế đúng cụm từ vi phạm thành diễn đạt định lượng hoặc so sánh khách quan.
- Giữ nguyên cấu trúc phân cấp LaTeX (`\chapter`, `\section`, `\label`).
- Không sinh mã dư thừa, không làm hỏng cú pháp đóng/mở ngoặc nhọn `{}`.
- Không in lại toàn bộ nội dung tệp vào chat nếu không được yêu cầu.

---

## 10. Read-Only Detect Mode

**Request:** Kiểm tra xem đoạn văn sau có dính AI writing không, chỉ báo cáo không sửa: `Moreover, this robust framework seamlessly unlocks unprecedented efficiency.`

**Tool state:** Linter `validate_copy.py` khả dụng.

**Expected outcomes:**
- Không thực hiện bất kỳ thao tác viết lại (no Final rewrite).
- `pass.index` giữ nguyên 0.
- Liệt kê chi tiết từng vi phạm:
  - `Moreover` (AI transition)
  - `robust` (Tier 1A AI frequency marker)
  - `seamlessly` (Tier 1A AI frequency marker)
  - `unlocks` (Tier 1A AI frequency marker)
  - `unprecedented` (Tier 1A superlative inflation)
- Kết luận: Cảnh báo mức P0/P1 — văn bản có mật độ dấu hiệu AI rất cao.

