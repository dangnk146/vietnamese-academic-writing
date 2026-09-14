# Chuẩn mực Trình bày Độ đo, Công thức Toán học & Kiểm định Thống kê (Metrics & Statistical Tests)

Tài liệu này cung cấp ký hiệu chuẩn LaTeX, công thức toán học và ngữ cảnh học thuật chuẩn mực cho các độ đo đánh giá mô hình học sâu y sinh và các phương pháp kiểm định thống kê trong Luận văn Thạc sĩ, Tiến sĩ và Paper IEEE/ISI/Scopus Q1.

---

## 1. Bảng Ký hiệu & Công thức các Độ đo Hiệu năng (Performance Metrics)

### 1.1. Hệ số tương quan Matthews (Matthews Correlation Coefficient — \acs{MCC})

- **Bản chất**: Độ đo đánh giá chất lượng phân loại nhị phân cân bằng, xem xét đồng thời cả 4 thành phần của ma trận nhầm lẫn ($\text{TP}, \text{TN}, \text{FP}, \text{FN}$). Đặc biệt tin cậy trong các bài toán dữ liệu y tế mất cân bằng nghiêm trọng (imbalanced datasets).
- **Công thức chuẩn LaTeX**:
  $$\text{MCC} = \frac{\text{TP} \times \text{TN} - \text{FP} \times \text{FN}}{\sqrt{(\text{TP} + \text{FP})(\text{TP} + \text{FN})(\text{TN} + \text{FP})(\text{TN} + \text{FN})}}$$
- **Miền giá trị & Diễn giải**:
  - $\text{MCC} \in [-1, 1]$.
  - $\text{MCC} = +1$: Phân loại hoàn hảo.
  - $\text{MCC} = 0$: Dự đoán tương đương ngẫu nhiên (random guess).
  - $\text{MCC} = -1$: Dự đoán hoàn toàn nghịch đảo với nhãn thực tế.
- **Quy tắc viết văn**: Nêu rõ MCC bên cạnh Accuracy và Macro-F1 khi báo cáo kết quả trên các tập dữ liệu có tỷ lệ mẫu chênh lệch giữa các giai đoạn bệnh (ví dụ: \acs{CN} vs \acs{EMCI} vs \acs{AD}).

---

### 1.2. Độ nhạy (Sensitivity / Recall / True Positive Rate — \acs{TPR})

- **Bản chất**: Đo lường tỷ lệ các ca thực sự mắc bệnh được mô hình nhận diện chính xác; tránh bỏ sót ca bệnh trong lâm sàng (giảm tối đa sai số âm tính giả $\text{FN}$).
- **Công thức chuẩn LaTeX**:
  $$\text{Sensitivity} = \text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}$$
- **Ngữ cảnh y khoa**: Độ nhạy cao là ưu tiên hàng đầu trong các bài toán sàng lọc sớm (screening), bảo đảm không bỏ sót bệnh nhân ở giai đoạn cửa sổ vàng can thiệp (\acs{EMCI}).

---

### 1.3. Độ đặc hiệu (Specificity / True Negative Rate — \acs{TNR})

- **Bản chất**: Đo lường tỷ lệ các ca thực sự bình thường (không mắc bệnh) được mô hình chẩn đoán đúng là âm tính; tránh kết luận sai gây hoang mang hoặc can thiệp y tế không cần thiết (giảm tối đa sai số dương tính giả $\text{FP}$).
- **Công thức chuẩn LaTeX**:
  $$\text{Specificity} = \frac{\text{TN}}{\text{TN} + \text{FP}}$$
- **Ngữ cảnh y khoa**: Độ đặc hiệu cao là bắt buộc trong chẩn đoán xác định (confirmatory diagnosis) trước khi ra quyết định điều trị chuyên sâu.

---

### 1.4. Điểm F1 (F1-Score) & Điểm trung bình điều hòa

- **Độ chuẩn xác (Precision)**:
  $$\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}$$
- **Công thức chuẩn F1-Score**:
  $$F_1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} = \frac{2\text{TP}}{2\text{TP} + \text{FP} + \text{FN}}$$
- **Mở rộng đa lớp**:
  - **Macro-F1**: Trung bình cộng không trọng số của điểm $F_1$ từng lớp; đánh giá công bằng năng lực nhận diện trên cả các lớp thiểu số.
  - **Weighted-F1**: Trung bình có trọng số theo kích thước từng lớp.

---

### 1.5. Hệ số đồng thuận Cohen's Kappa ($\kappa$)

