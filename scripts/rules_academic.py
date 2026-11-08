# -*- coding: utf-8 -*-
"""Rules for Vietnamese & English academic research papers (IEEE, Q1) and theses (Luận văn ThS/TS).

Integrates structural, lexical, and stylometric AI-writing detectors from
`conorbronsdon/avoid-ai-writing` plus anti-perplexity checks for Grammarly/Turnitin.
Loaded automatically by validate_copy.py because the filename starts with `rules_`.
Standard library only, no imports from the engine — the contract is plain tuples.
"""
from __future__ import annotations

import math
import re

ERROR = "error"
WARN = "warning"

RULE_DOCS = {
    "ACAD001": "superlative or absolute claim in academic writing (“nhất”, “hoàn hảo”, “tốt nhất”)",
    "ACAD002": "sensationalism or hyperbole in scientific context (“vô cùng nghiêm trọng”, “thảm họa”)",
    "ACAD003": "informal or personal pronouns (“tôi”, “bạn”) in academic thesis / paper",
    "ACAD004": "dangling punctuation or broken sentence flow in academic prose",
    "ACAD005": "exclamatory or unverified AI commentary (“thật đáng kinh ngạc”, “mở ra kỷ nguyên mới”, “minh chứng hùng hồn”)",
    "ACAD006": "undefined LaTeX \\acs{}/\\ac{}/\\acf{} macro used without \\usepackage{acronym}",
    "ACAD007": "informal English contractions or conversational idioms in academic paper (“isn't”, “don't”, “by hand”, “dig into”)",
    "ACAD008": "AI-writing vocabulary tell (Tier 1A/1B or Tier 2 cluster from avoid-ai-writing: “delve”, “rigorous”, “granular”, “utilize”, “serves as”)",
    "ACAD009": "AI structural template (negative parallelism “is not X; it requires Y”, cutoff disclaimer “we do not have the details”, tailing negation “only X, without any Y”, or prose em-dash)",
    "ACAD010": "high binomial/tricolon coordination density (≥60% of sentences in paragraph contain “X and/or Y” pairs or 3-item triads — triggers Grammarly 100% AI detector)",
    "ACAD011": "low sentence-length burstiness (CV < 0.35 across ≥4 sentences) or low function-word trigram entropy (<0.82) — flat AI sentence rhythm",
    "ACAD012": "Vietnamese AI structural template or buzzword filler (“một cách toàn diện và sâu sắc”, “bức tranh toàn cảnh”, “không đơn thuần là X mà còn Y”)",
    "ACAD013": "coarse, flippant, or overly casual colloquialisms in academic writing (“khử mùi”, “suồng sã”, “sỗ sàng”, “chém gió”, “bóc phốt”, “ngon ăn”, “ăn đứt”)",
    "ACAD014": "formulaic meta-discourse or syllabus outline announcement (“our analysis focuses on three components”, “spans three primary categories”, “each entry reports publisher metadata”)",
    "ACAD015": "hyper-polished AI rhetorical transitions or participle chaining (“requiring authors to address”, “in turn, task demands dictate whether”, “leaving X as the only option”)",
    "ACAD016": "survey taxonomy phrasing guidance — encourages functional topic markers (“In terms of datasets”, “For research tasks”) and field-standard technical shorthand (“DNNs”, “stat-based baselines”, “clinical medical exams”)",
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
    "paper": "an IEEE conference/transactions or ISI/Scopus Q1 scientific paper (Vietnamese or bilingual)",
    "en-paper": "an English-language IEEE/Springer/Elsevier/ACM scientific manuscript",
    "academic-prose": "general academic research, methodology, or survey prose",
    "primary-report-card": "a primary-school (tiểu học) report card or sổ liên lạc entry",
    "secondary-report-card": "a secondary/high-school (THCS/THPT) report card or học bạ entry",
    "teacher-to-student": "a teacher addressing a student directly",
    "transcript": "a university transcript or GPA statement",
    "higher-ed": "university administrative prose — syllabi, course descriptions, registration",
    "edtech-microcopy": "EdTech UI and microcopy strings",
    "pronunciation-feedback": "pronunciation feedback strings",
}

