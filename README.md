<!-- vlc-disable: NUM001, NUM003, TONE001, DIA001, LAW001 -->

# Vietnamese & International Academic Writing Skill (`vietnamese-academic-writing` v5.0)

Bộ kỹ năng (Skill) chuẩn hóa toàn diện việc **viết mới, dịch thuật song chiều (`VI -> EN` và `EN -> VI`), hiệu đính, phát hiện và sửa AI writing ("Avoid AI Writing")** cho **Bài báo Khoa học Quốc tế (IEEE, ACM, Springer, Elsevier ISI/Scopus Q1, PRISMA Systematic Review)** và **Luận văn Thạc sĩ / Luận án Tiến sĩ**.

Tích hợp kiến trúc chế độ thực thi, quy trình 2-Pass tự động và bộ lọc cấu trúc câu từ dự án [`conorbronsdon/avoid-ai-writing`](https://github.com/conorbronsdon/avoid-ai-writing) nhằm vượt qua các công cụ quét AI (Grammarly AI Detector, Turnitin, GPTZero).

---

## 1. Điểm Nổi bật của Phiên bản 5.0

1. **5 Chế độ Thực thi Chuyên biệt (Dedicated Execution Modes)**:
   - **`vi-to-en`**: Dịch từ tiếng Việt sang tiếng Anh học thuật chuẩn IEEE/Q1 + tự động khử sạch khung câu AI.
   - **`en-to-vi`**: Dịch từ tiếng Anh sang tiếng Việt chuẩn luận văn/bài báo trong nước, neo từ khóa chính xuyên suốt, khử bị động dịch máy và từ đệm AI tiếng Việt.
   - **`rewrite`**: Viết lại và nâng cấp một đoạn văn để chuẩn hóa và loại bỏ hoàn toàn các dấu hiệu AI writing, xuất kết quả hoàn chỉnh duy nhất trong một lần (**Final rewrite**).
   - **`edit`**: Chỉnh sửa trực tiếp tại chỗ trên tệp (`paper/main.tex`, `chapter1.tex`), **bảo toàn 100% các đoạn đã chuẩn của người viết thật (Surgical Editing)**.
   - **`detect`**: Rà soát và chỉ ra các vị trí bị dính cấu trúc AI theo các mức độ `P0`, `P1`, `P2`.
2. **Quy trình Hội tụ Tự động 2 Bước (2-Pass Convergence Pipeline)**:
   - **Pass 1 (Drafting)**: Chuyển ngữ chính xác nội dung kỹ thuật, giữ nguyên công thức toán, bảng biểu và trích dẫn khoa học.
   - **Pass 2 (Avoid-AI Polishing)**: Khử toàn bộ các khung câu máy móc (cắt câu mở đầu đạo lý `Truism opener`, xóa xếp chồng cặp `X and/or Y`, bỏ câu thú nhận kiểu chatbot, cân chỉnh độ dài câu đạt $CV \ge 0.45$).
3. **Hợp đồng Biên tập & 7 Điều Cấm Tự Nhét (Never-Inject Guardrails)**:
   - Ngăn chặn AI tự ý thêm các câu cảm thán/nhận định vô căn cứ ở cuối đoạn (*"Điều này mở ra một hướng đi đầy hứa hẹn..."*), tự ý nhét dấu gạch ngang kịch tính `—`, hoặc tự ý đổi từ khóa chính sang từ đồng nghĩa lạ.
4. **Bộ Luật Linter Tự động 12 Mã (ACAD001–ACAD012)**:
   - Tích hợp công cụ dòng lệnh Python thuần quét lỗi văn bản tự động cho cả tệp `.tex` và `.md`.

---

## 2. Cấu trúc Thư mục

```text
vietnamese-academic-writing/
├── SKILL.md                                   # Chỉ dẫn cốt lõi (5 Modes, 2-Pass Pipeline, 7 Never-Inject, 9 Trụ cột)
├── README.md                                  # Tài liệu hướng dẫn sử dụng & bảng mã lỗi
├── references/
│   ├── patterns.md                            # [MỚI] Toàn bộ catalog gốc 870 dòng của avoid-ai-writing (Tier 1A/1B, Tier 2/3, thẻ biên tập)
│   ├── avoid-ai-patterns.md                   # Catalog chi tiết các mẫu cấu trúc & từ vựng AI song ngữ Anh - Việt (P0/P1/P2)
│   ├── translation-and-keyword-plan.md        # Quy trình Neo từ khóa & Kỹ thuật dịch 2-Pass (VI <-> EN)
│   ├── banned-phrases.md                      # Bảng từ cấm, so sánh nhất, giật gân & từ vựng AI 3 tầng
│   ├── academic-structure.md                  # Cấu trúc đoạn văn Diễn dịch/Quy nạp đa miền & Bố cục IMRAD
│   ├── glossary.md                            # Từ điển thuật ngữ chuẩn hóa đa miền (AI, NLP, PRISMA, Forensics, Y sinh)
│   ├── latex-guide.md                         # Quy chuẩn LaTeX thích ứng đa mẫu (EN vs. VI)
│   ├── metrics-and-statistics.md              # Công thức độ đo (F1, ROC-AUC, PR-AUC, MCC) & Kiểm định thống kê
│   ├── medical-vs-cs-style.md                 # So sánh phong cách CS/AI, PRISMA Survey & Y sinh Q1
│   ├── examples.md                            # Các cặp ví dụ đối chứng (AI từ vựng vs. AI cấu trúc ngầm vs. Người thật)
│   ├── qa-checklist.md                        # Bảng kiểm 14 tiêu chí (thêm Burstiness & Binomial density)
│   ├── locale-formatting.md                   # Quy chuẩn định dạng số, ngày tháng và Unicode NFC
│   ├── register-matrix.md                     # Ma trận ngôi xưng (thesis-vi, paper-ieee, paper-q1)
│   └── compliance.md                          # Tham chiếu quy định pháp lý chung
├── evals/
│   └── rewrite/
│       ├── output-contract-scenarios.md       # [MỚI] 10 kịch bản kiểm thử hợp đồng đầu ra (Clean no-op, bảo toàn LaTeX, chống ảo giác)
│       └── cases.json                         # [MỚI] Dữ liệu mẫu kiểm thử đối chứng định dạng JSON
└── scripts/
    ├── validate_copy.py                       # Công cụ CLI kiểm lỗi văn bản tự động (Python 3.9+, stdlib only)
    └── rules_academic.py                      # Bộ luật kiểm tra học thuật & Avoid-AI song ngữ (ACAD001–ACAD012)
```

---

## 3. Hướng dẫn Sử dụng Nhanh trong Hội thoại với AI

Bạn có thể kích hoạt skill bằng các câu lệnh tự nhiên rất ngắn gọn:

### Kịch bản 1: Viết lại từ Tiếng Việt sang Tiếng Anh (`vi-to-en`)
> *"Dùng skill `vietnamese-academic-writing`, hãy viết lại đoạn tiếng Việt này sang tiếng Anh chuẩn IEEE, đảm bảo phát hiện và sửa AI writing (Avoid AI Writing) và không bị Grammarly bắt lỗi."*

### Kịch bản 2: Dịch bài báo Tiếng Anh sang Tiếng Việt (`en-to-vi`)
> *"Dùng skill `vietnamese-academic-writing`, neo từ khóa chính và dịch mục Methodology trong bài báo này sang tiếng Việt cho luận văn Thạc sĩ."*

### Kịch bản 3: Sửa trực tiếp file LaTeX (`edit`)
> *"Dùng skill `vietnamese-academic-writing`, sửa trực tiếp file `paper/main.tex` tại mục Discussion và Ethical Considerations để loại bỏ toàn bộ các câu dính văn nói, từ ngữ suồng sã và cấu trúc AI."*

### Kịch bản 4: Kiểm tra quét lỗi AI (`detect`)
> *"Dùng skill `vietnamese-academic-writing`, audit đoạn văn này xem có dính mẫu câu nào của AI hay từ ngữ suồng sã hay không (chế độ detect, không sửa)."*

---

## 4. Bảng Tra Cứu Bộ Luật Linter Tự Động (`validate_copy.py`)

Chạy kiểm tra tự động trên dòng lệnh:
```powershell
python vietnamese-academic-writing/scripts/validate_copy.py duong_dan/file.tex --doctype en-paper
```

| Mã luật | Phân loại | Nội dung kiểm tra |
|---|---|---|
| `ACAD001` | Lỗi học thuật | Từ so sánh nhất hoặc khẳng định tuyệt đối (`nhất`, `tốt nhất`, `hoàn hảo`, `số 1`) |
| `ACAD002` | Lỗi học thuật | Từ ngữ kịch tính hóa, giật gân (`vô cùng nghiêm trọng`, `thảm họa`, `bế tắc`) |
| `ACAD003` | Lỗi học thuật | Đại từ nhân xưng không phù hợp (`tôi`, `bạn`, `you`, hoặc `chúng tôi` trong luận văn cá nhân) |
| `ACAD004` | Dấu câu | Dấu phẩy treo lửng lơ cuối dòng làm đứt đoạn văn xuôi |
| `ACAD005` | Khử AI | Câu bình luận cảm thán vô căn cứ cuối đoạn (*"mở ra kỷ nguyên mới"*, *"minh chứng hùng hồn"*) |
| `ACAD006` | LaTeX | Dùng macro `\acs{}` khi tài liệu `.tex` không khai báo gói `acronym` trong Preamble |
| `ACAD007` | Khử AI (EN) | Từ viết tắt hoặc khẩu ngữ văn nói trong bài báo tiếng Anh (`isn't`, `don't`, `by hand`, `dig into`) |
| `ACAD008` | Khử AI (EN) | Từ vựng hoa mỹ mùi AI Tier 1A/1B hoặc cụm Tier 2 (`delve`, `rigorous`, `granular`, `utilize`) |
| `ACAD009` | Khử AI (EN) | Khung cấu trúc câu AI (`is not straightforward; it requires`, `although we do not have the details`, dấu `—`) |
| `ACAD010` | Khử AI (EN) | Mật độ xếp chồng cặp ghép `X and/or Y` $\ge 75\%$ số câu trong đoạn (nguyên nhân Grammarly báo 100% AI) |
| `ACAD011` | Khử AI (Song ngữ) | Chiều dài câu phẳng lì thiếu biến thiên ($CV < 0.28$ trên đoạn $\ge 4$ câu) |
| `ACAD012` | Khử AI (VI) | Cụm từ đệm & Khung cấu trúc AI tiếng Việt (*"một cách toàn diện và sâu sắc"*, *"bức tranh toàn cảnh"*) |
| `ACAD013` | Lỗi học thuật | Từ ngữ suồng sã, sỗ sàng hoặc khẩu ngữ bình dân (“khử mùi”, “chém gió”, “bóc phốt”, “ngon ăn”, “ăn đứt”) |

---

