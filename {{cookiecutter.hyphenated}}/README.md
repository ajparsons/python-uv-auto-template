# {{cookiecutter.lib_name}}

{{cookiecutter.description}}

## Development

### Setup
```bash
# Install dependencies
uv sync --dev

# Run tests
uv run pytest

# Run linting and formatting
uv run ruff check .
uv run ruff format .

# Run type checking
uv run pyright
```

### Version Management

This project uses standard version management where the version is defined in `pyproject.toml` and automatically read by `__init__.py`.

To bump the version, use uv's built-in version command:

```bash
# Bump patch version (1.0.0 -> 1.0.1)
uv version --bump patch

# Bump minor version (1.0.0 -> 1.1.0)
uv version --bump minor

# Bump major version (1.0.0 -> 2.0.0)
uv version --bump major

# Set specific version
uv version 1.2.3
```

After bumping the version and pushing to main, GitHub Actions will automatically publish to PyPI if all tests pass.