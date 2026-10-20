from __future__ import annotations

import re

from .models import Claim, EvidenceReport
from .parsing import bibliography_keys, citation_keys, citations_in_text, iter_sentences


EMPIRICAL_CUES = re.compile(
    r"(?i)\b(?:increase[sd]?|decrease[sd]?|improve[sd]?|reduce[sd]?|predict[sed]*|"
    r"associated|correlated|significant|outperform[sed]*|demonstrat(?:e|es|ed)|"
    r"show(?:s|ed)?|found|observed|participants?|patients?|respondents?|sample)\b"
    r"|(?:显著|提高|降低|改善|相关|预测|样本|受试者|参与者|调查显示|研究发现)"
)
NUMBER_CUE = re.compile(r"(?<!\w)(?:\d+(?:\.\d+)?%?|p\s*[<=>]\s*0?\.\d+)(?!\w)", re.I)


def _needs_evidence(sentence: str) -> tuple[bool, str]:
    has_empirical = bool(EMPIRICAL_CUES.search(sentence))
    has_number = bool(NUMBER_CUE.search(sentence))
    if has_empirical and has_number:
        return True, "empirical language and a quantitative value"
    if has_empirical:
        return True, "empirical or comparative language"
    if has_number:
        return True, "quantitative value"
    return False, ""


def analyze_manuscript(manuscript: str, bibliography: str) -> EvidenceReport:
    cited = citation_keys(manuscript)
    available = bibliography_keys(bibliography)
    available_set = set(available)
    cited_set = set(cited)
    claims: list[Claim] = []

    for line, sentence in iter_sentences(manuscript):
        candidate, reason = _needs_evidence(sentence)
        keys = citations_in_text(sentence)
        needs_review = candidate and not keys
        claims.append(Claim(line, sentence, keys, needs_review, reason if needs_review else ""))

    return EvidenceReport(
        citation_keys=cited,
        bibliography_keys=available,
        unresolved_keys=tuple(sorted(cited_set - available_set)),
        unused_bibliography_keys=tuple(sorted(available_set - cited_set)),
        claims=tuple(claims),
    )
