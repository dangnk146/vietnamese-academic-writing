# Hướng dẫn Phong cách Viết Bài báo Y khoa vs Máy tính & Chiến lược Công bố Q1 Y tế

Tài liệu này phân tích sự khác biệt cốt lõi giữa phong cách viết bài báo của chuyên ngành Khoa học Máy tính / Trí tuệ Nhân tạo (CS/AI) và Y khoa (Medical/Clinical), đồng thời cung cấp chiến lược dịch chuyển và khung sườn bài báo chuẩn mực (IMRAD) để các kỹ sư AI có thể công bố thành công trên các tạp chí y tế ISI/Scopus Q1 danh giá.

---

## 1. Sự Khác biệt Cốt lõi giữa Dân Máy tính (CS/AI) và Dân Y khoa

| Tiêu chí | Dân Máy tính (CS/AI Style) | Dân Y khoa (Medical / Clinical Style) |
|---|---|---|
| **Trọng tâm cốt lõi** | Phát triển, cải tiến kiến trúc mô hình, tối ưu hóa hàm mất mát, tăng tốc tính toán và giảm FLOPs/tham số. | Ứng dụng lâm sàng, tính hữu dụng y tế (Clinical Utility), độ an toàn và tác động thực tế lên việc điều trị bệnh nhân. |
| **Mục tiêu bài báo** | Đạt "State-of-the-Art" (SOTA) về độ chính xác hoặc chứng minh một cơ chế học mới trên các tập benchmark mở. | Trả lời một câu hỏi y học rõ ràng: *"Mô hình AI có giúp bác sĩ phát hiện bệnh sớm hơn, giảm tỷ lệ bỏ sót ca bệnh hoặc giảm chi phí chẩn đoán không?"* |
| **Tiêu chí Đổi mới (Novelty)** | Đổi mới về kỹ thuật: khối chú ý mới, bộ mã hóa mới, hàm mất mát mới, chiến lược tối ưu phần cứng. | Đổi mới về ứng dụng lâm sàng: thiết kế nghiên cứu nghiêm ngặt, tập dữ liệu đa trung tâm chất lượng cao, quy trình chuẩn hóa gán nhãn của chuyên gia. |
| **Phương pháp Đánh giá** | So sánh với nhiều baseline AI tiền nhiệm trên các tập dữ liệu công khai (public benchmarks). | So sánh đối đầu với bác sĩ chuyên khoa (Reader Study), thử nghiệm lâm sàng, phân tích độ nhạy/đặc hiệu, AUC, giá trị tiên đoán (\acs{PPV}, \acs{NPV}) và khoảng tin cậy 95\% \acs{CI}. |
| **Văn phong Trình bày** | Nặng về toán học, sơ đồ mạng nơ-ron, cấu trúc các tầng, đồ thị hàm mất mát và thời gian suy luận. | Nặng về thiết kế nghiên cứu (Inclusion/Exclusion criteria), đặc điểm nhân khẩu học, quy chuẩn đạo đức y sinh và ý nghĩa thực hành lâm sàng. |

---

## 2. Vì sao Dùng Mô hình Có sẵn (ResNet, U-Net, Mamba) vẫn Đăng được Q1 Y khoa?

Trong giới học thuật Y khoa và Y sinh (ví dụ: *Lancet Digital Health, Nature Medicine, Radiology, Medical Image Analysis, IEEE Transactions on Medical Imaging*), ban biên tập không yêu cầu tác giả phải phát minh ra một kiến trúc mạng nơ-ron hoàn toàn mới. Một nghiên cứu sử dụng các kiến trúc nền tảng nhưng vẫn được chấp nhận xuất bản ở phân hạng Q1 đỉnh cao nhờ 4 yếu tố then chốt:

1. **Dữ liệu Độc quyền & Chuẩn vàng (Gold Standard)**:
   - Sở hữu tập dữ liệu lâm sàng chất lượng cao, kích thước lớn, thu thập từ nhiều bệnh viện/trung tâm y tế (Multi-center).
   - Có tiêu chuẩn vàng xác thực chẩn đoán: kết quả sinh thiết, giải phẫu bệnh học (histopathology), hoặc kết luận đồng thuận của hội đồng chuyên gia đầu ngành.
