import pytest
import os
import subprocess as sp

from pipelinerun.git import get_git_sha, chdir


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


def test_chdir(tmpdir):
    initial_dir = os.getcwd()
    with chdir(str(tmpdir)):
        assert os.getcwd() == str(tmpdir)
    assert os.getcwd() == initial_dir


def test_check_git_sha(setup_sha):
    path, expected_sha = setup_sha
    assert get_git_sha(path) == expected_sha
