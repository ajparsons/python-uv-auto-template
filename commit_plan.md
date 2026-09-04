# Commit plan

The changes divide cleanly into four commits. The paths containing Cookiecutter
expressions are quoted below so the shell treats them literally.

## 1. Modernize the generated Python package

Suggested message:

```text
Modernize generated package for Python 3.10-3.14
```

Include:

```text
{{cookiecutter.hyphenated}}/pyproject.toml
{{cookiecutter.hyphenated}}/uv.lock
{{cookiecutter.hyphenated}}/src/{{cookiecutter.underscored}}/__init__.py
{{cookiecutter.hyphenated}}/scripts/bump_version.py
{{cookiecutter.hyphenated}}/tests/test_meta.py
{{cookiecutter.hyphenated}}/tests/test_{{cookiecutter.underscored}}.py
```

This commit raises the supported Python range, refreshes development-tool
versions, uses uv dependency groups, and updates the generated code and tests for
the current toolchain.

Suggested staging command:

```bash
git add \
  '{{cookiecutter.hyphenated}}/pyproject.toml' \
  '{{cookiecutter.hyphenated}}/uv.lock' \
  '{{cookiecutter.hyphenated}}/src/{{cookiecutter.underscored}}/__init__.py' \
  '{{cookiecutter.hyphenated}}/scripts/bump_version.py' \
  '{{cookiecutter.hyphenated}}/tests/test_meta.py' \
  '{{cookiecutter.hyphenated}}/tests/test_{{cookiecutter.underscored}}.py'
git commit -m "Modernize generated package for Python 3.10-3.14"
```

## 2. Use a project-local development environment

Suggested message:

```text
Configure devcontainer to use a local uv environment
```

Include:

```text
{{cookiecutter.hyphenated}}/Dockerfile
{{cookiecutter.hyphenated}}/.devcontainer/devcontainer.json
{{cookiecutter.hyphenated}}/.devcontainer/postCreateCommand
{{cookiecutter.hyphenated}}/.vscode/settings.json
{{cookiecutter.hyphenated}}/.gitignore
```

This commit moves installation out of the image build, creates `.venv` after the
workspace is mounted, and points the shell and editor at that environment.

Suggested staging command:

```bash
git add \
  '{{cookiecutter.hyphenated}}/Dockerfile' \
  '{{cookiecutter.hyphenated}}/.devcontainer/devcontainer.json' \
  '{{cookiecutter.hyphenated}}/.devcontainer/postCreateCommand' \
  '{{cookiecutter.hyphenated}}/.vscode/settings.json' \
  '{{cookiecutter.hyphenated}}/.gitignore'
git commit -m "Configure devcontainer to use a local uv environment"
```

## 3. Modernize and harden CI workflows

Suggested message:

```text
Harden GitHub Actions and test supported Python versions
```

Include:

```text
.github/workflows/auto_publish.yml
.github/workflows/template_setup.yml
.github/workflows/template_test.yml
.github/workflows/test.yml
requirements.dev.txt
```

This commit expands the test matrix through Python 3.14, pins action references
to immutable commits, applies least-privilege permissions and safer expression
handling, and changes publishing to PyPI trusted publishing.

Suggested staging command:

```bash
git add .github/workflows requirements.dev.txt
git commit -m "Harden GitHub Actions and test supported Python versions"
```

## 4. Update template documentation

Suggested message:

```text
Document Python support and trusted publishing
```

Include:

```text
README.md
```

Suggested staging command:

```bash
git add README.md
git commit -m "Document Python support and trusted publishing"
```

## Final verification

After creating the commits:

```bash
uv run --with-requirements requirements.dev.txt pytest -q
uvx zizmor .
git status --short
```
