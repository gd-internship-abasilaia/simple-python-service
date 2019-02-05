from setuptools import setup
from datetime import datetime
import os
from setuptools.command.install import install as InstallCommand


class Install(InstallCommand):
    """ Customized setuptools install command which uses pip. """

    def run(self, *args, **kwargs):
        import pip
        pip.main(['install', '.'])
        InstallCommand.run(self, *args, **kwargs)

exec(open(os.path.join('version.py')).read())

setup(
    name="Python-Calculator",
    version="0.4-SNAPSHOT",
    packages=['calc'],
    scripts=[
        'calculator_app.py',
        'service.py',
        'README.md',
        'pycodestyle.sh'],
    install_requires=['Flask']
)
