from pathlib import Path

from jinja2 import Environment, FileSystemLoader


def build_environment() -> Environment:
    directory = Path(__file__).parent / ".." / "templates"
    return Environment(loader=FileSystemLoader(directory), autoescape=True)


ENVIRONMENT = build_environment()
