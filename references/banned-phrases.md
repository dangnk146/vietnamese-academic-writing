<!-- vlc-disable: ALL -->

# Danh mục từ ngữ cấm trong Luận văn Thạc sĩ, Tiến sĩ và Paper IEEE / Q1

Văn phong học thuật quốc tế và luận văn sau đại học đòi hỏi tính khách quan, khiêm tốn khoa học, sự tự nhiên như người viết thật và lập luận dựa trên bằng chứng định lượng. Các từ ngữ dưới đây bị nghiêm cấm hoặc hạn chế tối đa trong quá trình viết, dịch thuật và biên tập.

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

Văn phong học thuật cấm dùng từ giật gân, hoang mang, cảm thán như báo chí lá cải. Tác động của bệnh lý, tội phạm mạng hoặc sai lệch kỹ thuật phải được mô tả bằng thuật ngữ khoa học và số liệu thống kê.

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
| `bạn` / `you` / `your` | Ngôn ngữ giao tiếp thân mật, hướng dẫn sử dụng phần mềm | Tiếng Việt: `người thao tác`, `người làm chuyên môn`, `bác sĩ lâm sàng`. Tiếng Anh: dùng câu bị động hoặc chủ ngữ `we` / `researchers`. |
| `quý vị` / `anh/chị` | Ngôn từ thuyết trình hội thảo hoặc bán hàng | Dùng ngôi thứ ba mô tả chức danh: `hội đồng`, `độc giả`, `các nhà nghiên cứu`. |

---

## 4. Dịch máy thô thiển (Academic Translationese & Clichés)

<!-- machine-readable: calques -->

