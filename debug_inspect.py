from pathlib import Path
lines = Path('japan-tours-v4-split.html').read_text(encoding='utf-8').splitlines()
for i, line in enumerate(lines[680:780], start=681):
    print(f"{i}: {line}")
