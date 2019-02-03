from setuptools import setup 
from random import randint 
from setuptools.command.install import install as InstallCommand


class Install(InstallCommand):
    """ Customized setuptools install command which uses pip. """

    def run(self, *args, **kwargs):
        import pip
        pip.main(['install', '.'])
        InstallCommand.run(self, *args, **kwargs)


setup(
    name="Python-Calculator",
    version=(randint(0,40)),
    packages=['calc'],
    test_suite="tests",
    scripts=[
        'calculator_app.py',
        'service.py',
        'README.md',
        'pycodestyle.sh'],
    install_requires=['Flask']
)
