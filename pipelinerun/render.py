from .templates import create_env, clean_date


class RendersTemplate(object):

    def __init__(self):
        self.env = create_env()

    def render(self, **kwargs):
        kwargs.update(run_name=self.run_name(kwargs))
        template = self.env.get_template('run-script.sh')
        return template.render(**kwargs)

    def run_name(self, kwargs):
        return '-'.join(map(str, [
            clean_date(kwargs['night']),
            kwargs['planetname'],
            kwargs['camera_id']]))
