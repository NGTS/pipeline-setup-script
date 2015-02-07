import jinja2


def clean_date(datestr):
    return datestr.replace('/', '')

def create_env():
    env = jinja2.Environment(
        loader=jinja2.PackageLoader('pipelinerun', 'templates'))
    env.filters['clean_date'] = clean_date
    return env
