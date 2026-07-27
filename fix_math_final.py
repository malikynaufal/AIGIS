#!/usr/bin/env python3
"""
Fix math expressions to be visually readable in Obsidian and GitHub Markdown.
Converts double-backslash LaTeX commands (\\frac, \\sum, etc.) to proper single-backslash
and ensures display math is properly formatted.
"""
import os, re, glob

FOLDER = r"C:\Obsidian\Brain Original\AIGIS"
GITHUB_FOLDER = r"/tmp/github_repo"

def fix_math_in_text(text):
    """Fix double-backslash LaTeX commands to single-backslash."""
    # Fix common double-backslash LaTeX commands
    replacements = [
        # Fractions and math symbols
        ('\\\\frac', '\\frac'),
        ('\\\\sum', '\\sum'),
        ('\\\\prod', '\\prod'),
        ('\\\\coprod', '\\coprod'),
        ('\\\\sqrt', '\\sqrt'),
        ('\\\\cdot', '\\cdot'),
        ('\\\\times', '\\times'),
        ('\\\\div', '\\div'),
        ('\\\\pm', '\\pm'),
        ('\\\\mp', '\\mp'),
        ('\\\\circ', '\\circ'),
        ('\\\\ast', '\\ast'),
        ('\\\\star', '\\star'),
        # Greek letters (lowercase)
        ('\\\\alpha', '\\alpha'),
        ('\\\\beta', '\\beta'),
        ('\\\\gamma', '\\gamma'),
        ('\\\\delta', '\\delta'),
        ('\\\\epsilon', '\\epsilon'),
        ('\\\\varepsilon', '\\varepsilon'),
        ('\\\\zeta', '\\zeta'),
        ('\\\\eta', '\\eta'),
        ('\\\\theta', '\\theta'),
        ('\\\\vartheta', '\\vartheta'),
        ('\\\\iota', '\\iota'),
        ('\\\\kappa', '\\kappa'),
        ('\\\\lambda', '\\lambda'),
        ('\\\\mu', '\\mu'),
        ('\\\\nu', '\\nu'),
        ('\\\\xi', '\\xi'),
        ('\\\\pi', '\\pi'),
        ('\\\\varpi', '\\varpi'),
        ('\\\\rho', '\\rho'),
        ('\\\\varrho', '\\varrho'),
        ('\\\\sigma', '\\sigma'),
        ('\\\\varsigma', '\\varsigma'),
        ('\\\\tau', '\\tau'),
        ('\\\\upsilon', '\\upsilon'),
        ('\\\\phi', '\\phi'),
        ('\\\\varphi', '\\varphi'),
        ('\\\\chi', '\\chi'),
        ('\\\\psi', '\\psi'),
        ('\\\\omega', '\\omega'),
        # Greek letters (uppercase)
        ('\\\\Gamma', '\\Gamma'),
        ('\\\\Delta', '\\Delta'),
        ('\\\\Theta', '\\Theta'),
        ('\\\\Lambda', '\\Lambda'),
        ('\\\\Xi', '\\Xi'),
        ('\\\\Sigma', '\\Sigma'),
        ('\\\\Upsilon', '\\Upsilon'),
        ('\\\\Phi', '\\Phi'),
        ('\\\\Psi', '\\Psi'),
        ('\\\\Omega', '\\Omega'),
        # Relations
        ('\\\\leq', '\\leq'),
        ('\\\\geq', '\\geq'),
        ('\\\\neq', '\\neq'),
        ('\\\\approx', '\\approx'),
        ('\\\\equiv', '\\equiv'),
        ('\\\\sim', '\\sim'),
        ('\\\\simeq', '\\simeq'),
        ('\\\\propto', '\\propto'),
        ('\\\\ll', '\\ll'),
        ('\\\\gg', '\\gg'),
        ('\\\\subset', '\\subset'),
        ('\\\\supset', '\\supset'),
        ('\\\\subseteq', '\\subseteq'),
        ('\\\\supseteq', '\\supseteq'),
        # Set operations
        ('\\\\cup', '\\cup'),
        ('\\\\cap', '\\cap'),
        ('\\\\setminus', '\\setminus'),
        ('\\\\emptyset', '\\emptyset'),
        ('\\\\in', '\\in'),
        ('\\\\ni', '\\ni'),
        # Arrows
        ('\\\\to', '\\to'),
        ('\\\\rightarrow', '\\rightarrow'),
        ('\\\\leftarrow', '\\leftarrow'),
        ('\\\\Rightarrow', '\\Rightarrow'),
        ('\\\\Leftarrow', '\\Leftarrow'),
        ('\\\\leftrightarrow', '\\leftrightarrow'),
        ('\\updownarrow', '\\updownarrow'),
        # Infinity / special
        ('\\\\infty', '\\infty'),
        ('\\\\aleph', '\\aleph'),
        ('\\\\top', '\\top'),
        ('\\\\bot', '\\bot'),
        # Calculus
        ('\\\\partial', '\\partial'),
        ('\\\\nabla', '\\nabla'),
        ('\\\\int', '\\int'),
        ('\\\\iint', '\\iint'),
        ('\\\\iiint', '\\iiint'),
        ('\\\\oint', '\\oint'),
        ('\\\\ointoint', '\\ointoint'),
        ('\\\\dd', '\\dd'),
        # Functions
        ('\\\\lim', '\\lim'),
        ('\\\\max', '\\max'),
        ('\\\\min', '\\min'),
        ('\\\\sup', '\\sup'),
        ('\\\\inf', '\\inf'),
        ('\\\\arg', '\\arg'),
        ('\\\\ln', '\\ln'),
        ('\\\\log', '\\log'),
        ('\\\\lg', '\\lg'),
        ('\\\\exp', '\\exp'),
        ('\\\\det', '\\det'),
        ('\\\\dim', '\\dim'),
        ('\\\\ker', '\\ker'),
        ('\\\\hom', '\\hom'),
        ('\\\\deg', '\\deg'),
        ('\\\\gcd', '\\gcd'),
        ('\\\\lcm', '\\lcm'),
        ('\\\\sgn', '\\sgn'),
        # Trig functions
        ('\\\\sin', '\\sin'),
        ('\\\\cos', '\\cos'),
        ('\\\\tan', '\\tan'),
        ('\\\\cot', '\\cot'),
        ('\\\\sec', '\\sec'),
        ('\\\\csc', '\\csc'),
        # Brackets and delimiters
        ('\\\\lfloor', '\\lfloor'),
        ('\\\\rfloor', '\\rfloor'),
        ('\\\\lceil', '\\lceil'),
        ('\\\\rceil', '\\rceil'),
        ('\\\\langle', '\\langle'),
        ('\\\\rangle', '\\rangle'),
        ('\\\\vert', '\\vert'),
        ('\\\\Vert', '\\Vert'),
        ('\\\\lvert', '\\lvert'),
        ('\\\\rvert', '\\rvert'),
        ('\\\\lVert', '\\lVert'),
        ('\\\\rVert', '\\rVert'),
        # Misc
        ('\\\\ldots', '\\ldots'),
        ('\\\\cdots', '\\cdots'),
        ('\\\\vdots', '\\vdots'),
        ('\\\\ddots', '\\ddots'),
        ('\\\\hat', '\\hat'),
        ('\\\\check', '\\check'),
        ('\\\\breve', '\\breve'),
        ('\\\\acute', '\\acute'),
        ('\\\\grave', '\\grave'),
        ('\\\\bar', '\\bar'),
        ('\\\\vec', '\\vec'),
        ('\\\\overline', '\\overline'),
        ('\\\\underline', '\\underline'),
        ('\\\\overbrace', '\\overbrace'),
        ('\\\\underbrace', '\\underbrace'),
        ('\\\\underset', '\\underset'),
        ('\\\\overset', '\\overset'),
        ('\\\\atop', '\\atop'),
        ('\\\\binom', '\\binom'),
        ('\\\\dbinom', '\\dbinom'),
        ('\\\\tbinom', '\\tbinom'),
        ('\\\\choose', '\\choose'),
        ('\\\\begin', '\\begin'),
        ('\\\\end', '\\end'),
        ('\\\\left', '\\left'),
        ('\\\\right', '\\right'),
        ('\\\\middle', '\\middle'),
        ('\\\\bigr', '\\bigr'),
        ('\\\\big', '\\big'),
        ('\\\\Big', '\\Big'),
        ('\\\\bigg', '\\bigg'),
        ('\\\\Bigg', '\\Bigg'),
        # Mathcal
        ('\\\\mathcal', '\\mathcal'),
        ('\\\\mathbb', '\\mathbb'),
        ('\\\\mathbf', '\\mathbf'),
        ('\\\\mathrm', '\\mathrm'),
        ('\\\\mathit', '\\mathit'),
        ('\\\\mathbfsf', '\\mathbfsf'),
        ('\\\\mathtt', '\\mathtt'),
        ('\\\\mathscr', '\\mathscr'),
        ('\\\\mathfrak', '\\mathfrak'),
        # Bold
        ('\\\\mathbf', '\\mathbf'),
        ('\\\\boldsymbol', '\\boldsymbol'),
        # Display
        ('\\\\displaylines', '\\displaylines'),
        ('\\\\boxed', '\\boxed'),
        ('\\\\fbox', '\\fbox'),
        ('\\\\cancel', '\\cancel'),
        ('\\\\bcancel', '\\bcancel'),
        ('\\\\xcancel', '\\xcancel'),
        ('\\\\cancelto', '\\cancelto'),
        # Tag/ref
        ('\\\\tag', '\\tag'),
        ('\\\\label', '\\label'),
        ('\\\\ref', '\\ref'),
        ('\\\\eqref', '\\eqref'),
        # Color
        ('\\\\color', '\\color'),
        ('\\\\textcolor', '\\textcolor'),
        ('\\\\colorbox', '\\colorbox'),
        # Spacing
        ('\\\\,', '\\,'),
        ('\\\\:', '\\:'),
        ('\\\\;', '\\;'),
        ('\\\\\\ ', '\\ '),
        ('\\\\\\quad', '\\quad'),
        # \pmod etc
        ('\\\\pmod', '\\pmod'),
        ('\\\\mod', '\\mod'),
        ('\\\\bmod', '\\bmod'),
        ('\\\\ast', '\\ast'),
    ]
    
    for old, new in replacements:
        text = text.replace(old, new)
    
    # Fix display math spacing
    # Ensure $$ on its own line with blank lines around it
    text = re.sub(r'([^\n])\n(\$\$)', r'\1\n\n\2', text)
    text = re.sub(r'(\$\$)\n([^\n$])', r'\1\n\n\2', text)
    # Fix $$\n\\ -> $\n\
    text = re.sub(r'\$\$\n\\\\', r'$$\n\\', text)
    
    # Fix inline math with spaces inside $ $
    text = re.sub(r'\$\s+([^$\n]+?)\s+\$', r'$\1$', text)
    
    return text


def process_folder(folder, label):
    if not os.path.exists(folder):
        print(f"Folder not found: {folder}")
        return 0
    
    count = 0
    skipped = 0
    for root, dirs, fnames in os.walk(folder):
        # Skip git and inbox directories
        if '.git' in root:
            continue
        for fn in fnames:
            if not fn.endswith('.md'):
                continue
            path = os.path.join(root, fn)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    original = f.read()
                
                updated = fix_math_in_text(original)
                
                if updated != original:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(updated)
                    count += 1
            except Exception as e:
                skipped += 1
                if skipped <= 3:
                    print(f"  Skipped {path}: {e}")
    
    print(f"  [{label}] Files fixed: {count}")
    return count


if __name__ == '__main__':
    print("=" * 60)
    print("AIGIS Math Expression Visual Formatter")
    print("=" * 60)
    
    total = 0
    total += process_folder(FOLDER, "Obsidian Vault")
    total += process_folder(GITHUB_FOLDER, "GitHub Repo")
    
    print(f"\n{'=' * 60}")
    print(f"Total files fixed: {total}")
    print(f"{'=' * 60}")
