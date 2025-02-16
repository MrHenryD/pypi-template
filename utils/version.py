import click
import re
from enum import StrEnum


class Change(StrEnum):
    BREAKING = "breaking"
    FEATURE = "feature"
    PATCH = "patch"
    FIX = "fix"
    DOCS = "docs"


def bump_version(change: Change, version: str) -> str:
    version_parts = [int(v) for v in version.split(".")]
    if len(version_parts) != 3:
        raise ValueError(f"Invalid version format: {version}")

    match change:
        case Change.BREAKING:
            version_parts[0] += 1
        case Change.FEATURE:
            version_parts[1] += 1
        case Change.PATCH | Change.FIX:
            version_parts[2] += 1
        case Change.DOCS:
            pass

    return ".".join([str(v) for v in version_parts])


@click.command()
@click.argument(
    "change",
    type=Change,
)
@click.option(
    "-f",
    "--file-path",
    default="setup.py",
    type=click.Path(exists=True),
    help="Location of `setup.py`",
)
def update_version(change: Change, file_path: str):
    """Bump the version number in setup.py

    CHANGE: Type of Change. Used to increment MAJOR.MINOR.FIX versions

    """

    # Read the setup.py file
    with open(file_path, "r") as f:
        setup_content = f.read()

    # Find the version line in setup.py using regex
    match = re.search(r"version=['\"](\d+\.\d+\.\d+)['\"]", setup_content)
    if not match:
        click.echo("Version not found in setup.py.")
        return

    # Extract the current version
    current_version = match.group(1)
    click.echo(f"Current version: {current_version}")

    # Bump the version
    new_version = bump_version(change, current_version)
    click.echo(f"New version: {new_version}")

    # Replace the old version with the new version in the setup.py content
    updated_content = setup_content.replace(
        f'version="{current_version}"', f'version="{new_version}"'
    )

    # Write the updated content back to setup.py
    with open(file_path, "w") as f:
        f.write(updated_content)

    click.echo(f"Version bumped to {new_version} in {file_path}")


if __name__ == "__main__":
    update_version()
