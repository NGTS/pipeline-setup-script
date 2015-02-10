try:
    from unittest import mock
except ImportError:
    import mock
import pytest

from pipelinerun import cli


@pytest.fixture
def valid_args():
    return ['--date', '2015/01/26', '-b', '101266',
            '-d', '101255', '-f', '101219', '101223', '-s', '101221',
            '--planet', 'wasp18', '-c', '803']


@pytest.fixture
def parser():
    return cli.create_parser()


@pytest.fixture
def args(parser, valid_args):
    return parser.parse_args(valid_args)


@mock.patch('pipelinerun.cli.argparse.ArgumentParser.exit')
def test_parse_args_help(exit, parser, capsys):
    parser.parse_args(['-h'])

    out, err = capsys.readouterr()
    assert 'usage:' in out
