from approvaltests import set_default_reporter
from approvaltests.reporters.generic_diff_reporter import GenericDiffReporter, GenericDiffReporterConfig
from pytest import fixture


@fixture(scope="session", autouse=True)
def set_reporter():
    reporter = GenericDiffReporter(GenericDiffReporterConfig("PyCharm", "/usr/local/bin/pycharm", ["diff"]))
    set_default_reporter(reporter)
