import os
from contextlib import contextmanager


@contextmanager
def chdir(new_path):
    old_path = os.getcwd()
    try:
        yield os.chdir(new_path)
    finally:
        os.chdir(old_path)


def get_git_sha(path):
    with chdir(path):
        with open('.git/refs/heads/master') as infile:
            return infile.read().strip()


def fetch_pipeline_sha():
    ngts_dir = os.environ['NGTS']
    pipeline_dir = os.path.realpath(os.path.join(
        ngts_dir, 'pipeline', 'ZLP', 'zlp-script'))
    if os.path.isdir(pipeline_dir):
        return get_git_sha(pipeline_dir)