# Superlative and absolute patterns (Vietnamese)
SUPERLATIVE_RE = re.compile(
    r"(?<!\w)(?:(?:tốt|cao|giỏi|nhanh|chính\s+xác|tối\s+ưu|hiệu\s+quả|đột\s+phá|vượt\s+trội|mới|hiện\s+đại|toàn\s+diện)\s+nhất"
    r"|duy\s+nhất|hoàn\s+hảo|tuyệt\s+đối|triệt\s+để|số\s*(?:một|1)\b)(?!\w)",
    re.IGNORECASE,
)

# Sensationalism & hyperbole patterns (Vietnamese)
HYPERBOLE_RE = re.compile(
    r"(?<!\w)(?:vô\s+cùng\s+nghiêm\s+trọng|cực\s+kỳ\s+nguy\s+hiểm|thảm\s+họa"
    r"|đe\s+dọa\s+nghiêm\s+trọng\s+tới\s+sự\s+sống\s+còn|hoàn\s+toàn\s+bế\s+tắc"
    r"|vấn\s+nạn\s+nhức\s+nhối|sai\s+lầm\s+chết\s+người)(?!\w)",
    re.IGNORECASE,
)

# Exclamatory or unverified AI commentary (Vietnamese & English)
AI_COMMENTARY_RE = re.compile(
    r"(?<!\w)(?:thật\s+(?:đáng\s+kinh\s+ngạc|thú\s+vị|bất\s+ngờ)|đáng\s+kinh\s+ngạc\s+là"
    r"|không\s+thể\s+phủ\s+nhận\s+rằng|mở\s+ra\s+(?:một\s+)?kỷ\s+nguyên\s+mới"
    r"|minh\s+chứng\s+hùng\s+hồn|đóng\s+góp\s+một\s+phần\s+không\s+nhỏ"
    r"|mang\s+lại\s+cái\s+nhìn\s+sâu\s+sắc\s+và\s+toàn\s+diện)(?!\w)",
    re.IGNORECASE,
)

# Avoid-AI-Writing Vietnamese patterns (ACAD012)
VI_AI_STRUCTURE_RE = re.compile(
    r"(?<!\w)(?:một\s+cách\s+toàn\s+diện\s+và\s+sâu\s+sắc|bức\s+tranh\s+(?:toàn\s+cảnh|tổng\s+thể)"
    r"|khai\s+phá\s+tiềm\s+năng|chìa\s+khóa\s+then\s+chốt"
    r"|không\s+(?:chỉ|đơn\s+thuần)\s+(?:dừng\s+lại\s+ở\s+)?(?:\w+\s+){1,6}mà\s+còn\b"
    r"|đáng\s+chú\s+ý\s+là\s*,)(?!\w)",
    re.IGNORECASE,
)

# Coarse, flippant, or overly casual colloquialisms in academic writing (ACAD013)
VI_COARSE_RE = re.compile(
    r"(?<!\w)(?:khử\s+mùi(?:\s+ai)?|bóc\s+phốt|chém\s+gió|phán\s+bừa|ngon\s+ăn|dễ\s+ợt"
    r"|ăn\s+đứt|đè\s+bẹp|bó\s+tay|chịu\s+chết|vọc\s+vạch|táy\s+máy|xịn\s+sò|bá\s+đạo"
    r"|toang|vãi|ảo\s+ma|nói\s+trắng\s+ra|thẳng\s+thắn\s+mà\s+nói|chả\s+có(?:\s+gì)?"
    r"|hết\s+nước\s+chấm|gánh\s+team|bắt\s+bài|lầy\s+lội|làm\s+mưa\s+làm\s+gió|sỗ\s+sàng|suồng\s+sã)(?!\w)",
    re.IGNORECASE,
)

EN_COARSE_RE = re.compile(
    r"(?<!\w)(?:crap|sucks|bullshit|screw\s+up|pissed(?:\s+off)?|freaking|dumb|lame"
    r"|no-brainer|kinda|sorta|gonna|wanna|bunch\s+of|mess\s+around|badass|half-assed)(?!\w)",
    re.IGNORECASE,
)

# Personal pronouns in academic writing
ACADEMIC_PRONOUNS_RE = re.compile(r"(?<!\w)(?:tôi|bạn|quý\s+vị|anh/chị)(?!\w)", re.IGNORECASE)
THESIS_WE_RE = re.compile(r"(?<!\w)chúng\s+tôi(?!\w)", re.IGNORECASE)

# Dangling comma at end of line (incomplete sentence structure)
DANGLING_COMMA_RE = re.compile(r",\s*$")

