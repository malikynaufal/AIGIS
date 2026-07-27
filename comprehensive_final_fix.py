#!/usr/bin/env python3
"""Final comprehensive fix for AIGIS math expressions."""
import os, re

def comprehensive_fix(content):
    original = content
    
    # 1. Fix double-backslash LaTeX
    content = content.replace('\\\\\\\\', '\\\\')
    
    # 2. Fix inline math spacing (BEFORE): "word$formula$" -> "word $formula$"
    # Only for single $ not $$
    content = re.sub(r'([a-zA-Z0-9)\]}])(\$[^$]{1,100}\$)', r'\1 \2', content)
    
    # 3. Fix inline math spacing (AFTER): "$formula$word" -> "$formula$ word"
    content = re.sub(r'(\$[^$]{1,100}\$)([a-zA-Z0-9\[({])', r'\1 \2', content)
    
    # 4. Fix display math line breaks
    content = re.sub(r'([^\n])\n(\$\$)', r'\1\n\n\2', content)
    content = re.sub(r'(\$\$)\n([^\n$])', r'\1\n\n\2', content)
    
    # 5. Remove [4pt] tags
    content = content.replace('[4pt]', '')
    
    # 6. Fix escaped brackets
    content = content.replace('\\\\[', '[').replace('\\\\]', ']')
    
    # 7. Fix ": $" -> ": $" (colon spacing)
    content = re.sub(r':(\$[^$]+\$)', r': \1', content)
    
    # 8. Fix display math with text on same line: "$$text$$" -> separate
    content = re.sub(r'(\$\$[^$]+\$\$)\s*([a-zA-Z]{2,})', r'\1\n\n\2', content)
    
    # 9. Fix consecutive inline math: "$a$$b$" -> "$a$ $b$"
    content = re.sub(r'(\$[^$]+\$)(\$[^$]+\$)', r'\1 \2', content)
    
    # 10. Clean up multiple blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    return content

def process_folder(folder):
    fixed_count = 0
    for root, dirs, files in os.walk(folder):
        if '.git' in root or '_Inbox' in root:
            continue
        for f in files:
            if not f.endswith('.md'):
                continue
            path = os.path.join(root, f)
            try:
                with open(path, 'r', encoding='utf-8') as fh:
                    original = fh.read()
                
                fixed = comprehensive_fix(original)
                
                if fixed != original:
                    with open(path, 'w', encoding='utf-8') as fh:
                        fh.write(fixed)
                    fixed_count += 1
            except Exception:
                pass
    
    return fixed_count

def main():
    base = r"C:\Obsidian\Brain Original\AIGIS"
    
    folders_to_process = [
        (os.path.join(base, 'Geodesy', 'Curriculum'), 'Geodesy Curriculum'),
        (os.path.join(base, 'Geodesy', 'Resources'), 'Geodesy Resources'),
        (os.path.join(base, 'Mathematics', 'Curriculum'), 'Mathematics Curriculum'),
        (os.path.join(base, 'Mathematics', 'Resources'), 'Mathematics Resources'),
        (os.path.join(base, 'Physics', 'Curriculum'), 'Physics Curriculum'),
        (os.path.join(base, 'Physics', 'Resources'), 'Physics Resources'),
    ]
    
    print("=" * 70)
    print("COMPREHENSIVE CURRICULUM / RESOURCES MATH FIX")
    print("=" * 70)
    
    total = 0
    for folder, label in folders_to_process:
        if os.path.exists(folder):
            n = process_folder(folder)
            total += n
            print(f"  {label}: {n} files fixed")
    
    # Also fix Semester files
    semester_fixed = process_folder(os.path.join(base, 'Geodesy'))
    semester_fixed += process_folder(os.path.join(base, 'Mathematics'))
    semester_fixed += process_folder(os.path.join(base, 'Physics'))
    total += semester_fixed
    print(f"  Semester/Concept files: additional {semester_fixed} files fixed")
    
    print(f"\nTotal files fixed: {total}")
    print("=" * 70)

if __name__ == '__main__':
    main()