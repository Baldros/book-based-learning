import os
import re
import json
import fnmatch

def get_imports_from_line(line):
    # Regex for standard imports
    # match "import x", "import x.y", "from x import y", "from x.y import z"
    # capturing group 1 is the module name
    
    # Clean up line first
    line = line.strip()
    
    # Handling .ipynb JSON string encoding artifacts if any, though we usually get clean strings from JSON parse
    # But if we regex typical python code:
    
    # Regex specific for 'import' or 'from' at start of logical line
    # We don't handle multi-line imports perfectly without parsing AST, but regex is usually good enough for listing libs.
    
    # Pattern 1: from X import Y
    match_from = re.match(r'^\s*from\s+([a-zA-Z0-9_\.]+)\s+import', line)
    if match_from:
        return match_from.group(1).split('.')[0]
    
    # Pattern 2: import X
    match_import = re.match(r'^\s*import\s+([a-zA-Z0-9_\.]+)', line)
    if match_import:
        return match_import.group(1).split('.')[0]
        
    return None

def scan_file(filepath):
    imports = set()
    try:
        if filepath.endswith('.py'):
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    lib = get_imports_from_line(line)
                    if lib:
                        imports.add(lib)
        elif filepath.endswith('.ipynb'):
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                try:
                    notebook = json.load(f)
                    if 'cells' in notebook:
                        for cell in notebook['cells']:
                            if cell.get('cell_type') == 'code':
                                source = cell.get('source', [])
                                if isinstance(source, str):
                                    source = source.splitlines()
                                for line in source:
                                    lib = get_imports_from_line(line)
                                    if lib:
                                        imports.add(lib)
                except json.JSONDecodeError:
                    pass
    except Exception as e:
        pass
    return imports

def main():
    root_dir = os.getcwd()
    exclude_dirs = {'ZLVenv', 'ZVenv', '.git', '__pycache__', '.ipynb_checkpoints'}
    
    all_imports = set()
    files_scanned = 0
    
    for root, dirs, files in os.walk(root_dir):
        # Modify dirs in-place to skip excluded directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        for file in files:
            if file.endswith(('.py', '.ipynb')):
                filepath = os.path.join(root, file)
                # Skip checking if file is inside an excluded dir (handled by os.walk logic above)
                lib_imports = scan_file(filepath)
                all_imports.update(lib_imports)
                files_scanned += 1
                
    # Standard library filtering could be added, but user asked for "libraries being used".
    # We might want to filter out built-int/standard libs if we had a list, 
    # but listing everything is safer, or maybe just noting them.
    # For now, listing all unique top-level modules.
    
    print(f"Scanned {files_scanned} files.")
    print("Libraries found:")
    for lib in sorted(all_imports):
        print(f"- {lib}")

if __name__ == "__main__":
    main()
