"""{{cookiecutter.description}}"""

from __future__ import annotations

__version__: str


def __getattr__(name: str) -> str:
    """Load module attributes that are derived from package metadata."""
    if name == "__version__":
        from importlib.metadata import version

        value = version("{{cookiecutter.hyphenated}}")
        globals()[name] = value
        return value

    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
