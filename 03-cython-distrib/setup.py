from setuptools import setup
from Cython.Build import cythonize

# For documentation, see:
# https://cython.readthedocs.io/en/latest/src/userguide/source_files_and_compilation.html#basic-setup-py
# https://setuptools.readthedocs.io/en/latest/deprecated/distutils/setupscript.html?highlight=libraries#library-options

setup(
  ext_modules = cythonize(
      'integrate_f6.pyx',
      language_level=3,
  )
)