| Cụm dịch máy thô (❌) | Dạng tiếng Việt chuẩn học thuật (✅) | Ghi chú |
|---|---|---|
| `được thiết kế bởi tác giả` | `do tác giả thiết kế` | Tránh lạm dụng bị động tiếng Anh (*is designed by*). |
| `đóng một vai trò quan trọng` | `đóng vai trò quan trọng` | Bỏ chữ "một" thừa thãi từ *play an important role*. |
| `thực hiện một cuộc điều tra` | `tiến hành khảo sát` | Bỏ *conduct an investigation*. |
| `đánh giá văn học` | `tổng quan tài liệu` | Dịch sai từ *literature review*. |
| `trong một cách thức hiệu quả` | `một cách hiệu quả` | Dịch thô từ *in an effective manner*. |
| `được dựa trên` | `dựa trên` | Tránh bị động kép không tự nhiên. |
| `cho thấy rằng` (dày đặc) | `cho thấy` / `chứng minh` / `kết quả chỉ ra` | Đa dạng hóa liên từ báo cáo kết quả. |
| `tái lấy mẫu không gian đẳng hướng` | `tái lấy mẫu về độ phân giải $1 \times 1 \times 1$\,mm` / `tái lấy mẫu đẳng hướng` | Tránh dịch gượng ép, dùng chuẩn độ đo. |
| `cấu trúc mô phi não bộ` | `xương sọ và các mô ngoài não` (non-brain tissues) | Chuẩn thuật ngữ y sinh giải phẫu sọ não. |
| `dữ liệu ảnh thô ban đầu` | `ảnh DICOM gốc` / `ảnh NIfTI gốc` | Chuẩn xác thực thể dữ liệu đầu vào. |
| `tác động tiêu cực` / `biến đổi bệnh học cốt lõi` | Mô tả kỹ thuật cụ thể: `gây nhiễu tín hiệu`, `đặc trưng teo mô não` | Bỏ cụm từ sáo rỗng, chung chung. |
| `thiết lập tuần tự nhằm` | `bao gồm các bước chuyển đổi...` | Bỏ cách diễn đạt khuôn mẫu rườm rà. |
| `khối thể tích 3D` / `khối thể tích` | `khối ảnh 3D` / `khối 3D` | Thừa chữ "thể tích", "khối 3D" đã thể hiện đầy đủ đối tượng thể tích 3 chiều. |
| `sáu bước kỹ thuật` / `bước kỹ thuật` | `sáu bước` / `các bước` | Lạm dụng từ "kỹ thuật" rườm rà, sáo rỗng. |
| `có định hướng giải phẫu kết hợp` / lạm dụng `giải phẫu` | Mô tả kỹ thuật xử lý ảnh: `ba mặt phẳng axial, coronal, sagittal`, `vùng mô não mang chỉ dấu` | Đề tài CNTT xử lý ảnh số; cấm lạm dụng từ "giải phẫu" đao to búa lớn gây hiểu nhầm sang phẫu thuật/ngoại khoa. |
| Lạm dụng ký hiệu toán học hình thức trong văn xuôi (VD: `$\mu_{\text{CSF}} < \mu_{\text{GM}} < \mu_{\text{WM}}$`, `$P_{\text{GM}} \in [0, 1]$`) | Diễn giải bằng văn xuôi khoa học tự nhiên: `cường độ sáng tăng dần từ dịch não tủy, chất xám đến chất trắng`, `vùng mô chất xám` | Tránh phô diễn ký hiệu hình thức gây rối mắt và làm đứt gãy luồng đọc; chỉ dùng công thức độc lập cho định nghĩa toán học cốt lõi. |
| `theo lịch trình suy giảm hàm cosin` | `giảm dần theo hàm cosin` | Dịch thô từ *cosine annealing schedule*. Diễn đạt trực tiếp quy luật biến thiên tốc độ học. |
| `khởi động tuyến tính ở các chu kỳ đầu` / dịch `epoch` thành `chu kỳ` | `bước khởi động ở các epoch đầu` / `bước khởi động (warmup)` | Cấm dịch `epoch` thành "chu kỳ" (dễ nhầm với cycle/period). Giữ nguyên `epoch`. |
| `tầng tự chú ý` / `các tầng tự chú ý` | `khối Attention` / `các khối Attention` | Tránh dịch thô *self-attention layers*. |
| `không gian trạng thái Mamba-2` / `Mamba-2` (trong ngữ cảnh mô hình) | `Mamba2` | Bỏ tiền tố rườm rà "không gian trạng thái", bỏ dấu gạch nối `-`, đồng bộ chuẩn với `Mamba2-Attention`. |
| `năng lượng giải tích` | `hàm năng lượng không tham số SimAM` / `năng lượng nơ-ron sinh học` | Dịch máy ngô nghê từ *analytical energy function minimization*. |
| `mô-đun quan hệ không gian SRM` | `mô-đun hiệu chuẩn phong cách đặc trưng SRM` | Nhận diện sai từ viết tắt; SRM là *Style-based Recalibration Module* (Lee et al., ICCV 2019), không phải Spatial Relationship Module. |
| Lặp công thức 3 dòng cho 3 góc nhìn ($x''_a, x''_c, x''_s$) | Dùng chỉ số đại diện $v \in \{a, c, s\}$: $\tilde{x}_v = \dots$ | Tránh viết lặp công thức vụn vặt gây loãng văn bản và đứt gãy luồng đọc. |

---

## 5. Phân định ngữ cảnh từ "Hệ thống" và "Tự động" trong mô tả giải thuật / mô hình

Trong viết luận văn Thạc sĩ/Tiến sĩ và bài báo khoa học, việc lạm dụng từ *"hệ thống"* và *"tự động"* khi mô tả một mô hình đơn lẻ tạo cảm giác quảng cáo phần mềm thương mại và mang màu sắc dịch máy:

| Từ kiểm soát | Nguy cơ văn phong | Cách diễn đạt chuẩn mực thay thế |
|---|---|---|
| `hệ thống thực hiện...` / `hệ thống tiếp nhận...` / `kiến trúc hệ thống` (khi chỉ nói về 1 mạng nơ-ron) | Mơ hồ hóa chủ thể, giọng điệu thương mại phần mềm | Dùng tên thực thể kỹ thuật cụ thể: `mô hình đề xuất`, `mạng nơ-ron`, `bộ mã hóa`, `thuật toán`, `quy trình`, `kiến trúc mô hình`. *(Giữ nguyên từ "hệ thống" trong danh từ khoa học chuẩn: tổng quan tài liệu hệ thống, có hệ thống, hệ thống y tế công cộng, hệ thống bảo vệ trẻ em, hệ thống phân loại tệp, hệ quy chiếu, hệ tọa độ, hệ thần kinh).* |
| `hệ thống tự động...` / `tự động trích xuất` / `tự động học` | Thổi phồng công nghệ, văn phong tiếp thị | Mô tả trực tiếp cơ chế: `khối tâm được xác định`, `trọng số thích nghi $w_s$ được học thông qua...`, `phương pháp bóc tách`, `trích chọn lát cắt`. *(Chỉ dùng "tự động" khi đối chiếu trực tiếp với kiểm tra thủ công `manual inspection`).* |

