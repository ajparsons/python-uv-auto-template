"""
Run meta tests on package (apply to muliple packages)

"""
from pathlib import Path
import {{cookiecutter.underscored}} as package
import toml


def test_version_in_workflow():
    """
    Check if the current version is mentioned in the changelog
    """
    package_init_version = package.__version__
    path = Path(__file__).resolve().parents[1] / "CHANGELOG.md"
    change_log = path.read_text()
    format = f"## [{package_init_version}]"
    assert format in change_log


def test_versions_are_in_sync():
    """Checks if the pyproject.toml version matches package.__init__.py __version__."""

    path = Path(__file__).resolve().parents[1] / "pyproject.toml"
    pyproject = toml.loads(open(str(path), encoding="utf-8").read())
    pyproject_version = pyproject["project"]["version"]

    package_init_version = package.__version__

    assert package_init_version == pyproject_version, f"Version mismatch: __init__.py has {package_init_version}, pyproject.toml has {pyproject_version}"
