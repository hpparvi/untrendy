#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import sys

from numpy.distutils.misc_util import get_numpy_include_dirs

try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

untrendy = Extension("untrendy._untrendy", ["untrendy/untrendy.c",
                                            "untrendy/_untrendy.c"],
                     include_dirs=["untrendy"] + get_numpy_include_dirs())

# Get the version number.
vre = re.compile("__version__ = \"(.*?)\"")
m = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      "untrendy", "__init__.py")).read()
version = vre.findall(m)[0]

setup(
    name="untrendy",
    url="https://github.com/dfm/untrendy",
    version=version,
    author="Dan Foreman-Mackey",
    author_email="danfm@nyu.edu",
    description="De-trending Kepler light curves in style",
    long_description=open("README.rst").read(),
    packages=["untrendy"],
    scripts=["bin/untrend"],
    package_data={"": ["README.rst", "LICENSE.rst"]},
    ext_modules=[untrendy],
    classifiers=[
        # "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
)
