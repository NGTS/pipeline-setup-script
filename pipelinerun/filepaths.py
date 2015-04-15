import os

ROOT_DIR = os.path.join('/', 'ngts', 'pipedev', 'ParanalOutput',
                        'running-the-pipeline', 'run-scripts')


def default_filename(night, planet_name, camera_id):
    file_stub = '{night}-{planet_name}-{camera_id}.sh'.format(
        night=night,
        planet_name=planet_name,
        camera_id=camera_id)
    return os.path.join(ROOT_DIR, file_stub)
