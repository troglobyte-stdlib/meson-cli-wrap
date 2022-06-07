#!/usr/bin/env python3

#
# Troglobyte stdlib:
# author: Michael Gene Brockus
# Gmail: <mail: michaelbrockus@gmail.com>
#
from libmesoncli.commands.install import MesonInstall
from libmesoncli.commands.subprojects import MesonSubprojects
from libmesoncli.commands.configure import MesonConfigure
from libmesoncli.commands.version import MesonVersion
from libmesoncli.commands.compile import MesonCompile
from libmesoncli.commands.clean import MesonClean
from libmesoncli.commands.setup import MesonSetup
from libmesoncli.commands.wrap import MesonWrap
from libmesoncli.commands.dist import MesonDist
from libmesoncli.commands.init import MesonInit
from libmesoncli.commands.test import MesonTest

from os.path import join as join_paths
from pathlib import Path


'''Meson build system command-line wrapper class'''
class MesonCLI:
    def __init__(self, srcdir: Path = Path().cwd(), builddir: Path = join_paths(Path().cwd(), 'builddir')) -> None:
        self._srcdir = srcdir
        self._builddir = builddir
    # end of method

    @property
    def srcdir(self):
        return self._srcdir
    # end of method

    @property
    def builddir(self):
        return self._builddir
    # end of method

    @srcdir.setter
    def srcdir(self, new_dir: Path):
        self._srcdir = new_dir
    # end of method

    @builddir.setter
    def builddir(self, new_dir: Path):
        self._builddir = new_dir
    # end of method

    def setup(self, args: list = []):
        return MesonSetup(self._srcdir, self._builddir).run(args)
    # end of method

    def subprojects(self, args: list = []):
        return MesonSubprojects(self._srcdir)
    # end of method

    def configure(self, args: list = []):
        return MesonConfigure(self._builddir).run(args)
    # end of method

    def compile(self, args: list = []):
        return MesonCompile(self._builddir).run(args)
    # end of method

    def install(self, args: list = []):
        return MesonInstall(self._builddir).run(args)
    # end of method

    def test(self, args: list = []):
        return MesonTest(self._builddir).run(args)
    # end of method

    def dist(self, args: list = []):
        return MesonDist(self._builddir).run(args)
    # end of method

    def wrap(self):
        return MesonWrap()
    # end of method

    def init(self, args: list = []):
        return MesonInit(self._srcdir).run(args)
    # end of method

    def version(self):
        return MesonVersion().run()
    # end of method

    def clean(self, args: list = []):
        return MesonClean(self._builddir).run(args)
    # end of method

# end of class
