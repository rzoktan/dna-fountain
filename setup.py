"""
Copyright (C) 2016 Yaniv Erlich
License: GPLv3-or-later. See COPYING file for details.
"""
#all .pyx files in a folder
# from distutils.core import setup
from setuptools import setup
from Cython.Build import cythonize

setup(
  name = 'MyProject',
  ext_modules = cythonize(
      module_list=['*.pyx'],
      compiler_directives={'language_level' : "3"}   # or "2" or "3str"
      ),
)
