"""Sphinx configuration / Configuração Sphinx."""

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "backend/src"))
sys.path.insert(0, str(ROOT / "scripts"))

project = "Lisamaria Studio"
author = "Lisamaria Studio"
extensions = ["myst_parser", "sphinx.ext.autodoc", "sphinx.ext.napoleon"]
html_theme = "furo"
language = "pt"
source_suffix = {".rst": "restructuredtext", ".md": "markdown"}
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
autodoc_member_order = "bysource"
autodoc_typehints = "description"
myst_heading_anchors = 5
html_title = "Lisamaria · Developer guide / Guia de desenvolvimento"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_js_files = ["language.js"]
html_theme_options = {
    "light_css_variables": {"color-brand-primary": "#315447", "color-brand-content": "#315447"},
    "footer_icons": [],
}
app_port = os.environ.get("LISAMARIA_APP_PORT", "3000")
rst_epilog = f"\n.. |app_port| replace:: {app_port}\n"


def select_docstring_language(app, what, name, obj, options, lines):
    """Select PT:/EN: sections for the current language page."""
    docname = app.env.docname
    language_prefix = "EN:" if docname.startswith("en/") else "PT:"
    expanded = [part for line in lines for part in line.replace(" EN:", "\nEN:").splitlines()]
    if any(line.strip().startswith(("PT:", "EN:")) for line in expanded):
        translated = []
        keep = False
        for line in expanded:
            if line.strip().startswith(("PT:", "EN:")):
                keep = line.strip().startswith(language_prefix)
                if keep:
                    translated.append(line.strip()[3:].strip())
            elif keep:
                translated.append(line)
        lines[:] = translated


def generate_references(app):
    from docs_generate import generate

    generate()


def setup(app):
    app.connect("builder-inited", generate_references)
    app.connect("autodoc-process-docstring", select_docstring_language)
