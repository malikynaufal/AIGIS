#!/usr/bin/env python3
"""Standardize math formatting in the AIGIS vault for visual appeal."""
import os, re

FOLDER = r"C:\Obsidian\Brain Original\AIGIS"

def improve_visuals(text):
    # 1. Standardize Block Math: Ensure block math is on its own line with empty lines around it
    # Pattern matches $$ math $$ and ensures it's properly spaced.
    text = re.sub(r'([^\n])\n\s*\$\$\s*', r'\1\n\n$$\n', text)
    text = re.sub(r'\s*\$\$\s*\n([^\n])', r'\n$$\n\n\1', text)
    
    # 2. Fix inline math with leading/trailing spaces inside the delimiters
    # $ x $ -> $x$
    text = re.sub(r'\$\s+([^$]+?)\s+\$', r'$\1$', text)
    
    # 3. Standardize Headers: Ensure empty line before headers (except at start of file)
    text = re.sub(r'([^\n])\n(#+ )', r'\1\n\n\2', text)
    
    # 4. Standardize Lists: Ensure empty line before a list starts
    text = re.sub(r'([^\n])\n([*-] )', r'\1\n\n\2', text)
    
    # 5. Fix multiple consecutive empty lines
    text = re.sub(r'\n{3,}', r'\n\n', text)
    
    # 6. Ensure LaTeX math symbols like \dots, \cdot, \mu are consistent
    # (Optional, but helps with "visual appeal")
    # text = text.replace(r'...', r'\dots')
    
    return text

count = 0
for root, dirs, fnames in os.walk(FOLDER):
    if ".git" in root or "_Inbox" in root:
        continue
    for fn in fnames:
        if not fn.endswith(".md"):
            continue
        path = os.path.join(root, fn)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                original = f.read()
            
            updated = improve_visuals(original)
            
            if updated != original:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(updated)
                count += 1
        except Exception as e:
            print(f"Error on {path}: {e}")

print(f"Total files improved visually: {count}")
