from pipelinerun.templates import create_env, clean_date


def test_template_loader():
    env = create_env()
    assert env.get_template('run-script.sh')


def test_clean_date():
    datestr = '2015/01/02'
    assert clean_date(datestr) == '20150102'
