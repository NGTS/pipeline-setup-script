import jinja2


def create_env():
    return jinja2.Environment(
        loader=jinja2.PackageLoader('pipelinerun', 'templates'))
