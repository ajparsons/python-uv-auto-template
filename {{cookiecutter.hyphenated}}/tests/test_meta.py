"""Run project metadata tests."""

from importlib.metadata import version
from pathlib import Path

import pytest

import {{cookiecutter.underscored}} as package


def test_version_is_loaded_lazily_and_cached() -> None:
    """The package version should be read from installed distribution metadata."""
    package.__dict__.pop("__version__", None)

    package_version = package.__version__

    assert package_version == version("{{cookiecutter.hyphenated}}")
    assert package.__dict__["__version__"] is package_version


def test_unknown_module_attribute_raises_attribute_error() -> None:
    """Unknown attributes should retain normal module behavior."""
    with pytest.raises(AttributeError, match="has no attribute 'missing'"):
        _ = package.missing


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
