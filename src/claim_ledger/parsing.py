from __future__ import annotations

import re


BIB_ENTRY = re.compile(r"(?m)^\s*@\w+\s*\{\s*([^,\s]+)\s*,")
PANDOC_GROUP = re.compile(r"\[([^\]]*@[A-Za-z0-9_:.+\-/]+[^\]]*)\]")
PANDOC_KEY = re.compile(r"@([A-Za-z0-9_:.+\-/]+)")
LATEX_CITE = re.compile(r"\\cite\w*\s*\{([^}]+)\}")


def bibliography_keys(text: str) -> tuple[str, ...]:
    return tuple(dict.fromkeys(match.group(1).strip() for match in BIB_ENTRY.finditer(text)))


def citation_keys(text: str) -> tuple[str, ...]:
    keys: list[str] = []
    for group in PANDOC_GROUP.finditer(text):
        keys.extend(match.group(1) for match in PANDOC_KEY.finditer(group.group(1)))
    for group in LATEX_CITE.finditer(text):
        keys.extend(part.strip() for part in group.group(1).split(",") if part.strip())
    return tuple(dict.fromkeys(keys))


def citations_in_text(text: str) -> tuple[str, ...]:
    return citation_keys(text)


def iter_sentences(text: str):
    """Yield line-aware sentence-like units from Markdown or LaTeX prose."""
    in_fence = False
    for line_number, raw in enumerate(text.splitlines(), start=1):
        line = raw.strip()
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or not line or line.startswith(("#", "%", "\\begin{", "\\end{")):
            continue
        line = re.sub(r"^[-*+]\s+", "", line)
        for sentence in re.split(r"(?<=[.!?。！？])\s+", line):
            sentence = sentence.strip()
            if len(sentence) >= 20:
                yield line_number, sentence