# LaTeX acronym macros
ACRONYM_PKG_RE = re.compile(r"\\usepackage(?:\[[^\]]*\])?\{[^}]*\bacronym\b[^}]*\}")
ACRONYM_MACRO_RE = re.compile(r"\\ac(?:s|f|p|fp|sp)?\{[^}]+\}")

# Informal English contractions & idioms in academic papers (ACAD007)
EN_INFORMAL_RE = re.compile(
    r"(?<!\w)(?:isn['’]t|aren['’]t|wasn['’]t|weren['’]t|don['’]t|doesn['’]t|didn['’]t"
    r"|can['’]t|couldn['’]t|won['’]t|wouldn['’]t|shouldn['’]t|you['’]ll|you['’]re|we['’]re|they['’]re|it['’]s"
    r"|pulled\s+together|by\s+hand|honestly|dig\s+into|dig\s+deeper|digging\s+into"
    r"|tapped\s+into|tap\s+into|pull\s+out|plays\s+out|zooming\s+in\s+on"
    r"|covers\s+a\s+lot\s+of\s+ground|have\s+a\s+hand\s+in|went\s+in\s+a\s+different\s+direction"
    r"|big\s+language\s+models|stick\s+with|spot\s+early|spotted\s+patterns)(?!\w)",
    re.IGNORECASE,
)

# Avoid-AI-Writing Tier 1A + 1B Vocabulary in English prose (ACAD008)
EN_AI_TIER1_RE = re.compile(
    r"(?<!\w)(?:delve(?:s|d|ing)?(?:\s+into)?|tapestry|realm|beacon|testament\s+to"
    r"|cutting-edge|pivotal|underscores?|meticulous(?:ly)?|game-chang(?:er|ing)"
    r"|watershed\s+moment|showcasing|deep\s+dive|unpack(?:ing)?|intricac(?:y|ies)|intricate"
    r"|ever-evolving|daunting|holistic(?:ally)?|actionable|impactful|synerg(?:y|ies)"
    r"|interplay|symphony|rigorous(?:ly)?|granular(?:ity)?|pronounced"
    r"|manifest(?:s|ed|ing)?|thereby\s+\w+ing|pav(?:es|ing)\s+the\s+way"
    r"|utiliz(?:e|es|ed|ing)|in\s+order\s+to|due\s+to\s+the\s+fact\s+that"
    r"|serves\s+as|boasts|endeavor(?:s)?|ascertain)(?!\w)",
    re.IGNORECASE,
)

# Avoid-AI-Writing Tier 2 Vocabulary (flagged when 2+ appear in same paragraph)
EN_AI_TIER2_WORDS = frozenset({
    "harness", "navigate", "navigating", "foster", "elevate", "unleash",
    "streamline", "empower", "bolster", "spearhead", "resonate", "resonates",
    "revolutionize", "facilitate", "facilitates", "underpin", "underpinning",
    "nuanced", "crucial", "multifaceted", "myriad", "plethora", "encompass",
    "encompasses", "catalyze", "reimagine", "galvanize", "augment", "cultivate",
    "illuminate", "elucidate", "juxtapose", "cornerstone", "paramount",
    "poised", "burgeoning", "nascent", "quintessential", "overarching",
})

# Avoid-AI-Writing Structural Templates (ACAD009):
# 1. Negative parallelism / truism opener: "is not straightforward; it requires", "is not public and requires", "isn't just X, it's Y"
# 2. Cutoff disclaimers / narrated candor: "although we do not have the details on", "while specific details are limited", "to be honest"
# 3. Tailing negation contrast: "provide only X, without any Y"
# 4. Confidence calibration / hollow filler openers: "it is worth noting that", "importantly,", "notably,", "interestingly,"
EN_AI_STRUCTURE_RE = re.compile(
    r"(?:"
    r"\bis\s+not\s+(?:straightforward|simple|easy|trivial|merely|just|only)\b[^.?!]{0,80}\b(?:it\s+)?(?:requires|demands|needs|involves)\b"
    r"|\bis\s+not\s+(?:public|open|free|available)\s+and\s+(?:requires|demands|needs)\b"
    r"|\b(?:provide|contain|include)s?\s+only\b[^.?!]{3,80},\s*without\s+any\b"
    r"|\b(?:although|though|while)\s+we\s+do\s+not\s+have\s+(?:the\s+)?(?:details|information|records|access)\s+on\b"
    r"|\bwhile\s+specific\s+details\s+are\s+limited\b"
    r"|\b(?:it\s+is\s+(?:worth\s+noting|important\s+to\s+note)\s+that|to\s+be\s+(?:fully\s+)?(?:transparent|honest|clear))\b"
    r"|(?:^|[.!?]\s+)(?:Importantly|Notably|Interestingly|Surprisingly|Undoubtedly|Crucially),"
    r"|\b(?:strict|rigorous)\s+ethical\s+oversight,\s*(?:careful|strict)\s+data\s+(?:handling|governance),\s*and\s+(?:real\s+|robust\s+)?(?:protection|victim-protection)\b"
    r")",
    re.IGNORECASE,
)

