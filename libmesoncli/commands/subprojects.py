#!/usr/bin/env python3

#
# Troglobyte stdlib:
# author: Michael Gene Brockus
# Gmail: <mail: michaelbrockus@gmail.com>
#
from pathlib import Path
import subprocess


class MesonSubprojects:
    '''Meson subprojects command wrapper class'''

    def __init__(self, srcdir: Path):
        '''Constructors are used to initialize the
        object’s state. The task of constructors is to
        initialize(assign values) to the data members
        of the class when an object of class is created.

        In this case anything for the meson subprojects
        command.
        '''
        self._srcdir: Path = srcdir
        super().__init__()
    # end of method

    def update(self, subproject):
        '''update current subprojects to the latest version'''
        run_cmd = ['meson', 'subprojects', 'update', subproject, '--sourcedir', str(self._srcdir)]
        process = subprocess.Popen(run_cmd, encoding='utf8', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return process.communicate()[0]
    # end of method

    def checkout(self, branch: str, subproject):
        '''Should checkout a branch in a project repo'''
        run_cmd = ['meson', 'subprojects', 'checkout', branch, subproject, '--sourcedir', str(self._srcdir)]
        process = subprocess.Popen(run_cmd, encoding='utf8', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return process.communicate()[0]
    # end of method

    def download(self, subproject):
        '''Should download subprojects ahead of time'''
        run_cmd = ['meson', 'subprojects', 'download', subproject, '--sourcedir', str(self._srcdir)]
        process = subprocess.Popen(run_cmd, encoding='utf8', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return process.communicate()[0]
    # end of method

# end class
