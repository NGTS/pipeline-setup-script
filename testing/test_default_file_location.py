import os

from pipelinerun import filepaths as f


def test_default_name():
    date = '20150131'
    planet_name = 'wasp19b'
    camera_id = 802

    expected = os.path.realpath(os.path.join(os.path.dirname(__file__), '..',
                                             'run-scripts',
                                             '20150131-wasp19b-802.sh'))

    assert f.default_filename(date=date,
                              planet_name=planet_name,
                              camera_id=camera_id) == expected
