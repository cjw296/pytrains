# Copyright (c) 2012 Simplistix Ltd
# See license.txt for license details.

import os, sys
from ConfigParser import RawConfigParser
from setuptools import setup, find_packages

name = 'pytrains'
base_dir = os.path.dirname(__file__)

# read test requirements from tox.ini
config = RawConfigParser()
config.read(os.path.join(base_dir, 'tox.ini'))
test_requires = []
for item in config.get('testenv', 'deps').split():
    test_requires.append(item)
# Tox doesn't need itself, but we need it for testing.
test_requires.append('tox')
    
setup(
    name=name,
    version='1.0dev',
    author='Chris Withers',
    author_email='chris@simplistix.co.uk',
    license='MIT',
    description="Parsers for UK train timetable data.",
    long_description='', #open(os.path.join(base_dir,'docs','description.txt')).read(),
    #url='http://github.com/cjw296/pytrains',
    classifiers=[
    #'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    ],    
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    entry_points = {
        'console_scripts': [
            'tester = pytrains.tester:main',
            'handler = pytrains.handler:main',
        ],
        },
    install_requires = (
        'fixed',
        ),
    extras_require=dict(
        test=test_requires,
        )
    )
