from pipelinerun.templates import create_env, clean_date, add_spacings


def test_template_loader():
    env = create_env()
    assert env.get_template('run-script.sh')


def test_clean_date():
    datestr = '2015/01/02'
    assert clean_date(datestr) == '20150102'


def test_add_spacings():
    items = [10101, 10102, 10103]
    assert add_spacings(items) == '10101 10102 10103'
