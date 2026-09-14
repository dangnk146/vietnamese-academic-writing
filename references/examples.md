# Các Cặp Ví dụ Đối chiếu Thực tế (Bad ❌ $\rightarrow$ Good ✅)

Tài liệu này tổng hợp các cặp ví dụ đối chiếu giữa cách viết sai thường gặp của LLM và cách viết chuẩn mực theo đúng văn phong học thuật của Luận văn Thạc sĩ, Tiến sĩ và Paper IEEE / Q1.

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