2. **Thiết kế Nghiên cứu Chuẩn mực Y học (Standardized Guidelines)**:
   - Tuân thủ nghiêm ngặt các hướng dẫn báo cáo quốc tế: **STARD** (cho nghiên cứu độ chính xác chẩn đoán), **TRIPOD** (cho mô hình tiên lượng/dự đoán), **CONSORT-AI** (cho thử nghiệm lâm sàng có can thiệp AI), hoặc **PRISMA** (cho tổng quan hệ thống).
   - Kèm phân tích thống kê chặt chẽ: kiểm định ý nghĩa thống kê ($p < 0{,}05$), kiểm định DeLong cho AUC, McNemar, khoảng tin cậy 95\% \acs{CI}.
3. **Chứng minh Tính hữu dụng Lâm sàng (Clinical Utility)**:
   - Nghiên cứu không dừng lại ở con số độ chính xác trên tập kiểm thử mà giải quyết bài toán: *"Khi bác sĩ sử dụng AI làm công cụ tham vấn (AI-assisted), thời gian đọc ảnh giảm bao nhiêu và độ nhạy phát hiện tổn thương tăng lên bao nhiêu?"*
4. **Hợp tác Liên ngành (Bác sĩ + Kỹ sư AI)**:
   - Có sự tham gia thực chất của các bác sĩ lâm sàng/chẩn đoán hình ảnh từ khâu thiết kế câu hỏi nghiên cứu, chuẩn hóa tiêu chuẩn chọn mẫu đến diễn giải hình thái học tổn thương trên bản đồ nhiệt Grad-CAM.

---

## 3. Chiến lược 5 Bước Chuyển dịch từ AI sang Q1 Y tế

```
  Bước 1: Giữ lõi AI mạnh, bọc vỏ lâm sàng (Clinical Framing)
     │
  Bước 2: Hợp tác thực chất với Bác sĩ chuyên khoa (Co-authorship)
     │
  Bước 3: Chuẩn hóa dữ liệu y tế & Phê duyệt Đạo đức y sinh (IRB Approval)
     │
  Bước 4: Đánh giá lâm sàng đối đầu (Reader Study: Bác sĩ vs AI vs Bác sĩ + AI)
     │
  Bước 5: Nhắm tạp chí Y khoa / Y sinh chuyên ngành (Radiology, IEEE TMI, MedIA)
```

1. **Bước 1 — Đặt Bệnh lý & Lâm sàng lên trước, AI ở sau**:
   - Tiêu đề và Tóm tắt phải làm nổi bật tên bệnh học và chuỗi xung hình ảnh, tên mô hình AI chỉ đóng vai trò bổ trợ.
   - *CS Style*: *"HTFV-Mamba2Attention: An Efficient Multi-View State Space Network for Alzheimer's Classification."*
   - *Medical Q1 Style*: *"Deep Learning–Assisted Multi-View Assessment of Alzheimer's Disease Progression in Brain MRI: Development and Multi-Cohort Validation of a Hybrid Mamba2-Attention Model."*
2. **Bước 2 — Đồng tác giả Bác sĩ (Clinical Co-authors)**:
   - Luôn có bác sĩ chuyên khoa thần kinh/chẩn đoán hình ảnh tham gia đồng tác giả, tốt nhất là đồng tác giả liên hệ (Co-corresponding author) từ các viện nghiên cứu y dược hoặc bệnh viện lớn.
3. **Bước 3 — Chuẩn hóa Tiêu chuẩn Chọn mẫu & Đạo đức Y sinh**:
   - Nêu rõ mã số chấp thuận của Hội đồng Đạo đức trong nghiên cứu Y sinh (IRB Approval Number).
   - Mô tả tiêu chí chọn vào (Inclusion criteria) và tiêu chí loại trừ (Exclusion criteria) minh bạch theo biểu đồ dòng bệnh nhân (Patient Flowchart).
