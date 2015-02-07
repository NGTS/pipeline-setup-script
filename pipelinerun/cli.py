import argparse

from .render import RendersTemplate


def create_run_script(args):
    r = RendersTemplate()
    text = r.render(
        date=args.date,
        bias=args.bias,
        dark=args.dark,
        flat=args.flat,
        science=args.science,
        pipeline_sha=args.pipeline_sha,
        planetname=args.planetname,
        camera_id=args.camera_id)

    with open(args.output, 'w') as outfile:
        outfile.write(text + '\n')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--date', required=True)
    parser.add_argument('-b', '--bias', nargs='+', required=True, type=int)
    parser.add_argument('-d', '--dark', nargs='+', required=True, type=int)
    parser.add_argument('-f', '--flat', nargs='+', required=True, type=int)
    parser.add_argument('-s', '--science', nargs='+', required=True, type=int)
    parser.add_argument('--sha', required=True)
    parser.add_argument('--planet', required=True)
    parser.add_argument('-c', '--camera_id', required=True, type=int)
    create_run_script(parser.parse_args())

if __name__ == '__main__':
    main()
