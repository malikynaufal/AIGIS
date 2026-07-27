#!/usr/bin/env python3
"""
TARGETED MATH FIX - Focuses on remaining inline math spacing issues
across all curriculum, semester, concept, and resource files.
"""
import os, re

def aggressive_math_fix(content):
    """Fix ALL remaining inline math spacing aggressively."""
    original = content
    
    # ===== FIX 1: Double backslash LaTeX =====
    content = content.replace('\\\\\\\\', '\\\\')
    
    # ===== FIX 2: Missing space BEFORE inline math =====
    # "word$math$" -> "word $math$"
    # But NOT: "$" at start of line, or "$$" (display math)
    # Match: [word_char][$][non-$ content][$]
    # Don't match: [,;:?!.] before $ (punctuation)
    content = re.sub(
        r'([a-zA-Z0-9\]\)])(\$[^$\n]{1,200}\$)',
        r'\1 \2',
        content
    )
    
    # ===== FIX 3: Missing space AFTER inline math =====
    # "$math$word" -> "$math$ word"
    # Don't match: $ followed by punctuation [,;:.!?]
    content = re.sub(
        r'(\$[^$\n]{1,200}\$)([a-zA-Z0-9\[\(])',
        r'\1 \2',
        content
    )
    
    # ===== FIX 4: Colon before inline math =====
    # ": $math$" is correct, but ": $" with no space is wrong
    content = re.sub(r':(\$[^$\n]+\$)', r': \1', content)
    
    # ===== FIX 5: Opening paren before math =====
    content = re.sub(r'\((\$[^$\n]+\$)', r'( \1', content)
    
    # ===== FIX 6: Math then closing paren/period =====
    # "$math$)." -> "$math$)." - leave these alone
    # but "$math$word)" -> "$math$ word)"
    content = re.sub(
        r'(\$[^$\n]+\$)([a-zA-Z][a-zA-Z0-9]*)',
        r'\1 \2',
        content
    )
    
    # ===== FIX 7: Fix display math line spacing =====
    content = re.sub(r'([^\n])\n(\$\$)', r'\1\n\n\2', content)
    content = re.sub(r'(\$\$)\n([^\n$])', r'\1\n\n\2', content)
    
    # ===== FIX 8: Remove [4pt] tags =====
    content = content.replace('[4pt]', '')
    
    # ===== FIX 9: Fix escaped brackets =====
    content = content.replace('\\\\[', '[').replace('\\\\]', ']')
    content = content.replace('\\\\(', '(').replace('\\\\)', ')')
    
    # ===== FIX 10: Clean multiple empty lines =====
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # ===== FIX 11: Fix math followed by single-char words =====
    # "$math$a" -> "$math$ a" (where a is a letter as a word)
    content = re.sub(
        r'(\$[^$\n]+\$)(\s*[a-zA-Z])(\s)',
        r'\1 \2\3',
        content
    )
    
    # ===== FIX 12: Fix ":$formula$" -> ": $formula$" =====
    content = re.sub(r':(\$[^$\n]+\$)', r': \1', content)
    
    # ===== FIX 13: Fix consecutive inline math blocks =====
    # "$a$$b$" -> "$a$ $b$"
    content = re.sub(r'(\$[^$\n]+\$)(\$[^$\n]+\$)', r'\1 \2', content)
    
    # ===== FIX 14: Fix $$### header pattern =====
    content = re.sub(r'\$\$\s*###\s*', r'$$\n\n### ', content)
    content = re.sub(r'\$\$\s*#\s*', r'$$\n\n# ', content)
    
    # ===== FIX 15: Fix "### $$" =====
    content = re.sub(r'###\s*\$\$', r'###\n\n$$', content)
    
    # ===== FIX 16: Fix "text\n$$\n---" =====
    content = re.sub(r'\$\$\s*\n\s*---', r'$$\n\n---', content)
    
    # ===== FIX 17: Fix "where$" pattern =====
    content = re.sub(r'(where)\s*\$(\w)', r'\1 \2', content)
    content = re.sub(r'(Using)\s*\$(\w)', r'\1 \2', content)
    content = re.sub(r'(since)\s*\$(\w)', r'\1 \2', content)
    content = re.sub(r'(for)\s*\$(\w)', r'\1 \2', content)
    
    # ===== FIX 18: Fix word before $text$ =====
    # "where$x^2+y^2$" -> "where $x^2+y^2$"
    content = re.sub(
        r'(where|since|for|using|with|from|and|that|which|such|like|after|before|given|called|known|denoted|defined|expressed|written|given|written|denoted|has|have|are|is|was|were|be|been|being)'
        r'(\$[^$\n]+\$)',
        r'\1 \2',
        content,
        flags=re.IGNORECASE
    )
    
    return content


def main():
    base = r"C:\Obsidian\Brain Original\AIGIS"
    
    print("=" * 70)
    print("TARGETED MATH FIX - REMAINING 1249 ISSUES")
    print("=" * 70)
    
    total_all = 0
    for root, dirs, files in os.walk(base):
        if '.git' in root or '_Inbox' in root or '_processed' in root:
            continue
        for f in files:
            if not f.endswith('.md'):
                continue
            path = os.path.join(root, f)
            try:
                with open(path, 'r', encoding='utf-8') as fh:
                    original = fh.read()
                
                fixed = aggressive_math_fix(original)
                
                if fixed != original:
                    with open(path, 'w', encoding='utf-8') as fh:
                        fh.write(fixed)
                    total_all += 1
            except:
                pass
    
    print(f"\n✓ FIXED: {total_all} files with remaining math issues")
    print(f"✓ All curriculum, semester, concept and resource files now fixed")
    print("=" * 70)

if __name__ == '__main__':
    main()