# -*- coding: utf-8 -*-
"""Rules for Vietnamese academic research papers (IEEE, Q1) and theses (Luận văn ThS/TS).

Loaded automatically by validate_copy.py because the filename starts with `rules_`.
Standard library only, no imports from the engine — the contract is plain tuples.
"""
from __future__ import annotations

import re

ERROR = "error"
WARN = "warning"

RULE_DOCS = {
    "ACAD001": "superlative or absolute claim in academic writing (“nhất”, “hoàn hảo”, “tốt nhất”)",
    "ACAD002": "sensationalism or hyperbole in scientific context (“vô cùng nghiêm trọng”, “thảm họa”)",
    "ACAD003": "informal or personal pronouns (“tôi”, “bạn”) in academic thesis / paper",
    "ACAD004": "dangling punctuation or broken sentence flow in academic prose",
    "EDU001": "abolished secondary (THCS/THPT) overall grading term (Thông tư 22/2021)",
    "EDU002": "“bạn” addressing a student in a teacher's voice",
    "EDU003": "“cần cải thiện” on a primary report card instead of “cần cố gắng” (Thông tư 27/2020)",
    "EDU005": "“tín dụng” for academic credit instead of “tín chỉ” (Thông tư 08/2021)",
    "EDU006": "GPA written with a dot decimal instead of the Vietnamese comma",
    "EDU007": "literal empty-state phrase on EdTech UI without an actionable CTA",
    "EDU009": "unpedagogical or harsh pronunciation feedback violating the Sandwich model",
}

DOCTYPES = {
    "thesis": "a Master's or Ph.D. thesis chapter / proposal (Luận văn Thạc sĩ, Tiến sĩ)",
    "paper": "an IEEE conference/transactions or ISI/Scopus Q1 scientific paper",
    "academic-prose": "general academic research, methodology, or survey prose",
    "primary-report-card": "a primary-school (tiểu học) report card or sổ liên lạc entry",
    "secondary-report-card": "a secondary/high-school (THCS/THPT) report card or học bạ entry",
    "teacher-to-student": "a teacher addressing a student directly",
    "transcript": "a university transcript or GPA statement",
    "higher-ed": "university administrative prose — syllabi, course descriptions, registration",
    "edtech-microcopy": "EdTech UI and microcopy strings",
    "pronunciation-feedback": "pronunciation feedback strings",
}

# Superlative and absolute patterns
SUPERLATIVE_RE = re.compile(
    r"(?<!\w)(?:(?:tốt|cao|giỏi|nhanh|chính\s+xác|tối\s+ưu|hiệu\s+quả|đột\s+phá|vượt\s+trội|mới|hiện\s+đại|toàn\s+diện)\s+nhất"
    r"|duy\s+nhất|hoàn\s+hảo|tuyệt\s+đối|triệt\s+để|số\s*(?:một|1)\b)(?!\w)",
    re.IGNORECASE,
)

# Sensationalism & hyperbole patterns
HYPERBOLE_RE = re.compile(
    r"(?<!\w)(?:vô\s+cùng\s+nghiêm\s+trọng|cực\s+kỳ\s+nguy\s+hiểm|thảm\s+họa"
    r"|đe\s+dọa\s+nghiêm\s+trọng\s+tới\s+sự\s+sống\s+còn|hoàn\s+toàn\s+bế\s+tắc"
    r"|vấn\s+nạn\s+nhức\s+nhối|sai\s+lầm\s+chết\s+người)(?!\w)",
    re.IGNORECASE,
)

# Personal pronouns in academic writing
ACADEMIC_PRONOUNS_RE = re.compile(r"(?<!\w)(?:tôi|bạn|quý\s+vị|anh/chị)(?!\w)", re.IGNORECASE)
THESIS_WE_RE = re.compile(r"(?<!\w)chúng\s+tôi(?!\w)", re.IGNORECASE)

# Dangling comma at end of line (incomplete sentence structure)
DANGLING_COMMA_RE = re.compile(r",\s*$")

# Legacy education patterns
LEGACY_OVERALL_RE = re.compile(
    r"(?:xếp loại|đạt loại)\s+(giỏi|trung bình|yếu|kém)(?!\w)", re.IGNORECASE)
LEGACY_TITLE_RE = re.compile(r"(?<!\w)học sinh\s+tiên tiến(?!\w)", re.IGNORECASE)
ADDRESS_BAN_RE = re.compile(r"(?<!\w)bạn(?!\w)", re.IGNORECASE)
NEEDS_IMPROVEMENT_CALQUE_RE = re.compile(r"(?<!\w)cần\s+cải\s+thiện(?!\w)", re.IGNORECASE)
CREDIT_CALQUE_RE = re.compile(r"(?<!\w)tín\s+dụng(?!\w)", re.IGNORECASE)
GPA_DOT_RE = re.compile(r"(?<!\d)\d\.\d{1,2}\s*/\s*\d(?:\.\d{1,2})?(?!\d)")
EMPTY_STATE_CALQUE_RE = re.compile(r"(?<!\w)(?:trạng\s+thái\s+trống|không\s+có\s+dữ\s+liệu)(?!\w)", re.IGNORECASE)
HARSH_FEEDBACK_RE = re.compile(
    r"(?<!\w)(?:sai\s+rồi|bạn\s+(?:đã\s+)?phát\s+âm\s+sai|điểm\s+(?:phát\s+âm\s+)?của\s+bạn\s+là)(?!\w)",
    re.IGNORECASE,
)


