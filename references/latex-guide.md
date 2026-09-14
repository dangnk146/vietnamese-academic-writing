# Hướng dẫn quy chuẩn soạn thảo LaTeX (Luận văn ThS / TS & Bài báo Khoa học)

Tài liệu này chuẩn hóa toàn bộ quy cách định dạng mã nguồn LaTeX cho luận văn Thạc sĩ và các bài báo khoa học tiếng Việt, được đúc kết trực tiếp từ cấu trúc chuẩn mực của `chapters/chapter1.tex`, `chapters/chapter2.tex` và cấu hình hệ thống tại `main.tex`.

---

## 1. Quy chuẩn số liệu, phần trăm và số thập phân

### 1.1. Tỷ lệ phần trăm trong văn xuôi (Khuyên dùng Text Mode)
Trong văn bản tiếng Việt, các chỉ số tỷ lệ phần trăm thông thường nằm trong câu văn **không cần và không nên đưa vào Math Mode** (`$...$`).
- **Quy tắc chuẩn**: Viết trực tiếp ở chế độ văn bản (Text Mode), dùng dấu phẩy `,` cho phần thập phân và escape ký tự phần trăm bằng `\%`.
  - ✅ `84,2\%`, `94,18\%`, `68,2\%`, `51,13\%`, `97,19\%`
  - ❌ `$84,2\%$` *(không có ngoặc nhọn: TeX chèn khoảng trắng thừa thành `84, 2%`)*
  - ⚠️ `$84{,}2\%$` *(đúng về mặt kỹ thuật toán TeX nhưng rườm rà không cần thiết khi viết trong câu văn)*
- **Khoảng giá trị phần trăm**:
  - Dùng chữ nối trong câu: `từ 60\% đến 70\%`
  - Dùng en-dash `--` trong bảng biểu: `94,18\% -- 98,96\%`

### 1.2. Bản chất dấu ngoặc nhọn `{,}` trong Math Mode
- **Tại sao lại có `{,}`?**
  - Trong TeX Math Mode (`$...$`), dấu phẩy `,` mặc định là ký hiệu ngắt câu (`\mathpunct` - punctuation), tương tự dấu phẩy trong tọa độ $(x, y)$ hay dãy số $1, 2, 3$.
  - Theo luật typography của TeX, sau bất kỳ `\mathpunct` nào, TeX sẽ **tự động thêm một khoảng trắng nhỏ** (`\thinspace`, 3mu).
  - Vì vậy, nếu viết `$84,2\%$` mà tài liệu không load package `icomma`, TeX sẽ render thành `84` + `,` + khoảng trắng + `2` + `%` $\rightarrow$ trông như `84, 2%`.
  - Bao bọc dấu phẩy trong cặp ngoặc nhọn `{,}` biến nó thành toán hạng thường (`\mathord`), triệt tiêu khoảng trắng thừa: `$84{,}2\%$`.
- **Khi nào BẮT BUỘC dùng Math Mode & `{,}`?**
  - Khi số thập phân nằm trong biểu thức toán, công thức hoặc đi kèm ký hiệu toán học:
    - ✅ `$p < 0{,}001$`, `$p < 0{,}05$` *(nếu không bọc `{,}` sẽ thành $p < 0, 05$)*
    - ✅ Ngưỡng kiểm định: `$\chi^2 > 3{,}841$`
    - ✅ Số đo sai số: `$73,0 \pm 7,7$`, `$4,03 \pm 2,55$`
    - ✅ Kích thước & chiều không gian: `$56\times 56$`, `$112\times 112$`, `$224\times 224$`, `$H \times W$`
    - ✅ Đơn vị đo lường có số mũ: `$6.116\text{ mm}^3$`, `$\text{cm}^3$`, `$15,0\text{ GFLOPs}$`

### 1.3. Phân cách hàng nghìn
Theo quy chuẩn tiếng Việt, phân cách hàng nghìn sử dụng dấu chấm `.`:
- Trong văn bản: `$1.225$`, `$1.717$`, `$6.820$`, `$4.071$`, `$16.000$`, `$3.670$` hoặc viết trực tiếp trong bảng: `1.726`, `1.161`.

