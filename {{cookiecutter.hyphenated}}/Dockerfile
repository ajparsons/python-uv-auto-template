FROM python:3.14-bookworm

COPY --from=ghcr.io/astral-sh/uv:0.12.9 /uv /uvx /bin/

ENV UV_LINK_MODE=copy
ENV UV_PROJECT_ENVIRONMENT=/workspaces/{{cookiecutter.hyphenated}}/.venv
ENV PATH="/workspaces/{{cookiecutter.hyphenated}}/.venv/bin:${PATH}"