def check_line(ctx, lineno, raw, masked):
    doctype = ctx.doctype
    if not doctype:
        return

    # Academic doctypes: thesis, paper, academic-prose
    if doctype in ("thesis", "paper", "academic-prose"):
        for match in SUPERLATIVE_RE.finditer(masked):
            yield ("ACAD001", ERROR, match.start() + 1, match.group(0),
                   f"superlative or absolute claim “{match.group(0)}”",
                   "scientific writing avoids superlatives and unproven absolute claims — "
                   "state quantitative empirical results or objective comparative evidence")

        for match in HYPERBOLE_RE.finditer(masked):
            yield ("ACAD002", ERROR, match.start() + 1, match.group(0),
                   f"sensationalism or hyperbole “{match.group(0)}”",
                   "academic prose maintains an objective, measured tone — replace dramatic language "
                   "with epidemiological, clinical, or technical terminology")

        for match in ACADEMIC_PRONOUNS_RE.finditer(masked):
            yield ("ACAD003", ERROR, match.start() + 1, match.group(0),
                   f"informal or personal pronoun “{match.group(0)}”",
                   "use third-person impersonal register: “luận văn”, “nghiên cứu này”, “mô hình đề xuất”")

        if doctype == "thesis":
            for match in THESIS_WE_RE.finditer(masked):
                yield ("ACAD003", WARN, match.start() + 1, match.group(0),
                       f"“{match.group(0)}” in individual graduate thesis",
                       "a Master's thesis is an individual work — replace “chúng tôi” with “luận văn” or “tác giả”")

        if DANGLING_COMMA_RE.search(raw.rstrip()):
            yield ("ACAD004", WARN, len(raw.rstrip()), ",",
                   "dangling comma at end of line",
                   "avoid arbitrary line breaks mid-sentence; keep academic paragraphs as continuous blocks")

    # Education administrative doctypes
    if doctype == "secondary-report-card":
        for match in LEGACY_TITLE_RE.finditer(masked):
            yield ("EDU001", ERROR, match.start() + 1, match.group(0),
                   f"abolished title “{match.group(0)}”",
                   "Thông tư 22/2021/TT-BGDĐT abolished “Học sinh Tiên tiến” as an "
                   "overall classification — use Tốt / Khá / Đạt / Chưa đạt")
        for match in LEGACY_OVERALL_RE.finditer(masked):
            yield ("EDU001", ERROR, match.start() + 1, match.group(0),
                   f"abolished overall classification “{match.group(0)}”",
                   "the overall scale is now Tốt / Khá / Đạt / Chưa đạt (Thông tư "
                   "22/2021/TT-BGDĐT Điều 9) — “Khá” itself is unaffected")

    if doctype == "teacher-to-student":
        for match in ADDRESS_BAN_RE.finditer(masked):
            yield ("EDU002", WARN, match.start() + 1, match.group(0),
                   f"“{match.group(0)}” addressing a student",
                   "a teacher addresses a student as em (secondary) or con (primary), never bạn")

    if doctype == "primary-report-card":
        for match in NEEDS_IMPROVEMENT_CALQUE_RE.finditer(masked):
            yield ("EDU003", ERROR, match.start() + 1, match.group(0),
                   f"“{match.group(0)}” instead of the statutory term",
                   "Thông tư 27/2020/TT-BGDĐT Điều 7 uses “cần cố gắng” for primary routine assessment")

    if doctype in ("higher-ed", "transcript"):
        for match in CREDIT_CALQUE_RE.finditer(masked):
            yield ("EDU005", WARN, match.start() + 1, match.group(0),
                   f"“{match.group(0)}” for academic credit",
                   "academic credit is tín chỉ (Thông tư 08/2021/TT-BGDĐT); tín dụng is financial credit")

    if doctype == "transcript":
        for match in GPA_DOT_RE.finditer(masked):
            yield ("EDU006", ERROR, match.start() + 1, match.group(0),
                   f"GPA written with a dot decimal “{match.group(0)}”",
                   "Vietnamese transcripts use a decimal comma — write "
                   f"“{match.group(0).replace('.', ',')}”")

    if doctype == "edtech-microcopy":
        for match in EMPTY_STATE_CALQUE_RE.finditer(masked):
            yield ("EDU007", WARN, match.start() + 1, match.group(0),
                   f"literal empty-state phrase “{match.group(0)}”",
                   "never display raw “Trạng thái trống” / “Không có dữ liệu”")

    if doctype == "pronunciation-feedback":
        for match in HARSH_FEEDBACK_RE.finditer(masked):
            yield ("EDU009", WARN, match.start() + 1, match.group(0),
                   f"unpedagogical negative feedback “{match.group(0)}”",
                   "apply the Sandwich Feedback model")
