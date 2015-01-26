# coding: utf-8
from distutils.core import setup
from distutils.command.install import install
from distutils.command.build import build
from setuptools import find_packages
from service import __app_version__, __author__, __project_name__


class Install(install):
    def run(self):
        install.run(self)


class Build(build):
    def run(self):
        build.run(self)


setup(
    name=__project_name__,
    version=__app_version__,
    author=__author__,
    author_email='email@example.org',
    description='Service description',
    packages=find_packages(),
    install_requires=[
        'tornado==4.0.2',
        'pyyaml==3.11',
    ],

    data_files=[],

    cmdclass={
        'install': Install,
        'build': Build,
    },
)