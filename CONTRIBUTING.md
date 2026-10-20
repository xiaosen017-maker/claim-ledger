# Contributing to claim-ledger

Contributions should make evidence review more reproducible without overstating what automation can establish.

## Development setup

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -e .
python -m unittest discover -s tests -v
```

## Proposals

Parser changes need a minimal synthetic input and expected output. Heuristic changes need both a positive example and a false-positive boundary. Do not submit unpublished text, licensed full-text articles, private bibliographies, or personal participant data.

Keep one logical change per pull request and update user-facing documentation when behavior changes.
