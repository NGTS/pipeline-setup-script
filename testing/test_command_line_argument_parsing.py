try:
    from unittest import mock
except ImportError:
    import mock
import pytest

from pipelinerun import cli


@mock.patch('pipelinerun.cli.argparse.ArgumentParser.exit')
def test_parse_args_help(exit, capsys):
    parser = cli.create_parser()
    parser.parse_args(['-h'])

    out, err = capsys.readouterr()
    assert 'usage:' in out
