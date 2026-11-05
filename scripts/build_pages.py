"""PT: Empacotar interface e guias para Pages. EN: Package UI and guides for Pages."""

import os
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    base = os.environ.get("PAGES_BASE_PATH", "/LisamariaStudio/").strip("/")
    env = dict(os.environ, PAGES_BASE_PATH=f"/{base}/" if base else "/")
    subprocess.run(
        ["npm", "run", "build", "--workspace", "frontend", "--", "--mode", "pages"],
        cwd=ROOT, env=env, check=True,
    )
    docs = ROOT / "build/docs"
    if docs.exists():
        shutil.rmtree(docs)
    subprocess.run(["npm", "run", "docs:build"], cwd=ROOT, env=env, check=True)
    target = ROOT / "build/pages"
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(ROOT / "frontend/dist", target)
    shutil.copytree(docs, target / "docs", ignore=shutil.ignore_patterns(".doctrees", ".buildinfo"))
    (target / ".nojekyll").touch()
    print(f"Pages artifact / Artefacto Pages: {target}")


if __name__ == "__main__":
    main()
