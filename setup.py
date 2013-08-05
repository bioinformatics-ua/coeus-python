# -*- coding: utf-8 -*-

'''
coeus-python - coeus API client for Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**coeus-python** is the un-official Python client for the coeus API.

This package allows usage of the coeus API from a programmatically from Python modules.

Install it with::

    $ pip install coeus

:copyright: (c) 2013, Luis A. Bastiao Silva, Universidade de Aveiro
:license: Creative Commons Attribution-Noncommercial


Resources
^^^^^^^^^


* `About coeus <http://bioinformatics.ua.pt/coeus/>`_

'''


import sys
from distutils.core import setup

__version__ = '0.1-dev'


if sys.version_info < (2, 7):
    raise NotImplementedError('Sorry, you need Python 2.7 or '
                              'Python 3.x to use `coeus-python`.')


# We cannot simply import coeus; coeus.__version__ because requests might
# not be installed and we would fail with an ImportError
def get_version(filepath='coeus.py'):
    import re
    VERSION_REGEX = re.compile(r"^__version__ = '(\d+\.\d+\.\d+(-dev)?)'$")

    with open(filepath, 'rt') as infile:
        for line in infile:
            match = VERSION_REGEX.match(line)
            if match:
                return match.group(1)
    raise ValueError("Could not find version in file %s" % filepath)


setup(name='coeus',
      description='coeus API client for Python.',
      long_description=__doc__,
      version=__version__,
      author='Luis A. Bastiao Silva',
      author_email='bastiao@ua.pt',
      license='CC-BY-NC',
      url='http://bioinformatics.ua.pt/coeus/',
      download_url='http://bioinformatics.ua.pt/coeus/',
      
      install_requires=['requests>=1.2.0'],
      py_modules=['coeus'],
      scripts=['coeus.py'],
      platforms='any',
      classifiers=[
          'Intended Audience :: Science/Research',
          'Intended Audience :: Developers',
          'Topic :: Software Development',
          'Topic :: Scientific/Engineering',
          'Topic :: Scientific/Engineering :: Bio-Informatics',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3'],
      keywords=[
          'coeus',
      ],
      )
