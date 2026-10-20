---
name: paper-evidence-audit
description: Build an evidence ledger for a Markdown or LaTeX research manuscript, reconcile citation keys with BibTeX, and identify claims that need human citation review.
---

# Paper Evidence Audit

Use this skill when the user asks to audit citations, build a claim-to-source matrix, find unresolved references, or identify likely evidence gaps in a manuscript.

## Inputs

- a UTF-8 Markdown or LaTeX manuscript;
- a BibTeX bibliography;
- optional scope such as one section or the whole manuscript.

Never invent bibliographic records or claim that a citation supports a statement without reading the source.

## Workflow

1. Preserve the source files and record the requested scope.
2. Run `claim-ledger` to create a Markdown report and CSV ledger.
3. Resolve every citation key missing from the bibliography.
4. Review every flagged claim in context. Remove false positives such as method parameters or author calculations.
5. For remaining claims, inspect the cited source and record a precise locator when available.
6. Separate four states: supported, partially supported, contradicted, and not verified.
7. Report limitations and unresolved items explicitly.

## Commands

```bash
claim-ledger manuscript.md references.bib --output evidence-report.md
claim-ledger manuscript.md references.bib --format csv --output evidence-ledger.csv
```

Use `--fail-on-unresolved` in automated checks when missing citation keys must stop the workflow.

## Output requirements

The final ledger should include manuscript line, claim text, citation key, verification state, source locator, and reviewer note. Automated candidate flags are prompts for review and must not be presented as factual errors.

## Evidence boundaries

- A matching BibTeX key proves only that the key exists.
- A nearby citation does not prove claim-level support.
- Search snippets and AI summaries are discovery aids, not source evidence.
- Keep the author's intended strength of claim unless the verified evidence requires revision.
