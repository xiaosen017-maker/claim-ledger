# claim-ledger

[![Quality checks](https://github.com/xiaosen017-maker/claim-ledger/actions/workflows/quality.yml/badge.svg)](https://github.com/xiaosen017-maker/claim-ledger/actions/workflows/quality.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-3776AB)](https://www.python.org/)
[![License MIT](https://img.shields.io/badge/license-MIT-2EA44F)](LICENSE)

Citation integrity checks and evidence ledgers for Markdown and LaTeX research manuscripts.

`claim-ledger` compares citation keys with a BibTeX library, identifies unresolved and unused entries, and flags empirical-looking statements that may need human evidence review. Reports are available as Markdown, JSON, or CSV.

## Why this exists

Reference managers answer whether a citation is formatted. They do not provide a compact ledger connecting manuscript claims to citation keys or highlight likely evidence gaps during drafting. `claim-ledger` provides a deterministic first pass while keeping scholarly judgment with the author.

## Features

- parses Pandoc citations such as `[@smith2024; @lee2025]`;
- parses LaTeX commands such as `\citep{smith2024,lee2025}`;
- extracts BibTeX entry keys;
- reports unresolved citations and unused bibliography entries;
- flags quantitative or empirical-looking statements without local citation markers;
- emits Markdown review notes, structured JSON, or a CSV claim ledger;
- includes a reusable Codex skill in [`skill/SKILL.md`](skill/SKILL.md).

## Quick start

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -e .
```

Run the example:

```bash
claim-ledger examples/manuscript.md examples/references.bib --output report.md
claim-ledger examples/manuscript.md examples/references.bib --format csv --output ledger.csv
```

Use `--fail-on-unresolved` in CI when missing BibTeX keys should fail a build.

## Example output

```text
Citation keys used: 3
Bibliography entries: 3
Unresolved citations: 1
Claims for review: 1
```

The tool does not assert that a claim is true, that a cited source supports it, or that every number needs a citation. It produces review prompts. See [docs/limitations.md](docs/limitations.md).

## Supported inputs

- UTF-8 Markdown with Pandoc citation syntax;
- UTF-8 LaTeX with common `\cite...{}` commands;
- BibTeX entries beginning with `@type{key,`.

## Project structure

```text
src/claim_ledger/  parsers, analysis, renderers, CLI
tests/             parser, analysis, and CLI checks
skill/             reusable research evidence workflow
examples/          small manuscript and bibliography
docs/              design and limitations
.github/            CI and collaboration templates
```

## Contributing and security

Read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing parser or heuristic changes. Do not include unpublished manuscripts or private bibliographies in public issues. Follow [SECURITY.md](SECURITY.md) for sensitive reports.

## License

MIT. See [LICENSE](LICENSE).