---

## 6. Nguyên tắc "Chống ảo giác & Bịa đặt chi tiết" (Zero-Hallucination & Speculative Claims)

Trong nghiên cứu khoa học, mọi nhận định chuyên môn và cơ chế kỹ thuật **phải bám sát tuyệt đối bài báo gốc hoặc tài liệu tham khảo có trích dẫn (`~\cite{...}`)**:

- **CẤM TUYỆT ĐỐI**: Tự suy diễn hoặc bịa đặt thêm các danh sách cơ quan giải phẫu, mô học, hoặc cơ sở bệnh học thần kinh không có trong tài liệu gốc (ví dụ: tự vẽ ra *"Cơ sở giải phẫu học thần kinh xuất phát từ đặc tính bệnh lý: chất xám là nơi tập trung mật độ cao thân tế bào nơ-ron và các khớp thần kinh..."* khi bài báo không đề cập).
- **CẤM TUYỆT ĐỐI**: Tự ý bịa đặt thêm các phương án kiến trúc hoặc biến thể mở rộng không có trong sơ đồ mô hình và không có thực nghiệm đối chứng.
- **CẤM DÙNG TỪ "KHẲNG ĐỊNH RẰNG" KHI TRÍCH DẪN NGHIÊN CỨU TIỀN NHIỆM**: Không được quy kết sai lệch rằng công trình của tác giả khác (như Tanveer et al., Nanni et al.) *"khẳng định rằng..."* nếu họ chỉ là bài khảo sát (review) hoặc thực nghiệm so sánh. Dùng động từ trung tính, chính xác: `khảo sát`, `sử dụng`, `thực nghiệm trên`, `kế thừa hướng tiếp cận`, `kết quả thực nghiệm cho thấy`.
- **CẤM TUYỆT ĐỐI CÁC CỤM TỪ CƯỜNG ĐIỆU CĂN CỨ KHOA HỌC**:
  - ❌ *"là bằng chứng giải phẫu thực nghiệm khẳng định cơ sở khoa học..."* $\rightarrow$ ✅ *"minh họa cơ sở cho việc lựa chọn phạm vi tìm kiếm..."*
  - ❌ *"bao trọn vùng giải phẫu đã được kiểm định"* $\rightarrow$ ✅ *"bao quát vùng giải phẫu mang thông tin biến đổi..."*
- **CẤM TUYỆT ĐỐI**: Tự bịa đặt các phân chia tiểu mục (ví dụ gom 6 bước của bài báo thành 3 "pha" với tên tự chế).
- **Quy tắc vàng**: Nếu tài liệu gốc ghi $N$ bước kỹ thuật, hãy trình bày trung thực $N$ bước kỹ thuật.

---

## 7. Cấm câu mở đầu sáo rỗng dạng diễn văn & Câu đuôi bình luận cảm thán của AI (No Boilerplate & No AI Commentary)

- **CẤM TUYỆT ĐỐI câu mở đầu triết lý sáo rỗng**:
  - ❌ *"Khả năng khái quát hóa và chất lượng biểu diễn của dữ liệu đầu vào giữ vai trò nền tảng quyết định độ chính xác chẩn đoán của các mô hình học sâu..."*
  - ❌ *"Trong kỷ nguyên số hóa y tế hiện nay, việc tiền xử lý ảnh đóng vai trò vô cùng cấp thiết..."*
