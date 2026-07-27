#!/usr/bin/env python3
"""
Comprehensive formatter for AIGIS mathematical expressions.
Fixes LaTeX escaping and improves visual readability.
"""
import os, re, sys

def fix_mathematical_expressions(content):
    """Fix mathematical expressions for better readability."""
    lines = content.split('\n')
    fixed = []
    
    for i, line in enumerate(lines):
        # Skip empty lines
        if not line.strip():
            fixed.append(line)
            continue
            
        original_line = line
        
        # 1. Fix common double-backslash LaTeX commands
        # Replace \\\\frac with \\frac
        line = re.sub(r'\\\\\\\\frac', r'\\\\frac', line)
        line = re.sub(r'\\\\\\\\sum', r'\\\\sum', line)
        line = re.sub(r'\\\\\\\\sqrt', r'\\\\sqrt', line)
        line = re.sub(r'\\\\\\\\cdot', r'\\\\cdot', line)
        line = re.sub(r'\\\\\\\\times', r'\\\\times', line)
        
        # More Greek letters
        greek_replacements = [
            ('\\\\\\\\alpha', '\\\\alpha'),
            ('\\\\\\\\beta', '\\\\beta'),
            ('\\\\\\\\gamma', '\\\\gamma'),
            ('\\\\\\\\delta', '\\\\delta'),
            ('\\\\\\\\epsilon', '\\\\epsilon'),
            ('\\\\\\\\lambda', '\\\\lambda'),
            ('\\\\\\\\mu', '\\\\mu'),
            ('\\\\\\\\pi', '\\\\pi'),
            ('\\\\\\\\sigma', '\\\\sigma'),
            ('\\\\\\\\phi', '\\\\phi'),
        ]
        for double, single in greek_replacements:
            line = line.replace(double, single)
            
        # 2. Fix escaped brackets in LaTeX
        line = line.replace('\\\\[', '[')
        line = line.replace('\\\\]', ']')
        
        # 3. Fix unbalanced parentheses in LaTeX
        line = line.replace('\\\\(', '(')
        line = line.replace('\\\\)', ')')
        
        # 4. Improve inline math spacing - remove spaces inside $ delimiters
        line = re.sub(r'\$\s*([^$\n]+)\s*\$', r'$\1$', line)
        
        # 5. Fix display math spacing - ensure empty lines around $$
        if line.strip().startswith('$$') and line.strip().endswith('$$'):
            # This is a display math block
            # Check if there's proper spacing
            if i > 0 and lines[i-1].strip():
                fixed.append('')  # Add empty line before
            fixed.append(line)
            if i < len(lines) - 1 and lines[i+1].strip():
                fixed.append('')  # Add empty line after
            continue
        elif line.strip().startswith('$$'):
            # Start of display math block
            if i > 0 and lines[i-1].strip():
                fixed.append('')
            fixed.append(line)
            continue
        elif line.strip().endswith('$$') and i > 0 and not lines[i-1].strip().startswith('$$'):
            # End of display math block
            fixed.append(line)
            if i < len(lines) - 1 and lines[i+1].strip():
                fixed.append('')
            continue
            
        fixed.append(line)
    
    # Join back and clean up
    result = '\n'.join(fixed)
    
    # 6. Fix multiple empty lines
    result = re.sub(r'\n\s*\n\s*\n', '\n\n', result)
    
    # 7. Clean up any remaining double backslashes at start of lines
    result = re.sub(r'^(\s*)\\\\\\\\', r'\1\\\\', result, flags=re.MULTILINE)
    
    return result

def process_file(file_path):
    """Process a single markdown file to fix math expressions."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        fixed_content = fix_mathematical_expressions(original_content)
        
        if original_content != fixed_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            return True, len(fixed_content.split('\n')) - len(original_content.split('\n'))
        return False, 0
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False, 0

def main():
    print("=" * 70)
    print("AIGIS Mathematical Expression Formatter")
    print("=" * 70)
    print("Fixing mathematical expressions for improved visual readability...")
    print()
    
    # Determine folders to process
    folders = []
    
    # Check if Obsidian vault exists
    obsidian_vault = os.path.join(os.path.expanduser('C:\\'), 'Obsidian', 'Brain Original', 'AIGIS')
    if os.path.exists(obsidian_vault):
        folders.append(('Obsidian Vault', obsidian_vault))
    
    # Check if GitHub repo exists
    github_repo = os.path.join(os.path.expanduser('C:\\'), 'Users', 'Owner', '.git_repo')
    if not os.path.exists(github_repo):
        github_repo = r"/tmp/github_repo"
    if os.path.exists(github_repo):
        folders.append(('GitHub Repo', github_repo))
    
    total_files_fixed = 0
    total_changes = 0
    
    for folder_name, folder_path in folders:
        print(f"Processing: {folder_name}")
        print(f"Location: {folder_path}")
        
        # Walk through all .md files
        for root, dirs, files in os.walk(folder_path):
            # Skip hidden directories and processed folders
            dirs[:] = [d for d in dirs if not d.startswith('.') 
                      and d not in ['_processed', '_Inbox']]
            
            for file in files:
                if not file.endswith('.md'):
                    continue
                
                file_path = os.path.join(root, file)
                was_fixed, changes = process_file(file_path)
                
                if was_fixed:
                    total_files_fixed += 1
                    total_changes += changes
                    print(f"  ✓ Fixed: {os.path.relpath(file_path, folder_path)}")
        
        print()
    
    print("=" * 70)
    print(f"Summary:")
    print(f"  Total files fixed: {total_files_fixed}")
    print(f"  Total line changes: {abs(total_changes)}")
    print("=" * 70)
    print("\nMathematical expressions have been reformatted for better readability!")

if __name__ == '__main__':
    main()