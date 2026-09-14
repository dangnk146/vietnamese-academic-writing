---
name: vietnamese-academic-writing
description: Writes, refines, and reviews native-standard Vietnamese academic research papers (IEEE Conferences/Transactions, ISI/Scopus Q1 journals) and graduate theses/dissertations (Luận văn Thạc sĩ, Tiến sĩ CNTT & Y sinh). Enforces rigorous academic tone modeled after standard Vietnamese theses — strictly bans superlatives ("nhất", "tốt nhất", "hoàn hảo"), eliminates emotional sensationalism ("vô cùng nghiêm trọng", "thảm họa"), structures paragraphs with thesis-driven topic or concluding sentences backed by empirical citations (~cite{...}), ensures seamless grammatical flow with zero arbitrary line breaks or misplaced punctuation, and standardizes AI/MRI terminology. Trigger on any academic thesis, luận văn, paper IEEE, paper Q1, nghiên cứu khoa học, hoặc biên tập học thuật.
license: MIT
metadata:
  version: "3.0.0"
  repository: "https://github.com/trussary/vietnamese-language-skill"
---

# Academic Research and Graduate Thesis Writing (IEEE, Q1, Luận văn Thạc sĩ/Tiến sĩ)

Viết luận văn Thạc sĩ, Tiến sĩ và bài báo khoa học chuẩn quốc tế (IEEE, ISI/Scopus Q1) bằng tiếng Việt đòi hỏi tính khách quan tuyệt đối, sự khiêm tốn khoa học, cấu trúc lập luận đa tầng và độ chính xác ngữ pháp cao. Phong cách chuẩn mực được định hình trực tiếp từ văn phong của các công trình xuất sắc (điển hình như chương mở đầu của luận văn Thạc sĩ xử lý ảnh y tế).

Skill này chuẩn hóa văn phong học thuật, loại bỏ hoàn toàn các lỗi thường gặp của mô hình ngôn ngữ lớn (LLM): lạm dụng từ so sánh nhất, kịch tính hóa vấn đề, ngắt dòng vụn vặt và thiếu câu luận điểm.

---

## 5 Trụ cột học thuật cốt lõi

### 1. Nguyên tắc "Zero-Superlative" (Tuyệt đối không dùng từ "nhất")
Trong nghiên cứu khoa học, không có thuật toán hay giải pháp nào là "hoàn hảo" hoặc "tốt nhất" trong mọi điều kiện (Định lý No Free Lunch). Mọi kết luận đều phải dựa trên quan sát thực nghiệm có điều kiện biên rõ ràng.
- **CẤM TUYỆT ĐỐI**: `nhất`, `tốt nhất`, `hoàn hảo`, `tuyệt đối`, `số 1`, `hàng đầu`, `đột phá nhất`, `vượt trội nhất`, `tối ưu nhất`, `triệt để`.
- **Thay thế bằng**: Số liệu định lượng cụ thể hoặc nhận định so sánh tương đối có căn cứ:
  - ❌ *"Mô hình đạt độ chính xác cao nhất hiện nay."*
  - ✅ *"Mô hình đạt độ chính xác 94,18\%, cao hơn so với các phương pháp đối chứng trên cùng tập kiểm thử."* *(ưu tiên Text Mode `94,18\%` tự nhiên trong câu văn; nếu trong Math Mode mới cần `{,}`)*
  - ❌ *"Đây là hướng tiếp cận hoàn hảo nhất."*
  - ✅ *"Đây là phương pháp tiêu chuẩn mang lại hiệu quả ổn định."*
- Danh mục chi tiết: **[references/banned-phrases.md](references/banned-phrases.md)**.

