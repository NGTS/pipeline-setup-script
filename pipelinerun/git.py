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
