import os
import shutil
from pathlib import Path

REMOVE_PATHS = [
    '{% if not cookiecutter.use_jupyter_notebooks %}notebooks{% endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if not path:
        continue
    p = Path(path)
    if not p.exists():
        continue
    if p.is_dir():
        shutil.rmtree(path)
    else:
        os.unlink(path)
