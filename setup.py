# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in rems/__init__.py
from rems import __version__ as version

setup(
	name='rems',
	version=version,
	description='Real Estate Management System',
	author='Atom Global',
	author_email='samad.abbasi99@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
