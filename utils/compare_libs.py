import os
import re
import json

# Mapping of import names to package names in requirements.txt
IMPORT_TO_PACKAGE = {
    'PIL': 'pillow',
    'bs4': 'beautifulsoup4',
    'cv2': 'opencv-python',
    'sklearn': 'scikit-learn',
    'skimage': 'scikit-image',
    'yaml': 'PyYAML',
}

# List of common standard libraries to ignore
STD_LIBS = {
    'os', 'sys', 're', 'json', 'math', 'time', 'datetime', 'collections', 
    'itertools', 'functools', 'pathlib', 'io', 'urllib', 'pickle', 'gzip', 
    'zlib', 'tarfile', 'random', 'string', 'fnmatch', 'importlib', 'shutil',
    'glob', 'base64', 'hashlib', 'threading', 'multiprocessing', 'abc',
    'argparse', 'csv', 'logging', 'socket', 'struct', 'subprocess', 'tempfile',
    'traceback', 'warnings', 'xml', 'zipfile', 'copy', 'enum', 'inspect',
    'operator', 'types', 'uuid', 'html', 'http', 'email', 'ast', 'asyncio',
    'bisect', 'calendar', 'contextlib', 'decimal', 'difflib', 'getopt', 'heapq',
    'keyword', 'linecache', 'locale', 'numbers', 'pprint', 'queue', 'select',
    'selectors', 'signal', 'smtplib', 'stat', 'statistics', 'token', 'tokenize',
    'unittest'
}

def get_imports_from_line(line):
    line = line.strip()
    match_from = re.match(r'^\s*from\s+([a-zA-Z0-9_\.]+)\s+import', line)
    if match_from:
        return match_from.group(1).split('.')[0]
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
                    if lib: imports.add(lib)
        elif filepath.endswith('.ipynb'):
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                notebook = json.load(f)
                if 'cells' in notebook:
                    for cell in notebook['cells']:
                        if cell.get('cell_type') == 'code':
                            source = cell.get('source', [])
                            if isinstance(source, str): source = source.splitlines()
                            for line in source:
                                lib = get_imports_from_line(line)
                                if lib: imports.add(lib)
    except: pass
    return imports

def main():
    root_dir = os.getcwd()
    exclude_dirs = {'ZLVenv', 'ZVenv', '.git', '__pycache__', '.ipynb_checkpoints', 'utils'} # Ignoring 'utils' as local
    
    used_libs = set()
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for file in files:
            if file.endswith(('.py', '.ipynb')):
                used_libs.update(scan_file(os.path.join(root, file)))

    # Read requirements.txt
    req_packages = set()
    if os.path.exists('requirements.txt'):
        with open('requirements.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    # Match name before == or @ or [
                    pkg = re.split(r'[=<>@\[]', line)[0].strip().lower()
                    req_packages.add(pkg)

    # Filter out stdlibs and locals
    # We'll treat anything that is a directory in root as local too
    root_items = {item.lower() for item in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, item))}
    
    missing = []
    matched = []
    
    for lib in sorted(used_libs):
        if lib.lower() in STD_LIBS or lib.lower() in root_items:
            continue
        
        pkg_name = IMPORT_TO_PACKAGE.get(lib, lib).lower()
        
        if pkg_name in req_packages:
            matched.append(f"{lib} -> {pkg_name}")
        else:
            missing.append(lib)

    print("--- MATCHED LIBRARIES ---")
    for m in matched: print(f"[OK] {m}")
    
    print("\n--- MISSING LIBRARIES (Used but not in requirements.txt) ---")
    for lib in missing:
        pkg_suggestion = IMPORT_TO_PACKAGE.get(lib, lib)
        print(f"[MISSING] {lib} (Sugerido: {pkg_suggestion})")

    # Optional: Libs in requirements but not used
    in_req_not_used = []
    used_pkg_names = {IMPORT_TO_PACKAGE.get(lib, lib).lower() for lib in used_libs}
    for req in sorted(req_packages):
        if req not in used_pkg_names and req not in {'ipykernel', 'ipython', 'jupyter_client', 'jupyter_core', 'debugpy'}: # Ignore dev/jupyter tools
            in_req_not_used.append(req)
            
    # print("\n--- UNUSED IN REQUIREMENTS ---")
    # for r in in_req_not_used: print(f"[UNUSED] {r}")

if __name__ == "__main__":
    main()
