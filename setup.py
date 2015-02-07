from setuptools import setup, find_packages

setup(
    name='pipelinerun',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'render-pipelinescript.py = pipelinerun.cli:main',
        ],
    }
)
