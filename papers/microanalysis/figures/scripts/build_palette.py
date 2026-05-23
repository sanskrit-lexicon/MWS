#!/usr/bin/env python3
"""Generate palette.css, mermaid-theme.json, palette.py from palette-tokens.json."""
import json
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

HERE = os.path.dirname(os.path.abspath(__file__))
FIG_DIR = os.path.normpath(os.path.join(HERE, '..'))
TOKENS_PATH = os.path.join(FIG_DIR, 'palette-tokens.json')


def load_tokens():
    with open(TOKENS_PATH, encoding='utf-8') as f:
        return json.load(f)


def write_css(tokens, out_path):
    """Emit palette.css with CSS custom properties."""
    lines = [
        '/* MW1899 microanalysis palette',
        f" *  Generated from palette-tokens.json v{tokens['_meta']['version']}",
        f" *  Last updated {tokens['_meta']['last-updated']}",
        ' *  DO NOT EDIT — regenerate via figures/scripts/build_palette.py',
        ' */',
        ':root {',
    ]
    for group_name, group in tokens.items():
        if group_name == '_meta':
            continue
        lines.append(f'  /* {group_name} */')
        for key, value in group.items():
            css_name = f'--mw-{group_name}-{key}'.replace('_', '-')
            lines.append(f'  {css_name}: {value};')
    lines.append('}')
    lines.append('')
    lines.append(f"/* Font: {tokens['_meta']['font-family']} */")
    lines.append('body, .mw-figure { font-family: "Noto Sans", "DejaVu Sans", sans-serif; }')
    with open(out_path, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines))
    print(f"  wrote {os.path.basename(out_path)}")


def write_mermaid_theme(tokens, out_path):
    """Emit mermaid-theme.json with Mermaid theme variables."""
    ce = tokens['chart-element']
    at = tokens['article-type']
    theme = {
        '_meta': {
            'description': 'Mermaid theme variables for MW1899 microanalysis figures',
            'source': 'figures/palette-tokens.json',
            'last-updated': tokens['_meta']['last-updated'],
        },
        'themeVariables': {
            'background': ce['background'],
            'primaryColor': at['noun-m'],
            'primaryTextColor': ce['text'],
            'primaryBorderColor': ce['axis'],
            'lineColor': ce['axis'],
            'secondaryColor': at['compound'],
            'tertiaryColor': at['continuation'],
            'fontFamily': '"Noto Sans", "DejaVu Sans", sans-serif',
            'fontSize': '14px',
            'noteBkgColor': ce['highlight'],
            'noteTextColor': ce['text'],
            'noteBorderColor': ce['axis'],
        }
    }
    with open(out_path, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(theme, f, indent=2, ensure_ascii=False)
        f.write('\n')
    print(f"  wrote {os.path.basename(out_path)}")


def write_python_module(tokens, out_path):
    """Emit palette.py — importable as a Python module for matplotlib renderers."""
    lines = [
        '"""MW1899 microanalysis palette — Python module.',
        '',
        'Generated from palette-tokens.json.',
        f"Last updated: {tokens['_meta']['last-updated']}",
        '"""',
        '',
        '# Article-type colours',
        'ARTICLE_TYPE = {',
    ]
    for key, value in tokens['article-type'].items():
        lines.append(f"    {key.replace('-', '_')!r}: {value!r},")
    lines.append('}')
    lines.append('')
    lines.append('# Semantic-block colours')
    lines.append('SEMANTIC_BLOCK = {')
    for key, value in tokens['semantic-block'].items():
        lines.append(f"    {key.replace('-', '_')!r}: {value!r},")
    lines.append('}')
    lines.append('')
    lines.append('# Fullness-tier colours')
    lines.append('FULLNESS_TIER = {')
    for key, value in tokens['fullness-tier'].items():
        lines.append(f"    {key.replace('-', '_')!r}: {value!r},")
    lines.append('}')
    lines.append('')
    lines.append('# Per-dictionary colours')
    lines.append('DICTIONARY = {')
    for key, value in tokens['dictionary'].items():
        lines.append(f"    {key!r}: {value!r},")
    lines.append('}')
    lines.append('')
    lines.append('# Chart elements')
    lines.append('CHART = {')
    for key, value in tokens['chart-element'].items():
        lines.append(f"    {key.replace('-', '_')!r}: {value!r},")
    lines.append('}')
    lines.append('')
    lines.append('# Footer style')
    lines.append('FOOTER = {')
    for key, value in tokens['footer'].items():
        lines.append(f"    {key.replace('-', '_')!r}: {value!r},")
    lines.append('}')
    lines.append('')
    lines.append('# Fonts')
    lines.append(f"FONT_FAMILY = {tokens['_meta']['font-family']!r}")
    lines.append(f"FONT_FAMILY_FALLBACK = {tokens['_meta']['font-family-fallback']!r}")
    lines.append('')
    with open(out_path, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines))
    print(f"  wrote {os.path.basename(out_path)}")


def main():
    tokens = load_tokens()
    print(f"Building palette artifacts from {os.path.basename(TOKENS_PATH)}...")
    write_css(tokens, os.path.join(FIG_DIR, 'palette.css'))
    write_mermaid_theme(tokens, os.path.join(FIG_DIR, 'mermaid-theme.json'))
    write_python_module(tokens, os.path.join(FIG_DIR, 'palette.py'))
    print("done.")


if __name__ == '__main__':
    main()
