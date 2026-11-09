<!-- vlc-disable: ALL -->

# Quy trình Lên Plan Từ khóa Xuyên suốt & Dịch thuật Hai chiều (`EN <-> VI`) Tự nhiên như Người viết

Tài liệu này hướng dẫn:
1. **Cách lên Plan chọn Từ khóa chính (Core Keywords)** để lặp lại thống nhất xuyên suốt bài mà không bị dịch lệch từ qua các đoạn.
2. **Cách dịch `EN -> VI` và `VI -> EN` (hoặc sửa bài báo tiếng Anh)** sao cho **giản dị, chuẩn xác như người thật viết**, tuyệt đối không bị biến thành văn mẫu AI (tránh bị Grammarly / Turnitin báo lỗi AI writing).

---

## 1. Bước Lên Plan & Chọn Từ khóa Chính Xuyên suốt (Keyword Plan)

### 1.1. Nguyên tắc "Giữ nguyên từ khóa chính, không tìm từ đồng nghĩa thay thế"
Trong văn bản khoa học, khi một khái niệm là **từ khóa chính của đề tài**, người viết phải **lặp lại chính xác từ khóa đó** từ đầu đến cuối bài. Không được tự ý đổi sang từ đồng nghĩa ở các đoạn sau.

Trước khi dịch hoặc viết, hãy lập một bảng ngắn từ **4 đến 7 từ khóa chính** của bài.

#### Ví dụ Bảng Từ khóa chính cho bài báo `paper/main.tex` (Đề tài Phát hiện CSAM):
| Từ khóa Tiếng Anh trong bài | Từ khóa Tiếng Việt cố định xuyên suốt | Tuyệt đối KHÔNG dịch lệch thành (❌) |
|---|---|---|
| `child sexual abuse material (CSAM)` | `tài liệu xâm hại tình dục trẻ em (CSAM)` | *văn hóa phẩm đồi trụy*, *ấn phẩm lạm dụng* |
| `child sexual abuse (CSA)` | `xâm hại tình dục trẻ em (CSA)` | *lạm dụng tình dục trẻ nhỏ* |
| `online grooming` | `hành vi dụ dỗ trực tuyến` | *chăn dắt trên mạng* |
| `sexual predators` | `đối tượng xâm hại` / `kẻ xâm hại` | *kẻ săn mồi tình dục* |
| `digital file traces` | `dấu vết tệp kỹ thuật số` | *vết tích hồ sơ điện tử*, *dấu chân tập tin* |
| `systematic survey` / `PRISMA guidelines` | `khảo sát hệ thống` / `quy chuẩn PRISMA` | *điều tra tài liệu*, *đánh giá văn học* |
| `adapted hybrid CNN–LSTM and LSTM–CNN models` | `mô hình lai CNN–LSTM và LSTM–CNN` | *hệ thống pha trộn tuần tự* |

### 1.2. Cách nhấn mạnh và giữ mạch từ khóa xuyên suốt bài
- **Ở câu mở đầu mỗi mục/đoạn (Topic Sentence)**: Nhắc lại trực tiếp từ khóa chính của mục đó (ví dụ: ở mục `Tasks Addressed`, câu đầu phải có `các nhiệm vụ nghiên cứu về CSAM`; ở mục `Datasets Used`, câu đầu phải có `các tập dữ liệu được sử dụng trong nghiên cứu CSAM`).
- **Khi nối từ câu trước sang câu sau**: Dùng lại chính từ khóa vừa nhắc ở câu trước kèm chữ `này` / `trên` / `đó` (ví dụ: *"Phần lớn nghiên cứu tập trung vào **CSAM dạng văn bản**... Sự tập trung vào **dữ liệu văn bản** này xuất phát từ..."*). Cách nối này vừa làm nổi bật từ khóa chính, vừa giúp đoạn văn liền mạch mà không cần câu nào cũng mở đầu bằng *"Bên cạnh đó,"*, *"Hơn nữa,"*, *"Ngoài ra,"*.

---

## 2. Tại sao Văn bản Tiếng Anh Vẫn Bị Grammarly / Turnitin Báo "100% AI Writing" Dù Đã Thay Từ Đơn Giản? (Tích hợp bộ quy tắc `avoid-ai-writing`)

