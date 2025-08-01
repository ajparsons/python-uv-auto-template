# Python project template

This template repository can be used to create a new repository with the skeleton of a uv-based Python library.

This is based on the general approach of [simonw/python-lib](https://github.com/simonw/python-lib), but with a different default structure and using uv instead of Poetry.

# Creating a new template

A new repository based on this template can be created in Github or through cookiecutter.

## Templating in GitHub

The templating process can be run entirely in GitHub to create a new repository. 

Start here: https://github.com/ajparsons/python-uv-auto-template/generate

Add a one-line description of your repository, then click "Create repository from template".

# Templating with cookiecutter

This repo can also be used to set up a template offline using [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/). To start the processs:

```
python -m cookiecutter https://github.com/ajparsons/python-uv-auto-template/
```

# Features
 
The default package uses:

* [uv](https://docs.astral.sh/uv/) for package management and dependency resolution,
* [pytest](https://docs.pytest.org/en/7.1.x/) for testing,
* [ruff](https://docs.astral.sh/ruff/) for linting and formatting,
* [pyright](https://github.com/microsoft/pyright) for typechecking. 
* [GitHub Actions](https://github.com/features/actions) for CI and publishing. 

New repositories include config files and Dockerfile for developing in VS Code or Codespaces, so the development process can happen end to end in Github. (Or not! Will still worked cloned locally). 

The test suite contains meta tests for alignment between the `__version__` of the package and the project version, and that the current version is documented in the change log. 

The template version includes a default GitHub Action for testing on Python 3.8-3.10, and publishing to pypi.

By default, the test action requires pytest, ruff and pyright to return no errors.

The default licence is the MIT Licence. Change if needed. 

# Publishing the package

* Set a GitHub Actions secret for PYPI_TOKEN. 
* For the initial publish. In the Actions tab for a repo, trigger a manual workfork flow with the 'force to pypi' box ticked.
* Subsequently, if the project version is bumped and all tests pass - the GitHub Action will automatically publish on push to the main branch.

# Version Management

The template uses **standard version management** with uv where:
- Version is defined in `pyproject.toml` 
- `__init__.py` automatically reads the version from `pyproject.toml`
- Use `uv version --bump patch/minor/major` to bump versions
- No manual syncing required between files

This follows modern Python packaging standards and integrates seamlessly with uv's workflow.

# Development and forking

If you want to modify or extend this approach - the self-bootstrapping behaviour will only happen when a repo does *not* end in '-auto-template'. If you clone this repo, into a different user or org space, it will not self-bootstrap because the name is the same.

If you wanted to extend this into a basic django template - you might fork or clone the repo and call it 'django-auto-template'. This will not self-bootstrap, but new projects created from that template would. 

## Meta tests

This project defines several meta tests in `tests/` that will:

* Attempt to provision a template with basic variables.
* Run the projects internal tests for self-integrity.

This requires the packages listed in `requirements.dev.txt` to be installed.
