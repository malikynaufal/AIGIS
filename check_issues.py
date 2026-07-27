#!/usr/bin/env python3
"""Quick check for remaining math issues."""
import os, re

def check_remaining():
    root = r'C:\Obsidian\Brain Original\AIGIS'
    issues = []
    
    for root_dir, dirs, files in os.walk(root):
        if '.git' in root_dir or '_Inbox' in root_dir:
            continue
        for f in files:
            if not f.endswith('.md'):
                continue
            path = os.path.join(root_dir, f)
            try:
                with open(path, 'r', encoding='utf-8') as fh:
                    content = fh.read()
                
                for i, line in enumerate(content.split('\n'), 1):
                    if '[4pt]' in line:
                        issues.append((path, i, 'Has [4pt] tag'))
                    if re.search(r'[a-zA-Z0-9\)\]](\$[^\$]+\$)', line):
                        issues.append((path, i, 'Missing space BEFORE inline math'))
                    if re.search(r'(\$[^\$]+\$)[a-zA-Z0-9\[\(]', line):
                        issues.append((path, i, 'Missing space AFTER inline math'))
            except Exception:
                pass
    
    print(f"Files with remaining issues: {len(set(i[0] for i in issues))}")
    print(f"Total issue instances: {len(issues)}")
    
    for path, line, issue in issues[:30]:
        print(f"  [{issue}] {path}:{line}")

check_remaining()