---

## 2. Dẫn chiếu chéo (Cross-Referencing) & Chống ngắt dòng

Mọi dẫn chiếu chéo đều phải có **dấu ngã `~` (non-breaking space)** đứng trước `\ref` để đảm bảo số hiệu không bị rớt xuống đầu dòng tiếp theo làm mất thẩm mỹ trang in:

| Loại đối tượng | Cách viết chuẩn | Ví dụ mẫu |
|---|---|---|
| **Hình vẽ (đầu câu)** | `Hình~\ref{fig:...}` | `Hình~\ref{fig:disease_distribution_mri} thể hiện phân bố...` |
| **Hình vẽ (giữa câu)** | `hình~\ref{fig:...}` hoặc `Hình~\ref{fig:...}` | `...được minh họa ở hình~\ref{fig:disease_distribution_mri}.` |
| **Bảng biểu** | `Bảng~\ref{tab:...}` | `...tổng hợp chi tiết trong Bảng~\ref{tab:data_leakage_inflation}.` |
| **Công thức / Phương trình** | `công thức~(\ref{eq:...})` hoặc `phương trình~(\ref{eq:...})` | `...xác định theo công thức~(\ref{eq:scaled_dot_product_attention}).` |
| **Chương** | `Chương~<N>` hoặc `Chương~\ref{chap:...}` | `...hiện thực hóa trong Chương~3.` |
| **Mục / Tiểu mục** | `Mục~\ref{sec:...}` hoặc `Mục~\ref{subsec:...}` | `...trình bày chi tiết tại Mục~\ref{sec:objectives}.` |

---

## 3. Trích dẫn tài liệu tham khảo (Citations)

- **Nguyên tắc gắn kết**: Luôn dùng `~\cite{key}` gắn liền sau tên tác giả hoặc nội dung kết luận trước dấu chấm câu, không chèn dấu cách rời trước `\cite`.
- **Mẫu câu trích dẫn tác giả**:
  - Tiếng Việt: `Tên_tác_giả và cộng sự~\cite{key}`
    - ✅ `Ali và cộng sự~\cite{ali2025deep}`
    - ✅ `Wen và cộng sự~\cite{wen2020convolutional}`
    - ✅ `Young và cộng sự~\cite{young2025data}`
  - Tiếng Anh (trong bảng biểu hoặc chú thích ngắn):
    - `Yagis et al.~\cite{yagis2021effect}`
- **Trích dẫn nhiều tài liệu**: Nhóm các khóa trong cùng một lệnh, phân cách bằng dấu phẩy:
  - ✅ `...hệ thống y tế công cộng~\cite{reitz_global_2023,m._ghazal_alzheimer_2022}.`
  - ❌ `...y tế công cộng~\cite{reitz_global_2023}~\cite{m._ghazal_alzheimer_2022}.`

---

## 4. Quản lý từ viết tắt (Acronyms)

Luận văn sử dụng gói `acronym` (khai báo tại `main.tex`).
- **Macro gọi từ viết tắt**: Dùng `\acs{KEY}` để in ra dạng viết tắt chuẩn:
  - `\acs{MRI}`, `\acs{AD}`, `\acs{CN}`, `\acs{EMCI}`, `\acs{LMCI}`, `\acs{GM}`, `\acs{WM}`, `\acs{CSF}`
  - `\acs{CNN}`, `\acs{ViT}`, `\acs{SSM}`, `\acs{Grad-CAM}`, `\acs{MCC}`, `\acs{AUC}`, `\acs{CBAM}`, `\acs{HBA}`, `\acs{SRM}`, `\acs{SSD}`
- **Quy tắc lần đầu xuất hiện**:
  - Phải ghi rõ thuật ngữ đầy đủ (tiếng Việt hoặc tiếng Anh) kèm mã viết tắt:
    - `chụp cộng hưởng từ \acs{MRI}`
    - `bệnh Alzheimer (\acs{AD})`
    - `nhận thức bình thường (\acs{CN})`
    - `suy giảm nhận thức nhẹ giai đoạn sớm (\acs{EMCI})`
    - `chất xám \acs{GM}, chất trắng \acs{WM} và dịch não tủy \acs{CSF}`

