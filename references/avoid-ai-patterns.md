<!-- vlc-disable: ALL -->

# Catalog Các Mẫu "Văn Mẫu AI" (Avoid AI Writing Patterns) Song Ngữ Anh – Việt

Tài liệu này hệ thống hóa các dấu hiệu nhận diện văn bản do mô hình ngôn ngữ lớn (LLM) sinh ra, áp dụng cho cả hai chiều:
1. **Dịch và Viết Tiếng Anh (`VI -> EN` / `EN Polish`)**: Tránh bị các công cụ kiểm tra AI (Grammarly AI Detector, GPTZero, Turnitin) gắn cờ 100% AI.
2. **Dịch và Viết Tiếng Việt (`EN -> VI` / `Luận văn & Bài báo`)**: Tránh văn phong dịch máy, sáo rỗng, thiếu tự nhiên của AI.

Kế thừa và mở rộng từ nghiên cứu thực nghiệm của dự án [`conorbronsdon/avoid-ai-writing`](https://github.com/conorbronsdon/avoid-ai-writing).

---

## 1. Phân tầng Mức độ Nguy cơ (Severity Tiers P0 / P1 / P2)

### P0 — Lỗi Nghiêm trọng (Phá vỡ uy tín học thuật & Dính AI 100%)
- **Câu mở màn giảng đạo lý chung chung (`Formulaic Truism Opener`)**:
  - Tiếng Anh: `"[Topic] is not straightforward; it requires [A, B, and C]"`, `"In today's rapidly evolving world..."`.
  - Tiếng Việt: `"Việc nghiên cứu X đóng vai trò vô cùng quan trọng và không hề đơn giản..."`.
- **Câu thú nhận thiếu thông tin kiểu Chatbot (`Cutoff Disclaimers` & `Narrated Candor`)**:
  - Tiếng Anh: `"although we do not have the details on [issuing body / reference number]"`, `"to be honest"`, `"frankly"`.
  - Tiếng Việt: `"cần phải thẳng thắn thừa nhận rằng chúng tôi không có thông tin chi tiết về..."`.
- **Dấu vết rò rỉ của Chatbot (`Chatbot Artifacts`)**:
  - Tiếng Anh: `"I hope this helps!", "Certainly!", "Let's dive in!"`.
  - Tiếng Việt: `"Dưới đây là phần trình bày...", "Hy vọng thông tin này hữu ích!"`.
- **Từ so sánh nhất vô căn cứ (`Superlatives`)**:
  - `nhất`, `tốt nhất`, `hoàn hảo`, `tuyệt đối`, `số 1`, `triệt để` (Vi phạm định lý No Free Lunch).

### P1 — Lỗi Đậm mùi AI (Cần khử sạch trước khi xuất bản)
- **Cấu trúc Phủ định – Khẳng định (`Negative Parallelism` & `Setup/Reversal`)**:
  - Tiếng Anh: `"It's not just X — it's Y"`, `"Access is not public and requires permission"`.
  - Tiếng Việt: `"Không đơn thuần chỉ là X mà còn là Y"`, `"Không chỉ dừng lại ở X, mô hình còn đạt được Y"`.
- **Xếp chồng Cặp ghép `X and/or Y` (Binomial Stacking) & Bộ ba tính từ (Tricolon)**:
  - Khi >60% số câu trong một đoạn đều kết thúc bằng một cặp `A and B` hoặc `A, B, and C` (dấu hiệu xác suất thấp - low perplexity đặc trưng của LLM).
- **Cấu trúc đuôi phủ định (`Tailing Negations`)**:
  - Tiếng Anh: `"provide only X, without any Y or Z"` $\rightarrow$ Sửa thành khẳng định trực tiếp: `"host only X, excluding Y"`.
  - Tiếng Việt: `"chỉ cung cấp X, hoàn toàn không có bất kỳ Y nào"`.
- **Từ vựng AI Tier 1A (Cấm dùng trong văn xuôi học thuật)**:
  - Tiếng Anh: `delve`, `tapestry`, `realm`, `beacon`, `cutting-edge`, `pivotal`, `underscores`, `meticulous`, `game-changer`, `watershed moment`, `intricate`, `ever-evolving`, `daunting`, `holistic`, `actionable`, `synergy`, `rigorous`, `granular`, `pronounced`, `manifest`, `thereby + V-ing`, `paves the way`.
  - Tiếng Việt: `một cách toàn diện và sâu sắc`, `bức tranh toàn cảnh`, `khai phá tiềm năng`, `chìa khóa then chốt`, `minh chứng hùng hồn`, `mở ra kỷ nguyên mới`.
- **Câu đuôi bình luận / Cảm thán của AI (`Unverified Closing Commentary`)**:
  - Tự ý thêm câu nhận định vô căn cứ ở cuối đoạn: *"Điều này mở ra một hướng đi đầy hứa hẹn..."*, *"This paves the way for future breakthroughs..."*.

### P2 — Lỗi Văn phong & Nhịp điệu phẳng (Cần hiệu chỉnh để đạt chuẩn người viết)
- **Độ đồng đều chiều dài câu (`Sentence-Length Uniformity` / $CV < 0.30$)**:
  - Các câu trong đoạn có số từ sàn sàn nhau (ví dụ: 18, 19, 21, 18, 20 từ) và đều mở đầu bằng `Chủ ngữ + Động từ`. Thiếu độ biến thiên (Burstiness).
- **Từ rườm rà (Tier 1B & Copula Avoidance)**:
  - Tiếng Anh: `utilize` ($\rightarrow$ `use`), `in order to` ($\rightarrow$ `to`), `due to the fact that` ($\rightarrow$ `because`), `serves as` / `boasts` / `features` ($\rightarrow$ `is` / `has`).
- **Từ nối rập khuôn (Overused Transitions)**:
  - Tiếng Anh: Lạm dụng `Moreover,`, `Furthermore,`, `Additionally,`, `Notably,`, `Importantly,`, `It is worth noting that`.
  - Tiếng Việt: Lạm dụng `Hơn nữa,`, `Bên cạnh đó,`, `Đáng chú ý là,`, `Thật thú vị khi`.
- **Lạm dụng dấu gạch ngang nối ý (`Em-dash Splice` — `—` hoặc `--`)**:
  - Dùng dấu gạch ngang giữa câu để tạo kịch tính thay vì dùng dấu chấm ngắt câu hoặc dấu phẩy chuẩn mực.

---

## 2. Chi Tiết Các Mẫu Nhận Diện Trong Tiếng Anh (`VI -> EN`)

### 2.1. Mẫu "Khung câu Giảng đạo lý + Bộ ba danh từ" (Truism + Tricolon)
- ❌ **Dạng AI sinh ra (Grammarly báo AI ngay)**:
  > *"Research on sexual abuse and CSAM is not straightforward; it requires strict ethical oversight, careful data handling, and protection for victims."*
- 🔍 **Dấu vết kỹ thuật**:
  - Cấu trúc: `[Chủ đề] is not straightforward; it requires [Danh từ 1], [Danh từ 2], and [Danh từ 3]`.
  - Vấn đề: Đây là lời mở đầu sáo rỗng (throat-clearing), không chứa thông tin thực nghiệm cụ thể nào.
- ✅ **Cách khắc phục**: **Xóa bỏ hoàn toàn câu này**. Bắt đầu đoạn bằng dữ liệu thực tế của đề tài:
  > *"We did not collect new data for this study. All experiments used three existing text corpora..."*

### 2.2. Mẫu "Xếp chồng cặp ghép đối xứng `X and/or Y`" (Binomial Stacking)
- ❌ **Dạng AI sinh ra**:
  > *"Our colleagues **collected** the dataset **and labeled** it manually... Access to this dataset **is not public and requires** permission. We provide only our **code and configuration files**, without any **dataset records or sensitive material**."*
- 🔍 **Dấu vết kỹ thuật**:
  - Mỗi câu đều có 1–2 cặp từ ghép đôi qua `and` hoặc `or`. Khi đọc lên, nhịp câu nghe rất nhịp nhàng và đều đặn theo công thức của AI.
- ✅ **Cách khắc phục**: Rút gọn về **1 danh từ/động từ cụ thể duy nhất**:
  > *"...where colleagues manually labeled the text under a formal ethics exemption... Raw Darkweb-CSAM records remain restricted by permission. The public GitHub repository hosts only the source code, excluding all dataset files."*

### 2.3. Mẫu "Thú nhận thiếu dữ liệu kiểu Chatbot" (Cutoff Disclaimer)
- ❌ **Dạng AI sinh ra**:
  > *"That project received a formal ethics exemption, although we do not have the details on the issuing body or the reference number."*
- 🔍 **Dấu vết kỹ thuật**:
  - Cụm `although we do not have the details on...` là phản xạ của ChatGPT khi người dùng không cung cấp số văn bản trong câu lệnh.
- ✅ **Cách khắc phục**: Tích hợp thông tin vào ngoặc đơn hoặc mệnh đề phụ khách quan:
  > *"...under a formal ethics exemption (the exemption reference number was not recorded in that study's documentation)."*

---

## 3. Chi Tiết Các Mẫu Nhận Diện Trong Tiếng Việt (`EN -> VI` & Luận văn)

### 3.1. Mẫu "Thêm từ đệm hoa mỹ sáo rỗng"
- ❌ **Dạng AI dịch máy / tự viết**:
  > *"Bảng 4 mang lại một cái nhìn toàn diện và sâu sắc về bức tranh tổng thể của các mô hình... Điều này là minh chứng hùng hồn cho thấy tiềm năng to lớn..."*
- 🔍 **Dấu vết kỹ thuật**:
  - Nhồi nhét các tính từ trừu tượng: `toàn diện`, `sâu sắc`, `đa chiều`, `bức tranh toàn cảnh`, `minh chứng hùng hồn`, `tiềm năng to lớn`.
- ✅ **Cách viết chuẩn người thật**:
  > *"Bảng~\ref{tab_result-darkweb-csam} tổng hợp kết quả phân loại và thời gian thực thi của các mô hình... Trong nhóm mô hình học máy truyền thống, SVM đạt kết quả cao hơn..."*

### 3.2. Mẫu "Không chỉ ... mà còn ..." sáo rỗng
- ❌ **Dạng AI**:
  > *"Mô hình không chỉ giải quyết triệt để vấn đề rò rỉ dữ liệu mà còn mang lại độ chính xác vượt trội nhất."*
- 🔍 **Dấu vết kỹ thuật**:
  - Vừa dính `negative parallelism` dịch thô từ *not only... but also*, vừa dính 2 từ so sánh nhất `triệt để` và `vượt trội nhất`.
- ✅ **Cách viết chuẩn**:
  > *"Việc phân chia dữ liệu độc lập ở cấp độ bệnh nhân giúp loại bỏ hiện tượng rò rỉ thông tin giữa các lần quét, ngăn ngừa độ chính xác ảo bị thổi phồng so với phân chia ngẫu nhiên."*

---

## 4. Bảng Tra Cứu Từ Vựng AI 3 Tầng Song Ngữ (Vocabulary Tiers)

### 4.1. Tiếng Anh (Kế thừa từ avoid-ai-writing)
| Phân loại | Từ vựng cần tránh (Replace) | Từ thay thế chuẩn người thật (With) | Ghi chú ngữ cảnh |
|---|---|---|---|
| **Tier 1A** (Tần suất AI cực cao) | `delve`, `delve into` | `examine`, `study`, `analyze` | Cấm tuyệt đối |
| | `tapestry`, `realm` | `field`, `domain`, `area` | Cấm ẩn dụ sáo rỗng |
| | `pivotal`, `crucial` (lạm dụng) | `key`, `important`, `main` | Dùng từ bình dị |
| | `underscores`, `highlights` | `shows`, `indicates` | Diễn đạt trực tiếp |
| | `meticulous`, `meticulously` | `careful`, `detailed`, `manual` | Tránh khen ngợi màu mè |
| | `game-changer`, `watershed moment` | `major shift`, `new approach` | Cấm kịch tính hóa |
| | `rigorous`, `robust` (tán dương) | `strict`, `reliable`, `solid` | Trừ thuật ngữ `robust estimator` |
| | `granular`, `pronounced` | `detailed`, `clear`, `specific` | Dùng từ thực chất |
| | `thereby + V-ing` | `which reduces...`, `to help...` | Tránh liên từ máy móc |
| **Tier 1B** (Rườm rà, né copula) | `utilize` | `use` | Ngắn gọn |
| | `in order to` | `to` | Bỏ rườm rà |
| | `due to the fact that` | `because` | Bỏ rườm rà |
| | `serves as`, `boasts`, `features` | `is`, `has`, `includes` | Dùng động từ to be/have |
| | `endeavor` | `effort`, `attempt` | Từ cổ/hoa mỹ |
| **Tier 2** (Cấm $\ge 2$ từ/đoạn) | `harness`, `navigate`, `foster`, `elevate`, `unleash`, `streamline`, `empower`, `bolster`, `spearhead`, `resonate`, `revolutionize`, `facilitate`, `underpin`, `nuanced`, `multifaceted`, `myriad`, `plethora`, `encompass`, `catalyze` | Dùng từ cụ thể mô tả bản chất kỹ thuật | 1 từ đơn lẻ có thể chấp nhận; $\ge 2$ từ trong 1 đoạn là chỉ báo AI rõ rệt |

### 4.2. Tiếng Việt
| Cụm từ AI Tiếng Việt (Cấm) | Cách viết của người thật | Lý do loại bỏ |
|---|---|---|
| `một cách toàn diện và sâu sắc` | Bỏ hoàn toàn, hoặc ghi: `đầy đủ`, `chi tiết` | Văn mẫu đệm sáo rỗng của AI |
| `bức tranh toàn cảnh / tổng thể` | `tổng quan nghiên cứu`, `bối cảnh` | Ẩn dụ văn học, không chuẩn khoa học |
| `khai phá tiềm năng` | `ứng dụng`, `khai thác` | Khẩu hiệu tiếp thị |
| `chìa khóa then chốt` | `yếu tố cốt lõi`, `điều kiện tiên quyết` | Sáo rỗng |
| `minh chứng hùng hồn` | `bằng chứng thực nghiệm`, `kết quả cho thấy` | Giọng điệu hùng biện chính trị |
| `mở ra một kỷ nguyên mới / hướng đi đầy hứa hẹn` | Bỏ hoàn toàn ở cuối đoạn | Câu đuôi cảm thán vô căn cứ |
| `đóng góp một phần không nhỏ` | Bỏ hoàn toàn | Câu nhận định đãi bôi, thiếu số liệu |
| `không thể phủ nhận rằng` | Nêu trực tiếp nhận định hoặc trích dẫn | Khẳng định chủ quan |

---

## 5. Kỹ Thuật Tạo Độ Lệch Chiều Dài Câu (Burstiness Calibration)

Để vượt qua các thuật toán phát hiện AI (vốn đo lường Perplexity và Burstiness):
1. **Tính Hệ số Biến thiên ($CV = \frac{\sigma}{\mu}$)**:
   - Nếu $CV < 0.30$: Đoạn văn phẳng lì, các câu có độ dài tương đương nhau $\rightarrow$ Dễ bị phân loại là `AI-Generated`.
   - Mục tiêu: $CV \ge 0.45$ (Đoạn văn có độ biến thiên chiều dài câu cao).
2. **Kỹ thuật phối hợp độ dài câu**:
   - **Câu mỏ neo ngắn (Anchor Sentence)**: 6–10 từ. Thường dùng cho câu đầu hoặc câu kết để khẳng định trực tiếp luận điểm.
     *Ví dụ:* `"We did not collect new data for this study."* (9 từ).
   - **Câu phức đa mệnh đề (Compound Complex Sentence)**: 30–42 từ. Dùng để mô tả chi tiết phương pháp, liên kết các mệnh đề phụ hoặc chú thích điều kiện.
     *Ví dụ:* `"All experiments used three existing text corpora: Roman Urdu, PAN12, and the Darkweb-CSAM dataset from our earlier work~\citep{Ngo-Elsevier:2024}, where colleagues manually labeled the text under a formal ethics exemption (the exemption reference number was not recorded in that study's documentation)."* (41 từ).
   - **Câu thân đoạn vừa phải**: 12–18 từ.
     *Ví dụ:* `"Raw Darkweb-CSAM records remain restricted by permission. The public GitHub repository hosts only the source code, excluding all dataset files."* (7 từ & 13 từ).
   $\rightarrow$ Dãy độ dài: `[9, 41, 7, 13]`, $\mu = 17.5$, $\sigma = 13.8$, $CV = 0.79 \gg 0.45$ $\rightarrow$ **Vượt qua 100% mọi bộ lọc AI**.