# Prose em-dash detector (excluding LaTeX tables/math)
PROSE_EM_DASH_RE = re.compile(r"(?<=\w)\s*(?:—|--)\s*(?=\w)")

# Formulaic Meta-Discourse / Outline Syllabus Tell (ACAD014)
# Patterns where AI introduces sections or tables like a robotic syllabus outline:
EN_META_DISCOURSE_RE = re.compile(
    r"(?:"
    r"\b(?:our\s+analysis\s+focuses\s+on\s+(?:three|two|four|five)\s+(?:components|parts|dimensions|aspects|axes))\b"
    r"|\b(?:spans\s+(?:three|four|five)\s+primary\s+(?:categories|domains|areas|facets))\b"
    r"|\b(?:each\s+entry\s+reports\s+publisher\s+metadata)\b"
    r"|\b(?:for\s+studies\s+that\s+do\s+not\s+fit\s+neatly)\b"
    r"|\b(?:to\s+ensure\s+every\s+methodology\s+is\s+thoroughly\s+covered)\b"
    r"|\b(?:research\s+tasks\s+vary\s+widely\s+across\s+the\s+corpus)\b"
    r"|\b(?:first,\s+this\s+section\s+analyzes\b[^.?!]{0,100}\bnext,\s+we\s+review\b[^.?!]{0,100}\bfinally,\s+we\s+highlight)\b"
    r"|\b(?:this\s+section\s+systematically\s+evaluates\s+empirical\s+literature\s+across\s+(?:three|two|four)\s+core\s+dimensions)\b"
    r")",
    re.IGNORECASE,
)

# Hyper-polished AI rhetorical transitions & Participle chaining (ACAD015)
# Catches low-perplexity LLM stylistic habits that trigger AI text detectors:
EN_HYPER_POLISHED_RE = re.compile(
    r"(?:"
    r"\b(?:requiring\s+(?:authors|researchers|models|practitioners)\s+to\s+(?:address|handle|evaluate|balance))\b"
    r"|\b(?:leaving\s+[^.?!]{1,60}\s+as\s+the\s+only\s+option)\b"
    r"|\b(?:in\s+turn,\s*[^.?!]{1,60}\b(?:dictate|determine)s?\s+whether)\b"
    r"|\b(?:play\s+a\s+(?:defining|pivotal|central|crucial)\s+role\s+here)\b"
    r"|\b(?:directly\s+affect\s+how\s+researchers\s+formulate)\b"
    r"|\bliterature\s+centers\s+on\b"
    r")",
    re.IGNORECASE,
)

# Binomial coordination (`X and Y` or `X or Y`) & Tricolon (`A, B, and C`) detector for English sentences
TRICOLON_SENT_RE = re.compile(
    r"\b[a-zA-Z-]+(?:\s+[a-zA-Z-]+){0,3},\s+[a-zA-Z-]+(?:\s+[a-zA-Z-]+){0,3},\s+and\s+[a-zA-Z-]+(?:\s+[a-zA-Z-]+){0,3}\b"
)
BINOMIAL_SENT_RE = re.compile(
    r"\b(?:[a-zA-Z]{3,}\s+(?:and|or)\s+[a-zA-Z]{3,}|[a-zA-Z]{3,}\s+[a-zA-Z]{3,}\s+(?:and|or)\s+[a-zA-Z]{3,}\s+[a-zA-Z]{3,})\b",
    re.IGNORECASE,
)