- **Bản chất**: Đo lường mức độ đồng thuận giữa hai người đánh giá (hoặc giữa dự đoán mô hình và chẩn đoán của chuyên gia), loại trừ hoàn toàn yếu tố đồng thuận ngẫu nhiên.
- **Bảng chéo (Confusion Matrix) $2 \times 2$**:
  | Thực tế \ Dự đoán | Dương tính | Âm tính |
  |---|---|---|
  | **Dương tính** | $a$ ($\text{TP}$) | $b$ ($\text{FN}$) |
  | **Âm tính** | $c$ ($\text{FP}$) | $d$ ($\text{TN}$) |
- **Công thức chuẩn LaTeX**:
  $$\kappa = \frac{p_o - p_e}{1 - p_e}$$
  Trong đó:
  - $N = a + b + c + d$
  - Tỷ lệ đồng thuận quan sát: $p_o = \frac{a + d}{N}$
  - Tỷ lệ đồng thuận ngẫu nhiên kỳ vọng: $p_e = \frac{(a + b)(a + c) + (c + d)(b + d)}{N^2}$
- **Thang đo mức độ đồng thuận (Landis & Koch)**:
  - $\kappa < 0{,}00$: Không đồng thuận (Poor).
  - $0{,}01 - 0{,}20$: Đồng thuận rất nhẹ (Slight).
  - $0{,}21 - 0{,}40$: Đồng thuận trung bình yếu (Fair).
  - $0{,}41 - 0{,}60$: Đồng thuận mức độ vừa phải (Moderate).
  - $0{,}61 - 0{,}80$: Đồng thuận đáng kể / tốt (Substantial).
  - $0{,}81 - 1{,}00$: Đồng thuận gần như hoàn hảo (Almost perfect).

---

### 1.6. Khoảng tin cậy (Confidence Interval — \acs{CI})

- **Bản chất**: Xác định khoảng dao động ước tính của chỉ số thống kê (Accuracy, AUC, Sensitivity) ở một mức độ tin cậy định trước (thường là $95\%$).
- **Trường hợp 1 (Biết độ lệch chuẩn quần thể $\sigma$ hoặc mẫu lớn, phân phối chuẩn $Z$)**:
  $$\text{CI}_{1-\alpha} = \bar{x} \pm Z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$$
  *(Với mức tin cậy $95\%$, $Z_{0{,}025} \approx 1{,}96$)*.
