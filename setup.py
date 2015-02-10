from setuptools import setup, find_packages

setup(
    name='pipelinerun',
    packages=find_packages(),
    install_requires=['jinja2', ],
    entry_points={
        'console_scripts': [
            'render-pipelinescript.py = pipelinerun.cli:main',
        ],
    }
)