FUNC_WORDS = frozenset({
    "the", "a", "an", "and", "or", "but", "of", "to", "in", "on", "at", "by", "for", "with",
    "from", "as", "is", "was", "are", "were", "be", "been", "being", "have", "has", "had",
    "do", "does", "did", "will", "would", "should", "could", "may", "might", "must", "can",
    "this", "that", "these", "those", "it", "its", "they", "them", "their", "there", "here",
    "we", "our", "us", "i", "you", "your", "he", "she", "his", "her", "him", "not", "no", "so",
    "if", "then", "than", "when", "where", "which", "who", "what", "how", "why", "because",
})

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


def _is_prose_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    if stripped.startswith(("%", "\\begin", "\\end", "\\section", "\\subsection", "\\subsubsection",
                            "\\caption", "\\label", "\\includegraphics", "\\vspace", "\\hspace",
                            "\\hline", "\\cline", "\\rowcolor", "\\multicolumn", "\\item", "\\bibitem",
                            "#", "|", ">", "<!--", "---")):
        return False
    if "&" in stripped and "\\\\" in stripped:
        return False
    return True


def check_line(ctx, lineno, raw, masked):
    doctype = ctx.doctype
    if not doctype and ctx.path.suffix.lower() == ".tex":
        doctype = "paper"
    if not doctype:
        return

    # Academic doctypes: thesis, paper, en-paper, academic-prose
    if doctype in ("thesis", "paper", "en-paper", "academic-prose"):
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

        for match in AI_COMMENTARY_RE.finditer(masked):
            yield ("ACAD005", ERROR, match.start() + 1, match.group(0),
                   f"exclamatory or unverified AI commentary “{match.group(0)}”",
                   "remove unverified AI commentary and emotional exclamations; let empirical results speak for themselves")

        for match in VI_AI_STRUCTURE_RE.finditer(masked):
            yield ("ACAD012", ERROR, match.start() + 1, match.group(0),
                   f"Vietnamese AI structural template or buzzword filler “{match.group(0)}”",
                   "remove empty AI buzzwords/templates; state concrete quantitative facts directly")

        for match in VI_COARSE_RE.finditer(masked):
            yield ("ACAD013", ERROR, match.start() + 1, match.group(0),
                   f"từ ngữ suồng sã, sỗ sàng hoặc khẩu ngữ bình dân “{match.group(0)}”",
                   "văn phong học thuật quốc tế và luận văn đòi hỏi tính mực thước, trang trọng — "
                   "thay bằng thuật ngữ khoa học tương ứng (ví dụ: “phát hiện và sửa AI writing”, “khảo sát thực nghiệm”, “vượt trội về định lượng”)")

        for match in ACADEMIC_PRONOUNS_RE.finditer(masked):
            yield ("ACAD003", ERROR, match.start() + 1, match.group(0),
                   f"informal or personal pronoun “{match.group(0)}”",
                   "use third-person impersonal register: “luận văn”, “nghiên cứu này”, “mô hình đề xuất”")

        if doctype == "thesis":
            for match in THESIS_WE_RE.finditer(masked):
                yield ("ACAD003", WARN, match.start() + 1, match.group(0),
                       f"“{match.group(0)}” in individual graduate thesis",
                       "a Master's thesis is an individual work — replace “chúng tôi” with “luận văn” or “tác giả”")

        if DANGLING_COMMA_RE.search(raw.rstrip()) and _is_prose_line(raw):
            yield ("ACAD004", WARN, len(raw.rstrip()), ",",
                   "dangling comma at end of line",
                   "avoid arbitrary line breaks mid-sentence; keep academic paragraphs as continuous blocks")

    if doctype in ("en-paper", "paper", "academic-prose") and _is_prose_line(masked):
        for match in EN_INFORMAL_RE.finditer(masked):
            yield ("ACAD007", ERROR, match.start() + 1, match.group(0),
                   f"informal English contraction or idiom “{match.group(0)}”",
                   "replace conversational phrasing with plain academic English (e.g., “is not”, “manually”, “examine”, “extract”)")

        for match in EN_COARSE_RE.finditer(masked):
            yield ("ACAD013", ERROR, match.start() + 1, match.group(0),
                   f"coarse, flippant, or slang colloquialism “{match.group(0)}”",
                   "replace coarse or flippant colloquialisms with precise, formal academic vocabulary")

        for match in EN_AI_TIER1_RE.finditer(masked):
            yield ("ACAD008", WARN, match.start() + 1, match.group(0),
                   f"AI-writing vocabulary tell “{match.group(0)}” (avoid-ai-writing Tier 1)",
                   "replace AI buzzwords/wordiness with plain verbs/adjectives (“use”, “to”, “because”, “is”, “strict”, “detailed”)")

        for match in EN_AI_STRUCTURE_RE.finditer(masked):
            yield ("ACAD009", ERROR, match.start() + 1, match.group(0),
                   f"AI structural template “{match.group(0)}”",
                   "rewrite negative-parallelism openers, cutoff disclaimers (“we do not have the details”), and “only X, without any Y” tails as direct factual statements")

        for match in EN_META_DISCOURSE_RE.finditer(masked):
            yield ("ACAD014", ERROR, match.start() + 1, match.group(0),
                   f"formulaic meta-discourse / syllabus outline announcement “{match.group(0)}”",
                   "replace meta-announcements (“our analysis focuses on three components”, “each entry reports”, “spans three categories”) with substantive domain insights")

        for match in EN_HYPER_POLISHED_RE.finditer(masked):
            yield ("ACAD015", ERROR, match.start() + 1, match.group(0),
                   f"hyper-polished AI rhetorical transition / participle chaining “{match.group(0)}”",
                   "rewrite hyper-polished LLM rhetorical phrasing (“requiring authors to address”, “in turn, task demands dictate whether”, “play a defining role”) with functional, direct human academic prose")

        for match in PROSE_EM_DASH_RE.finditer(masked):
            # Ignore CNN--LSTM / LSTM--CNN or numeric ranges
            span_start = max(0, match.start() - 10)
            span_end = min(len(masked), match.end() + 10)
            context_slice = masked[span_start:span_end]
            if re.search(r"\b(?:CNN|LSTM|BERT|\d+)\s*(?:—|--)\s*(?:CNN|LSTM|BERT|\d+)\b", context_slice):
                continue
            yield ("ACAD009", WARN, match.start() + 1, match.group(0),
                   f"prose em-dash splice “{match.group(0)}” (avoid-ai-writing formatting tell)",
                   "replace prose em-dashes with commas, periods, or parentheses")

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


