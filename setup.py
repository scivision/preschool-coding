#!/usr/bin/env python
import setuptools  # noqa: F401
from numpy.distutils.core import setup, Extension

ext = [Extension(name="num", sources=["numerical.f90"], f2py_options=["--quiet"])]

setup(ext_modules=ext)
