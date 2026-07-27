#!/usr/bin/env python3
import os, re
path = r"C:\Obsidian\Brain Original\AIGIS\Physics\_Study Packs\Electromagnetism.md"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()
original = content
# Fix double backslashes
content = content.replace('\\\\\\\\frac', '\\\\frac')
content = content.replace('\\\\\\\\sum', '\\\\sum')
content = content.replace('\\\\\\\\int', '\\\\int')
content = content.replace('\\\\\\\\nabla', '\\\\nabla')
content = content.replace('\\\\\\\\begin', '\\\\begin')
content = content.replace('\\\\\\\\end', '\\\\end')
content = content.replace('\\\\\\\\cdot', '\\\\cdot')
content = content.replace('\\\\\\\\times', '\\\\times')
content = content.replace('\\\\\\\\vec', '\\\\vec')
content = content.replace('\\\\\\\\perp', '\\\\perp')
content = content.replace('\\\\\\\\sigma', '\\\\sigma')
content = content.replace('\\\\\\\\phi', '\\\\phi')
content = content.replace('\\\\\\\\omega', '\\\\omega')
content = content.replace('\\\\\\\\epsilon', '\\\\epsilon')
content = content.replace('\\\\\\\\lambda', '\\\\lambda')
content = content.replace('\\\\\\\\mu', '\\\\mu')
content = content.replace('\\\\\\\\pi', '\\\\pi')
content = content.replace('\\\\\\\\partial', '\\\\partial')
content = content.replace('\\\\\\\\lim', '\\\\lim')
content = content.replace('\\\\\\\\dfrac', '\\\\dfrac')
content = content.replace('\\\\\\\\tfrac', '\\\\tfrac')
content = content.replace('\\\\\\\\cfrac', '\\\\cfrac')
content = content.replace('\\\\\\\\sqrt', '\\\\sqrt')
content = content.replace('\\\\\\\\angle', '\\\\angle')
content = content.replace('\\\\\\\\degree', '\\\\degree')
content = content.replace('\\\\\\\\parallel', '\\\\parallel')
content = content.replace('\\\\\\\\perp', '\\\\perp')
content = content.replace('\\\\\\\\approx', '\\\\approx')
content = content.replace('\\\\\\\\simeq', '\\\\simeq')
content = content.replace('\\\\\\\\sim', '\\\\sim')
content = content.replace('\\\\\\\\equiv', '\\\\equiv')
content = content.replace('\\\\\\\\cong', '\\\\cong')
content = content.replace('\\\\\\\\propto', '\\\\propto')
# Also fix remaining double
content = re.sub(r'\\\\\\\\[a-zA-Z]', lambda m: '\\\\' + m.group(0)[-1], content)
# Fix escaped brackets
content = content.replace('\\\\[', '[')
content = content.replace('\\\\]', ']')
content = content.replace('\\\\(', '(')
content = content.replace('\\\\)', ')')
# Fix **###** -> ###
content = re.sub(r'\*\*###\s*([^$]+)\*\*', r'### \1', content)
# Fix line 25 "$$ ### Integral Form $$"
content = re.sub(r'\$\$\s*###\s*Integral Form\s*\$\$', r'\n\n### Integral Form\n\n$$', content)
# Fix "$$... $$---"
content = re.sub(r'(\$\$\s*[^$]+\$\$)\s*---', r'\1\n\n---', content)
# Fix "Using$..." -> "Using ..."
content = re.sub(r'(Using)\s*\$(\w)', r'\1 \2', content)
content = re.sub(r'\(since\s*\$(\w)', r'(since \1', content)
# Fix spacing between words and inline math
content = re.sub(r'(Wave speed:|Total power:|Intensity:|Energy density:|Poynting vector:)(\s*\$)', r'\1 \2', content)
content = re.sub(r'([a-zA-Z])\s*\$(\w)', r'\1 \2', content)
content = re.sub(r'(\$[^$]+\$)([a-zA-Z])', r'\1 \2', content)
# Fix "For non-rel..." after math
content = re.sub(r'(\$[^$]+\$)(For\s+[A-Za-z])', r'\1 \2', content)
# Fix "where$" pattern
content = re.sub(r'(where)\s*\$(\w)', r'\1 \2', content)
# Clean excessive blank lines
content = re.sub(r'\n\n\n+', '\n\n', content)
# Fix $$ followed by text without newline
content = re.sub(r'(\$\$)\s*(\w)', r'\1\n\n\2', content)
# Fix text followed by $$ without newline
content = re.sub(r'(\w)\s*(\$\$)', r'\1\n\n\2', content)
# Final cleanup
content = re.sub(r'\n\n\n+', '\n\n', content)
if content != original:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Fixed. Original={len(original)} chars, Fixed={len(content)} chars")
else:
    print("No changes needed.")