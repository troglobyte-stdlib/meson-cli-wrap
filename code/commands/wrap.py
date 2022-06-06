#!/usr/bin/env python3

#
# Troglobyte stdlib:
# author: Michael Gene Brockus
# Gmail: <mail: michaelbrockus@gmail.com>
#
import subprocess


class MesonWrap:
    '''Meson wrap command wrapper class'''

    def __init__(self):
        '''Constructors are used to initialize the
        object’s state. The task of constructors is to
        initialize(assign values) to the data members
        of the class when an object of class is created.

        In this case anything for the meson wrap
        command.
        '''
        super().__init__()
    # end of method

    def update(self, wrap_args) -> None:
        '''Update a subproject wrap file is there is one
        in the subprojects directory.
        '''
        run_cmd = ['meson', 'wrap', 'update', wrap_args]
        process = subprocess.Popen(run_cmd, encoding='utf8', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return process.communicate()[0]
    # end of method

    def search(self, wrap_args) -> None:
        '''Should search the database for a wrap file'''
        run_cmd = ['meson', 'wrap', 'search', wrap_args]
        process = subprocess.Popen(run_cmd, encoding='utf8', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return process.communicate()[0]
    # end of method

    def info(self, wrap_args) -> None:
        '''Should get information on a wrap package'''
        run_cmd = ['meson', 'wrap', 'info', wrap_args]
        process = subprocess.Popen(run_cmd, encoding='utf8', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return process.communicate()[0]
    # end of method

    def install(self, wrap_args) -> None:
        '''Should install a wrap file from the dist, could
        be a github repo or a wrap package from the
        database'''
        run_cmd = ['meson', 'wrap', 'install', wrap_args]
        process = subprocess.Popen(run_cmd, encoding='utf8', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return process.communicate()[0]
    # end of method

    def list_wraps(self) -> None:
        '''Should list all wrap files in the current project'''
        run_cmd = ['meson', 'wrap', 'list']
        process = subprocess.Popen(run_cmd, encoding='utf8', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return process.communicate()[0]
    # end of method

    def status(self) -> None:
        '''Should get the status'''
        run_cmd = ['meson', 'wrap', 'status']
        process = subprocess.Popen(run_cmd, encoding='utf8', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return process.communicate()[0]
    # end of method

# end class
