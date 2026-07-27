#!/usr/bin/env python3
"""Fix math formatting in curriculum, resources, and semester files."""
import os, re

def fix_math(content):
    """Fix common math formatting issues."""
    # Fix double-backslash LaTeX commands (replace \\ with \)
    content = content.replace('\\\\\\\\', '\\\\')
    
    # Fix inline math spacing: "word$formula" -> "word $formula"
    content = re.sub(r'([a-zA-Z0-9\)\]}])(\$[^$]+\$)', r'\1 \2', content)
    content = re.sub(r'(\$[^$]+\$)([a-zA-Z0-9\[({])', r'\1 \2', content)
    
    # Fix display math spacing
    content = re.sub(r'([^\n])\n(\$\$)', r'\1\n\n\2', content)
    content = re.sub(r'(\$\$)\n([^\n$])', r'\1\n\n\2', content)
    
    # Remove [4pt] alignment tags
    content = content.replace('[4pt]', '')
    
    # Fix escaped brackets
    content = content.replace('\\\\[', '[')
    content = content.replace('\\\\]', ']')
    
    return content

def process(path):
    """Process a single file, return True if modified."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            c = f.read()
        new_c = fix_math(c)
        if new_c != c:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_c)
            return True
    except Exception as e:
        print(f"  Error {path}: {e}")
    return False

def main():
    root_path = r"C:\Obsidian\Brain Original\AIGIS"
    targets = ['Curriculum', 'Semester', 'Resources', '_Study Packs', 'Concepts']
    count = 0
    
    print("=" * 70)
    print("CURRICULUM/RESOURCES/SEMESTER MATH FIX")
    print("=" * 70)
    
    for target in targets:
        target_fixed = 0
        for root, _, files in os.walk(root_path):
            if '.git' in root:
                continue
            if target not in root:
                continue
            for f in files:
                if f.endswith('.md'):
                    path = os.path.join(root, f)
                    if process(path):
                        target_fixed += 1
                        count += 1
        
        if target_fixed > 0:
            print(f"  {target}s: {target_fixed} files fixed")
    
    print(f"\nTotal files fixed: {count}")
    print("=" * 70)

if __name__ == '__main__':
    main()