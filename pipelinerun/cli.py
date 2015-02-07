import argparse
import sys

from .render import RendersTemplate
from .git import fetch_pipeline_sha


def create_run_script(args):
    r = RendersTemplate()
    pipeline_sha = args.sha if args.sha is not None else fetch_pipeline_sha()
    if not pipeline_sha:
        raise RuntimeError("Cannot determine pipeline sha, please specify")

    text = r.render(
        date=args.date,
        bias=args.bias,
        dark=args.dark,
        flat=args.flat,
        science=args.science,
        pipeline_sha=pipeline_sha,
        planetname=args.planet,
        camera_id=args.camera_id)

    args.output.write(text + '\n')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--date', required=True)
    parser.add_argument('-b', '--bias', nargs='+', required=True, type=int)
    parser.add_argument('-d', '--dark', nargs='+', required=True, type=int)
    parser.add_argument('-f', '--flat', nargs='+', required=True, type=int)
    parser.add_argument('-s', '--science', nargs='+', required=True, type=int)
    parser.add_argument('--sha', required=False)
    parser.add_argument('--planet', required=True)
    parser.add_argument('-c', '--camera_id', required=True, type=int)
    parser.add_argument('-o', '--output', type=argparse.FileType('w'),
                        nargs='?', default=sys.stdout)
    create_run_script(parser.parse_args())

if __name__ == '__main__':
    main()
