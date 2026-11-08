<!-- vlc-disable: ALL -->

# Cấu trúc Đoạn văn và Nghệ thuật Lập luận Học thuật (Academic Paragraph Engineering)

Mỗi đoạn văn trong bài báo IEEE/Q1 và Luận văn Thạc sĩ/Tiến sĩ là một **đơn vị tư duy lập luận hoàn chỉnh**. Một đoạn văn xuất sắc không bao giờ là tập hợp các câu rời rạc hay các dòng ngắt vụn vặt; nó phải vận hành như một chuỗi logic chặt chẽ, dẫn dắt độc giả từ tiền đề đến kết luận khoa học vững chắc.

---

## 1. Nguyên tắc vàng: Mở đoạn hoặc Kết đoạn LUÔN là Luận điểm

Mỗi đoạn văn phải chứa đúng một **Luận điểm trung tâm (Core Thesis / Central Claim)**:
- Nếu đoạn viết theo lối **Diễn dịch (Deductive)**: Luận điểm nằm ở **Câu mở đầu (Topic Sentence)**.
- Nếu đoạn viết theo lối **Quy nạp (Inductive)**: Luận điểm nằm ở **Câu kết thúc (Concluding Claim)**.
- Nếu đoạn viết theo lối **Tổng - Phân - Hợp (Synthesis)**: Mở đoạn nêu luận điểm khái quát $\rightarrow$ Thân đoạn phân tích đa chiều $\rightarrow$ Kết đoạn chốt hạ và chuyển tiếp logic.

Tuyệt đối không để một đoạn văn trôi nổi không có câu chủ đề, hoặc mở đầu bằng một câu phụ vô thưởng vô phạt rồi kết thúc lửng lơ, hoặc tự ý thêm một câu bình luận cảm thán sáo rỗng ở cuối đoạn.

---

## 2. Phân tích Mô hình Đoạn văn Thực tế (Chuẩn Văn phong Người viết thật)

### 2.1. Đoạn văn Diễn dịch mẫu (Mở đầu là Luận điểm — Từ `chapter1.tex`)

> **[Câu 1 - Luận điểm trung tâm]:** *Mặc dù các mô hình học sâu công bố trên \acs{ADNI} thường xuyên báo cáo độ chính xác rất cao vượt ngưỡng 95\%, thậm chí tiếp cận 99\%, song các kết quả này tiềm ẩn nguy cơ bị thổi phồng do những hạn chế trong phương pháp luận thực nghiệm.*  
> **[Câu 2 - Giải thích bản chất dữ liệu]:** *Do \acs{ADNI} là một nghiên cứu theo dõi dọc với mỗi bệnh nhân trải qua từ bốn đến sáu lượt chụp định kỳ theo thời gian, việc sử dụng nguồn dữ liệu này thường tiềm ẩn năm dạng rò rỉ dữ liệu phổ biến theo phân loại từ hai nghiên cứu của Wen và cộng sự~\cite{wen2020convolutional} cùng Young và cộng sự~\cite{young2025data}.*  
> **[Câu 3 - Liệt kê cụ thể luận cứ]:** *Các dạng rò rỉ này bao gồm việc phân chia dữ liệu ở cấp độ lát cắt, rò rỉ qua các lần chụp định kỳ của cùng một bệnh nhân, áp dụng tiền xử lý hoặc tăng cường dữ liệu trên toàn bộ tập mẫu trước khi phân chia, rò rỉ qua khâu học chuyển giao và thiếu bước kiểm chứng độc lập trên dữ liệu ngoài.*  
> **[Câu 4 - Cơ chế nhân - quả]:** *Khi các lát cắt hoặc các lần chụp của cùng một bệnh nhân cùng phân tán ở cả tập huấn luyện và kiểm thử, mức độ tương quan nội tại rất cao giữa các lát cắt của cùng một người bệnh dẫn đến việc các lát cắt chứa hàm lượng thông tin tương đồng.*  
> **[Câu 5 - Kết luận hệ quả logic]:** *Hệ quả là mô hình học sâu có xu hướng nhận diện cá thể người bệnh thay vì thực sự nắm bắt các tổn thương thoái hóa não do bệnh lý gây ra.*

