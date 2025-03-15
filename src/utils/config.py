import os
import sys
from pathlib import Path

PROJECT_PATH = Path(__file__).resolve().parent.parent.parent
print('PROJECT_PATH: ', PROJECT_PATH)


def _add_src_to_path(source_dir: Path) -> None:
    if str(source_dir) not in sys.path:
        sys.path.insert(0, str(source_dir))

    python_path = os.getenv("PYTHONPATH", "")
    if str(source_dir) not in python_path:
        sep = os.pathsep if python_path else ""
        os.environ["PYTHONPATH"] = f"{str(source_dir)}{sep}{python_path}"


_add_src_to_path(PROJECT_PATH)
