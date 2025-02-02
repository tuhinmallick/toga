#/usr/bin/env python
import io
import re

from setuptools import setup, find_packages

with io.open('toga_win32/__init__.py', encoding='utf8') as version_file:
    if version_match := re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", version_file.read(), re.M
    ):
        version = version_match[1]
    else:
        raise RuntimeError("Unable to find version string.")


with io.open('README.rst', encoding='utf8') as readme:
    long_description = readme.read()


setup(
    name='toga-win32',
    version=version,
    description='A Win32 (Microsoft Windows) backend for the Toga widget toolkit.',
    long_description=long_description,
    author='Russell Keith-Magee',
    author_email='russell@keith-magee.com',
    url='http://beeware.org/toga',
    packages=find_packages(exclude='tests'),
    python_requires='>=3.5',
    install_requires=[f'toga-core=={version}'],
    tests_require=[f'toga-dummy=={version}'],
    license='New BSD',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Environment :: Win32 (MS Windows)',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Software Development :: Widget Sets',
    ],
    test_suite='tests',
)
