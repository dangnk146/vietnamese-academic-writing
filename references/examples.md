<!-- vlc-disable: ALL -->

# Các Cặp Ví dụ Đối chiếu Thực tế (Bad ❌ $\rightarrow$ Good ✅)

Tài liệu này tổng hợp các cặp ví dụ đối chiếu giữa cách viết sai thường gặp của LLM và cách viết chuẩn mực của người viết học thuật thật trong Luận văn Thạc sĩ, Tiến sĩ và Paper IEEE / Q1.

---

## Nhóm 1: Loại bỏ từ so sánh nhất và khẳng định tuyệt đối (Zero-Superlative)

### Ví dụ 1.1: Khẳng định hiệu năng mô hình
❌ **Sai:**
> Mô hình đề xuất HTFV-Mamba2Attention đạt kết quả tốt nhất hiện nay trên bộ dữ liệu ADNI, hoàn toàn vượt trội so với các nghiên cứu trước đó với độ chính xác tuyệt đối 99%.

✅ **Đúng:**
> Mô hình đề xuất HTFV-Mamba2Attention đạt độ chính xác 94,18\%, cải thiện đáng kể so với các kiến trúc tích chập truyền thống trên cùng điều kiện phân chia dữ liệu độc lập ở cấp độ bệnh nhân.

*Giải thích lỗi:* Từ "tốt nhất hiện nay", "hoàn toàn vượt trội", "độ chính xác tuyệt đối" vi phạm tính khiêm tốn khoa học. Trong nghiên cứu y tế, 99\% thường là độ chính xác ảo do rò rỉ dữ liệu. Cần nêu số liệu thực tế có kiểm soát và so sánh công bằng.

---

### Ví dụ 1.2: Đánh giá phương pháp tiếp cận
❌ **Sai:**
> Chuỗi xung T1 là phương pháp chụp cộng hưởng từ hoàn hảo nhất và tối ưu nhất để nhìn rõ vỏ não.

✅ **Đúng:**
> Trong các kỹ thuật chẩn đoán hình ảnh, chụp cộng hưởng từ \acs{MRI}, đặc biệt là chuỗi xung T1, được xem là phương pháp tiêu chuẩn không xâm lấn. Ảnh MRI T1 cung cấp độ tương phản sắc nét giữa chất xám \acs{GM}, chất trắng \acs{WM} và dịch não tủy \acs{CSF}, cho phép quan sát rõ độ dày vỏ não và các tổn thương cấu trúc trong nhu mô não~\cite{despotovic2015mri}.

*Giải thích lỗi:* "Hoàn hảo nhất và tối ưu nhất" là lỗi lặp từ khẳng định tuyệt đối phi khoa học. Thay bằng "phương pháp tiêu chuẩn không xâm lấn" kèm giải thích cơ chế tương phản mô học và trích dẫn chuẩn.

---

## Nhóm 2: Loại bỏ kịch tính hóa & ngôn từ nghiêm trọng hóa (Zero-Hyperbole)

### Ví dụ 2.1: Trình bày bối cảnh bệnh lý
❌ **Sai:**
> Bệnh Alzheimer là một thảm họa vô cùng nghiêm trọng và cực kỳ nguy hiểm, đang đe dọa sự sống còn của hàng triệu người già mà y học hoàn toàn bế tắc không thể cứu vãn.

✅ **Đúng:**
> Cùng với xu hướng già hóa dân số toàn cầu, các bệnh lý thoái hóa thần kinh mạn tính đã và đang trở thành thách thức to lớn đối với hệ thống y tế công cộng~\cite{reitz_global_2023}. Trong số đó, bệnh Alzheimer (\acs{AD}) là nguyên nhân phổ biến gây ra hội chứng sa sút trí tuệ ở người cao tuổi, chiếm tỷ lệ khoảng từ 60\% đến 70\% trong tổng số hơn 55 triệu người mắc chứng sa sút trí tuệ trên toàn thế giới~\cite{reitz_global_2023}.

*Giải thích lỗi:* Từ "thảm họa vô cùng nghiêm trọng", "cực kỳ nguy hiểm", "hoàn toàn bế tắc" mang tính cảm tính, giật gân như báo lá cải. Thay bằng các nhận định mực thước: "thách thức to lớn", kết hợp trích dẫn số liệu dịch tễ chính xác.

