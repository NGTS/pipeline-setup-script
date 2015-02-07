from unittest import mock
from pipelinerun import render

@mock.patch('pipelinerun.render.create_env')
def test_environment_loading(create_env):
    r = render.RendersTemplate()
    assert r.env == create_env.return_value


def test_render_contents():
    r = render.RendersTemplate()
    assert r.render(date='2015/01/01')
