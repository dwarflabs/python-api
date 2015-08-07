# -*- coding: utf-8 -*-
import sys
from distutils.core import setup

f = open('README')
readme = f.read().strip()

f = open('LICENSE')
license = f.read().strip()

# For python 2.4 support
script_args = sys.argv[1:]
if (sys.version_info[0] <= 2) or (sys.version_info[0] == 2 and sys.version_info[1] <= 5):
    if 'install' in script_args and '--no-compile' not in script_args:
        script_args.append('--no-compile')


setup(
    name='shotgun_api3',
    version='3.0.16',
    description='Shotgun Python API ',
    long_description=readme,
    author='Shotgun Software',
    author_email='support@shotgunsoftware.com',
    url='https://github.com/shotgunsoftware/python-api',
    license=license,
    packages=['shotgun_api3', 'shotgun_api3.lib', 'shotgun_api3.lib.httplib2', 'shotgun_api3.lib.httplib3', 'shotgun_api3.lib.httplibtest', 'shotgun_api3.lib.simplejson'],
    script_args=script_args,
    include_package_data=True,
    package_data={'': [ 'cacerts.txt']},
    zip_safe=False,
)
