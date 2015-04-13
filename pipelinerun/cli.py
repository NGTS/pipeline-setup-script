import argparse
import sys
import logging
import fetchactions.cli as fetchactions
from collections import namedtuple

from .actioncheck import check_actions
from .render import RendersTemplate
from .git import fetch_pipeline_sha
from .validations import ensure_all_actions_available
from .filepaths import default_filename


ActionList = namedtuple('ActionList', ['bias', 'dark', 'flat', 'science'])

def sanitise_planet_name(name):
    return (name.lower().replace(' ', '').replace('b', '').replace('-', '')
            .strip()) + 'b'


def render_default_file(night, planet_name, camera_id, text):
    default_script_location = default_filename(night=night,
                                               planet_name=planet_name,
                                               camera_id=camera_id)
    with open(default_script_location, 'w') as outfile:
        outfile.write(text + '\n')


def get_actions(args):
    try:
        result = fetchactions.fetch_night_info(args.camera_id, args.night)
    except fetchactions.NoResults as err:
        if (args.bias is None or
                args.dark is None or
                args.flat is None or
                args.science is None):
            raise RuntimeError('Could not find actions in the database '
                    'for the night specified. Please specify actions manually')
        else:
            return ActionList(args.bias, args.dark, args.flat, args.science)
    else:
        return ActionList(result['bias'], result['dark'],
                result['flat'], result['science'][args.field.upper()])

def create_run_script(args):
    action_listing = get_actions(args)
    ensure_all_actions_available(action_listing)
    r = RendersTemplate()
    pipeline_sha = args.sha if args.sha is not None else fetch_pipeline_sha()
    if not pipeline_sha:
        raise RuntimeError("Cannot determine pipeline sha, please specify")

    check_actions(action_listing)

    text = r.render(night=args.night,
                    bias=action_listing.bias,
                    dark=action_listing.dark,
                    flat=action_listing.flat,
                    science=action_listing.science,
                    pipeline_sha=pipeline_sha,
                    planetname=sanitise_planet_name(args.planet),
                    camera_id=args.camera_id)

    if args.output is None:
        render_default_file(night=args.night,
                            planet_name=sanitise_planet_name(args.planet),
                            camera_id=args.camera_id,
                            text=text)
    else:
        args.output.write(text + '\n')


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--night', required=True, help='Must match wiki night')
    parser.add_argument('-b', '--bias', nargs='+', required=False, type=int)
    parser.add_argument('-d', '--dark', nargs='+', required=False, type=int)
    parser.add_argument('-f', '--flat', nargs='+', required=False, type=int)
    parser.add_argument('-s', '--science', nargs='+', required=False, type=int)
    parser.add_argument('--sha', required=False)
    parser.add_argument('--planet', required=True)
    parser.add_argument('-c', '--camera_id', required=True, type=int)
    parser.add_argument('-F', '--field', required=True)
    parser.add_argument('-o', '--output',
                        type=argparse.FileType('w'),
                        required=False)
    return parser

def commandline_args(parser):
    args = parser.parse_args()
    return args


def main():
    parser = create_parser()
    create_run_script(parser.parse_args())


if __name__ == '__main__':
    main()
