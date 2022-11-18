# SPDX-License-Identifier: Apache-2.0
# Copyright 2013-2022 The Foundry Visionmongers Ltd
from setuptools import setup, find_packages

setup(
    package_dir={"": "python"},
    packages=find_packages(where="python"),
    install_requires=["openassetio>=1.0.0a6"]
)