---

### Ví dụ 2.2: Phân tích hiện tượng rò rỉ dữ liệu
❌ **Sai:**
> Rò rỉ dữ liệu là một sai lầm chết người và là vấn nạn nhức nhối phá hủy toàn bộ độ tin cậy của các bài báo trước đây.

✅ **Đúng:**
> Mặc dù các mô hình học sâu công bố trên \acs{ADNI} thường xuyên báo cáo độ chính xác rất cao vượt ngưỡng 95\%, thậm chí tiếp cận 99\%, song các kết quả này tiềm ẩn nguy cơ bị thổi phồng do những hạn chế trong phương pháp luận thực nghiệm. Khi các lát cắt của cùng một bệnh nhân xuất hiện ở cả tập huấn luyện và kiểm thử, mô hình có xu hướng nhận diện cá thể người bệnh thay vì thực sự nắm bắt các tổn thương thoái hóa não do bệnh lý gây ra.

*Giải thích lỗi:* "Sai lầm chết người", "vấn nạn nhức nhối" mang sắc thái công kích, thiếu khách quan. Cần phân tích nguyên nhân phương pháp luận và cơ chế kỹ thuật dẫn đến sự thiên lệch dữ liệu.

---

## Nhóm 3: Cấu trúc đoạn văn chuẩn & Luận điểm mở/kết (Paragraph Architecture)

### Ví dụ 3.1: Chuyển đổi đoạn văn vụn vặt thành đoạn Diễn dịch hoàn chỉnh
❌ **Sai (Ngắt dòng tùy tiện, chia vụn kiểu gạch đầu dòng, không có luận điểm):**
> Nghiên cứu này dùng ADNI.
> ADNI có nhiều bệnh nhân chụp nhiều lần.
> Nếu chia dữ liệu ngẫu nhiên sẽ bị sai lệch.
> Chúng tôi thấy các bài báo trước đây bị sai nhiều.
> Vì vậy cần phải chia theo bệnh nhân.

✅ **Đúng (Đoạn văn Diễn dịch liền mạch, câu đầu là Luận điểm):**
> Để khắc phục các hạn chế về mặt phương pháp luận này, việc thiết lập quy trình phân chia dữ liệu độc lập ở cấp độ bệnh nhân là yêu cầu bắt buộc nhằm loại bỏ hoàn toàn hiện tượng rò rỉ thông tin giữa các lần quét định kỳ. Khi phân chia đúng chuẩn theo từng cá thể, mô hình học sâu buộc phải học các đặc trưng biến đổi bệnh học tổng quát thay vì ghi nhớ hình thái cấu trúc riêng biệt của từng người bệnh. Thực nghiệm đối chứng của Yagis và cộng sự~\cite{yagis2021effect} đã chứng minh rằng quy trình phân chia nghiêm ngặt này phản ánh chính xác năng lực chẩn đoán thực tế, ngăn ngừa độ chính xác ảo bị thổi phồng tới 30\% so với phân chia theo lát cắt ngẫu nhiên.

*Giải thích cấu trúc:* Câu 1 nêu rõ luận điểm phương pháp luận bắt buộc. Câu 2 giải thích lý do bản chất học máy. Câu 3 củng cố bằng thực nghiệm đối chứng định lượng và trích dẫn khoa học. Toàn bộ đoạn văn là một khối thống nhất, không ngắt dòng ngẫu nhiên.

---

## Nhóm 4: Ngôi xưng khách quan & Dấu câu chuẩn mực

### Ví dụ 4.1: Loại bỏ ngôi xưng thứ nhất và dấu phẩy bừa bãi
❌ **Sai:**
> Tôi đề xuất, một mô hình mới kết hợp Mamba và Attention, để giúp bạn có thể, phân loại bệnh nhân Alzheimer một cách dễ dàng nhất.

✅ **Đúng:**
> Luận văn đề xuất kiến trúc mạng lai HTFV-Mamba2Attention kết hợp mô hình không gian trạng thái Mamba-2 với cơ chế tự chú ý, nhằm nâng cao hiệu quả phân loại đa giai đoạn bệnh Alzheimer trên ảnh cộng hưởng từ não bộ.

