def create_run_script(args):
    with open(args.output, 'w') as outfile:
        with open('testing/examples/run-40-wasp18b-20141105.sh') as infile:
            outfile.write(infile.read())

