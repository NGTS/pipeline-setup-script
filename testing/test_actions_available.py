from unittest import mock

from pipelinerun import actioncheck


def test_actions_not_present():
    action = 101
    assert actioncheck.check_action(action) == False


@mock.patch('pipelinerun.actioncheck.glob.glob')
def test_actions_present(glob):
    glob.return_value = ['action101']
    action = 101
    assert actioncheck.check_action(action) == True