4. **Bước 4 — Thiết kế Reader Study**:
   - Thiết lập thực nghiệm đối chứng:
     - Nhóm 1: Bác sĩ đọc ảnh độc lập.
     - Nhóm 2: Mô hình AI suy luận độc lập.
     - Nhóm 3: Bác sĩ đọc ảnh với sự hỗ trợ của bản đồ nhiệt Grad-CAM từ AI.
   - Đo lường mức độ cải thiện về Sensitivity, Specificity, và thời gian chẩn đoán trên mỗi ca quét.
5. **Bước 5 — Lựa chọn Tạp chí Mục tiêu**:
   - Tạp chí liên ngành AI - Y sinh: *Medical Image Analysis (MedIA), IEEE Transactions on Medical Imaging (TMI), Computerized Medical Imaging and Graphics, Computers in Biology and Medicine*.
   - Tạp chí Y học số & Lâm sàng: *Lancet Digital Health, Nature Medicine, Radiology: Artificial Intelligence, European Radiology*.

---

## 4. Khung sườn Bài báo AI $\to$ Y khoa Chuẩn IMRAD

### 4.1. Tiêu đề (Title)
- **Công thức vàng**: `[Bệnh lý / Bộ phận giải phẫu] + [Kỹ thuật hình ảnh] + [Phương pháp AI đề xuất] + [Thiết kế nghiên cứu & Kiểm chứng]`.
- Ví dụ: *"Early Detection of Mild Cognitive Impairment in Structural Brain MRI: External Multi-Cohort Validation of a Mamba-Enhanced Deep Learning Framework."*

### 4.2. Tóm tắt (Abstract)
- **Bối cảnh & Mục tiêu (Background & Objectives)**: 1–2 câu nêu gánh nặng bệnh tật và khoảng trống chẩn đoán lâm sàng hiện tại.
- **Dữ liệu & Phương pháp (Materials & Methods)**: Nêu rõ loại nghiên cứu (hồi cứu/tiến cứu, đơn trung tâm/đa trung tâm), số lượng bệnh nhân ($N$), tiêu chuẩn vàng xác nhận nhãn, tóm tắt pipeline AI, quy trình kiểm chứng ngoài (External validation cohort).
- **Kết quả (Results)**: Báo cáo các chỉ số định lượng kèm khoảng tin cậy $95\%$ \acs{CI}: Accuracy, AUC, Sensitivity, Specificity, kết quả Reader study.
- **Ý nghĩa Lâm sàng (Conclusion)**: Chốt hạ tiềm năng ứng dụng thực tế trong việc hỗ trợ bác sĩ sàng lọc sớm hoặc phân loại bệnh nhân.

### 4.3. Đặt vấn đề (Introduction)
- **Đoạn 1**: Gánh nặng dịch tễ học của bệnh, tầm quan trọng của phát hiện sớm trong giai đoạn cửa sổ vàng.
- **Đoạn 2**: Rào cản lâm sàng hiện nay: số lượng lát cắt MRI quá lớn, thời gian đọc kéo dài, sự tương đồng hình thái học giữa lão hóa tự nhiên và thoái hóa bệnh lý khiến tỷ lệ chẩn đoán sai sót còn cao.
- **Đoạn 3**: Phân tích khoảng trống của các nghiên cứu AI trước: cỡ mẫu hạn chế, rò rỉ dữ liệu (data leakage) giữa các lần quét dọc, thiếu kiểm chứng ngoài độc lập.
- **Đoạn 4 (Luận điểm nghiên cứu)**: Tuyên bố mục tiêu nghiên cứu và các đóng góp chính về mặt y sinh học lẫn kỹ thuật.

