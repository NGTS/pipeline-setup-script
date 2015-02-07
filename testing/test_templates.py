from pipelinerun.templates import create_env


def test_template_loader():
    env = create_env()
    assert env.get_template('run-script.sh')
