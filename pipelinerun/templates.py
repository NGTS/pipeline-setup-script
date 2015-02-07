import jinja2


def create_env():
    env = jinja2.Environment(
        loader=jinja2.PackageLoader('pipelinerun', 'templates'))

    env.filters['clean_date'] = lambda x: x
    return env
