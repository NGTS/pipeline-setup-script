from .templates import create_env


class RendersTemplate(object):
    def __init__(self):
        self.env = create_env()

    def render(self, **kwargs):
        template = self.env.get_template('run-script.sh')
        return template.render(**kwargs)
