#!/usr/bin/env python3

#
# Troglobyte stdlib:
# author: Michael Gene Brockus
# Gmail: <mail: michaelbrockus@gmail.com>
#
from code.mesoncli import MesonCLI as Meson

from os.path import join as join_paths
import subprocess
import functools
import unittest
import shutil
import os

import pytest


class CIUtility:
    def is_ci(self):
        if 'CI' in os.environ:
            return True
        return False

    def is_pull(self):
        # Travis
        if os.environ.get('TRAVIS_PULL_REQUEST', 'false') != 'false':
            return True
        # Azure
        if 'SYSTEM_PULLREQUEST_ISFORK' in os.environ:
            return True
        return False

    @staticmethod
    def _git_init():
        #
        # TODO: impl GitUtility and Git wrapper class
        subprocess.Popen(['git', 'init'], stderr=subprocess.PIPE).communicate()[0]
        subprocess.Popen(['git', 'config', 'user.name', 'Author Person'], stderr=subprocess.PIPE).communicate()[0]
        subprocess.Popen(['git', 'config', 'user.email', 'teh_coderz@example.com'], stderr=subprocess.PIPE).communicate()[0]
        subprocess.Popen(['git', 'add', '*'], stderr=subprocess.PIPE).communicate()[0]
        subprocess.Popen(['git', 'commit', '-a', '-m', 'I am a project'], stderr=subprocess.PIPE).communicate()[0]

    def skip_if_no_git(self, f):
        '''
        Skip this test if no git is found, unless we're on CI.
        This allows users to run our test suite without having
        git installed on, f.ex., macOS, while ensuring that our CI does not
        silently skip the test because of misconfiguration.
        '''
        @functools.wraps(f)
        def wrapped(self, *args, **kwargs):
            if not self.is_ci() and shutil.which('git') is None:
                raise unittest.SkipTest('Git not found')
            return f(*args, **kwargs)
        return

TEST_WRAP: str = '''\
[wrap-file]
directory = sqlite-amalgamation-3080802
source_url = http://sqlite.com/2015/sqlite-amalgamation-3080802.zip
source_filename = sqlite-amalgamation-3080802.zip
source_hash = 5ebeea0dfb75d090ea0e7ff84799b2a7a1550db3fe61eb5f6f61c2e971e57663
patch_url = https://wrapdb.mesonbuild.com/v1/projects/sqlite/3080802/5/get_zip
patch_filename = sqlite-3080802-5-wrap.zip
patch_hash = d66469a73fa1344562d56a1d7627d5d0ee4044a77b32d16cf4bbb85741d4c9fd
'''

info = '''\
Meson-UI is an open source build GUI meant to be both extremely fast,
and, even more importantly, as user friendly as possible.
The main design point of Meson-UI is to provide a standalone portable
build GUI and allow the user to access all or most of Meson build
systems features.
'''

