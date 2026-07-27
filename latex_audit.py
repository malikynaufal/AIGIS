import os, re, glob

vault = r'C:\Obsidian\Brain Original\AIGIS'
md_files = glob.glob(os.path.join(vault, '**', '*.md'), recursive=True)

total_files = len(md_files)
total_dollar_outside_code = 0
files_with_unbalanced = []
code_block_pattern = re.compile(r'```.*?```', re.DOTALL)
key_escape = re.compile(r'(?<!\\)\$')
dollar_pattern = re.compile(r'(?<!\\)\$')

# Simple $ detection for balance - avoid complex regex
for f in md_files:
    with open(f, 'r', encoding='utf-8', errors='ignore') as fh:
        content = fh.read()
    
    # Count $ signs outside code blocks
    code_dollar_count = 0
    in_code = False
    i = 0
    while i < len(content):
        if content[i:i+3] == '```':
            in_code = not in_code
            i += 3
            continue
        if not in_code and content[i] == '$':
            code_dollar_count += 1
        i += 1
    
    total_dollar_outside_code += code_dollar_count
    if code_dollar_count % 2 != 0:
        files_with_unbalanced.append((f, code_dollar_count))

print(f'Total MD files: {total_files}')
print(f'Total $ outside code blocks: {total_dollar_outside_code}')
print(f'Files with unbalanced $: {len(files_with_unbalanced)}')
for f, c in files_with_unbalanced[:20]:
    rel = f.replace('C:\\Obsidian\\Brain Original\\AIGIS\\', '')
    print(f'  {rel}: {c} $ signs')