*Giải thích lỗi:* 
1. Thay "Tôi đề xuất" bằng "Luận văn đề xuất" (Impersonal).
2. Xóa bỏ từ "bạn" và từ so sánh nhất "dễ dàng nhất".
3. Xóa các dấu phẩy ngắt vụn giữa chủ ngữ, vị ngữ và bổ ngữ.

---

## Nhóm 5: Phân biệt "Sửa kiểu Văn mẫu AI" (Bị Grammarly bắt lỗi AI) vs. "Viết như Người Thật"

Khi dịch hoặc sửa văn bản (cả tiếng Việt lẫn tiếng Anh), lỗi nặng nhất của AI là **tự ý thay từ giản dị bằng từ đao to búa lớn**, dùng **cấu trúc bộ 3 tính từ (tricolon)** và **tự bịa thêm câu nhận định/cảm thán ở cuối đoạn**.

### Ví dụ 5.1: Dịch từ Tiếng Anh sang Tiếng Việt (`EN -> VI`) tự nhiên, giữ nguyên từ khóa chính, không thêm lời bình của AI
- **Câu gốc Tiếng Anh (`paper/main.tex`):**
  > *"Table 4 summarized the performance and running time of the different models on the Darkweb-CSAM dataset. Among the traditional ML models, SVM has the best results, achieving 87.6% Acc, 88.0% F1, and 93.29% ROC-AUC. For speed, NB was the fastest to train (0.90s), while LR had the quickest prediction time (0.001s)."*

❌ **Dịch kiểu AI Writing (Tự ý nhét từ hoa mỹ, tự bịa thêm câu nhận định cảm thán ở cuối):**
> Bảng 4 mang lại cái nhìn sâu sắc và toàn diện về hiệu năng cũng như thời gian thực thi của các mô hình trên tập dữ liệu Darkweb-CSAM. Không chỉ vượt trội trong nhóm học máy truyền thống, SVM còn xuất sắc đạt độ chính xác 87,6\%, điểm F1 88,0\% và ROC-AUC 93,29\%. Đáng kinh ngạc là về mặt tốc độ, NB chỉ mất 0,90 giây để huấn luyện, trong khi LR có thời gian suy luận cực nhanh ở mức 0,001 giây. **Điều này là minh chứng hùng hồn cho thấy các mô hình truyền thống vẫn đóng góp một phần không nhỏ trong thực tiễn.**

✅ **Dịch chuẩn Người viết thật (Bám sát bản gốc, giữ đúng từ khóa chính, câu chữ gọn gàng, không bình luận thừa):**
> Bảng~\ref{tab_result-darkweb-csam} tổng hợp kết quả phân loại và thời gian chạy của các mô hình trên tập dữ liệu Darkweb-CSAM. Trong nhóm mô hình học máy truyền thống, SVM đạt kết quả cao hơn các phương pháp còn lại với Accuracy đạt 87,6\%, F1-Score đạt 88,0\% và ROC-AUC đạt 93,29\%. Xét về tốc độ xử lý, NB có thời gian huấn luyện ngắn nhất (0,90 giây), trong khi LR có thời gian dự đoán nhanh nhất (0,001 giây).

---

### Ví dụ 5.2: Sửa lỗi văn nói Tiếng Anh (`VI -> EN` / `EN Polish`) và Phá bỏ Khung Cấu trúc AI (`avoid-ai-writing`) để Vượt qua Grammarly AI Detector
- **Đoạn gốc có lỗi văn nói và khung câu AI-Humanizer (`paper/main.tex`):**
  > *"Research on sexual abuse and CSAM isn’t straightforward—it demands strict ethical oversight, careful data handling, and real protection for victims... Our colleagues pulled together the Darkweb-CSAM dataset and labeled it by hand in our earlier work. That project got a formal ethics exemption, but honestly, we don’t have the details on who issued it or the reference number. Access to this dataset isn’t open—people need permission. On GitHub, you’ll only find our code and configuration files; we never include dataset records or anything sensitive there."*

❌ **Sửa sai Mức 1 — Kiểu AI Từ vựng hoa mỹ (Bị Grammarly báo 100% AI vì dùng bộ 3 tính từ `rigorous... strict... robust...` và từ vựng làm màu `compiled`, `archived in the secondary metadata`):**
> Research involving CSAM requires **rigorous** ethical oversight, **strict** data governance, and **robust** victim-protection protocols. The Darkweb-CSAM dataset was **compiled** and manually annotated in our prior study under an institutional ethics exemption, although the specific issuing body and reference number were not **archived in the secondary metadata**. Access to the raw dataset remains restricted to authorized researchers; the public GitHub repository contains only source code and configuration files, excluding all sensitive records.

