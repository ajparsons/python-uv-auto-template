FROM python:3.10-bullseye

ENV DEBIAN_FRONTEND noninteractive
COPY pyproject.toml uv.loc[k] /
RUN curl -LsSf https://astral.sh/uv/install.sh | sh && \
    echo 'export PATH="/root/.local/bin:$PATH"' > ~/.bashrc && \
    export PATH="/root/.local/bin:$PATH" && \
    uv pip install --system -e . && \
    echo "/workspaces/{{cookiecutter.hyphenated}}/src/" > /usr/local/lib/python3.10/site-packages/{{cookiecutter.underscored}}.pth