import nox

nox.options.sessions = ["check", "format", "lint", "tests"]


@nox.session()
def check(session: nox.Session) -> None:
    session.run("mypy", ".", external=True)


@nox.session()
def format(session: nox.Session) -> None:
    session.run("ruff", "format", ".", external=True)


@nox.session()
def lint(session: nox.Session) -> None:
    session.run("ruff", "check", ".", "--fix", external=True)


@nox.session()
def tests(session: nox.Session) -> None:
    session.run("pytest", external=True)


@nox.session()
def make_docs(session: nox.Session) -> None:
    session.run("mkdocs", "build", external=True)


@nox.session()
def install_pre_commit_hook(session: nox.Session) -> None:
    session.run("pre-commit", "install", external=True)
