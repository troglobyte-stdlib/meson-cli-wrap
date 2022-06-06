#!/usr/bin/env python3

#
# Troglobyte stdlib:
# author: Michael Gene Brockus
# Gmail: <mail: michaelbrockus@gmail.com>
#
from pathlib import Path
import subprocess


class MesonClean:
    '''Meson clean command wrapper class'''

    def __init__(self, builddir: Path):
        '''Constructors are used to initialize the
        object’s state. The task of constructors is to
        initialize(assign values) to the data members
        of the class when an object of class is created.

        In this case anything for the --clean switch from
        the meson compile command.
        '''
        self._builddir: Path = builddir
        super().__init__()
    # end of method

    def run(self, args: list = []):
        '''Should run the process of the current command
        which in this case is to clean the build directory
        with the --clean switch from the compile command.
        '''
        run_cmd = ['meson', 'compile', '--clean', '-C', str(self._builddir)]
        process = subprocess.Popen(run_cmd, encoding='utf8', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return process.communicate()[0]
    # end of method

# end class
