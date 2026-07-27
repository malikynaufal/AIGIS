#!/usr/bin/env python3
"""
FIX STUDY PACKS - Aggressive fix for all remaining math issues.
"""
import os, re

def fix_study_pack(content):
    """Fix all math formatting issues in study packs."""
    original = content
    
    # 1. Fix double-backslash LaTeX commands
    content = content.replace('\\\\\\\\', '\\\\')
    
    # 2. Fix escaped brackets in LaTeX
    content = content.replace('\\\\[', '[').replace('\\\\]', ']')
    content = content.replace('\\\\(', '(').replace('\\\\)', ')')
    
    # 3. Fix inline math spacing BEFORE: "word$formula" -> "word $formula"
    # Don't match if preceded by punctuation
    content = re.sub(r'([a-zA-Z0-9\]\)])(\$[^$\n]{1,200}\$)', r'\1 \2', content)
    
    # 4. Fix inline math spacing AFTER: "$formula$word" -> "$formula$ word"
    content = re.sub(r'(\$[^$\n]{1,200}\$)([a-zA-Z0-9\[\(])', r'\1 \2', content)
    
    # 5. Fix display math line spacing
    content = re.sub(r'([^\n])\n(\$\$)', r'\1\n\n\2', content)
    content = re.sub(r'(\$\$)\n([^\n$])', r'\1\n\n\2', content)
    
    # 6. Remove [4pt] tags
    content = content.replace('[4pt]', '')
    
    # 7. Fix "$$###" pattern
    content = re.sub(r'\$\$\s*###\s*', r'$$\n\n### ', content)
    content = re.sub(r'\$\$\s*#\s*', r'$$\n\n# ', content)
    
    # 8. Fix "###$$" pattern
    content = re.sub(r'###\s*\$\$', r'###\n\n$$', content)
    
    # 9. Fix consecutive inline math: "$a$$b$" -> "$a$ $b$"
    content = re.sub(r'(\$[^$\n]+\$)(\$[^$\n]+\$)', r'\1 \2', content)
    
    # 10. Fix "$$...$$word" -> "$$...$$\n\nword"
    content = re.sub(r'(\$\$[^$]+\$\$)\s*([a-zA-Z]{2,})', r'\1\n\n\2', content)
    
    # 11. Fix "word$$...$$" -> "word\n\n$$...$$"
    content = re.sub(r'([a-zA-Z]{2,})\s*(\$\$)', r'\1\n\n\2', content)
    
    # 12. Clean up excessive blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # 13. Fix "where$" -> "where $"
    content = re.sub(r'(where)\s*\$(\w)', r'\1 \2', content)
    content = re.sub(r'(Using)\s*\$(\w)', r'\1 \2', content)
    content = re.sub(r'(since)\s*\$(\w)', r'\1 \2', content)
    content = re.sub(r'(for)\s*\$(\w)', r'\1 \2', content)
    
    # 14. Fix ":$formula$" -> ": $formula$"
    content = re.sub(r':(\$[^$\n]+\$)', r': \1', content)
    
    # 15. Fix "$$---" patterns
    content = re.sub(r'\$\$\s*---', r'$$\n\n---', content)
    
    return content

def process_study_packs(base_path, subjects):
    """Process all study packs in the given subjects."""
    total_fixed = 0
    
    for subject in subjects:
        study_pack_path = os.path.join(base_path, subject, '_Study Packs')
        if not os.path.exists(study_pack_path):
            continue
        
        print(f"\nProcessing {subject} Study Packs:")
        subject_fixed = 0
        
        for root, dirs, files in os.walk(study_pack_path):
            if '.git' in root:
                continue
            for f in files:
                if not f.endswith('.md'):
                    continue
                path = os.path.join(root, f)
                try:
                    with open(path, 'r', encoding='utf-8') as fh:
                        original = fh.read()
                    
                    fixed = fix_study_pack(original)
                    
                    if fixed != original:
                        with open(path, 'w', encoding='utf-8') as fh:
                            fh.write(fixed)
                        subject_fixed += 1
                        print(f"  ✓ Fixed: {f}")
                except Exception as e:
                    print(f"  ✗ Error: {f} - {e}")
        
        total_fixed += subject_fixed
        print(f"  Total: {subject_fixed} files fixed")
    
    return total_fixed

def main():
    base = r"C:\Obsidian\Brain Original\AIGIS"
    
    print("=" * 70)
    print("STUDY PACKS MATH FIX")
    print("=" * 70)
    
    total = process_study_packs(base, ['Geodesy', 'Mathematics', 'Physics'])
    
    print(f"\n{'=' * 70}")
    print(f"GRAND TOTAL: {total} study pack files fixed")
    print(f"{'=' * 70}")

if __name__ == '__main__':
    main()