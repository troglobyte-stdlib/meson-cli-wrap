#!/usr/bin/env python3

#
# Troglobyte stdlib:
# author: Michael Gene Brockus
# Gmail: <mail: michaelbrockus@gmail.com>
#
from pathlib import Path
import subprocess


'''Meson version wrapper command class'''
class MesonVersion:
    '''Constructors are used to initialize the
    object’s state. The task of constructors is to
    initialize(assign values) to the data members
    of the class when an object of class is created.
    
    In this case anything for the meson test
    command.
    '''
    def __init__(self):
        super().__init__()
    # end of method

    '''Should run the process of the current command
    which in this case is to get the current version
    of the Meson build system background.
    '''
    def run(self, args: list = []):
        run_cmd = ['meson', '--version']
        process = subprocess.Popen(run_cmd, encoding='utf8', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return process.communicate()[0]
    # end of method

# end class
