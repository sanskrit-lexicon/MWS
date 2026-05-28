#!/usr/bin/env python3
"""Add version-stamp footers to SVG figures.

Format: "Source: CDSL mw.txt 2026-05-23 · CC-BY-SA-4.0 · build {SHA}"
Injected as <text> element at bottom-right per Decision 26.
"""
import os
import sys
import re
import subprocess

sys.stdout.reconfigure(encoding='utf-8')

HERE = os.path.dirname(os.path.abspath(__file__))
FIGURES = os.path.normpath(os.path.join(HERE, '..', 'figures'))

def get_short_sha():
    """Get current HEAD short SHA."""
    try:
        result = subprocess.run(
            ['git', 'rev-parse', '--short', 'HEAD'],
            capture_output=True,
            text=True,
            cwd=os.path.dirname(FIGURES)
        )
        return result.stdout.strip()
    except Exception:
        return 'unknown'

def extract_viewbox(svg_path):
    """Extract viewBox from SVG file. Returns (width, height) or None."""
    try:
        with open(svg_path, 'r', encoding='utf-8') as f:
            content = f.read()
        m = re.search(r'viewBox=["\']([0-9.]+)\s+([0-9.]+)\s+([0-9.]+)\s+([0-9.]+)["\']', content)
        if m:
            x, y, w, h = float(m.group(1)), float(m.group(2)), float(m.group(3)), float(m.group(4))
            return (x + w, y + h, w, h)
    except Exception:
        pass
    return None

def footer_element(x_max, y_max, text):
    """Create SVG <text> element for footer at bottom-right."""
    # Position text 10px from right edge, 15px from bottom
    x = x_max - 10
    y = y_max - 5
    return (f'  <text x="{x}" y="{y}" text-anchor="end" font-size="10" '
            f'fill="#666" font-family="Noto Sans">{text}</text>\n')

def add_footer_to_svg(svg_path, text):
    """Add footer to SVG file if not already present."""
    with open(svg_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if footer already exists (look for "Source: CDSL")
    if 'Source: CDSL' in content:
        return False

    # Extract viewBox
    dims = extract_viewbox(svg_path)
    if not dims:
        print(f"  SKIP {os.path.basename(svg_path)} — could not extract viewBox")
        return False

    x_max, y_max, w, h = dims
    footer_elem = footer_element(x_max, y_max, text)

    # Find closing </svg> tag and insert before it
    new_content = content.replace('</svg>', footer_elem + '</svg>')

    with open(svg_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True

def main():
    short_sha = get_short_sha()
    footer_text = f"Source: CDSL mw.txt 2026-05-23 · CC-BY-SA-4.0 · build {short_sha}"

    print(f"Adding footers with build SHA: {short_sha}\n")

    if not os.path.exists(FIGURES):
        print(f"ERROR: {FIGURES} not found")
        return 1

    modified = 0
    for root, dirs, files in os.walk(FIGURES):
        for name in sorted(files):
            if not name.endswith('.svg'):
                continue
            path = os.path.join(root, name)
            if add_footer_to_svg(path, footer_text):
                rel_path = os.path.relpath(path, FIGURES)
                print(f"  ADDED {rel_path}")
                modified += 1

    print()
    if modified > 0:
        print(f"✓ Modified {modified} SVG file(s)")
    else:
        print("✓ All SVG files already have footers (or none found)")

    return 0

if __name__ == '__main__':
    sys.exit(main())
