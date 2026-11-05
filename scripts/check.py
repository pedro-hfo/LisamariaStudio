"""PT: Validação local reproduzível. EN: Reproducible local validation."""

import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    env = dict(os.environ, PATH=str(ROOT / ".venv/bin") + os.pathsep + os.environ["PATH"])
    commands = [
        ["ruff", "check", "backend", "acceptance", "scripts", "docs/conf.py"],
        ["mypy"],
        ["pytest"],
        ["npm", "test"],
        ["npm", "run", "build"],
        ["npm", "run", "docs:build"],
    ]
    for command in commands:
        wrapped = ["rtk", *command] if shutil.which("rtk") else command
        print("\n> " + " ".join(command), flush=True)
        result = subprocess.run(wrapped, cwd=ROOT, env=env)
        if result.returncode:
            return result.returncode
    return 0


if __name__ == "__main__":
    sys.exit(main())