- **CẤM TUYỆT ĐỐI câu đuôi nhận định vô căn cứ / cảm thán của AI**:
  - ❌ *"Điều này mở ra một kỷ nguyên mới / hướng đi đầy hứa hẹn..."*
  - ❌ *"Đây là minh chứng hùng hồn cho sức mạnh vượt trội của..."*
  - ❌ *"Thật thú vị khi nhận thấy rằng..."* / *"Đáng kinh ngạc là..."* / *"Không thể phủ nhận rằng..."*
  - ❌ *"mang lại cái nhìn sâu sắc và toàn diện về bức tranh tổng thể..."*
- **CẤM TUYỆT ĐỐI các từ "làm màu" và Khung Cấu trúc AI trong Tiếng Anh (Tích hợp `conorbronsdon/avoid-ai-writing` & Chống Grammarly AI Detector)**:
  - ❌ **Tier 1A — Từ vựng đặc trưng của AI (Cấm tuyệt đối)**: `delve`, `delve into`, `tapestry`, `realm`, `beacon`, `testament to`, `cutting-edge`, `pivotal`, `underscores`, `meticulous`, `meticulously`, `game-changer`, `watershed moment`, `showcasing`, `deep dive`, `unpack`, `intricate`, `intricacies`, `ever-evolving`, `daunting`, `holistic`, `actionable`, `impactful`, `synergy`, `interplay`, `symphony`, `load-bearing` (nghĩa bóng), `rigorous`, `granular`, `pronounced`, `manifest`, `thereby + V-ing`, `paves the way`.
  - ❌ **Tier 1B — Từ rườm rà và Né động từ `to be/have` (Copula Avoidance)**: `utilize` ($\rightarrow$ `use`), `in order to` ($\rightarrow$ `to`), `due to the fact that` ($\rightarrow$ `because`), `serves as` / `boasts` / `features` (động từ) ($\rightarrow$ `is` / `has` / `includes`), `endeavor` ($\rightarrow$ `effort`), `ascertain` ($\rightarrow$ `determine`).
  - ❌ **Tier 2 — Cụm từ cấm xuất hiện từ 2 từ trở lên trong cùng 1 đoạn (`Tier 2 Cluster`)**: `harness`, `navigate`, `foster`, `elevate`, `unleash`, `streamline`, `empower`, `bolster`, `spearhead`, `resonate`, `revolutionize`, `facilitate`, `underpin`, `nuanced`, `crucial`, `multifaceted`, `myriad`, `plethora`, `encompass`, `catalyze`, `augment`, `illuminate`, `elucidate`, `juxtapose`, `cornerstone`, `paramount`, `poised`, `burgeoning`, `nascent`, `overarching`.
  - ❌ **Khung câu Phủ định – Khẳng định & Đạo lý mở màn (`Negative Parallelism` + `Formulaic Opener`)**:
    - Cấm mở đầu đoạn bằng: `"[Topic] is not straightforward; it requires [A, B, and C]"` hoặc `"It is not X — it is Y"`, `"Access to X is not public and requires..."`, `"provide only X, without any Y or Z"`.
  - ❌ **Câu thú nhận thiếu thông tin kiểu Chatbot (`Cutoff Disclaimers` & `Narrated Candor`)**:
    - Cấm viết: `"although we do not have the details on..."`, `"while specific details are limited based on available information"`, `"to be honest"`, `"it is worth noting that"`, `"importantly,"`, `"notably,"`, `"interestingly,"`.
  - ❌ **Xếp chồng cặp ghép `X and/or Y` (Binomial Stacking) & Nhịp câu đều đặn (`Low Burstiness`)**:
    - Cấm viết đoạn văn mà hơn 50% số câu đều kết thúc bằng cặp ghép `A and B` / `A or B` (ví dụ: `collected and labeled`, `issuing body or reference number`, `code and configuration files`, `dataset records or sensitive material`).
    - Cấm viết 4–6 câu liên tiếp có độ dài sàn sàn 14–21 từ ($CV < 0.35$); bắt buộc trộn câu rất ngắn (6–9 từ) với câu dài nhiều mệnh đề (30–40 từ, $CV \ge 0.45$).
  - ❌ **Các từ văn nói tiếng Anh trong bài báo**: `it's`, `isn't`, `don't`, `doesn't`, `can't`, `you'll`, `honestly`, `dig into`, `dig deeper`, `tap into`, `pull out`, `covers a lot of ground`, `have a hand in`, `went in a different direction`, `big language models`, `by hand`.
  - ✅ **Thay bằng động từ học thuật giản dị và cấu trúc câu lệch nhịp của người viết thật**: `use`, `apply`, `show`, `find`, `collect`, `label manually`, `examine`, `extract`, `help`, `require`, `provide`, `host`, `exclude`.