*Nhận xét cấu trúc:*
- Câu 1: Xác lập ngay nhận định phản biện (độ chính xác ảo do hạn chế phương pháp luận).
- Câu 2-3: Dẫn chiếu tài liệu uy tín và liệt kê cụ thể các dạng rò rỉ.
- Câu 4: Phân tích cơ chế kỹ thuật sinh ra lỗi.
- Câu 5: Chốt hạ bằng hệ quả khoa học (mô hình nhận diện cá thể thay vì bệnh học).

---

### 2.2. Đoạn văn Quy nạp mẫu (Kết thúc là Luận điểm — Từ `chapter1.tex`)

> **[Câu 1 - Bối cảnh & Tiền đề]:** *Tổng hợp các phân tích trên cho thấy việc ứng dụng học sâu trong chẩn đoán hình ảnh bệnh Alzheimer hiện nay đang đối mặt với ba thách thức cần được giải quyết đồng thời.*  
> **[Câu 2 - Thách thức 1 (Lâm sàng)]:** *Về mặt lâm sàng, bài toán phân loại bốn giai đoạn tiến triển bệnh từ ảnh \acs{MRI} đòi hỏi mô hình phải phân biệt giai đoạn suy giảm nhận thức nhẹ sớm và muộn có độ tương đồng cao.*  
> **[Câu 3 - Thách thức 2 (Không gian & Kiến trúc)]:** *Về mặt biểu diễn không gian giải phẫu, ảnh \acs{MRI} là dữ liệu thể tích ba chiều phức tạp, việc xử lý trực tiếp toàn bộ khối ảnh ba chiều đòi hỏi chi phí tính toán lớn và dễ dẫn đến quá khớp do kích thước tập dữ liệu y tế bị giới hạn; ngược lại, các hướng tiếp cận lát cắt đơn góc nhìn truyền thống lại gặp phải điểm mù không gian, bỏ sót các thoái hóa chỉ bộc lộ ở những góc quan sát khác, do đó việc kết hợp thông tin bổ trợ từ ba mặt phẳng giải phẫu axial, coronal và sagittal là hướng đi cần thiết nhằm tái tạo ngữ cảnh không gian ba chiều mà vẫn bảo đảm tính tinh gọn của mô hình.*  
> **[Câu 4 - Thách thức 3 (Phương pháp luận thực nghiệm)]:** *Về mặt phương pháp luận, nghiên cứu cần loại bỏ kết quả sai lệch bắt nguồn từ rò rỉ dữ liệu thông qua quy trình phân chia độc lập theo từng bệnh nhân, đồng thời kiểm chứng mô hình trên tập dữ liệu độc lập \acs{AIBL}.*  
> **[Câu 5 - Luận điểm kết luận]:** *Việc giải quyết đồng bộ ba thách thức này chính là tiền đề khoa học để luận văn xác định các mục tiêu và nhiệm vụ nghiên cứu cụ thể trong phần tiếp theo.*

---

### 2.3. Đoạn văn Tổng quan & Phân loại Văn bản (Dịch chuẩn từ `paper/main.tex` — Giữ từ khóa chính xuyên suốt)

