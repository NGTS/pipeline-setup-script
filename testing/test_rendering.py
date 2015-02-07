from unittest import mock
from pipelinerun import render

@mock.patch('pipelinerun.render.create_env')
def test_environment_loading(create_env):
    r = render.RendersTemplate()
    assert r.env == create_env.return_value