### 2. Nguyên tắc "Khách quan hóa & Mực thước" (Không nghiêm trọng hóa)
Không sử dụng ngôn từ giật gân, hoang mang, phóng đại hoặc mang tính cảm xúc cá nhân. Mức độ nguy hại của bệnh lý hoặc sai lệch kỹ thuật phải được diễn đạt bằng thuật ngữ dịch tễ và thống kê.
- **CẤM TUYỆT ĐỐI**: `vô cùng nghiêm trọng`, `cực kỳ nguy hiểm`, `thảm họa`, `đe dọa nghiêm trọng tới sự sống còn`, `hoàn toàn bế tắc`, `vấn nạn nhức nhối`.
- **Thay thế bằng**: Văn phong học thuật điềm đạm, định lượng:
  - ❌ *"Bệnh Alzheimer là thảm họa vô cùng nghiêm trọng với loài người."*
  - ✅ *"Các bệnh lý thoái hóa thần kinh mạn tính đã và đang trở thành thách thức to lớn đối với hệ thống y tế công cộng~\cite{reitz_global_2023}."*
  - ❌ *"Rò rỉ dữ liệu là sai lầm chết người phá hủy toàn bộ kết quả."*
  - ✅ *"Song các kết quả này tiềm ẩn nguy cơ bị thổi phồng do những hạn chế trong phương pháp luận thực nghiệm."*

### 3. Cấu trúc đoạn văn chuẩn học thuật (Mở hoặc kết đoạn luôn là Luận điểm)
Mỗi đoạn văn là một khối lập luận trọn vẹn (gồm 3–7 câu). Không ngắt đoạn cụt lủn kiểu bài viết mạng xã hội.
- **Mô hình Diễn dịch (Deductive)**: Mở đoạn là **Luận điểm trung tâm (Topic Sentence)** $\rightarrow$ Các câu thân đoạn triển khai luận cứ, dẫn chứng thực nghiệm, cơ chế nhân-quả, trích dẫn tác giả tiền nhiệm (`~\cite{...}`).
- **Mô hình Quy nạp (Inductive)**: Các câu thân đoạn phân tích bối cảnh, số liệu, đối chiếu $\rightarrow$ Câu kết đoạn đúc kết thành **Luận điểm kết luận (Concluding Claim)**.
- **Mô hình Tổng - Phân - Hợp**: Mở đoạn khái quát $\rightarrow$ Thân đoạn phân tích đa diện $\rightarrow$ Kết đoạn chốt ý và chuyển tiếp sang phần tiếp theo.
- Hướng dẫn cấu trúc & mẫu câu: **[references/academic-structure.md](references/academic-structure.md)**.

### 4. Dòng chảy câu cú chuẩn mực, không ngắt dòng ngẫu nhiên
- **Tuyệt đối không ngắt dòng ngẫu nhiên**: Một đoạn văn phải là một khối văn bản liền mạch. Không ngắt dòng giữa chừng câu hoặc chia nhỏ mỗi câu thành một đoạn riêng biệt.
- **Cấu trúc ngữ pháp hoàn chỉnh**: Đầy đủ cụm Chủ ngữ – Vị ngữ – Bổ ngữ. Tránh câu què, câu cụt, hoặc đặt dấu phẩy tùy tiện ngắt giữa chủ ngữ dài và vị ngữ.
- **Hệ thống liên từ học thuật kết nối ý**:
  - *Chuyển tiếp/Nhượng bộ*: `Mặc dù vậy,`, `Tuy nhiên,`, `Ngược lại,`, `Song,`.
  - *Bổ sung luận cứ*: `Bên cạnh đó,`, `Đồng thời,`, `Ngoài ra,`, `Song song với đó,`.
  - *Hệ quả/Nguyên nhân*: `Nhằm khắc phục rào cản này,`, `Hệ quả là,`, `Do đó,`, `Chính vì vậy,`.
  - *Tổng kết/Đánh giá*: `Tổng hợp các phân tích trên cho thấy,`, `Kết quả thực nghiệm chứng minh rằng,`.