> **[Câu 1 - Luận điểm mở đoạn gắn với số liệu]:** *Hình~\ref{fig:pie-chart-tasks-addressed} trình bày phân bố các nhiệm vụ nghiên cứu về **CSAM** trong các công trình đã chọn, được chia thành năm nhóm chính: (1) phát hiện bình luận hoặc hội thoại xâm hại tình dục trực tuyến; (2) phân tích hành vi của đối tượng vi phạm; (3) nhận diện hình ảnh liên quan đến **CSA** qua phát hiện nội dung khiêu dâm, nhận diện khuôn mặt và ước lượng độ tuổi; (4) phát hiện và đối sánh sinh trắc học khuôn mặt, giọng nói trong video **CSA**; và (5) phát hiện, phân loại **CSAM** dựa trên siêu dữ liệu và **dấu vết tệp kỹ thuật số**.*  
> **[Câu 2 - So sánh tỷ lệ]:** *Phần lớn các nghiên cứu (khoảng 74,5\%, tương ứng 38 bài báo) tập trung vào phân tích **CSAM** dạng văn bản, trong khi **CSAM** dạng hình ảnh chiếm tỷ lệ thấp hơn (khoảng 13,7\%), tiếp theo là video và **dấu vết tệp kỹ thuật số** với tỷ lệ tương đương nhau (khoảng 5,9\% mỗi nhóm).*  
> **[Câu 3 - Giải thích nguyên nhân pháp lý và tâm lý]:** *Sự phân bố này xuất phát từ tính chất nhạy cảm và bất hợp pháp của các tập dữ liệu **CSAM** dạng ảnh và video, vốn đòi hỏi cơ chế kiểm soát truy cập nghiêm ngặt và giấy phép pháp lý đặc thù; đồng thời, nội dung gây sang chấn tâm lý khiến nhiều nhà nghiên cứu công nghệ e ngại tiếp cận trực tiếp.*  
> **[Câu 4 - Giải thích nguyên nhân kỹ thuật]:** *Việc ít nghiên cứu khai thác **dấu vết tệp kỹ thuật số** chủ yếu do hướng công nghệ này mới phát triển gần đây khi bắt đầu ứng dụng dữ liệu cảm biến và thông tin quyền riêng tư để phát hiện hành vi xâm hại.*

---

## 3. Quy tắc Câu cú và Tránh ngắt dòng tùy tiện

1. **Khối văn bản liền mạch (Block Integrity)**:
   - Trong LaTeX và Markdown khoa học, mỗi đoạn văn là một khối không ngắt dòng.
   - Không được bấm Enter ngắt dòng giữa chừng câu.
   - Không được viết kiểu mạng xã hội (mỗi ý xuống dòng một gạch đầu dòng ngắn ngủn 1 câu) khi viết phần thân bài (Introduction, Related Work, Method). Gạch đầu dòng chỉ dùng cho: danh sách đóng góp chính (Contributions), mục tiêu cụ thể, hoặc tóm tắt cấu trúc chương.
2. **Ngữ pháp chuẩn mực**:
   - Mỗi câu phải có đầy đủ Chủ ngữ - Vị ngữ hoàn chỉnh.
   - Tránh câu cụt bắt đầu bằng liên từ nhưng thiếu chủ ngữ (Ví dụ sai: *"Do đó, dẫn đến việc mô hình bị quá khớp."* $\rightarrow$ Sửa đúng: *"Do đó, hiện tượng này dẫn đến việc mô hình bị quá khớp."*).
3. **Dấu phẩy và dấu chấm logic**:
   - Không đặt dấu phẩy tùy tiện ngắt giữa chủ ngữ và động từ chính khi chủ ngữ dài.
   - Dùng dấu chấm phẩy (`;`) để phân tách hai mệnh đề đẳng lập có mối quan hệ nhân quả hoặc đối lập bổ trợ.

---

## 4. Bảng tra cứu Liên từ Học thuật (Academic Transition Vocabulary)

| Mục đích liên kết | Liên từ học thuật chuẩn mực | Ví dụ thực tế |
|---|---|---|
| **Chuyển tiếp nhượng bộ** | `Mặc dù vậy,`, `Tuy nhiên,`, `Song,`, `Dẫu vậy,` | *"Mặc dù các mô hình... báo cáo độ chính xác cao, song các kết quả này..."* |
| **Đối lập / Tương phản** | `Ngược lại,`, `Trái lại,`, `Trong khi đó,` | *"Ngược lại, các hướng tiếp cận lát cắt đơn lại gặp phải điểm mù không gian..."* |
| **Bổ sung / Phát triển ý** | `Bên cạnh đó,`, `Đồng thời,`, `Ngoài ra,`, `Song song với đó,` | *"Bên cạnh đó, để kiểm chứng tính khách quan... đề tài sử dụng thêm..."* |
| **Hệ quả / Kết quả** | `Hệ quả là,`, `Do đó,`, `Chính vì vậy,`, `Kéo theo,` | *"Hệ quả là mô hình có xu hướng nhận diện cá thể..."* |
| **Mục đích / Định hướng** | `Nhằm khắc phục rào cản này,`, `Để hiện thực hóa mục tiêu trên,` | *"Nhằm khắc phục rào cản này, việc ứng dụng học máy..."* |
| **Tổng hợp / Đúc kết** | `Tổng hợp các phân tích trên cho thấy,`, `Kết quả thực nghiệm chứng minh rằng,` | *"Tổng hợp các phân tích trên cho thấy việc ứng dụng học sâu..."* |