---

## 5. Môi trường hình ảnh (`figure`)

Cấu trúc chuẩn của một hình ảnh trong luận văn:

```latex
\begin{figure}[htbp]
\centering
\includegraphics[width=0.9\linewidth]{figs/ten_file_anh.png}
\caption{Tiêu đề hình ảnh súc tích, mô tả khách quan bản chất dữ liệu hoặc kiến trúc.}
\label{fig:nhan_dinh_danh}
\end{figure}
```

### Các quy tắc cốt lõi:
1. **Vị trí định vị**: Luôn ưu tiên `[htbp]` (Here, Top, Bottom, Page).
2. **Căn lề**: Luôn có `\centering`.
3. **Kích thước ảnh**: Điều chỉnh theo tỷ lệ chiều rộng trang `\linewidth`:
   - Ảnh thông thường: `[width=0.88\linewidth]` đến `[width=0.95\linewidth]`.
   - Ảnh ngang toàn trang / đồ thị phức hợp: `[width=\linewidth]` hoặc `[width=0.98\linewidth]`.
   - Ảnh khối dọc, sơ đồ nhỏ: `[width=0.52\linewidth]` đến `[width=0.65\linewidth]`.
4. **Trật tự Caption và Label**: `\caption{...}` bắt buộc phải đặt **TRƯỚC** `\label{fig:...}`. Nếu đảo ngược, `\ref` sẽ trỏ sai số thứ tự hình.

---

## 6. Môi trường bảng biểu (`table`)

Bảng biểu trong luận văn phải đáp ứng tính mực thước khoa học, có khả năng tự động co giãn theo độ rộng văn bản:

```latex
\begin{table}[htbp]
\centering
\caption{Tiêu đề bảng đặt ở TRÊN bảng, nêu rõ nội dung và phân nhóm dữ liệu.}
\label{tab:nhan_bang}
\renewcommand{\arraystretch}{1.15}
\setlength{\tabcolsep}{8pt}
\resizebox{\linewidth}{!}{
\begin{tabular}{lccccc}
\hline
\textbf{Cột 1} & \textbf{Cột 2} & \textbf{Cột 3} & \textbf{Cột 4} & \textbf{Cột 5} & \textbf{Cột 6} \\
\hline
Dữ liệu A & 100 & 50 / 50 & 75,3 $\pm$ 7,2 & 905 & 95,24\% \\
Dữ liệu B & 200 & 90 / 110 & 71,5 $\pm$ 8,1 & 862 & 96,87\% \\
\hline
\textbf{Tổng cộng} & \textbf{300} & \textbf{140 / 160} & \textbf{73,0 $\pm$ 7,7} & \textbf{1.767} & \textbf{96,00\%} \\
\hline
\end{tabular}
}
\end{table}
```

### Các quy tắc cốt lõi:
1. **Caption ở trên**: Khác với Figure, `\caption{...}` và `\label{tab:...}` của Table bắt buộc đặt ở **TRÊN** nội dung bảng.
2. **Khoảng cách dòng & cột**:
   - `\renewcommand{\arraystretch}{1.15}`: Giúp các hàng thông thoáng, chữ không bị dính vào đường kẻ ngang.
   - `\setlength{\tabcolsep}{8pt}`: Điều chỉnh khoảng cách giữa các cột.
3. **Co giãn chống tràn trang**: Bọc `\begin{tabular}` trong `\resizebox{\linewidth}{!}{ ... }` (hoặc `\resizebox{0.75\linewidth}{!}{ ... }` cho bảng ít cột) để bảng vừa khít độ rộng trang in, không bao giờ bị tràn lề phải.
4. **Căn lề cột (`tabular`)**:
   - Cột văn bản: Căn trái `l`.
   - Cột số liệu, tỷ lệ, số lượng: Căn giữa `c` hoặc căn phải `r`.
