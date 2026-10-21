"""Calculate GC content for each record in a FASTA file."""

import argparse
import sys


def fasta_records(path):
    """Yield (header, sequence) pairs from a FASTA file."""
    header = None
    sequence = []

    with open(path) as fasta_file:
        for line in fasta_file:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if header is not None:
                    yield header, "".join(sequence)
                header = line[1:]
                sequence = []
            elif header is not None:
                sequence.append("".join(line.split()))

    if header is not None:
        yield header, "".join(sequence)


def main():
    parser = argparse.ArgumentParser(
        description="Print GC content for each record in a FASTA file."
    )
    parser.add_argument("fasta", help="path to the FASTA file")
    parser.add_argument(
        "--min-gc",
        type=float,
        metavar="FLOAT",
        help="only print records with GC content strictly above this percentage",
    )
    args = parser.parse_args()
    if args.min_gc is not None and not 0 <= args.min_gc <= 100:
        parser.error("--min-gc must be between 0 and 100")

    for header, sequence in fasta_records(args.fasta):
        if not sequence:
            print(f"Warning: skipping empty sequence for {header!r}", file=sys.stderr)
            continue
        sequence = sequence.upper()
        gc_content = 100 * (sequence.count("G") + sequence.count("C")) / len(sequence)
        if args.min_gc is not None and gc_content <= args.min_gc:
            continue
        print(f">{header}\t{gc_content:.3f}%")


if __name__ == "__main__":
    main()