---

## 5. Mẫu Bố cục Chuẩn cho Luận văn Thạc sĩ & Bài báo Khoa học

### 5.1. Bố cục 5 Chương Luận văn Thạc sĩ Chuẩn
- **Chương 1: Tổng quan**:
  Bối cảnh $\rightarrow$ Tính cấp thiết $\rightarrow$ Khoảng trống nghiên cứu & phân tích hạn chế phương pháp luận $\rightarrow$ Mục tiêu và nhiệm vụ cụ thể $\rightarrow$ Đối tượng và phạm vi nghiên cứu $\rightarrow$ Ý nghĩa khoa học và thực tiễn $\rightarrow$ Các đóng góp chính $\rightarrow$ Bố cục luận văn.
- **Chương 2: Cơ sở lý thuyết**:
  Tổng quan bài toán/ngữ cảnh chuyên môn $\rightarrow$ Nền tảng dữ liệu và kỹ thuật $\rightarrow$ Các phương pháp tiền xử lý $\rightarrow$ Các kiến trúc học máy / học sâu nền tảng (CNN, LSTM, BERT, ViT, Mamba) $\rightarrow$ Khảo sát các công trình liên quan và phân tích hạn chế.
- **Chương 3: Phương pháp đề xuất**:
  Tổng quan kiến trúc toàn mô hình $\rightarrow$ Quy trình tiền xử lý chi tiết $\rightarrow$ Thiết kế chi tiết các khối mô-đun mới / kiến trúc lai $\rightarrow$ Định nghĩa toán học của các hàm mất mát (Loss functions).
- **Chương 4: Thực nghiệm và Đánh giá kết quả**:
  Môi trường thực nghiệm & Nguồn dữ liệu $\rightarrow$ Các chỉ số đo lường (Accuracy, Balanced Acc, Precision, Recall, F1, MCC, ROC-AUC, PR-AUC) $\rightarrow$ Kết quả phân loại & Thời gian thực thi $\rightarrow$ Thực nghiệm cô lập thành phần (Ablation Study) $\rightarrow$ So sánh đối chứng.
- **Chương 5: Kết luận và Hướng phát triển**:
  Tổng kết kết quả đạt được $\rightarrow$ Đóng góp khoa học và ứng dụng thực tiễn $\rightarrow$ Phân tích hạn chế hiện tại (cỡ mẫu, tài nguyên, kiểm định thống kê) $\rightarrow$ Định hướng nghiên cứu tiếp theo.

### 5.2. Bố cục Bài báo Tổng quan Hệ thống kết hợp Thực nghiệm (Như `paper/main.tex`)
- **Section 1 (Introduction)**: Bối cảnh bài toán $\rightarrow$ Khảo sát các bài review tiền nhiệm (Related surveys) $\rightarrow$ Đóng góp chính (Contributions) $\rightarrow$ Cấu trúc bài báo.
- **Section 2 (Systematic Survey Method)**: Khung PRISMA, thư viện số (Springer, Elsevier, IEEE, ACM, Google Scholar), câu truy vấn Boolean, tiêu chí lọc và sơ đồ PRISMA.
- **Section 3 (Classification, Analysis and Discussion)**: Bảng tổng hợp các nghiên cứu $\rightarrow$ Phân tích theo Nhiệm vụ (Tasks Addressed) $\rightarrow$ Phân tích theo Tập dữ liệu (Self-Build vs. Third-Party) $\rightarrow$ Phân tích theo Kỹ thuật mô hình hóa (Statistical, ML/DL, NLP, Hybrid).
- **Section 4 (Experimental Evaluation)**: Phương pháp & kiến trúc lai đề xuất $\rightarrow$ Các tập dữ liệu chuẩn $\rightarrow$ Độ đo và cài đặt thực nghiệm $\rightarrow$ Kết quả trên từng tập dữ liệu.
- **Section 5 & 6 (Discussion, Limitations, Ethical Considerations & Conclusion)**: Tổng kết xu hướng, giới hạn nghiên cứu, đạo đức dữ liệu và kết luận.