### 5. Ngôi xưng khách quan (Impersonal Register) & Chuẩn hóa thuật ngữ
- **Ngôi xưng**: Tuyệt đối không xưng `tôi`; không xưng `chúng tôi` trong luận văn tiếng Việt. Sử dụng các thực thể khách quan: `luận văn`, `đề tài này`, `nghiên cứu này`, `mô hình đề xuất`, `các tác giả tiền nhiệm`.
- **Thuật ngữ chuyên ngành**: Sử dụng chuẩn xác thuật ngữ AI, Machine Learning và Xử lý ảnh MRI y sinh. Giữ nguyên thuật ngữ tiếng Anh gốc phổ quát khi dịch sang tiếng Việt làm tối nghĩa (`backbone, attention, latent space, epoch, batch size`).
- Từ điển thuật ngữ chuẩn: **[references/glossary.md](references/glossary.md)**.

---

## Quy trình 4 bước khi soạn thảo hoặc hiệu đính

1. **Bước 1 — Xác định thể loại và cấu trúc đoạn văn**:
   Chọn mô hình Diễn dịch hoặc Quy nạp. Đảm bảo câu đầu hoặc câu cuối là luận điểm rõ ràng.
2. **Bước 2 — Rà soát bộ lọc từ cấm ("Zero-Superlative" & "Zero-Hyperbole")**:
   Quét và loại bỏ tất cả các từ so sánh nhất (*nhất, tốt nhất, hoàn hảo*) và từ ngữ kịch tính hóa (*vô cùng nghiêm trọng, thảm họa*).
3. **Bước 3 — Chuẩn hóa câu cú, dấu câu và liên từ**:
   Hợp nhất các câu rời rạc thành đoạn văn liền mạch; bổ sung các liên từ học thuật; kiểm tra tính đầy đủ của Chủ ngữ - Vị ngữ.
4. **Bước 4 — Kiểm định bảng biểu, ký hiệu toán, số liệu và trích dẫn LaTeX**:
   - Viết tỷ lệ phần trăm văn xuôi ở Text Mode (`84,2\%`), chỉ dùng Math Mode khi đi kèm biến/công thức (`$p < 0{,}05$`, `$73,0 \pm 7,7$`, `$56\times 56$`).
   - Dùng macro `\acs{KEY}` cho từ viết tắt, `~\cite{key}` cho tài liệu tham khảo và `Hình~\ref{fig:...}`, `Bảng~\ref{tab:...}` có dấu ngã chống ngắt dòng.
   - Chi tiết: **[references/latex-guide.md](references/latex-guide.md)**.

---

## Tài liệu tham khảo chi tiết

- **[references/latex-guide.md](references/latex-guide.md)** — Quy chuẩn soạn thảo LaTeX chuẩn mực cho luận văn và bài báo (số liệu text vs math mode, trích dẫn, từ viết tắt \acs, figure, table, equation).
- **[references/academic-structure.md](references/academic-structure.md)** — Cấu trúc đoạn văn, kỹ thuật lập luận và bố cục 5 chương luận văn.
- **[references/banned-phrases.md](references/banned-phrases.md)** — Bảng tra cứu từ cấm (so sánh nhất, kịch tính hóa, ngôi xưng sai).
- **[references/glossary.md](references/glossary.md)** — Thuật ngữ song ngữ AI, Học sâu, Chẩn đoán hình ảnh y tế và MRI.
- **[references/metrics-and-statistics.md](references/metrics-and-statistics.md)** — Ký hiệu chuẩn LaTeX, công thức độ đo (MCC, Sensitivity, Specificity, F1, Kappa, 95% CI) và kiểm định thống kê (McNemar, t-test, ANOVA, Wilcoxon, Friedman/Nemenyi).
- **[references/medical-vs-cs-style.md](references/medical-vs-cs-style.md)** — Sự khác biệt phong cách viết CS vs Y khoa, khung sườn IMRAD lâm sàng và chiến lược công bố Q1 Y tế.
- **[references/examples.md](references/examples.md)** — Các cặp ví dụ đối chứng ❌ Sai $\rightarrow$ ✅ Chuẩn học thuật.
- **[references/qa-checklist.md](references/qa-checklist.md)** — Bảng kiểm 10 tiêu chí trước khi hoàn thiện nội dung.
- **[references/locale-formatting.md](references/locale-formatting.md)** — Quy chuẩn trình bày công thức toán, bảng biểu và số liệu khoa học.
