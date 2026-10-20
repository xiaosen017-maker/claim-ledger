import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from claim_ledger.cli import main  # noqa: E402


class CliTests(unittest.TestCase):
    def test_json_output_and_unresolved_exit_code(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "report.json"
            code = main([
                str(ROOT / "examples" / "manuscript.md"),
                str(ROOT / "examples" / "references.bib"),
                "--format", "json", "--output", str(output), "--fail-on-unresolved",
            ])
            self.assertEqual(code, 2)
            data = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(data["unresolved_keys"], ["missing2026"])
            self.assertGreaterEqual(data["summary"]["claims_for_review"], 1)


if __name__ == "__main__":
    unittest.main()
