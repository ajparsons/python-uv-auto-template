"""Run project metadata tests."""

from pathlib import Path

import {{cookiecutter.underscored}} as package


def test_version_in_workflow():
    """
    Check if the current version is mentioned in the changelog
    """
    package_init_version = package.__version__
    path = Path(__file__).resolve().parents[1] / "CHANGELOG.md"
    change_log = path.read_text(encoding="utf-8")
    version_heading = f"## [{package_init_version}]"
    assert version_heading in change_log


def test_versions_are_in_sync():
    """Checks if the pyproject.toml version matches package.__init__.py __version__."""

    pyproject = Path(__file__).resolve().parents[1] / "pyproject.toml"
    expected_version = 'version = "0.1.0"'
    assert expected_version in pyproject.read_text(encoding="utf-8")
    assert package.__version__ == "0.1.0"
