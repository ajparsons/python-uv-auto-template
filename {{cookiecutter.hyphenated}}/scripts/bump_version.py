#!/usr/bin/env python3
"""Bump the project version with uv."""

from __future__ import annotations

import argparse
import subprocess


def main() -> None:
    """Bump to a semantic version component or set an explicit version."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("version", help="major, minor, patch, or an explicit version")
    args = parser.parse_args()

    command = ["uv", "version"]
    if args.version in {"major", "minor", "patch"}:
        command.extend(["--bump", args.version])
    else:
        command.append(args.version)
    subprocess.run(command, check=True)


if __name__ == "__main__":
    main()
