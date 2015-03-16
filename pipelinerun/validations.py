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


class NoFiles(RuntimeError):

    def __init__(self, path):
        msg = 'Cannot find any files in {}'.format(path)
        super(NoFiles, self).__init__(msg)


def ensure_all_actions_available(bias, dark, flat, science):
    '''
    Given lists of actions, ensure the directories are all available on disk
    under /ngts/testdata/paranal
    '''
    keys = ['bias', 'dark', 'flat', 'science']
    for (key, values) in zip(keys, [bias, dark, flat, science]):
        for action_id in values:
            found, action_path = False, None
            dirname_options = [os.path.join(data_root,
                                            'action{action}_{suffix}'.format(
                                                action=action_id, suffix=suffix))
                               for suffix in suffixes[key]]
            for option in dirname_options:
                if os.path.isdir(option):
                    found, action_path = True, option
                    break
            if not found:
                raise NotFound(action_id, dirname_options)
            else:
                files = os.listdir(action_path)
                if not len(files) > 0:
                    raise NoFiles(action_path)
