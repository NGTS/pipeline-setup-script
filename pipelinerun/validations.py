import os


suffixes = {
    'bias': ['biasFrames', ],
    'dark': ['darkFrames', ],
    'flat': ['flatField', ],
    'science': ['observeField', 'exposureCycle'],
}

data_root = os.path.join('/', 'ngts', 'testdata', 'paranal')


class NotFound(RuntimeError):

    def __init__(self, action_id, dirname_options):
        msg = 'Cannot find action {}. Tried {}'.format(action_id,
                                                       dirname_options)
        super(NotFound, self).__init__(msg)


def ensure_all_actions_available(bias, dark, flat, science):
    '''
    Given lists of actions, ensure the directories are all available on disk
    under /ngts/testdata/paranal
    '''
    keys = ['bias', 'dark', 'flat', 'science']
    for (key, values) in zip(keys, [bias, dark, flat, science]):
        for action_id in values:
            found = False
            dirname_options = [os.path.join(data_root,
                                            'action{action}_{suffix}'.format(
                                                action=action_id, suffix=suffix))
                               for suffix in suffixes[key]]
            for option in dirname_options:
                if os.path.isdir(option):
                    found = True
                    break
            if not found:
                raise NotFound(action_id, dirname_options)
