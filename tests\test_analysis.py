import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from claim_ledger.analysis import analyze_manuscript  # noqa: E402


class AnalysisTests(unittest.TestCase):
    def test_reconciles_keys_and_flags_uncited_empirical_claim(self):
        manuscript = (ROOT / "examples" / "manuscript.md").read_text(encoding="utf-8")
        bibliography = (ROOT / "examples" / "references.bib").read_text(encoding="utf-8")
        report = analyze_manuscript(manuscript, bibliography)

        self.assertEqual(report.unresolved_keys, ("missing2026",))
        self.assertEqual(report.unused_bibliography_keys, ("unused2023",))
        self.assertTrue(any("126 participants" in claim.text for claim in report.review_claims))
        self.assertFalse(any("18%" in claim.text for claim in report.review_claims))

    def test_latex_citations_are_supported(self):
        report = analyze_manuscript(
            "Results improved significantly \\citep{smith2024,lee2025}.",
            "@article{smith2024, title={A}}\n@article{lee2025, title={B}}",
        )
        self.assertEqual(report.unresolved_keys, ())
        self.assertEqual(report.citation_keys, ("smith2024", "lee2025"))


if __name__ == "__main__":
    unittest.main()