❌ **Sửa sai Mức 2 — Chỉ thay từ đơn giản nhưng GIỮ NGUYÊN KHUNG CẤU TRÚC AI (Vẫn bị Grammarly báo 100% AI Writing!):**
> Research on sexual abuse and CSAM **is not straightforward; it requires** **strict ethical oversight, careful data handling, and protection for victims**. Our colleagues **collected** the Darkweb-CSAM dataset **and labeled** it manually in our earlier work~\citep{Ngo-Elsevier:2024}. That project received a formal ethics exemption, **although we do not have the details on** **the issuing body or the reference number**. Access to this dataset **is not public and requires** permission. On GitHub, we provide **only** **our code and configuration files**, **without any** **dataset records or sensitive material**.

*Tại sao Mức 2 dùng toàn từ đơn giản mà vẫn bị Grammarly bắt 100% AI?*
Theo bộ quy tắc [`avoid-ai-writing`](https://github.com/conorbronsdon/avoid-ai-writing) và cơ chế chấm điểm Perplexity/Burstiness của Grammarly, đoạn Mức 2 giữ nguyên **5 dấu vân tay cấu trúc của GPT-4**:
1. **Câu mở màn giảng đạo lý + Phủ định kép + Bộ 3 danh từ (`Formulaic Opener` + `Negative Parallelism` + `Rule of Three`)**: `"Research on X is not straightforward; it requires A, B, and C."` — Không một nhà nghiên cứu con người nào mở đầu mục Đạo đức nghiên cứu bằng câu giảng giải hiển nhiên này.
2. **Mật độ Cặp ghép `X and/or Y` (Binomial Stacking) ở 100% số câu**: Cả 5 câu liên tiếp đều kết thúc bằng các cặp song hành (`sexual abuse and CSAM`, `collected and labeled`, `issuing body or the reference number`, `not public and requires`, `code and configuration files`, `dataset records or sensitive material` — tổng cộng **6 cặp + 1 bộ ba** chỉ trong 84 từ!).
3. **Câu thú nhận kiểu Chatbot thiếu dữ liệu (`Cutoff Disclaimer` / `Narrated Candor`)**: `"although we do not have the details on..."` là mẫu câu đặc trưng khi AI không được cung cấp số hồ sơ IRB trong prompt.
4. **Cấu trúc Đuôi phủ định (`Tailing Negation`)**: `"is not public and requires..."`, `"provide only X, without any Y"`.
5. **Độ dài câu đồng đều phẳng lì (`Low Burstiness`, $CV = 0.26$)**: 5 câu có độ dài sàn sàn nhau (`21 - 15 - 21 - 9 - 18` từ), câu nào cũng mở đầu bằng `Chủ ngữ + Động từ` đơn điệu.

✅ **Sửa đúng Chuẩn Người viết thật 100% (Phá bỏ khung câu AI, cắt câu đạo lý, xóa các cặp `X and/or Y` thừa, tạo nhịp câu lệch `9 - 41 - 7 - 13` từ với $CV = 0.78$):**
> We did not collect new data for this study. All experiments used three existing text corpora: Roman Urdu, PAN12, and the Darkweb-CSAM dataset from our earlier work~\citep{Ngo-Elsevier:2024}, where colleagues manually labeled the text under a formal ethics exemption (the exemption reference number was not recorded in that study's documentation). Raw Darkweb-CSAM records remain restricted by permission. The public GitHub repository hosts only the source code, excluding all dataset files.

*Quy tắc rút ra:* Khi viết hoặc sửa tiếng Anh học thuật, chỉ dùng từ đơn giản là **chưa đủ**. Phải **xóa bỏ câu mở đầu giảng đạo lý**, **không xếp chồng các cặp `X and/or Y` ở cuối mỗi câu**, **không dùng câu thú nhận kiểu AI (`we do not have the details`)**, và **xen kẽ câu rất ngắn (7–9 từ) với câu dài nhiều mệnh đề (30–40 từ)**.
