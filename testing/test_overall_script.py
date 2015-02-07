from pipelinerun.cli import create_run_script


class Arguments(object):
    pass


def test_final_product(tmpdir):
    with open('testing/examples/run-40-wasp18b-20141105.sh') as infile:
        expected_contents = infile.read()

    args = Arguments()
    args.date = '2014/11/05'
    args.bias = [101141, ]
    args.dark = [101143, ]
    args.flat = [101126, ]
    args.science = [101140, ]
    args.sha = '59aa1ec756657430048c45beea8093ed724f5ea2'
    args.planetname = 'wasp18b'
    args.camera_id = 804
    args.output = str(tmpdir.join('out.sh'))

    create_run_script(args)

    with open(args.output) as infile:
        assert infile.read() == expected_contents
