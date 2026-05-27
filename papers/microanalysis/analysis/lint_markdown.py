#!/usr/bin/env python3
"""Markdown format-conformance sweep.

Fixes:
- Missing blank line before code fences
- Trailing whitespace on all lines
- Mixed tabs/spaces (convert all to spaces)
- Reports: inconsistent heading levels
"""
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

HERE = os.path.dirname(os.path.abspath(__file__))
MICRO = os.path.normpath(os.path.join(HERE, '..'))
DECISIONS = os.path.normpath(os.path.join(MICRO, 'decisions'))

def fix_file(path):
    """Apply linting fixes to a markdown file. Return (fixed, issues)."""
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    original = lines[:]
    issues = []

    # Pass 1: Remove trailing whitespace, convert tabs to spaces
    for i, line in enumerate(lines):
        if '\t' in line:
            lines[i] = line.replace('\t', '    ')  # 1 tab = 4 spaces
        if line.rstrip('\n') != line.rstrip('\n').rstrip():
            lines[i] = line.rstrip() + '\n'

    # Pass 2: Ensure blank line before code fences (unless at start)
    i = 0
    while i < len(lines):
        if lines[i].lstrip().startswith('```'):
            if i > 0 and lines[i-1].strip() != '':
                # Insert blank line before code fence
                lines.insert(i, '\n')
                i += 1
        i += 1

    # Check for inconsistent heading levels
    heading_level_changes = []
    last_level = None
    for i, line in enumerate(lines):
        m = re.match(r'^(#+) ', line)
        if m:
            level = len(m.group(1))
            if last_level is not None and abs(level - last_level) > 1:
                heading_level_changes.append(f"Line {i+1}: jumped from H{last_level} to H{level}")
            last_level = level

    if heading_level_changes:
        issues.extend(heading_level_changes)

    fixed = (lines != original)
    if fixed:
        with open(path, 'w', encoding='utf-8') as f:
            f.writelines(lines)

    return fixed, issues

def main():
    files_fixed = 0
    total_issues = []

    for dirpath, dirs, names in os.walk(MICRO):
        # Skip certain dirs
        dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', '.pytest_cache']]

        for name in sorted(names):
            if not name.endswith('.md'):
                continue
            path = os.path.join(dirpath, name)
            fixed, issues = fix_file(path)
            if fixed:
                rel_path = os.path.relpath(path, MICRO)
                print(f"  FIXED {rel_path}")
                files_fixed += 1
            if issues:
                for issue in issues:
                    total_issues.append((os.path.relpath(path, MICRO), issue))

    # Also check decisions/ if it exists
    if os.path.exists(DECISIONS):
        for name in sorted(os.listdir(DECISIONS)):
            if not name.endswith('.md'):
                continue
            path = os.path.join(DECISIONS, name)
            if not os.path.isfile(path):
                continue
            fixed, issues = fix_file(path)
            if fixed:
                rel_path = os.path.relpath(path, MICRO)
                print(f"  FIXED {rel_path}")
                files_fixed += 1
            if issues:
                for issue in issues:
                    total_issues.append((os.path.relpath(path, MICRO), issue))

    print()
    if files_fixed > 0:
        print(f"✓ Fixed {files_fixed} file(s)")
    else:
        print("✓ All files already conform")

    if total_issues:
        print(f"\nNotes (not auto-fixable):")
        for path, issue in total_issues:
            print(f"  {path}: {issue}")

    return 0

if __name__ == '__main__':
    sys.exit(main())
