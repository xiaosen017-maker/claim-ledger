from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Sequence

from .analysis import analyze_manuscript
from .render import csv_ledger, markdown_report


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="claim-ledger", description="Audit manuscript citation integrity and evidence prompts.")
    parser.add_argument("manuscript", help="Markdown or LaTeX manuscript path.")
    parser.add_argument("bibliography", help="BibTeX bibliography path.")
    parser.add_argument("--format", choices=("markdown", "json", "csv"), default="markdown")
    parser.add_argument("--output", "-o", help="Output path; defaults to stdout.")
    parser.add_argument("--fail-on-unresolved", action="store_true", help="Return exit code 2 for unresolved citation keys.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        manuscript_path = Path(args.manuscript)
        bibliography_path = Path(args.bibliography)
        report = analyze_manuscript(
            manuscript_path.read_text(encoding="utf-8"),
            bibliography_path.read_text(encoding="utf-8"),
        )
        if args.format == "json":
            rendered = json.dumps(report.to_dict(), indent=2, ensure_ascii=False) + "\n"
        elif args.format == "csv":
            rendered = csv_ledger(report)
        else:
            rendered = markdown_report(report, manuscript_path.name)
        if args.output:
            Path(args.output).write_text(rendered, encoding="utf-8")
        else:
            print(rendered, end="" if rendered.endswith("\n") else "\n")
        return 2 if args.fail_on_unresolved and report.unresolved_keys else 0
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"claim-ledger: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
