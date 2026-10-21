# AI for Programming

This repository contains programming exercises and small Python tools for
biological sequence analysis.

## GC content

Use `scripts/gc_content.py` to calculate GC content for each record in a
FASTA file:

```bash
python3 scripts/gc_content.py input/multi_seq.fasta
```

The optional `--min-gc` argument filters the output to records whose GC
content is strictly above the given percentage:

```bash
python3 scripts/gc_content.py input/multi_seq.fasta --min-gc 50
```

GC content is reported as a percentage to two decimal places. Empty FASTA
records are skipped with a warning.
