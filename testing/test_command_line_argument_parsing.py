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
            '--planet', 'wasp-18b', '-c', '803']


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


def test_parse_args_multiple_actions(args):
    assert len(args.flat) == 2


@pytest.mark.parametrize('input',
                         ['WASP-18 b', 'WASP-18', 'WASP18', 'wasp18',
                          'wasp 18b'])
def test_sanitise_planet_name(input):
    assert cli.sanitise_planet_name(input) == 'wasp18b'