---

## 8. Nguyên tắc kế thừa tên viết tắt (Acronym Reuse)

- Đối với luận văn hoặc bài báo **có khai báo gói `acronym`**: Khi một tổ chức, bộ dữ liệu hoặc phương pháp đã được giới thiệu và định nghĩa tên đầy đủ ở Chương 1 hoặc Chương 2 (ví dụ: `ADNI`, `MRI`, `GMM`), ở các chương sau **CHỈ ĐƯỢC DÙNG MACRO VIẾT TẮT** `\acs{ADNI}`. Cấm lặp lại diễn giải dài dòng như *"từ sáng kiến Chẩn đoán hình ảnh ADNI được..."*.
- Đối với bài báo **không dùng gói `acronym`** (như `paper/main.tex`): Viết tên đầy đủ kèm chữ viết tắt trong ngoặc đơn ở lần đầu xuất hiện (`child sexual abuse material (CSAM)`), các lần sau viết thẳng `CSAM`; tuyệt đối không chèn `\acs{CSAM}` gây lỗi biên dịch.

---

## 9. Cấm biến mô hình Deep Learning thành danh mục thông số phần cứng (No Hardware-Spec Style & No-Itemize Abuse)

Trong paper IEEE/Q1 và luận văn Thạc sĩ/Tiến sĩ, mô hình học sâu là một tiến trình toán học biến đổi không gian đặc trưng ($X \rightarrow Z \rightarrow Y$), không phải là một danh mục cài đặt phần cứng hay sổ tay kỹ thuật thiết bị:

| Lối viết sai / Cụm từ cấm (❌) | Nguy cơ văn phong | Cách diễn đạt chuẩn mực thay thế (✅) |
|---|---|---|
| `Kiến trúc mạng được thiết lập với các thông số cấu hình chi tiết:` | Giọng điệu sổ tay hướng dẫn phần cứng / phần mềm, vi phạm chuẩn bài báo khoa học | Dẫn dắt bằng câu luận điểm kiến trúc: *"Bộ mã hóa áp dụng kiến trúc phân cấp đa giai đoạn nhằm chuyển hóa dần biểu diễn từ không gian điểm ảnh..."* |
| `Bộ mã hóa được tổ chức tuần tự qua các tầng...` / `tinh chỉnh tuần tự` (trong mạng thị giác) | Nhầm lẫn thuật ngữ deep learning: "tuần tự" (sequential) chỉ quy trình RNN / LSTM / chuỗi thời gian, không mô tả mạng thị giác phân tầng | Với mạng thị giác phân tầng, dùng: `kiến trúc phân cấp đa giai đoạn`, `tiếp nối`, `chuỗi khối tiếp nối`. Chỉ giữ từ `tuần tự` khi nói về dữ liệu chuỗi / mạng LSTM. |
| `Các thông số kỹ thuật của mô hình bao gồm:` | Nhầm lẫn giữa đặc tả kiến trúc học sâu và thông số thiết bị | *"Mô hình thiết lập cấu trúc phân cấp đa tầng với các khối chức năng chuyên biệt:"* |
| Lạm dụng `\begin{itemize}` để liệt kê từng tầng mạng (`Stem`, `Giai đoạn 1`, `Giai đoạn 2`...) | Cắt vụn dòng chảy văn bản, thiếu tính liên kết ngữ nghĩa của luồng tensor toán học | Trình bày thành các đoạn văn học thuật liền mạch (prose); phân tích rõ cơ chế xử lý luồng tensor, hàm kích hoạt và cơ sở toán học/thiết kế của từng khối. |
