import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_domain_and_application_do_not_depend_on_adapters():
    for path in (ROOT / "backend/src/lisamaria/modules").rglob("*.py"):
        if path.stem not in {"domain", "application", "ports"}:
            continue
        for node in ast.walk(ast.parse(path.read_text())):
            names = []
            if isinstance(node, ast.Import):
                names = [alias.name for alias in node.names]
            elif isinstance(node, ast.ImportFrom):
                names = [node.module or ""]
            assert not any(
                name.split(".")[0] in {"fastapi", "pydantic", "httpx", "sqlalchemy"}
                or "adapters" in name.split(".")
                or "bootstrap" in name.split(".")
                for name in names
            ), f"Architecture dependency violation: {path}"
