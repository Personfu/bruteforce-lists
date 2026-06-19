#!/usr/bin/env python3
"""Audit wordlists for authorized password-policy education.

This does not attempt authentication, spraying, cracking, or network access. It
summarizes local lists so defenders and learners can understand password hygiene
patterns before writing policy or training material.
"""
from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path


def bucket_length(length: int) -> str:
    if length < 8:
        return '<8'
    if length <= 11:
        return '8-11'
    if length <= 15:
        return '12-15'
    return '16+'


def classify(word: str) -> list[str]:
    labels: list[str] = []
    if any(c.islower() for c in word) and any(c.isupper() for c in word):
        labels.append('mixed-case')
    if any(c.isdigit() for c in word):
        labels.append('has-digit')
    if any(not c.isalnum() for c in word):
        labels.append('has-symbol')
    if word.lower() in {'password', 'admin', 'welcome', 'qwerty', 'letmein'}:
        labels.append('common-bad-pattern')
    if not labels:
        labels.append('plain')
    return labels


def audit(path: Path) -> str:
    words = [line.strip() for line in path.read_text(encoding='utf-8', errors='ignore').splitlines() if line.strip()]
    unique = set(words)
    length_counts = Counter(bucket_length(len(word)) for word in words)
    label_counts = Counter(label for word in words for label in classify(word))

    lines = [
        '# Wordlist Audit',
        '',
        f'- Source file: `{path}`',
        f'- Total entries: {len(words):,}',
        f'- Unique entries: {len(unique):,}',
        f'- Duplicates: {len(words) - len(unique):,}',
        '',
        '## Length Distribution',
        '',
    ]
    for label in ['<8', '8-11', '12-15', '16+']:
        lines.append(f'- `{label}`: {length_counts[label]:,}')

    lines.extend(['', '## Pattern Distribution', ''])
    for label, count in label_counts.most_common():
        lines.append(f'- `{label}`: {count:,}')

    lines.extend([
        '',
        '## Safety Boundary',
        'Use this report for education, password-policy design, and authorized defensive audits only. Do not use it for credential stuffing, spraying, or unauthorized authentication attempts.',
        '',
    ])
    return '\n'.join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description='Create a defensive wordlist audit report.')
    parser.add_argument('wordlist', type=Path)
    parser.add_argument('-o', '--output', type=Path)
    args = parser.parse_args()
    report = audit(args.wordlist)
    if args.output:
        args.output.write_text(report, encoding='utf-8')
        print(f'wrote {args.output}')
    else:
        print(report)


if __name__ == '__main__':
    main()
