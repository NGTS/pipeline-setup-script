import jinja2


def clean_date(datestr):
    return datestr.replace('/', '')


def add_spacings(items):
    return ' '.join(map(str, items))


def create_env():
    env = jinja2.Environment(
        loader=jinja2.PackageLoader('pipelinerun', 'templates'))
    env.filters['clean_date'] = clean_date
    env.filters['add_spacings'] = add_spacings
    return env