5. **Tiêu đề cột**: Luôn in đậm bằng `\textbf{...}`.
6. **Đường kẻ**: Dùng `\hline` phân cách tiêu đề, thân bảng và dòng tổng kết.

---

## 7. Môi trường công thức toán học (`equation`, `aligned`)

### 7.1. Công thức đơn dòng có đánh số
```latex
\begin{equation}
\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
\label{eq:scaled_dot_product_attention}
\end{equation}
```

### 7.2. Hệ phương trình hoặc công thức nhiều dòng
Sử dụng môi trường con `aligned` bên trong `equation` để dùng chung một số hiệu phương trình:
```latex
\begin{equation}
\begin{aligned}
x'(t) &= A x(t) + B u(t) \\
y(t) &= C x(t)
\end{aligned}
\label{eq:ssm_continuous}
\end{equation}
```

### 7.3. Quy tắc typography trong toán học
1. **Tên hàm, tên toán tử, tên lớp mạng**: Bắt buộc bọc trong `\text{...}` hoặc `\operatorname{...}`, không để LaTeX hiểu nhầm là tích của các biến rời:
   - ✅ `\text{Attention}`, `\text{softmax}`, `\text{Conv}`, `\text{Linear}`, `\text{Scan}`, `\text{Concat}`, `\text{SimAM}`, `\text{BN}`, `\text{GAP}`, `\text{ReLU}`
   - ❌ $Attention$, $softmax$, $Conv$ *(chữ sẽ bị nghiêng và khoảng cách ký tự rời rạc)*
2. **Chỉ số dưới/trên dạng chữ**: Bọc trong `\text{...}`:
   - `X_{\text{in}}`, `X_{\text{out}}`, `F^c_{\text{avg}}`, `F^c_{\text{max}}`, `z_{\text{std}}`
3. **Toán tử đại số Tensor**:
   - Tích Hadamard (nhân từng phần tử): `\odot`
   - Phép cộng từng phần tử / kết nối tắt: `\oplus`
   - Phép tích chập: `*`
   - Kích thước ma trận / tích Descartes: `\times` (ví dụ `$H \times W$`, `$56\times 56$`)
4. **Dấu ngoặc co giãn linh hoạt**:
   - Dùng `\left( ... \right)`, `\left[ ... \right]` cho các biểu thức có phân số.
   - Dùng `\Big( ... \Big)` cho các hàm bọc lồng nhau để dễ phân biệt cấp bậc.

---

## 8. Môi trường danh sách (`itemize` & `enumerate`)

- **Danh sách không thứ tự (`itemize`)**: Dùng cho mục tiêu nghiên cứu, phạm vi, ý nghĩa khoa học, cấu trúc chương.
  ```latex
  \begin{itemize}
      \item \textbf{Phạm vi dữ liệu}: Nghiên cứu sử dụng tập dữ liệu ảnh \acs{MRI}...
      \item \textbf{Phạm vi bài toán}: Luận văn giới hạn ở bài toán phân loại đa lớp...
  \end{itemize}
  ```
- **Danh sách có thứ tự (`enumerate`)**: Dùng cho các đóng góp chính, các giai đoạn/nhiệm vụ có tuần tự logic.
  ```latex
  \begin{enumerate}
      \item Phân loại các giai đoạn tiến triển bệnh: Đề xuất mô hình...
      \item Quy trình tiền xử lý ảnh y tế: Xây dựng quy trình sáu giai đoạn...
  \end{enumerate}
  ```

---

## 9. Mở đầu chương (Chapter Opener)

Theo phong cách thiết kế của luận văn, ngay sau tiêu đề `\chapter` và nhãn `\label`, luôn có biểu tượng bút `\ding{45}` (gói `pifont`) kèm câu tóm lược nội dung chương:

```latex
\chapter{TỔNG QUAN}
\label{chap:introduction}

\ding{45} \ Nội dung chương này trình bày bối cảnh nghiên cứu, tính cấp thiết, khoảng trống nghiên cứu và xác định phạm vi, mục tiêu thực hiện chính của nghiên cứu.

\section{Bối cảnh nghiên cứu}
\label{sec:background_necessity}
...
```
