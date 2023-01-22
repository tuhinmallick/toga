#!/usr/bin/env python
import re

from setuptools import setup

# Version handline needs to be programatic because
# we can't import toga_django to compute the version;
# and to support versioned subpackage dependencies
with open('toga_django/__init__.py', encoding='utf8') as version_file:
    if version_match := re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", version_file.read(), re.M
    ):
        version = version_match[1]
    else:
        raise RuntimeError("Unable to find version string.")

setup(
    version=version,
    description='A Django backend for the Toga widget toolkit.',
    install_requires=[
        'django~=3.0',
        'django-environ==0.4.1',
        f'toga-web=={version}',
    ],
)
