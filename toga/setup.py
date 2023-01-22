#!/usr/bin/env python
from setuptools import setup

version = "0.3.0.dev39"

setup(
    version=version,
    extras_require={
        ':sys_platform=="win32"': [f"toga-winforms=={version}"],
        ':sys_platform=="linux"': [f"toga-gtk=={version}"],
        ':sys_platform=="darwin"': [f"toga-cocoa=={version}"],
    },
)
