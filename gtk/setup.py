#!/usr/bin/env python
import re

from setuptools import setup

# Version handline needs to be programatic because
# we can't import toga_gtk to compute the version;
# and to support versioned subpackage dependencies
with open("src/toga_gtk/__init__.py", encoding="utf8") as version_file:
    if version_match := re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", version_file.read(), re.M
    ):
        version = version_match[1]
    else:
        raise RuntimeError("Unable to find version string.")

setup(
    version=version,
    install_requires=[
        f"toga-core=={version}",
        "gbulb>=0.5.3",
        "pycairo>=1.17.0",
        "pygobject>=3.14.0",
    ],
)
