from pathlib import Path

def check_path_exists(path):
    result = Path(path).exists()
    return result
print(check_path_exists("main.py"))