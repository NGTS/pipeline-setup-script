from unittest import mock
import pytest

from pipelinerun.cli import create_run_script, create_parser


class Arguments(object):
    pass


@pytest.fixture
def args():
    args = Arguments()
    args.date = '2014/11/05'
    args.bias = [101141, ]
    args.dark = [101143, ]
    args.flat = [101126, ]
    args.science = [101140, ]
    args.sha = '59aa1ec756657430048c45beea8093ed724f5ea2'
    args.planet = 'WASP-18 b'
    args.camera_id = 804
    return args


@mock.patch('pipelinerun.cli.fetch_pipeline_sha', return_value=None)
def test_bad_sha_passed(pipeline_sha, args):
    args.sha = None
    with pytest.raises(RuntimeError) as err:
        create_run_script(args)

    assert 'Cannot determine pipeline sha' in str(err)


def test_final_product(tmpdir, args):
    with open('testing/examples/run-40-wasp18b-20141105.sh') as infile:
        expected_contents = infile.read()

    output_filename = str(tmpdir.join('out.sh'))

    with open(output_filename, 'w') as outfile:
        args.output = outfile
        create_run_script(args)

    with open(output_filename) as infile:
        assert infile.read() == expected_contents


@mock.patch('pipelinerun.cli.argparse.ArgumentParser', autospec=True)
def test_create_parser(ArgumentParser):
    parser = create_parser()
    ArgumentParser.return_value.add_argument.assert_any_call(
        '--date', required=True)
