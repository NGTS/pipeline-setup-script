import pytest
import os
import subprocess as sp
from contextlib import contextmanager

from pipelinerun.git import get_git_sha, chdir, fetch_pipeline_sha


@pytest.fixture
def setup_sha(tmpdir):
    with chdir(str(tmpdir)):
        sp.check_call(['git', 'init', '-q'])
        with open('test.txt', 'w') as outfile:
            pass
        sp.check_call(['git', 'add', '--all', '.'])
        sp.check_call(['git', 'commit', '-qm', 'Initial commit'])
        with open('.git/refs/heads/master') as infile:
            return str(tmpdir), infile.read().strip()


@contextmanager
def change_ngts_envar(value):
    _environ = dict(os.environ)
    try:
        os.environ['NGTS'] = value
        yield
    finally:
        os.environ.clear()
        os.environ.update(_environ)


def test_chdir(tmpdir):
    initial_dir = os.getcwd()
    with chdir(str(tmpdir)):
        assert os.getcwd() == str(tmpdir)
    assert os.getcwd() == initial_dir


def test_check_git_sha(setup_sha):
    path, expected_sha = setup_sha
    assert get_git_sha(path) == expected_sha


def test_fetch_pipeline_sha(tmpdir):
    containing_dir = os.path.join(str(tmpdir), 'pipeline', 'ZLP', 'zlp-script',
                                  '.git', 'refs', 'heads')
    with change_ngts_envar(str(tmpdir)):
        os.makedirs(containing_dir)
        with open(os.path.join(containing_dir, 'master'), 'w') as outfile:
            outfile.write('hello-world')

        sha = fetch_pipeline_sha()
        assert sha == 'hello-world'
