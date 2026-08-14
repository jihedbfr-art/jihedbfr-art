import os
import sys
import argparse
from pathlib import Path
import re

def get_markdown_files(root_dir):
    md_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        if '.git' in dirpath or '.github' in dirpath:
            continue
        for f in filenames:
            if f.endswith('.md'):
                md_files.append(Path(dirpath) / f)
    return md_files

def check_readme_twins(md_files):
    errors = []
    dirs_with_readmes = set(f.parent for f in md_files if f.name.startswith('README'))
    
    for d in dirs_with_readmes:
        en = d / 'README.md'
        fr = d / 'README.fr.md'
        
        if not en.exists():
            errors.append(f"Missing English README.md in {d}")
        if not fr.exists():
            errors.append(f"Missing French README.fr.md in {d}")
            
    return errors

def check_h2_parity(md_files):
    errors = []
    dirs_with_readmes = set(f.parent for f in md_files if f.name.startswith('README'))
    
    for d in dirs_with_readmes:
        en = d / 'README.md'
        fr = d / 'README.fr.md'
        
        counts = {}
        if en.exists():
            counts['en'] = len([l for l in en.read_text(encoding='utf-8').split('\n') if l.startswith('## ')])
        if fr.exists():
            counts['fr'] = len([l for l in fr.read_text(encoding='utf-8').split('\n') if l.startswith('## ')])
            
        if len(set(counts.values())) > 1:
            errors.append(f"H2 parity mismatch in {d}: {counts}")
            
    return errors

def check_logos_and_tags(md_files):
    errors = []
    for f in md_files:
        content = f.read_text(encoding='utf-8')
        if f.name.startswith('README'):
            if 'assets/brand/jihedailabs-logo' not in content:
                errors.append(f"Missing logo in {f}")
            if not re.search(r'(English|Français)', content):
                errors.append(f"Missing standard language toggle (English/Français) in {f}")
        elif f.name == 'SKILL.md':
            if '<img' in content or '<picture>' in content or '![[' in content or '![' in content:
                errors.append(f"Logo/Image forbidden in SKILL.md: {f}")
    return errors

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type=str, default='.', help='Directory to scan')
    args = parser.parse_args()
    
    root_dir = Path(args.dir)
    md_files = get_markdown_files(root_dir)
    
    errors = []
    errors.extend(check_readme_twins(md_files))
    errors.extend(check_h2_parity(md_files))
    errors.extend(check_logos_and_tags(md_files))
    
    if errors:
        print("Linting failed with the following errors:")
        for e in errors:
            print(f" - {e}")
        sys.exit(1)
    else:
        print("All i18n checks passed.")
        sys.exit(0)

if __name__ == "__main__":
    main()
