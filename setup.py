#!/usr/bin/env python
"""Setup to install FileWaveAPI Python Module."""
from distutils.core import setup
setup(name='FileWaveAPI',
      version='0.1',
      py_modules=['FileWaveAPI'],
      install_requires=['requests', 'base64', 'json'],
      description='Provides functions to work with FileWave Restful API.',
      url='https://github.com/peshay/filewave',
      author='Andreas Hubert, censhare AG',
      author_email='andreas.hubert@censhare.com',
      license='MIT',
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers',
                   'Topic :: Software Development :: Libraries :: Application '
                   'Frameworks',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.2',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5', ],
      keywords='FileWave json api',

      )
