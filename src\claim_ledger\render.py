from __future__ import annotations

import csv
import io

from .models import EvidenceReport


def markdown_report(report: EvidenceReport, manuscript_name: str) -> str:
    summary = report.to_dict()["summary"]
    lines = [
        "# Claim evidence ledger",
        "",
        f"- Manuscript: `{manuscript_name}`",
        f"- Citation keys used: **{summary['citations']}**",
        f"- Bibliography entries: **{summary['bibliography_entries']}**",
        f"- Unresolved citations: **{summary['unresolved_citations']}**",
        f"- Unused bibliography entries: **{summary['unused_bibliography_entries']}**",
        f"- Claims for review: **{summary['claims_for_review']}**",
        "",
        "## Citation integrity",
        "",
        f"**Unresolved:** {', '.join(report.unresolved_keys) or 'None'}",
        "",
        f"**Unused bibliography entries:** {', '.join(report.unused_bibliography_keys) or 'None'}",
        "",
        "## Claims for human review",
        "",
        "| Line | Reason | Claim |",
        "|---:|---|---|",
    ]
    for claim in report.review_claims:
        text = claim.text.replace("|", "\\|").replace("\n", " ")
        lines.append(f"| {claim.line} | {claim.reason} | {text} |")
    if not report.review_claims:
        lines.append("| - | - | No uncited candidate claims detected |")
    lines += [
        "",
        "> Automated flags are review prompts, not judgments about truth or citation quality.",
        "",
    ]
    return "\n".join(lines)


def csv_ledger(report: EvidenceReport) -> str:
    stream = io.StringIO(newline="")
    writer = csv.writer(stream)
    writer.writerow(["line", "claim", "citation_keys", "needs_review", "reason"])
    for claim in report.claims:
        writer.writerow([claim.line, claim.text, ";".join(claim.citation_keys), claim.needs_review, claim.reason])
    return stream.getvalue()
