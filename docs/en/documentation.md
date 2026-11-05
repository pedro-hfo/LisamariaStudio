# Document without overwhelming

Each module should explain **what it does, why it exists and how to test it**. Add detail when it helps understanding or decisions; do not comment obvious operations line by line.

## Three levels

1. **Essential:** responsibility, vocabulary, an example and a test command.
2. **When needed:** invariants, dependencies, errors and relevant decisions.
3. **Reference:** signatures and docstrings generated from code.

Start with the first level. Use hints for unfamiliar terms. We will adjust depth as your experience grows.

## Two languages, matching structure

Guides live under `docs/pt/` and `docs/en/` with matching paths. The language switch keeps the equivalent page. Update both files in the same change. The glossary preserves English terms useful in the literature.

Python docstrings have `PT:` and `EN:` blocks; Sphinx selects the matching translation. TypeScript comments also have PT/EN; TypeDoc extracts the reference and integrates it into Sphinx. Code names and signatures stay unchanged.

```python
def execute(...):
    """PT: Descreve a intenção em português.

    EN: Describe the intention in English.
    """
```

The server rebuilds references when code changes. Files under `reference/generated/` are derived and must not be edited manually. Published scenarios are generated from `.feature` files to avoid stale copies.

## Add a module

Create the code module and the identically named folder under `acceptance/`. Add matching PT/EN guides, update indexes and the glossary. Document one behaviour first; then introduce only the abstractions it requires.

`npm run docs:build` treats documentation warnings as errors. The parity test verifies equivalent guides in both languages and matching scenario IDs and structure.
