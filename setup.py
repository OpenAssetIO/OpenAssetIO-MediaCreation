# SPDX-License-Identifier: Apache-2.0
# Copyright 2013-2022 The Foundry Visionmongers Ltd
from setuptools import setup, find_packages

setup(
    name="openassetio_mediacreation",
    version="0.0.0",
    package_dir={"": "python"},
    packages=find_packages(where="python"),
    python_requires=">=3.9.1",
)