### 4.4. Đối tượng và Phương pháp nghiên cứu (Materials and Methods)
- **Thiết kế nghiên cứu & Đạo đức (Study Design & Ethical Approval)**: Mã số phê duyệt IRB, cam kết tuân thủ Tuyên ngôn Helsinki, quy trình ẩn danh hóa dữ liệu (de-identification).
- **Nhóm thuần tập dữ liệu (Patient Cohorts)**: Nguồn dữ liệu huấn luyện (ADNI) và tập kiểm chứng độc lập ngoài (AIBL). Bảng đặc điểm nhân khẩu học (Demographics: độ tuổi, giới tính, chỉ số MMSE/CDR).
- **Tiêu chuẩn chọn và loại trừ bệnh nhân (Inclusion & Exclusion Criteria)**: Minh họa bằng sơ đồ dòng bệnh nhân (Patient Flowchart).
- **Quy trình chuẩn hóa ảnh & Tiêu chuẩn vàng (Imaging Protocol & Reference Standard)**: Thông số chuỗi xung MRI, hãng máy (Siemens, GE, Philips), cường độ từ trường ($1{,}5\text{T}, 3\text{T}$), quy trình gán nhãn chẩn đoán.
- **Kiến trúc mô hình đề xuất**: Mô tả ngắn gọn, súc tích pipeline học sâu, các khối mô-đun mới, cơ chế dung hợp đa mặt phẳng giải phẫu.
- **Phân tích thống kê (Statistical Analysis)**: Trình bày chi tiết các phép kiểm định: $95\%$ \acs{CI}, kiểm định McNemar, kiểm định DeLong so sánh AUC, hệ số đồng thuận Kappa ($\kappa$), ngưỡng ý nghĩa thống kê ($\alpha = 0{,}05$).

### 4.5. Kết quả thực nghiệm (Results)
- **Đặc trưng ban đầu của mẫu (Baseline Characteristics)**: Bảng thống kê nhân khẩu học giữa các nhóm chẩn đoán (\acs{CN}, \acs{EMCI}, \acs{LMCI}, \acs{AD}).
- **Năng lực phân loại của mô hình**: Bảng số liệu chi tiết các độ đo (\acs{MCC}, Balanced Accuracy, Sensitivity, Specificity, AUC) trên kiểm chứng chéo $k$-fold.
- **Kiểm chứng độc lập ngoài (External Validation)**: Báo cáo kết quả trên tập độc lập AIBL chứng minh khả năng tổng quát hóa không bị quá khớp.
- **Reader Study (Đánh giá tương tác Lâm sàng)**: Bảng so sánh giữa bác sĩ độc lập và bác sĩ có AI hỗ trợ.
- **Giải thích mô hình (Model Explainability)**: Bản đồ kích hoạt Grad-CAM minh họa sự tập trung chú ý của mô hình vào hồi hải mã và thùy thái dương trong, đối chiếu với kiến thức giải phẫu thần kinh.

### 4.6. Bàn luận (Discussion)
- **Ý nghĩa lâm sàng**: Mô hình giải quyết bài toán lâm sàng như thế nào, khả năng tích hợp vào hệ thống lưu trữ và truyền hình ảnh y tế (\acs{PACS}).
- **Đối chiếu với các công trình tiền nhiệm**: Phân tích vì sao nghiên cứu này đạt kết quả tin cậy hơn (nhờ kiểm soát rò rỉ dữ liệu và kiểm chứng ngoài).
- **Điểm mạnh của nghiên cứu**: Cỡ mẫu lớn, kiểm chứng đa trung tâm, mô hình tinh gọn có thể chạy trên máy tính thông dụng.
- **Giới hạn nghiên cứu (Limitations)**: Thừa nhận khách quan các hạn chế (ví dụ: dữ liệu hồi cứu, chưa thử nghiệm tiến cứu đa chủng tộc).

### 4.7. Các phần bắt buộc theo Quy chuẩn Quốc tế
1. **Ethical Approval and Consent to Participate**: Tên hội đồng đạo đức, số quyết định phê duyệt.
2. **Data and Code Availability**: Đường dẫn mã nguồn công khai (GitHub), quy trình xin quyền truy cập dữ liệu (ADNI/AIBL).
3. **Funding Statement**: Cơ quan cấp kinh phí nghiên cứu.
4. **Conflicts of Interest**: Tuyên bố không có xung đột lợi ích tài chính.
5. **Authors' Contributions**: Mô tả đóng góp của từng tác giả theo chuẩn phân loại **CRediT** (Conceptualization, Methodology, Data curation, Formal analysis, Writing – review & editing).
