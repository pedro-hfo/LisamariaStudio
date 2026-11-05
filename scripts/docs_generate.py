"""PT: Gera referências e inclui os cenários executáveis sem os copiar à mão.

EN: Generate references and include executable scenarios without hand-copying them.
"""

import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def write_if_changed(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists() or path.read_text() != content:
        path.write_text(content)


def generate():
    subprocess.run(["npm", "run", "docs:frontend"], cwd=ROOT, check=True)
    typedoc = ROOT / "build/typedoc"
    for language in ("pt", "en"):
        target = ROOT / "docs" / language / "reference/generated"
        # This directory contains reproducible generated files only.
        if target.exists():
            shutil.rmtree(target)
        target.mkdir(parents=True)
        shutil.copytree(typedoc, target / "frontend")
        frontend_pages = sorted((target / "frontend").rglob("*.md"))
        for page in frontend_pages:
            translated = []
            for line in page.read_text().splitlines():
                if line.startswith(("PT:", "EN:")):
                    if line.startswith("PT:" if language == "pt" else "EN:"):
                        translated.append(line[3:].strip())
                else:
                    translated.append(line)
            page.write_text("\n".join(translated) + "\n")
        title = "Front-end · TypeDoc"
        lines = [title, "=" * len(title), "", ".. toctree::", "   :maxdepth: 2", ""]
        for page in frontend_pages:
            lines.append("   " + page.relative_to(target).with_suffix("").as_posix())
        write_if_changed(target / "frontend.rst", "\n".join(lines) + "\n")

        modules = []
        for source in sorted((ROOT / "backend/src/lisamaria").rglob("*.py")):
            if source.name == "__init__.py":
                continue
            module = ".".join(source.relative_to(ROOT / "backend/src").with_suffix("").parts)
            relative = source.relative_to(ROOT / "backend/src/lisamaria").with_suffix("")
            destination = target / "backend" / relative.with_suffix(".rst")
            content = (
                f"{module}\n{'=' * len(module)}\n\n.. automodule:: {module}\n"
                "   :members:\n   :undoc-members:\n"
            )
            if language == "en":
                content += "   :no-index:\n"
            write_if_changed(destination, content)
            modules.append("   backend/" + relative.as_posix())
        title = "Back-end · Sphinx autodoc"
        write_if_changed(
            target / "backend.rst",
            f"{title}\n{'=' * len(title)}\n\n.. toctree::\n   :maxdepth: 2\n\n"
            + "\n".join(modules)
            + "\n",
        )

        title = "Cenários executáveis" if language == "pt" else "Executable scenarios"
        scenario_lines = [title, "=" * len(title), ""]
        for feature in sorted((ROOT / "acceptance/backend").rglob(f"{language}/*.feature")):
            relative = feature.relative_to(ROOT).as_posix()
            scenario_lines.extend(
                [relative, "-" * len(relative), "", ".. code-block:: gherkin", ""]
            )
            scenario_lines.extend("   " + line for line in feature.read_text().splitlines())
            scenario_lines.append("")
        write_if_changed(target / "scenarios.rst", "\n".join(scenario_lines))


if __name__ == "__main__":
    generate()
