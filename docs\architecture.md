# Architecture

`claim-ledger` uses a deliberately small pipeline so every flag can be reproduced from local files.

```text
manuscript.md / paper.tex ----> citation and sentence parser
                                         |
references.bib --------------------------+
                                         v
                                evidence analysis
                                         |
                          +--------------+--------------+
                          v              v              v
                      Markdown          JSON            CSV
```

## Parsing

The parser recognizes Pandoc citation groups and common LaTeX `\cite...{}` commands. It extracts BibTeX keys from entry headers and yields line-aware prose units while skipping fenced code blocks and common LaTeX environment markers.

## Analysis

Analysis is deterministic and offline. It compares cited and available keys, then applies transparent lexical cues to identify sentences that may describe empirical or quantitative findings. A claim is flagged only when a cue is present and no citation marker occurs in the same sentence-like unit.

## Reporting

Markdown is intended for author review, JSON for automation, and CSV for a claim-by-claim evidence matrix. All formats are generated from the same immutable report model.

## Extension points

- add citation syntaxes in `parsing.py`;
- add domain-specific cue profiles without changing the default profile;
- add bibliography metadata validation as a separate stage;
- add renderers without changing parsing or analysis.
