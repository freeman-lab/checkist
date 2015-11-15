#!/usr/bin/env python

from setuptools import setup
import checkist

setup(
    name='checkist',
    version=checkist.__version__,
    description='minimal module for argument checking',
    author='freeman-lab',
    author_email='the.freeman.lab@gmail.com',
    packages=['checkist'],
    url='https://github.com/freeman-lab/checkist',
    install_requires=open('requirements.txt').read().split(),
    long_description='See https://github.com/freeman-lab/checkist'
)
