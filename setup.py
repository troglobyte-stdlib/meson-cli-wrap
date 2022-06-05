#!/usr/bin/env python3

#
# file: setup.py
# author: Michael Brockus
# gmail: <michaelbrockus@gmail.com>
#
from setuptools import setup


if __name__ == '__main__':
    setup(
        name='package',
        version='0.1.0',
        author='Michael Gene Brockus',
        license='Apache 2',
        zip_safe=True,
        url='https://github.com/troglobyte-coder/pypi_package_py',
        packages=[
            'code'
        ],
        python_requires='>=3.8')
