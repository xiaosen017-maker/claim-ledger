# Limitations

`claim-ledger` is a review aid. Its output must not be treated as a verdict on research validity.

## What it does not establish

- A resolved citation key does not prove that the source exists or supports the claim.
- A citation in the same sentence may support only part of that sentence.
- An uncited quantitative statement may be a method parameter, equation result, or common fact.
- A statement without empirical cue words may still require a citation.
- BibTeX parsing identifies entry keys; it does not fully validate nested braces or field semantics.
- Sentence boundaries in complex LaTeX macros may be approximate.

## Safe review workflow

1. Resolve missing keys first.
2. Inspect every flagged claim in manuscript context.
3. Open each cited source and confirm claim-level support.
4. Record page, table, figure, or section locators when precision matters.
5. Use a reference verifier for DOI, author, title, year, and publication metadata.

Do not upload unpublished manuscripts or private bibliographies to public issues.
