import re
from pathlib import Path

from gherkin.parser import Parser

ROOT = Path(__file__).resolve().parents[2]


def test_guides_have_a_matching_translation():
    def pages(language):
        return {
            path.relative_to(ROOT / "docs" / language)
            for path in (ROOT / "docs" / language).rglob("*.md")
            if "generated" not in path.parts
        }

    assert pages("pt") == pages("en")


def test_scenario_ids_structure_and_example_values_match():
    def contracts(language):
        path = (
            ROOT / f"acceptance/backend/appointments/features/{language}/book_appointment.feature"
        )
        feature = Parser().parse(path.read_text())["feature"]
        result = {}
        for child in feature["children"]:
            scenario = child["scenario"]
            identifier = next(tag["name"] for tag in scenario["tags"] if "APT-" in tag["name"])
            assert identifier not in result
            result[identifier] = [
                (step["keywordType"], re.findall(r'"[^"]*"|\b\d+\b', step["text"]))
                for step in scenario["steps"]
            ]
        return result

    assert contracts("pt") == contracts("en")
