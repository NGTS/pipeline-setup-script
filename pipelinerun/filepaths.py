import os

ROOT_DIR = os.path.join('/', 'ngts', 'pipedev', 'ParanalOutput',
                        'running-the-pipeline', 'run-scripts')


def default_filename(date, planet_name, camera_id):
    file_stub = '{date}-{planet_name}-{camera_id}.sh'.format(
        date=date,
        planet_name=planet_name,
        camera_id=camera_id)
    return os.path.join(ROOT_DIR, file_stub)
