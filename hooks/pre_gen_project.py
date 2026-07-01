#!/usr/bin/env python3
"""Pre-generation hook for the Marp slides project."""

import re
import sys


def validate_project_slug():
    project_slug = "{{ cookiecutter.project_slug }}"

    if not re.match(r"^[a-zA-Z][a-zA-Z0-9_-]*$", project_slug):
        print(
            "❌ Error: Project slug must start with a letter and contain only "
            "letters, numbers, hyphens, and underscores."
        )
        sys.exit(1)

    print(f"✅ Project slug '{project_slug}' is valid.")


def main():
    print("🔍 Validating cookiecutter parameters...")
    validate_project_slug()
    print("✅ All parameters are valid. Generating project...")


if __name__ == "__main__":
    main()
