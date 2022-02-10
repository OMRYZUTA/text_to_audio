import sys
import pytest
from src.engine.parsers.arguments_parser import ArgumentsParser


@pytest.fixture
def argument_parser():
    return ArgumentsParser()


class TestCaseArgumentsParser:

    @pytest.fixture(scope='class')
    def append_argv_files(self):
        sys.argv.append("file1")
        sys.argv.append("file2")

    def test_using_parse_returns_two_items(self, argument_parser, append_argv_files):
        assert 2 == len(argument_parser.parse())
