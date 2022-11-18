# SPDX-License-Identifier: Apache-2.0
# Copyright 2013-2022 The Foundry Visionmongers Ltd
from distutils.command.build_py import build_py
import logging
import os
from shutil import copyfile
from setuptools import setup

import openassetio_traitgen

# The python sources don't exist in this repo, but are generated via
# openassetio-traitgen at point of build.
# We generate them directly into the build directory structured as a
# package.
class GenerateThenBuild(build_py):
    def run(self):
        # Generate traits package directly into the package directory.
        openassetio_traitgen.generate(
            "traits.yml",
            self.build_lib,
            "python",
            lambda _: _,
            logging.Logger("openassetio-mediacreation-traitgen"),
            False,
            None,
        )

        # Move the source trait yaml to the package directory.
        copyfile(
            "traits.yml", os.path.join(self.build_lib, "openassetio_mediacreation", "traits.yml")
        )

        build_py.run(self)


setup(
    cmdclass={
        "build_py": GenerateThenBuild,
    },
)
