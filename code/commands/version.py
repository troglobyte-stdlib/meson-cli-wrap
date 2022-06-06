#!/usr/bin/env python3

#
# Troglobyte stdlib:
# author: Michael Gene Brockus
# Gmail: <mail: michaelbrockus@gmail.com>
#
import subprocess


class MesonVersion:
    '''Meson version wrapper command class'''

    def __init__(self):
        '''Constructors are used to initialize the
        object’s state. The task of constructors is to
        initialize(assign values) to the data members
        of the class when an object of class is created.

        In this case anything for the meson test
        command.
        '''
        super().__init__()
    # end of method

    def run(self, args: list = []):
        '''Should run the process of the current command
        which in this case is to get the current version
        of the Meson build system background.
        '''
        run_cmd = ['meson', '--version']
        process = subprocess.Popen(run_cmd, encoding='utf8', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return process.communicate()[0]
    # end of method

# end class
