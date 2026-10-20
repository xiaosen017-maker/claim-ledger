from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any


@dataclass(frozen=True)
class Claim:
    line: int
    text: str
    citation_keys: tuple[str, ...]
    needs_review: bool
    reason: str

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["citation_keys"] = list(self.citation_keys)
        return data


@dataclass(frozen=True)
class EvidenceReport:
    citation_keys: tuple[str, ...]
    bibliography_keys: tuple[str, ...]
    unresolved_keys: tuple[str, ...]
    unused_bibliography_keys: tuple[str, ...]
    claims: tuple[Claim, ...]

    @property
    def review_claims(self) -> tuple[Claim, ...]:
        return tuple(claim for claim in self.claims if claim.needs_review)

    def to_dict(self) -> dict[str, Any]:
        return {
            "summary": {
                "citations": len(self.citation_keys),
                "bibliography_entries": len(self.bibliography_keys),
                "unresolved_citations": len(self.unresolved_keys),
                "unused_bibliography_entries": len(self.unused_bibliography_keys),
                "claims_for_review": len(self.review_claims),
            },
            "citation_keys": list(self.citation_keys),
            "bibliography_keys": list(self.bibliography_keys),
            "unresolved_keys": list(self.unresolved_keys),
            "unused_bibliography_keys": list(self.unused_bibliography_keys),
            "claims": [claim.to_dict() for claim in self.claims],
        }
