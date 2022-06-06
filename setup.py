#!/usr/bin/env python3

#
# file: setup.py
# author: Michael Brockus
# gmail: <michaelbrockus@gmail.com>
#
from setuptools import setup


if __name__ == '__main__':
    setup(
        name='meson-cli-wrap',
        version='0.1.0',
        author='Michael Gene Brockus',
        license='Apache 2',
        zip_safe=True,
        url='https://github.com/troglobyte-stdlib/meson-cli-wrap',
        packages=[
            'code',
            'code.mesoncli'
        ],
        python_requires='>=3.8')