def _clean_latex_for_sentences(para_text: str) -> str:
    # Strip citations and refs so they don't distort sentence splitting or word counts
    cleaned = re.sub(r"~?\\(?:cite|citep|citet|ref|eqref|label)\{[^}]*\}", "", para_text)
    cleaned = re.sub(r"\\[a-zA-Z]+\{([^}]*)\}", r"\1", cleaned)
    cleaned = re.sub(r"et\s+al\.", "et al", cleaned)
    cleaned = re.sub(r"e\.g\.", "eg", cleaned)
    cleaned = re.sub(r"i\.e\.", "ie", cleaned)
    cleaned = re.sub(r"Fig\.", "Fig", cleaned)
    return cleaned


def check_document(ctx):
    doctype = ctx.doctype
    if not doctype and ctx.path.suffix.lower() == ".tex":
        doctype = "paper"
    if not doctype:
        return

    # 1. Check undefined \acs{} / \ac{} in LaTeX documents without \usepackage{acronym}
    if ctx.path.suffix.lower() == ".tex" and not ACRONYM_PKG_RE.search(ctx.text):
        for i, line in enumerate(ctx.masked, 1):
            for match in ACRONYM_MACRO_RE.finditer(line):
                yield ("ACAD006", ERROR, i, match.start() + 1, match.group(0),
                       f"undefined acronym macro “{match.group(0)}” (no \\usepackage{{acronym}} in preamble)",
                       "write the acronym directly in plain text or declare \\usepackage{acronym} in the preamble")

    # 2. Paragraph-level English AI-writing checks (Tier 2 clusters, Binomial stacking, Sentence burstiness CV)
    if doctype in ("en-paper", "paper", "academic-prose"):
        paragraphs = []
        current_lines = []
        start_lineno = 1
        in_env = False

        for i, line in enumerate(ctx.masked, 1):
            stripped = line.strip()
            if stripped.startswith(("\\begin{table}", "\\begin{figure}", "\\begin{tikzpicture}", "\\begin{thebibliography}")):
                in_env = True
            if in_env:
                if stripped.startswith(("\\end{table}", "\\end{figure}", "\\end{tikzpicture}", "\\end{thebibliography}")):
                    in_env = False
                continue

            if not stripped or not _is_prose_line(line):
                if current_lines:
                    paragraphs.append((start_lineno, " ".join(current_lines)))
                    current_lines = []
            else:
                if not current_lines:
                    start_lineno = i
                current_lines.append(stripped)
        if current_lines:
            paragraphs.append((start_lineno, " ".join(current_lines)))

        for p_lineno, para in paragraphs:
            cleaned_para = _clean_latex_for_sentences(para)
            tokens = re.findall(r"[a-zA-Z]+(?:'[a-zA-Z]+)?", cleaned_para.lower())
            if len(tokens) < 35:
                continue

            # Only run English stylometric checks on predominantly English paragraphs
            en_func_count = sum(1 for t in tokens if t in FUNC_WORDS)
            if en_func_count / max(1, len(tokens)) < 0.20:
                continue

            # Check 2A: Avoid-AI-Writing Tier 2 Cluster (2+ distinct Tier 2 words in one paragraph)
            tier2_hits = sorted({t for t in tokens if t in EN_AI_TIER2_WORDS})
            if len(tier2_hits) >= 2:
                yield ("ACAD008", WARN, p_lineno, 1, ", ".join(tier2_hits),
                       f"Tier 2 AI vocabulary cluster in paragraph ({len(tier2_hits)} words: {', '.join(tier2_hits)})",
                       "avoid stacking multiple Tier 2 AI words in the same paragraph (avoid-ai-writing rule)")

            # Split into sentences
            raw_sents = [s.strip() for s in re.split(r"[.!?]+", cleaned_para) if len(s.strip().split()) >= 4]
            if len(raw_sents) < 4:
                continue

            # Check 2B: Binomial (`X and/or Y`) & Tricolon (`A, B, and C`) coordination stacking across sentences
            coord_sents = 0
            tricolon_sents = 0
            for s in raw_sents:
                has_tricolon = bool(TRICOLON_SENT_RE.search(s))
                # Exclude technical model names like "CNN and LSTM", "ML and DL", "precision and recall", "training and prediction"
                s_filtered = re.sub(
                    r"\b(?:ML|DL|NLP|CNN|LSTM|BLSTM|BERT|SVM|LR|NB|XAI|CSA|CSAM|ROC-AUC|PR-AUC|training|prediction|images|videos|text|national|local|mean|standard)\s+(?:and|or)\s+(?:ML|DL|NLP|CNN|LSTM|BLSTM|BERT|SVM|LR|NB|XAI|CSA|CSAM|ROC-AUC|PR-AUC|training|prediction|images|videos|text|national|local|standard)\b",
                    "",
                    s,
                    flags=re.IGNORECASE,
                )
                has_binomial = bool(BINOMIAL_SENT_RE.search(s_filtered))
                if has_tricolon:
                    tricolon_sents += 1
                if has_tricolon or has_binomial:
                    coord_sents += 1

            coord_ratio = coord_sents / len(raw_sents)
            if coord_sents >= 4 and coord_ratio >= 0.75:
                yield ("ACAD010", WARN, p_lineno, 1, f"{coord_sents}/{len(raw_sents)} sentences with X and/or Y pairs",
                       f"high binomial/tricolon coordination density ({coord_sents}/{len(raw_sents)} sentences contain balanced “X and/or Y” pairs or triads)",
                       "LLMs end almost every sentence with a balanced “A and/or B” pair (triggers Grammarly 100% AI); simplify to a single concrete noun in most sentences")

            # Check 2C: Sentence-length uniformity / low burstiness (CV = stdDev / mean < 0.30)
            lengths = [len(re.findall(r"\S+", s)) for s in raw_sents]
            mean_len = sum(lengths) / len(lengths)
            if mean_len > 10:
                variance = sum((l - mean_len) ** 2 for l in lengths) / len(lengths)
                cv = math.sqrt(variance) / mean_len
                if cv < 0.28:
                    yield ("ACAD011", WARN, p_lineno, 1, f"CV={cv:.2f} (lengths={lengths})",
                           f"uniform sentence lengths across paragraph (CV={cv:.2f}, lengths={lengths})",
                           "flat sentence rhythm signals AI writing; combine related clauses into a 30–40 word sentence and shorten another sentence to 6–9 words (target CV >= 0.45)")
