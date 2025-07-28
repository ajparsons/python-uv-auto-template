"""
{{cookiecutter.description}}
"""

try:
    # Try to read version from pyproject.toml
    import tomllib
    from pathlib import Path
    
    _pyproject_path = Path(__file__).parent.parent.parent / "pyproject.toml"
    with open(_pyproject_path, "rb") as f:
        _pyproject_data = tomllib.load(f)
    __version__ = _pyproject_data["project"]["version"]
except (ImportError, FileNotFoundError, KeyError):
    # Fallback for Python < 3.11 or if tomllib is not available
    try:
        import toml
        from pathlib import Path
        
        _pyproject_path = Path(__file__).parent.parent.parent / "pyproject.toml"
        with open(_pyproject_path, "r") as f:
            _pyproject_data = toml.load(f)
        __version__ = _pyproject_data["project"]["version"]
    except (ImportError, FileNotFoundError, KeyError):
        # Ultimate fallback
        __version__ = "unknown"