class TestMeson:

    def test_change_srcdir(self):
        meson = Meson('test/dir/one', 'test/dir/one/builddir')

        assert(meson.srcdir == 'test/dir/one')
        assert(meson.builddir == 'test/dir/one/builddir')

        meson.srcdir = 'test/dir/two'
        meson.builddir = 'test/dir/two/builddir'

        assert(meson.srcdir == 'test/dir/two')
        assert(meson.builddir == 'test/dir/two/builddir')

    def test_setup_command(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        meson: Meson = Meson(srcdir=tmpdir, builddir=(tmpdir / 'builddir'))

        meson.init(['--language=c', '--type=executable'])
        meson.setup(['--backend=ninja'])

        #
        # Run asserts to check it is working
        assert tmpdir.join('meson.build').ensure()
        assert tmpdir.join('builddir', 'build.ninja').ensure()
        assert tmpdir.join('builddir', 'compile_commands.json').ensure()

    def test_configure_command(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        meson: Meson = Meson(srcdir=tmpdir, builddir=(tmpdir / 'builddir'))

        meson.init(['--language=c', '--type=executable'])
        meson.setup(['--backend=ninja'])
        meson.configure(['--werror', '--buildtype=minsize'])

        #
        # Run asserts to check it is working
        assert tmpdir.join('meson.build').ensure()
        assert tmpdir.join('builddir', 'build.ninja').ensure()
        assert tmpdir.join('builddir', 'compile_commands.json').ensure()

    def test_rebuild_command(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        meson: Meson = Meson(srcdir=tmpdir, builddir=(tmpdir / 'builddir'))

        meson.init(['--language=c', '--type=executable'])
        meson.setup(['--backend=ninja'])
        meson.compile()

        meson.setup(['--wipe'])

        #
        # Run asserts to check it is working
        assert tmpdir.join('meson.build').ensure()
        assert tmpdir.join('builddir', 'build.ninja').ensure()
        assert tmpdir.join('builddir', 'compile_commands.json').ensure()

    def test_compile_command(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        meson: Meson = Meson(srcdir=tmpdir, builddir=(tmpdir / 'builddir'))

        meson.init(['--language=c', '--type=executable'])
        meson.setup(['--backend=ninja'])
        meson.compile()

        #
        # Run asserts to check it is working
        assert tmpdir.join('meson.build').ensure()
        assert tmpdir.join('builddir', 'build.ninja').ensure()
        assert tmpdir.join('builddir', 'compile_commands.json').ensure()

    def test_clean_command(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        meson: Meson = Meson(srcdir=tmpdir, builddir=(tmpdir / 'builddir'))

        meson.init(['--language=c', '--type=executable'])
        meson.setup(['--backend=ninja'])
        meson.compile()
        meson.clean()

        #
        # Run asserts to check it is working
        assert tmpdir.join('meson.build').ensure()
        assert tmpdir.join('builddir', 'build.ninja').ensure()
        assert tmpdir.join('builddir', 'compile_commands.json').ensure()

    def test_install_command(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        meson: Meson = Meson(srcdir=tmpdir, builddir=(tmpdir / 'builddir'))

        meson.init(['--language=c', '--type=executable'])
        meson.setup(['--backend=ninja'])
        meson.compile()
        meson.install()

        #
        # Run asserts to check it is working
        assert tmpdir.join('meson.build').ensure()
        assert tmpdir.join('builddir', 'build.ninja').ensure()
        assert tmpdir.join('builddir', 'compile_commands.json').ensure()

    def test_mtest_command(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        meson: Meson = Meson(srcdir=tmpdir, builddir=(tmpdir / 'builddir'))

        meson.init(['--language=c', '--type=executable'])
        meson.setup(['--backend=ninja'])
        meson.compile()
        meson.test()

        #
        # Run asserts to check it is working
        assert tmpdir.join('meson.build').ensure()
        assert tmpdir.join('builddir', 'build.ninja').ensure()
        assert tmpdir.join('builddir', 'compile_commands.json').ensure()

    @pytest.mark.skipif(not shutil.which('git'), reason='Did not find "git" on this system')
    def test_mdist_command(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        meson: Meson = Meson(srcdir=tmpdir, builddir=(tmpdir / 'builddir'))

        meson.init(['--language=c', '--type=executable'])
        meson.setup(['--backend=ninja'])
        meson.compile()

        CIUtility._git_init()
        meson.dist()

        #
        # Run asserts to check it is working
        assert tmpdir.join('meson.build').ensure()
        assert tmpdir.join('builddir', 'build.ninja').ensure()
        assert tmpdir.join('builddir', 'compile_commands.json').ensure()
        assert tmpdir.join('builddir', 'meson-dist', 'test_mdist_command0-0.1.tar.xz').ensure()

    def test_init_command(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        meson: Meson = Meson(srcdir=tmpdir, builddir=(tmpdir / 'builddir'))

        meson.init(['--language=c'])
        meson.setup()
        meson.compile()
        meson.test()

        #
        # Run asserts to check it is working
        assert tmpdir.join('meson.build').ensure()
        assert tmpdir.join('builddir', 'build.ninja').ensure()
        assert tmpdir.join('builddir', 'compile_commands.json').ensure()

    @pytest.mark.skipif(not shutil.which('git'), reason='Did not find "git" on this system')
    def test_subproject_checkout_subcommand(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        meson: Meson = Meson(srcdir=tmpdir, builddir=(tmpdir / 'builddir'))
        meson.init(['--language=c', '--deps', 'samplesubproject'])
        os.mkdir('subprojects')

        tmpdir.join(join_paths('subprojects', 'samplesubproject.wrap')).write('''\
        [wrap-git]
        directory=samplesubproject
        url=https://github.com/jpakkane/samplesubproject.git
        revision=head
        ''')

        meson.subprojects().download('samplesubproject')
        meson.subprojects().checkout('master', 'samplesubproject')

        #
        # Run asserts to check it is working
        assert tmpdir.join('meson.build').ensure()
        assert tmpdir.join('subprojects', 'samplesubproject.wrap').ensure()
        assert tmpdir.join('subprojects', 'samplesubproject', '.gitignore').ensure()
        assert tmpdir.join('subprojects', 'samplesubproject', 'README.md').ensure()

    def test_subproject_update_subcommand(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        meson: Meson = Meson(srcdir=tmpdir, builddir=(tmpdir / 'builddir'))
        meson.init(['--language=c', '--deps', 'sqlite'])
        os.mkdir('subprojects')

        tmpdir.join(join_paths('subprojects', 'sqlite.wrap')).write(TEST_WRAP)

        meson.subprojects().download('sqlite')
        meson.subprojects().update('sqlite')

        #
        # Run asserts to check it is working
        assert tmpdir.join('meson.build').ensure()
        assert tmpdir.join('subprojects', 'sqlite.wrap').ensure()

    def test_subproject_download_subcommand(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        meson: Meson = Meson(srcdir=tmpdir, builddir=(tmpdir / 'builddir'))
        meson.init(['--language=c', '--deps', 'sqlite'])
        os.mkdir('subprojects')

        tmpdir.join(join_paths('subprojects', 'sqlite.wrap')).write(TEST_WRAP)

        meson.subprojects().download('sqlite')

        #
        # Run asserts to check it is working
        assert tmpdir.join('meson.build').ensure()
        assert tmpdir.join('subprojects', 'sqlite.wrap').ensure()

    def test_wrap_info_subcommand(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        meson: Meson = Meson(srcdir=tmpdir, builddir=(tmpdir / 'builddir'))
        meson.init(['--language=c', '--deps', 'sqlite'])
        os.mkdir('subprojects')

        tmpdir.join(join_paths('subprojects', 'sqlite.wrap')).write(TEST_WRAP)

        meson.wrap().info('sqlite')

        #
        # Run asserts to check it is working
        assert tmpdir.join('meson.build').ensure()
        assert tmpdir.join('subprojects', 'sqlite.wrap').ensure()

    def test_wrap_search_subcommand(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        meson: Meson = Meson(srcdir=tmpdir, builddir=(tmpdir / 'builddir'))
        meson.init(['--language=c', '--deps', 'sqlite'])
        os.mkdir('subprojects')

        tmpdir.join(join_paths('subprojects', 'sqlite.wrap')).write(TEST_WRAP)

        meson.wrap().search('sqlite')

        #
        # Run asserts to check it is working
        assert tmpdir.join('meson.build').ensure()
        assert tmpdir.join('subprojects', 'sqlite.wrap').ensure()

    def test_wrap_install_subcommand(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        meson: Meson = Meson(srcdir=tmpdir, builddir=(tmpdir / 'builddir'))
        meson.init(['--language=c', '--deps', 'sqlite'])
        os.mkdir('subprojects')

        meson.wrap().install('sqlite')

        #
        # Run asserts to check it is working
        assert tmpdir.join('meson.build').ensure()
        assert tmpdir.join('subprojects', 'sqlite.wrap').ensure()

    def test_wrap_status_subcommand(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        meson: Meson = Meson(srcdir=tmpdir, builddir=(tmpdir / 'builddir'))
        meson.init(['--language=c', '--deps', 'sqlite'])
        os.mkdir('subprojects')

        tmpdir.join(join_paths('subprojects', 'sqlite.wrap')).write(TEST_WRAP)

        meson.wrap().status()

        #
        # Run asserts to check it is working
        assert tmpdir.join('meson.build').ensure()
        assert tmpdir.join('subprojects', 'sqlite.wrap').ensure()

    def test_wrap_update_subcommand(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        meson: Meson = Meson(srcdir=tmpdir, builddir=(tmpdir / 'builddir'))
        meson.init(['--language=c', '--deps', 'sqlite'])
        os.mkdir('subprojects')

        tmpdir.join(join_paths('subprojects', 'sqlite.wrap')).write(TEST_WRAP)

        meson.wrap().update('sqlite')

        #
        # Run asserts to check it is working
        assert tmpdir.join('meson.build').ensure()
        assert tmpdir.join('subprojects', 'sqlite.wrap').ensure()

    def test_wrap_list_subcommand(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        meson: Meson = Meson(srcdir=tmpdir, builddir=(tmpdir / 'builddir'))
        meson.init(['--language=c', '--deps', 'sqlite'])
        os.mkdir('subprojects')

        tmpdir.join(join_paths('subprojects', 'sqlite.wrap')).write(TEST_WRAP)

        meson.wrap().list_wraps()

        #
        # Run asserts to check it is working
        assert tmpdir.join('meson.build').ensure()
        assert tmpdir.join('subprojects', 'sqlite.wrap').ensure()
