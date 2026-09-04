from importlib.metadata import version


def test_package_is_installed() -> None:
    """The distribution should be installed in the project environment."""
    assert version("{{cookiecutter.hyphenated}}") == "0.1.0"
