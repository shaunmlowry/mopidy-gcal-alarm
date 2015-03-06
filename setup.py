from __future__ import unicode_literals

import re

from setuptools import find_packages, setup


def get_version(filename):
    content = open(filename).read()
    metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", content))
    return metadata['version']


setup(
    name='Mopidy-GCal-Alarm',
    version=get_version('mopidy_gcal-alarm/__init__.py'),
    url='https://github.com/shaunmlowry/mopidy-gcal-alarm',
    license='Apache License, Version 2.0',
    author='Shaun Lowry',
    author_email='shaun@monolith.co.uk',
    description='Mopidy extension for running a GCal Alarm Clock on a Raspberry Pi',
    long_description=open('README.rst').read(),
    packages=find_packages(exclude=['tests', 'tests.*']),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'setuptools',
        'Mopidy >= 0.18',
        'Pykka >= 1.1',
    ],
    entry_points={
        'mopidy.ext': [
            'gcal-alarm = mopidy_gcal-alarm:Extension',
        ],
    },
    classifiers=[
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Multimedia :: Sound/Audio :: Players',
    ],
)