- **Trường hợp 2 (Không biết $\sigma$, cỡ mẫu nhỏ, phân phối Student's $t$ với $n - 1$ bậc tự do)**:
  $$\text{CI}_{1-\alpha} = \bar{x} \pm t_{\alpha/2, n-1} \frac{s}{\sqrt{n}}$$
- **Cách trình bày chuẩn trong y khoa**:
  - Viết liền sau chỉ số: *$\text{Accuracy} = 94{,}18\% \ [95\%\ \text{CI}: 92{,}45\% - 95{,}80\%]$*.
  - Đối với diện tích dưới đường cong ROC: *$\text{AUC} = 0{,}962 \ (95\%\ \text{CI}: 0{,}945 - 0{,}978)$*.

---

## 2. Các Kiểm định Thống kê Chuyên sâu (Statistical Significance Tests)

Trong nghiên cứu khoa học, để khẳng định thuật toán đề xuất vượt trội hơn các mô hình tiền nhiệm, tác giả bắt buộc phải chứng minh sự khác biệt có ý nghĩa thống kê ($p < 0{,}05$), tránh ngộ nhận do phương sai ngẫu nhiên.

```
                                  KIỂM ĐỊNH SO SÁNH THUẬT TOÁN
                                               │
             ┌─────────────────────────────────┴─────────────────────────────────┐
             ▼                                                                   ▼
       So sánh 2 thuật toán                                            So sánh ≥ 3 thuật toán
             │                                                                   │
    ┌────────┴────────┐                                                 ┌────────┴────────┐
    ▼                 ▼                                                 ▼                 ▼
Tham số (Parametric)  Phi tham số (Non-parametric)              Tham số (Parametric)  Phi tham số (Non-parametric)
- Paired t-test       - McNemar's Test (1 dataset, nhị phân)    - One-way ANOVA       - Friedman Test (nhiều datasets)
                      - Wilcoxon Signed-Rank (nhiều datasets)                         - Nemenyi Post-hoc Test
```

---

### 2.1. Kiểm định McNemar (McNemar’s Test)

- **Mục đích**: So sánh hiệu năng của hai mô hình phân loại $A$ và $B$ trên cùng một tập dữ liệu kiểm thử (dữ liệu cặp đôi nhị phân).
- **Bảng liên hệ chéo $2 \times 2$**:
  | Mô hình A \ Mô hình B | Dự đoán Đúng | Dự đoán Sai |
  |---|---|---|
  | **Dự đoán Đúng** | $a$ (Cả hai đều đúng) | $b$ (A đúng, B sai) |
  | **Dự đoán Sai** | $c$ (A sai, B đúng) | $d$ (Cả hai đều sai) |
- **Công thức chuẩn (có hiệu chỉnh tính liên tục Edwards)**:
  $$\chi^2 = \frac{(|b - c| - 1)^2}{b + c}, \quad df = 1$$
- **Diễn giải**:
  - So sánh $\chi^2$ với ngưỡng phân phối Chi-bình phương bậc tự do $df = 1$. Với $\alpha = 0{,}05$, giá trị tới hạn là $3{,}841$.
  - Nếu $\chi^2 > 3{,}841 \iff p < 0{,}05$: Bác bỏ giả thuyết vô hiệu $H_0$, kết luận hai mô hình có sự khác biệt đáng kể về mặt thống kê.

---

### 2.2. Kiểm định Student's t-test (Paired / Two-sample)

- **Mục đích**: So sánh giá trị trung bình giữa hai nhóm kết quả.
- **Điều kiện áp dụng**: Dữ liệu phải tuân theo phân phối xấp xỉ chuẩn và độc lập.
- **Ứng dụng & Giới hạn**: Phù hợp khi so sánh hai thuật toán trên các lần chạy $k$-fold cross-validation của cùng một tập dữ liệu. **Không dùng khi so sánh $\ge 3$ thuật toán** vì sẽ làm bùng nổ sai số loại I (Family-wise Error Rate inflation).

---

### 2.3. Phân tích phương sai ANOVA (Analysis of Variance)

- **Mục đích**: Kiểm định sự khác biệt có ý nghĩa thống kê giữa trung bình của $\ge 3$ thuật toán/nhóm can thiệp trên một tập thử nghiệm.
- **Điều kiện bắt buộc**: Phân phối chuẩn, phương sai các nhóm đồng nhất (Homoscedasticity).
- **Lưu ý học thuật**: Trong học máy, kết quả của các thuật toán trên nhiều bộ dữ liệu benchmark hiếm khi thỏa mãn phân phối chuẩn; do đó ANOVA ít được khuyến nghị bằng các kiểm định phi tham số (Friedman Test).

---

### 2.4. Kiểm định Wilcoxon Signed-Rank Test (Phi tham số cho 2 thuật toán)

- **Mục đích**: So sánh hai thuật toán ghép cặp trên cùng một tập dữ liệu hoặc trên nhiều tập dữ liệu độc lập khi **không đảm bảo giả định phân phối chuẩn**.
- **Nguyên lý**: Tính hiệu số chênh lệch $d_i = x_{1,i} - x_{2,i}$, loại bỏ các cặp có $d_i = 0$, xếp hạng giá trị tuyệt đối $|d_i|$ và tính tổng hạng theo dấu ($W^+, W^-$).
- **Ứng dụng**: Kiểm tra sự vượt trội của mô hình đề xuất so với Baseline trên $10-20$ tập benchmark hoặc các fold kiểm chứng.

---

### 2.5. Kiểm định Friedman Test & Hậu kiểm Nemenyi (So sánh $\ge 3$ thuật toán)

- **Mục đích**: Tiêu chuẩn vàng quốc tế (theo khuyến nghị của Demšar, JMLR 2006) để so sánh đồng thời nhiều thuật toán ($\ge 3$) trên nhiều bộ dữ liệu độc lập.
- **Nguyên lý**:
  1. Với mỗi bộ dữ liệu, xếp hạng các thuật toán từ $1$ (tốt nhất) đến $k$ (kém nhất).
  2. Tính hạng trung bình $R_j$ của từng thuật toán $j$.
  3. Tính thống kê Friedman $\chi_F^2$ hoặc thống kê hiệu chỉnh Iman-Davenport $F_F$.
- **Hậu kiểm Nemenyi (Post-hoc Nemenyi Test)**:
  - Nếu kiểm định Friedman chỉ ra sự khác biệt tổng thể ($p < 0{,}05$), tiến hành kiểm định Nemenyi để tìm cặp thuật toán cụ thể có sự khác biệt vượt ngưỡng khoảng cách tới hạn (Critical Difference — \acs{CD}):
    $$\text{CD} = q_\alpha \sqrt{\frac{k(k + 1)}{6N}}$$
  - Trực quan hóa bằng biểu đồ khoảng cách tới hạn (CD Diagram).
