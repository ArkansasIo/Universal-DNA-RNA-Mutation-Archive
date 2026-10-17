"""Command-line interface for validation, comparison, and archive inspection."""
from __future__ import annotations
import argparse, json
from .core import validate_sequence, compare_equal_length
from .io import read_variants_json

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="mutation-archive")
    sub = p.add_subparsers(dest="command", required=True)
    v = sub.add_parser("validate-sequence"); v.add_argument("molecule"); v.add_argument("sequence")
    c = sub.add_parser("compare"); c.add_argument("molecule"); c.add_argument("reference"); c.add_argument("alternate")
    s = sub.add_parser("stats"); s.add_argument("file")
    return p

def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "validate-sequence":
        ok, message = validate_sequence(args.molecule, args.sequence)
        print(json.dumps({"valid": ok, "message": message})); return 0 if ok else 2
    if args.command == "compare":
        ok1, m1 = validate_sequence(args.molecule, args.reference); ok2, m2 = validate_sequence(args.molecule, args.alternate)
        if not ok1 or not ok2: print(json.dumps({"error": m1 if not ok1 else m2})); return 2
        print(json.dumps(compare_equal_length(args.reference, args.alternate), indent=2)); return 0
    variants = read_variants_json(args.file)
    print(json.dumps({"total": len(variants)}, indent=2)); return 0

if __name__ == "__main__": raise SystemExit(main())
