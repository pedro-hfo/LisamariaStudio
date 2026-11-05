"""PT: Instala as dependências bloqueadas. EN: Install locked dependencies."""

import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    for command in ("uv", "npm"):
        if not shutil.which(command):
            sys.exit(f"Missing / Em falta: {command}. See / Consulta README.md.")
    env = dict(os.environ)
    env.update(
        UV_CACHE_DIR=str(ROOT / ".cache/uv"),
        UV_PYTHON_INSTALL_DIR=str(ROOT / ".tools/python"),
        NPM_CONFIG_CACHE=str(ROOT / ".cache/npm"),
    )
    subprocess.run(["uv", "sync", "--locked"], cwd=ROOT, env=env, check=True)
    subprocess.run(["npm", "ci"], cwd=ROOT, env=env, check=True)
    print("Dependencies ready / Dependências prontas. See / Consulta README.md.")


if __name__ == "__main__":
    main()
