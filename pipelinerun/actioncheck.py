import glob
import os

from .logging import get_logger

logger = get_logger(__name__)

ROOT_DIR = '/ngts/testdata/paranal'


def check_action(action):
    logger.debug('Checking action %s', action)
    glob_stub = '{root}/action{action}_*'.format(
        root=ROOT_DIR, action=action
    )
    logger.debug('Glob stub: %s', glob_stub)
    actions = glob.glob(glob_stub)
    return len(actions)


def check_actions(args):
    keys = ['bias', 'dark', 'flat', 'science']
    for key in keys:
        actions = getattr(args, key)
        for action in actions:
            if not check_action(action):
                logger.warning('Cannot find action {}'.format(action))
