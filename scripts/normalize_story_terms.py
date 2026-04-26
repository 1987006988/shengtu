from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TARGETS = [
    ROOT / "worldbible" / "08_story" / "59_act1_minimal_main_quest_pilot.md",
    ROOT / "worldbible" / "08_story" / "60_act1_minimal_journal_pilot.md",
    ROOT / "worldbible" / "08_story" / "61_act1_minimal_codex_pilot.md",
]
DEFAULT_REPLACEMENTS = {
    "医棚": "照护棚",
    "病床": "承接位",
    "粮药": "基础补给",
}


@dataclass
class FileResult:
    path: Path
    replacements: int
    changed: bool


def resolve_markdown_files(targets: list[Path]) -> list[Path]:
    files: list[Path] = []
    seen: set[Path] = set()

    for target in targets:
        resolved = target.resolve()
        if not resolved.exists():
            raise FileNotFoundError(f"Target does not exist: {resolved}")

        if resolved.is_file():
            candidates = [resolved] if resolved.suffix.lower() == ".md" else []
        else:
            candidates = sorted(resolved.rglob("*.md"))

        for candidate in candidates:
            if candidate not in seen:
                seen.add(candidate)
                files.append(candidate)

    return files


def apply_replacements(text: str, replacements: dict[str, str]) -> tuple[str, int]:
    updated = text
    count = 0

    for old, new in replacements.items():
        hits = updated.count(old)
        if hits:
            updated = updated.replace(old, new)
            count += hits

    return updated, count


def process_file(path: Path, replacements: dict[str, str], dry_run: bool) -> FileResult:
    original = path.read_text(encoding="utf-8")
    updated, count = apply_replacements(original, replacements)
    changed = updated != original

    if changed and not dry_run:
        path.write_text(updated, encoding="utf-8", newline="")

    return FileResult(path=path, replacements=count, changed=changed)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Normalize selected story terms in the target markdown files."
    )
    parser.add_argument(
        "targets",
        nargs="*",
        type=Path,
        default=DEFAULT_TARGETS,
        help="Markdown files or directories to process. Defaults to the three Act 1 pilot targets.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show which files would change without writing them.",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    files = resolve_markdown_files([path if path.is_absolute() else ROOT / path for path in args.targets])
    results = [process_file(path, DEFAULT_REPLACEMENTS, args.dry_run) for path in files]

    changed_files = [result for result in results if result.changed]
    total_replacements = sum(result.replacements for result in results)

    mode = "DRY-RUN" if args.dry_run else "APPLY"
    print(f"[{mode}] scanned={len(results)} changed={len(changed_files)} replacements={total_replacements}")

    for result in changed_files:
        relative = result.path.relative_to(ROOT)
        print(f"- {relative} ({result.replacements} replacements)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
