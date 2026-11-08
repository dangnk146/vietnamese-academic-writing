<!-- vlc-disable: ALL -->

# Bảng Kiểm Đánh giá Chất lượng Học thuật (Academic QA Checklist)

Bảng kiểm 14 tiêu chí bắt buộc trước khi phê duyệt một đoạn văn, một bản dịch (`VI <-> EN`), một mục hoặc một chương trong Luận văn Thạc sĩ, Tiến sĩ và Paper IEEE/Q1.

---

| STT | Tiêu chí đánh giá | Câu hỏi kiểm tra | Đạt chuẩn khi |
|---|---|---|---|
| **1** | **Luận điểm đoạn văn (Topic Sentence)** | Mở đoạn hoặc kết đoạn có nêu rõ luận điểm trung tâm không? | Mỗi đoạn văn vận hành theo mô hình Diễn dịch hoặc Quy nạp; có câu chủ đề rõ ràng, không trôi nổi ý. |
| **2** | **Bộ lọc "Zero-Superlative"** | Có từ "nhất", "tốt nhất", "hoàn hảo", "số 1", "vượt trội nhất" nào không? | Tuyệt đối không xuất hiện từ so sánh nhất; mọi đánh giá hiệu năng đều kèm số liệu định lượng cụ thể. |
| **3** | **Bộ lọc "Zero-Hyperbole"** | Có từ ngữ kịch tính hóa (*vô cùng nghiêm trọng, thảm họa, bế tắc*) không? | Ngôn từ điềm đạm, khách quan; mô tả rủi ro bằng thuật ngữ dịch tễ, kỹ thuật và phương pháp luận. |
| **4** | **Tính liền mạch & Dòng chảy** | Đoạn văn có bị ngắt dòng ngẫu nhiên hoặc chia thành các câu 1 dòng không? | Toàn bộ đoạn văn là một khối thống nhất từ 3–7 câu, chuyển ý bằng các liên từ học thuật thích hợp. |
| **5** | **Ngữ pháp & Dấu câu** | Các câu có đầy đủ Chủ ngữ - Vị ngữ không? Dấu phẩy có bị đặt ngắt quãng tùy tiện không? | Câu cú mạch lạc, chuẩn ngữ pháp tiếng Việt học thuật, không có câu cụt, câu què hoặc lỗi chấm phẩy lửng lơ. |
| **6** | **Ngôi xưng khách quan (Impersonal)** | Có xuất hiện "tôi", "chúng tôi", "bạn" (`you`) không? | Toàn văn dùng ngôi thứ ba khách quan: *"luận văn", "nghiên cứu này", "đề tài", "mô hình đề xuất"*. |
| **7** | **Căn cứ & Trích dẫn khoa học** | Mọi nhận định, số liệu đối chứng có trích dẫn tài liệu tham khảo kèm theo không? | Đầy đủ trích dẫn chuẩn `~\cite{...}` / `~\citep{...}` cho các số liệu, phương pháp của tác giả tiền nhiệm. |
| **8** | **Chuẩn hóa Thuật ngữ & Từ khóa chính** | Đã lên bảng từ khóa chính và giữ thống nhất xuyên suốt từ đầu đến cuối bài chưa? | Không bị dịch lệch từ khóa chính qua các mục; thống nhất cách gọi thuật ngữ AI, Học sâu, NLP, PRISMA, MRI. |
| **9** | **Định dạng Toán học & Số liệu** | Các biến số, thông số thực nghiệm và dấu thập phân có đúng theo ngôn ngữ đích không? | Tiếng Việt dùng dấu phẩy (`98,3\%`, `$p < 0{,}05$`, `$1.225$`); Tiếng Anh dùng dấu chấm (`98.3\%`, `6,280`). |
| **10**| **Tham chiếu Bảng biểu & Hình vẽ** | Mọi bảng số liệu và hình minh họa có được giải thích và dẫn chiếu trong văn bản không? | Có đầy đủ nhãn `\label{...}` và tham chiếu bằng `hình~\ref{...}`, `Bảng~\ref{...}`, `Figure~\ref{...}`, `Table~\ref{...}`. |
| **11**| **Phát hiện và Sửa AI Writing & Loại trừ Từ ngữ Suồng sã** | Có xuất hiện từ ngữ suồng sã, sỗ sàng, khẩu ngữ bình dân (như *khử mùi*, *bóc phốt*, *chém gió*, *ngon ăn*, *ăn đứt*), hay câu bình luận cảm thán vô căn cứ cuối đoạn, bộ 3 tính từ hoa mỹ và từ tủ của AI (`rigorous`, `robust`, `granular`, `leverage`) không? | Văn phong học thuật mực thước, trang trọng, trực diện như người thật viết, giữ nguyên các câu đã chuẩn của tác giả, vượt qua kiểm tra AI của Grammarly. |
| **12**| **Tương thích Mẫu LaTeX (Preamble)** | Có tự ý chèn `\acs{}` vào bài báo không khai báo gói `acronym` không? | Kiểm tra Preamble trước khi sửa/dịch để đảm bảo mã LaTeX biên dịch không lỗi. |
| **13**| **Kiểm soát Khung câu & Cặp ghép `X and/or Y` (Binomial Stacking)** | Đoạn văn có bị lặp cấu trúc phủ định `is not X; it requires Y`, câu thú nhận kiểu chatbot (`although we do not have the details`), hay kết thúc mọi câu bằng cặp `A and/or B` không? | Đạt chuẩn khi $\le 2$ câu trong đoạn chứa cặp ghép `X and/or Y`; mở đầu trực diện vào dữ liệu thực nghiệm; không có câu thú nhận kiểu chatbot; cấu trúc phủ định đuôi được sửa thành khẳng định ngắn gọn. |
| **14**| **Độ biến thiên chiều dài câu (Sentence Burstiness $CV \ge 0.45$)** | Chiều dài các câu trong đoạn có bị đều nhau chằn chặn quanh mức 15–20 từ ($CV < 0.30$) không? | Đạt chuẩn khi đoạn văn có nhịp điệu sinh động: xen kẽ câu ngắn trực diện (7–9 từ) bên cạnh câu phức đa mệnh đề (30–42 từ) với hệ số biến thiên $CV \ge 0.45$. |