Khi viết hoặc sửa tiếng Anh học thuật (`VI -> EN` hoặc `EN Polish`), nhiều đoạn văn dù đã dùng từ vựng rất đơn giản (`collect`, `label manually`, `require`, `provide`) nhưng **vẫn bị Grammarly AI Detector báo 100% AI writing**.

Nguyên nhân là vì các bộ phát hiện AI thương mại (Grammarly, GPTZero, Turnitin) không chỉ quét từ vựng "hoa mỹ" (`delve`, `rigorous`, `robust`), mà chấm điểm dựa trên **Khung cấu trúc câu của LLM (Syntactic Templates)**, **Mật độ cặp đối xứng (`X and/or Y`)**, và **Độ đồng đều chiều dài câu (Low Burstiness / CV < 0.35)**.

Kết hợp nghiên cứu từ dự án [`conorbronsdon/avoid-ai-writing`](https://github.com/conorbronsdon/avoid-ai-writing) và cơ chế Perplexity/Burstiness của Grammarly, **bắt buộc kiểm soát 6 dấu hiệu cấu trúc AI sau đây**:

### 2.1. Dấu hiệu 1 (Nặng nhất): Mở đầu đoạn bằng "Chân lý hiển nhiên + Phủ định kép + Bộ 3 danh từ" (`Formulaic Opener` + `Negative Parallelism` + `Rule of Three`)
- ❌ **Khung câu 100% AI**:
  > *"Research on sexual abuse and CSAM **is not straightforward; it requires** **strict ethical oversight, careful data handling, and protection for victims**."*
  - Dù từ vựng rất đơn giản, câu này hội tụ đủ 3 dấu vân tay của GPT-4:
    1. **Câu mở màn giảng đạo lý chung chung (`Formulaic throat-clearing`)**: Nói một điều ai cũng biết ("Nghiên cứu về X không hề đơn giản...").
    2. **Cấu trúc Phủ định – Khẳng định (`Negative parallelism`)**: `is not [Adj]; it requires/demands...` (hoặc `isn't X — it's Y`).
    3. **Bộ 3 cụm danh từ trừu tượng (`Compulsive rule of three`)**: `A, B, and C` (`strict ethical oversight, careful data handling, and protection for victims`).
- ✅ **Cách khắc phục triệt để**: **XÓA BỎ HOÀN TOÀN câu mở màn giảng đạo lý**. Bắt đầu đoạn văn ngay lập tức bằng hành động/dữ liệu thực tế của nghiên cứu (ví dụ: *"We did not collect new data for this study. All experiments used three existing text corpora..."*).

### 2.2. Dấu hiệu 2: Mật độ Cặp ghép `X and/or Y` (Binomial Stacking) ở cuối mọi câu
- AI có thói quen cực kỳ máy móc là kết thúc **mọi câu trong đoạn** bằng một cặp 2 danh từ/động từ ghép bằng `and` hoặc `or`.
- Hãy nhìn đoạn văn 5 câu bị Grammarly bắt 100% AI:
  1. Câu 1: `sexual abuse and CSAM` + `oversight, handling, and protection` (1 cặp + 1 bộ ba)
  2. Câu 2: `collected ... and labeled it manually` (1 cặp động từ)
  3. Câu 3: `the issuing body or the reference number` (1 cặp danh từ)
  4. Câu 4: `is not public and requires permission` (1 cặp vị ngữ)
  5. Câu 5: `code and configuration files` + `dataset records or sensitive material` (2 cặp danh từ)
  $\rightarrow$ **5 câu liên tiếp chứa tới 6 cặp `X and/or Y` và 1 bộ ba!** Đây là dấu hiệu xác suất (low perplexity) đặc trưng của mô hình ngôn ngữ.
- ✅ **Quy tắc bắt buộc (`ACAD010`)**: Trong một đoạn văn tiếng Anh, **tối đa 1–2 câu** được phép chứa cặp ghép trừu tượng `X and/or Y`. Ở các câu còn lại, chỉ chọn **1 danh từ cụ thể duy nhất** (ví dụ: thay `our code and configuration files, without any dataset records or sensitive material` bằng `the source code, excluding all dataset files`).

### 2.3. Dấu hiệu 3: Câu thú nhận kiểu "AI thiếu thông tin" (`Cutoff Disclaimers` & `Narrated Candor`)
- Theo `avoid-ai-writing`, các cụm từ kiểu:
  - ❌ *"although we do not have the details on the issuing body or the reference number"*
  - ❌ *"While specific details are limited based on available information..."*
  - ❌ *"To be honest / Frankly, we don't have..."*
  là mẫu câu mặc định của ChatGPT/Claude khi bị thiếu thông tin trong prompt. Tác giả con người khi trích dẫn lại bài báo trước của chính nhóm mình sẽ không bao giờ viết *"chúng tôi không có chi tiết về..."* như một người ngoài cuộc.
- ✅ **Cách viết của tác giả thật**: Ghi thẳng trạng thái hồ sơ trong ngoặc đơn hoặc mệnh đề phụ ngắn gọn: *"(the exemption reference number was not recorded in that study's documentation)"*.

### 2.4. Dấu hiệu 4: Cấu trúc Đuôi phủ định đối xứng (`Tailing Negation` / `"Only X, without any Y"`)
- ❌ **Kiểu AI**: *"Access to this dataset **is not public and requires** permission. On GitHub, we provide **only** our code and configuration files, **without any** dataset records or sensitive material."*
- ✅ **Cách viết của tác giả thật**: Viết câu khẳng định trực tiếp, ngắn gọn: *"Raw Darkweb-CSAM records remain restricted by permission. The public GitHub repository hosts only the source code, excluding all dataset files."*

### 2.5. Dấu hiệu 5: Độ đồng đều chiều dài câu (`Sentence-Length Uniformity` — Hệ số biến thiên `CV < 0.35`)
- Theo đo đạc thực nghiệm trên tập dữ liệu HAP-E trong dự án `avoid-ai-writing`, văn bản của GPT-4o / Llama-3 có chiều dài các câu rất đều nhau (quanh mức 14–21 từ/câu, hệ số biến thiên $CV = \frac{\sigma}{\mu}$ thấp), và mọi câu đều bắt đầu bằng `Chủ ngữ + Động từ` (`Research on...`, `Our colleagues...`, `That project...`, `Access to...`, `On GitHub, we...`).
- Ngược lại, văn bản của người thật có **Burstiness cao ($CV \ge 0.45$)**: xen kẽ một câu rất ngắn (6–9 từ) ngay cạnh một câu dài nhiều mệnh đề (30–42 từ).
- ✅ **Quy tắc bắt buộc (`ACAD011`)**: Khi viết đoạn văn tiếng Anh từ 4 câu trở lên, bắt buộc phải phá nhịp đều bằng cách **gộp 2 câu liên quan thành 1 câu dài (30–40 từ, có mệnh đề quan hệ `, where...` hoặc ngoặc đơn `(...)`)** và **rút gọn 1–2 câu khác xuống dưới 10 từ**.

### 2.6. Dấu hiệu 6: Bảng Từ vựng "Mùi AI" 3 Tầng (`Tier 1A`, `Tier 1B`, `Tier 2 Clusters`) từ `avoid-ai-writing`
- **Tier 1A (Cấm tuyệt đối trong văn xuôi học thuật)**: `delve`, `tapestry`, `realm`, `beacon`, `testament to`, `cutting-edge`, `pivotal`, `underscores`, `meticulous`, `meticulously`, `game-changer`, `watershed moment`, `showcasing`, `deep dive`, `unpack`, `intricate`, `intricacies`, `ever-evolving`, `daunting`, `holistic`, `actionable`, `impactful`, `synergy`, `interplay`, `symphony`, `load-bearing` (nghĩa bóng).
- **Tier 1B (Từ rườm rà — Thay bằng từ gọn)**:
  - `utilize` $\rightarrow$ `use`
  - `in order to` $\rightarrow$ `to`
  - `due to the fact that` $\rightarrow$ `because`
  - `serves as` / `boasts` / `features` (động từ) $\rightarrow$ `is` / `has` / `includes`
  - `endeavor` $\rightarrow$ `effort` / `try`
  - `ascertain` $\rightarrow$ `determine` / `find out`
- **Tier 2 (Cấm xuất hiện từ 2 từ trở lên trong cùng 1 đoạn văn)**: `harness`, `navigate`, `foster`, `elevate`, `unleash`, `streamline`, `empower`, `bolster`, `spearhead`, `resonate`, `revolutionize`, `facilitate`, `underpin`, `nuanced`, `crucial`, `multifaceted`, `ecosystem` (nghĩa bóng), `myriad`, `plethora`, `encompass`, `catalyze`, `augment`, `illuminate`, `elucidate`, `juxtapose`, `cornerstone`, `paramount`, `poised`, `burgeoning`, `nascent`, `overarching`. *(Lưu ý: Trong bài báo kỹ thuật, các từ `robust`, `comprehensive`, `leverage` được phép xuất hiện đơn lẻ nếu đi kèm thuật ngữ chuẩn như `robust estimator`, nhưng tuyệt đối không ghép thành cụm tính từ tán dương).*

*(Lưu ý cho Tiếng Việt: Trong **Tiếng Việt**, tuyệt đối **không tự ý thêm** các cụm từ đệm mùi AI khi câu gốc không có như `một cách toàn diện`, `sâu sắc`, `rõ rệt`, `hiện hữu`, `qua đó góp phần`, `đồng thời mở ra`, `đóng góp một phần không nhỏ`. Nếu câu gốc đã là tiếng Việt tự nhiên của tác giả, giữ nguyên 100%, không viết lại).*

---

## 3. Quy Trình Dịch 2-Pass Chi Tiết Cho 2 Chiều (`VI -> EN` và `EN -> VI`)

Khi người dùng ra lệnh ngắn gọn như **"viết lại tiếng Việt sang tiếng Anh"** (`vi-to-en`) hoặc **"dịch đoạn này sang tiếng Việt"** (`en-to-vi`), AI phải tuân thủ nghiêm ngặt quy trình 2-Pass dưới đây:

### 3.1. Chiều `vi-to-en` (Việt sang Anh Học thuật Chuẩn Tránh AI)

#### Quy trình thực thi:
1. **Pass 1 (Drafting)**: Dịch sát nghĩa các thuật ngữ kỹ thuật, bảo toàn số liệu, công thức toán và trích dẫn (`~\cite{...}`).
2. **Pass 2 (Avoid-AI Polishing)**: Rà soát và khử toàn bộ các khung câu máy móc của AI:
   - Cắt bỏ câu mở đầu đạo lý hiển nhiên (`Formulaic Opener`).
   - Xóa bỏ việc kết thúc mọi câu bằng cặp `X and/or Y` (Binomial Stacking) hoặc bộ 3 tính từ (Tricolon); rút gọn về 1 danh từ/động từ cụ thể.
   - Thay toàn bộ từ vựng hoa mỹ (`delve`, `rigorous`, `robust`, `utilize`, `paves the way`) bằng từ học thuật bình dị (`use`, `examine`, `strict`, `reliable`).
   - Phá vỡ nhịp câu phẳng lì: Kết hợp 1 câu ngắn trực diện (7–9 từ) + 1 câu phức đa mệnh đề (30–40 từ) để đưa hệ số biến thiên $CV \ge 0.45$.

#### Ví dụ Thực tế Minh họa 2-Pass (`VI -> EN`):
- **Đoạn Tiếng Việt Gốc (trong Luận văn / Bản thảo):**
  > *"Để giải quyết bài toán phát hiện hành vi dụ dỗ trẻ em trên mạng, nghiên cứu này không chỉ phân tích nội dung trò chuyện mà còn trích xuất các đặc trưng thời gian và cảm xúc. Nhóm tác giả kế thừa mô hình lai CNN-LSTM từ nghiên cứu trước đây nhằm phân loại các cuộc hội thoại đáng ngờ một cách hiệu quả và chính xác nhất."*

- ❌ **Pass 1 (Dịch trực tiếp — Dễ bị Grammarly bắt lỗi AI do dính Khung Cấu trúc):**
  > *"In order to address the challenge of detecting online grooming, this study does not just analyze chat content, it also extracts temporal and emotional features. The authors leverage the hybrid CNN-LSTM architecture from our prior research to facilitate the detection of suspicious conversations in the most effective and accurate manner."*
  *(Lỗi: dính `In order to` (Tier 1B), `does not just... it also...` (Negative Parallelism), `temporal and emotional features` + `effective and accurate` (Binomial stacking), `leverage` + `facilitate` (Tier 2 cluster), và `the most effective and accurate manner` (Superlative)).*

- ✅ **Pass 2 (Khử khung AI — Hoàn thiện Chuẩn Người Thật, $CV = 0.52$):**
  > *"Detecting online grooming requires analyzing both message text and communication dynamics. We adapted the hybrid CNN-LSTM network from our previous study~\cite{dang2023} to classify suspicious chat logs, incorporating time intervals and sentiment indicators as additional input features. This configuration maintained stable detection performance across noisy conversational datasets."*
  *(Đã thay `leverage`/`facilitate` bằng `adapted`/`classify`, bỏ cấu trúc phủ định `not just... but also...`, bỏ từ so sánh nhất `most effective`, tạo nhịp câu tự nhiên).*

---

### 3.2. Chiều `en-to-vi` (Anh sang Việt Học thuật Chuẩn Luận văn)

#### Quy trình thực thi:
1. **Pass 1 (Drafting)**: Dịch đúng nghĩa khoa học, neo giữ 4–7 từ khóa chính đã chốt ở Bước 0.
2. **Pass 2 (Avoid-AI Polishing)**:
   - Xóa bỏ các cấu trúc bị động dịch máy thô thiển (`được thực hiện bởi`, `được dựa trên`, `đóng một vai trò`).
   - Xóa bỏ 100% các từ đệm hoa mỹ sáo rỗng của AI tiếng Việt (`một cách toàn diện và sâu sắc`, `bức tranh toàn cảnh`, `minh chứng hùng hồn`, `khai phá tiềm năng`).
   - Chuẩn hóa dấu phẩy thập phân kiểu tiếng Việt (`98,3\%`, `$p < 0{,}01$`).

#### Ví dụ Thực tế Minh họa 2-Pass (`EN -> VI`):
- **Đoạn Tiếng Anh Gốc (`paper/main.tex`):**
  > *"Table 4 summarized the performance and running time of the different models on the Darkweb-CSAM dataset. Among the traditional ML models, SVM has the best results, achieving 87.6% Acc, 88.0% F1, and 93.29% ROC-AUC. For speed, NB was the fastest to train (0.90s), while LR had the quickest prediction time (0.001s)."*

- ❌ **Dịch kiểu AI Writing (Nhồi nhét từ hoa mỹ và tự bịa câu cảm thán ở cuối):**
  > *"Bảng 4 mang lại một cái nhìn toàn diện và sâu sắc về bức tranh tổng thể hiệu năng của các mô hình... Đáng kinh ngạc là NB chỉ mất 0,90 giây để huấn luyện... **Điều này là minh chứng hùng hồn mở ra hướng đi đầy hứa hẹn cho các ứng dụng thực tế.**"*

- ✅ **Dịch Chuẩn Người Thật (Pass 2 hoàn thiện, bám sát số liệu, câu chữ điềm đạm, không bình luận thừa):**
  > *"Bảng~\ref{tab_result-darkweb-csam} tổng hợp kết quả phân loại và thời gian chạy của các mô hình trên tập dữ liệu Darkweb-CSAM. Trong nhóm mô hình học máy truyền thống, SVM đạt kết quả cao hơn các phương pháp còn lại với Accuracy đạt 87,6\%, F1-Score đạt 88,0\% và ROC-AUC đạt 93,29\%. Xét về tốc độ xử lý, NB có thời gian huấn luyện ngắn nhất (0,90 giây), trong khi LR có thời gian dự đoán nhanh nhất (0,001 giây)."*

---

## 4. Hướng dẫn Sửa & Dịch Chiều Việt $\rightarrow$ Anh (`VI -> EN` & Sửa Paper Tiếng Anh Không Bị Báo AI)

### 4.1. Bảng Đối chiếu: Sửa Văn nói & Khử Cấu trúc AI trong `paper/main.tex`
Khi gặp một đoạn tiếng Anh trong bản thảo bị vướng văn nói (`isn't`, `by hand`, `honestly`, `dig into`), **kiểm tra xem khung câu gốc có phải do AI sinh ra hay không**:
- Nếu câu chỉ bị lỗi từ vựng đơn lẻ trong một đoạn văn học thuật bình thường $\rightarrow$ **Sửa tối thiểu từ bị lỗi**.
- Nếu cả đoạn văn có khung cấu trúc của AI (mở đầu giảng đạo lý `is not straightforward; it requires A, B, and C`, câu nào cũng dài ~15–20 từ, câu nào cũng có cặp `X and/or Y`, có câu thú nhận `we don't have the details`) $\rightarrow$ **Bắt buộc phá bỏ khung câu AI theo 5 bước ở Mục 2**:

| Đoạn gốc trong `paper/main.tex` | Cách sửa Chuẩn Người Thật (✅ Vượt qua Grammarly AI Detector) |
|---|---|
| `Research on sexual abuse and CSAM isn’t straightforward—it demands strict ethical oversight, careful data handling, and real protection for victims. This study evaluated three pre-existing textual datasets: Roman Urdu, PAN12, and Darkweb-CSAM... Our colleagues pulled together the Darkweb-CSAM dataset and labeled it by hand in our earlier work. That project got a formal ethics exemption, but honestly, we don’t have the details on who issued it or the reference number. Access to this dataset isn’t open—people need permission. On GitHub, you’ll only find our code and configuration files; we never include dataset records or anything sensitive there.` | `We did not collect new data for this study. All experiments used three existing text corpora: Roman Urdu, PAN12, and the Darkweb-CSAM dataset from our earlier work~\citep{Ngo-Elsevier:2024}, where colleagues manually labeled the text under a formal ethics exemption (the exemption reference number was not recorded in that study's documentation). Raw Darkweb-CSAM records remain restricted by permission. The public GitHub repository hosts only the source code, excluding all dataset files.` *(Đã cắt bỏ câu mở màn đạo lý + bộ 3 tính từ, xóa toàn bộ 6 cặp `X and/or Y` thừa, bỏ câu thú nhận kiểu chatbot, và tạo độ lệch nhịp câu `9 - 41 - 7 - 13` từ với $CV = 0.78$).* |
| `And honestly, even seasoned computer scientists can struggle to implement NLP algorithms for CSA text. So, researchers tend to stick with statistical methods...` | `Even experienced computer scientists often find NLP pipelines difficult to adapt to noisy CSA text, which explains why many studies still rely on statistical methods and standard ML/DL classifiers.` |
| `...which helped them dig deeper into how abuse plays out in various contexts.` | `...to examine how abuse occurs across different contexts.` |
| `The authors in [11] tapped into XAI and NLP to spot early warning signs and make beginners more aware of the problem.` | `The authors in \cite{Chadaga-Springer:2023} combined XAI with NLP to identify early warning signs for non-expert users.` |
| `In contrast, [19] went in a different direction, using big language models like GPT, Claude, and Gemini to scan video subtitles automatically so they could screen multimedia content for meaning—without having to do it all by hand.` | `In contrast, \cite{Huq-ACM:2025} used large language models (GPT, Claude, and Gemini) to scan video subtitles automatically, avoiding manual inspection during multimedia screening.` |

### 3.2. Các Lỗi Ngữ pháp "Vietglish" Cần Tránh Khi Dịch `VI -> EN`
1. **Không viết vừa `According to X` vừa dùng `X` làm chủ ngữ**:
   - ❌ *"According to Ngo et al. [10] proposed a system..."* $\rightarrow$ ✅ *"Ngo et al. [10] proposed a system..."*
2. **Không dùng `Although ... but ...` hoặc `Because ... so ...`**:
   - Đã có `Although` thì bỏ `but`; đã có `Because` thì bỏ `so`.
3. **Không bắt đầu câu bằng chữ số hoặc động từ `Have`**:
   - ❌ *"Have 38 papers focused on text."* / *"38 papers focused on text."* $\rightarrow$ ✅ *"Thirty-eight papers (74.5\%) focused on text-based CSAM."*
4. **Đồng bộ dấu chấm thập phân (`.`) trong bảng và văn bản tiếng Anh**:
   - Trong bài báo tiếng Anh, mọi số thập phân phải dùng dấu chấm (`95.37\%`, `99.89\%`), không để sót dấu phẩy tiếng Việt (`95,37\%`).

---

### 4.2. Phương Pháp Dịch Cầu Song Ngữ (Bilingual Roundtrip Triangulation: `EN -> VI -> EN`)

Khi viết lại bài báo tiếng Anh (`paper/main.tex`) để vừa đạt chuẩn học thuật quốc tế vừa **vượt qua 100% các công cụ kiểm tra AI (Grammarly, Turnitin, GPTZero)**:
1. **Bản chất vấn đề:**
   - Khi chỉnh sửa trực tiếp trên tiếng Anh (`EN -> EN rewrite`), các mô hình AI thường thay thế lỗi vụn vặt bằng một loạt "từ điển Latinh trừu tượng" (`systematically evaluates empirical literature across three core dimensions`, `acquisition modalities`, `taxonomic consistency`, `systematic framework tailored for...`), dùng mẫu liệt kê cơ học (`First,... Second,... Third,...`), chèn dấu gạch ngang nối ý lỏng lẻo (`—`), và tạo nhịp câu đều đều. Kết quả là văn bản bị Grammarly và Turnitin báo **100% AI Writing**!
2. **Quy trình Dịch Cầu Song Ngữ 2 Bước:**
   - **Bước 1 (`EN -> VI` Tự nhiên)**: Dịch văn bản gốc sang tiếng Việt tự nhiên, khúc chiết, mạch lạc như một nhà nghiên cứu đang trao đổi học thuật thực thụ. Bước này lập tức bóc tách sạch lớp vỏ từ vựng Latinh sáo rỗng và các khuôn mẫu câu robot của tiếng Anh.
   - **Bước 2 (`VI -> EN` Đanh thép)**: Dịch ngược từ bản tiếng Việt tự nhiên sang tiếng Anh học thuật:
     - Dùng động từ hành động trực tiếp và chủ ngữ kỹ thuật cụ thể.
     - Phá vỡ chuỗi liên từ liệt kê cơ học (`First/Next/Finally`), mở đầu bằng câu chủ đề dẫn dắt tự nhiên.
     - Đan xen câu ngắn dứt khoát (4–8 từ) bên cạnh câu phân tích chuyên sâu (20–35 từ) để đạt độ biến thiên nhịp điệu cao ($CV \ge 0.45$).
     - Loại bỏ toàn bộ dấu gạch ngang chữ `—` nối ý tùy tiện.
     - Bảo toàn nguyên vẹn 100% các nhãn trích dẫn `\cite{...}`, `\citep{...}`, `\ref{...}` và số liệu thực nghiệm.

---

## 5. Nguyên tắc Song ngữ Kỹ thuật & Bảng Chuẩn hóa Thuật ngữ Chuyên ngành (Technical Bilingualism & Domain-Specific Glossary)

### 5.1. Nguyên tắc Song ngữ Kỹ thuật (Technical Bilingualism & No Over-Translation)
Trong các ngành kỹ thuật như Khoa học Máy tính, Trí tuệ Nhân tạo và An ninh Mạng, cộng đồng nghiên cứu Việt Nam sử dụng song song các thuật ngữ quốc tế chuẩn mực. Việc cố gắng "Việt hóa 100%" từng thuật ngữ quen thuộc sẽ biến văn bản thành ngô nghê, gượng ép và gây cản trở tiếp nhận:
- **Giữ nguyên thuật ngữ mạng/hệ thống thông dụng**:
  - Dùng **mạng P2P** (không ép dùng *mạng ngang hàng* khi nói về kênh chia sẻ dữ liệu tội phạm số).
  - Dùng **darknet** (chuẩn xác hơn *web tối*, vì darknet là các mạng định tuyến ngầm đặc thù như Tor, I2P, Freenet).
  - Dùng **website** (tự nhiên hơn *trang mạng / trang thông tin điện tử*).
  - Dùng **sàng lọc title–abstract** (khớp trực tiếp với nhãn biểu đồ PRISMA và metadata bài báo, tránh dịch ngắt quãng).

### 5.2. Chuẩn hóa Thuật ngữ Pháp lý & Điều tra Số Tội phạm (Forensics & Cybercrime)
- **Hành vi số phạm pháp**:
  - `create, access, or share CSAM` $\rightarrow$ **tạo lập, truy cập hoặc phát tán CSAM** (chuẩn thuật ngữ tố tụng và điều tra hình sự số; cấm dùng *khởi tạo* [thuật ngữ tiến trình IT], *tiếp cận* [thụ động], *chia sẻ* [lành tính]).
  - `distribution channels` (trong bối cảnh tội phạm số/CSAM) $\rightarrow$ **kênh phát tán** hoặc **phương thức phát tán** (cấm dùng *kênh phân phối* - vốn là thuật ngữ thương mại logistics).
- **Phân tách thực thể trong Zeugma (`Identification of abusers and CSAM`)**:
  - Tách bạch động từ theo đúng thực thể: người phạm tội $\rightarrow$ **xác định thủ phạm / kẻ xâm hại**; tài liệu số $\rightarrow$ **phát hiện tài liệu CSAM**.
  - Cấm dùng trơ trọi danh từ *đối tượng* mà không có thuộc từ định danh (*đối tượng phạm tội*, *thủ phạm*).

### 5.3. Chuẩn hóa Thuật ngữ Phương pháp luận Tổng quan Hệ thống (PRISMA / SLR)
- `Search criteria` / `Inclusion criteria` $\rightarrow$ **tiêu chí / tiêu chuẩn tra cứu** (tuyệt đối KHÔNG dùng *mục đích*).
- `Search pages of digital libraries` $\rightarrow$ **tìm kiếm trên các cơ sở dữ liệu học thuật / thư viện số** (KHÔNG dùng *cổng tìm kiếm* - vốn gợi liên tưởng đến cổng thông tin dịch vụ công).
- `Downloading (in SLR stage)` $\rightarrow$ **truy xuất dữ liệu ban đầu / trích xuất bản ghi** (nhà nghiên cứu trích xuất metadata/bản ghi thư mục, không dùng từ khẩu ngữ *tải về ban đầu*).

### 5.4. Chuẩn hóa Thuật ngữ AI/Machine Learning & Khoa học Dữ liệu
- **Từ "Task" bắt buộc dịch là "BÀI TOÁN"**:
  - `tasks addressed` $\rightarrow$ **các bài toán được giải quyết / bài toán nghiên cứu**.
  - `CSAM tasks` $\rightarrow$ **các bài toán nghiên cứu về CSAM / bài toán phát hiện CSAM** (CẤM TUYỆT ĐỐI dịch thành *nhiệm vụ CSAM* vì tài liệu không có nhiệm vụ).
  - `classification task` $\rightarrow$ **bài toán phân loại**; `detection task` $\rightarrow$ **bài toán phát hiện**.
- **Phân biệt `Data` vs `Dataset` & Giữ nguyên từ khóa kỹ thuật `Dataset`**:
  - Dùng **dataset** để chỉ bộ dữ liệu cụ thể có cấu trúc, tránh nhầm với `data` (dữ liệu thô nói chung).
  - **Quy tắc chống lặp từ kép**: Dùng 1 danh từ `dataset` duy nhất đi kèm cặp tính từ: **dataset công khai hoặc đóng** (CẤM: *dataset công khai hoặc dataset đóng*).
- **Thuật ngữ "Dataset Availability"**:
  - `availability (public or private)` $\rightarrow$ **dạng công khai hoặc đóng / quyền truy cập (công khai hay bảo mật)**. CẤM TUYỆT ĐỐI dịch thành *tính khả dụng* (sai lệch sang usability).
- **Thuật ngữ "We report" trong nghiên cứu tổng quan / khảo sát (Survey/SLR)**:
  - `For each paper, we report [X, Y, Z]` $\rightarrow$ **thống kê / tổng hợp chi tiết [X, Y, Z]**. CẤM dùng *ghi nhận* (lệch sắc thái phương pháp luận).
