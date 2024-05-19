import os
from pathlib import Path

list_of_files = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/mongodb/__init__.py"
    "src/mongodb/mongo_crud.py"
    "src/utils/__init__.py",
    "src/utils/utils.py",    
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/unit/unit.py"
    "tests/integration/__init__.py",
    "tests/integration/integration.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "research_env/experiments.ipynb",
    "pyproject.toml",
    "tox.ini"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # create the directory
    if filedir != "":
        os.makedirs(filedir, exist_ok = True)

    # create file 
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass