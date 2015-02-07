from .templates import create_env


class RendersTemplate(object):
    def __init__(self):
        self.env = create_env()
