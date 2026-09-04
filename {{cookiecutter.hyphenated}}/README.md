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

### Version management

The version is defined in `pyproject.toml`.

```bash
# Bump the current version
uv version --bump patch
uv version --bump minor
uv version --bump major

# Set an explicit version
uv version 1.2.3
```

After changing the version and pushing to `main`, GitHub Actions will publish the
new release to PyPI if all tests pass.