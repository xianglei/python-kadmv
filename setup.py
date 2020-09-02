#!/usr/bin/env python
# -*- coding: utf-8 -*-
import platform
try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension
from distutils.util import execute, newer
from distutils.spawn import spawn

#
# hack to support linking when running
#  python setup.py sdist
#

import os
del os.link

if newer('./src/getdate.y', './src/getdate.c'):
    execute(spawn, (['bison', '-y', '-o', './src/getdate.c', './src/getdate.y'],))

include_dirs = ["/usr/include", "/usr/include/et"]
if platform.system() == 'Darwin' or platform.system() == 'FreeBSD':
    include_dirs += ['/usr/local/include', '/usr/local/include/et']

setup(name='python-kadmV',
      version='0.1.7',
      description='Python module for kerberos admin (kadm5)',
      long_description_content_type="text/markdown",
      url='https://github.com/xianglei/python-kadmv',
      download_url='https://github.com/xianglei/python-kadmv/tarball/v0.1.5',
      author='xianglei',
      author_email='horseman@163.com',
      license='MIT',
      setup_requires=['wheel'],
      ext_modules=[
          Extension(
              "kadmin",
              libraries=["krb5", "kadm5clnt", "kdb5"],
              include_dirs=include_dirs,
              sources=[
                  "src/kadmin.c",
                  "src/PyKAdminErrors.c",
                  "src/PyKAdminObject.c",
                  "src/PyKAdminIterator.c",
                  "src/PyKAdminPrincipalObject.c",
                  "src/PyKAdminPolicyObject.c",
                  "src/PyKAdminCommon.c",
                  "src/PyKAdminXDR.c",
                  "src/getdate.c"
                  ],
              #extra_compile_args=["-O0"]
#
#               extra_compile_args=["--std=gnu89"]
#               )
#           ],
#       classifiers=[
#           "Development Status :: 4 - Beta",
#           "Environment :: Console",
#           "Intended Audience :: System Administrators",
#           "Intended Audience :: Developers",
#           "Operating System :: POSIX",
#           "Programming Language :: C",
#           "Programming Language :: Python",
#           "Programming Language :: YACC",
#           "License :: OSI Approved :: MIT License",
#           "Topic :: Software Development :: Libraries :: Python Modules",
#           "Topic :: System :: Systems Administration :: Authentication/Directory",
#           ]
#       )

# setup(name='python-kadmV-local',
#       version='0.1.5',
#       description='Python module for kerberos admin (kadm5) via root local interface',
#       url='https://github.com/xianglei/python-kadmv',
#       download_url='https://github.com/xianglei/python-kadmv/tarball/v0.1.5',
#       author='xianglei',
#       author_email='horseman@163.com',
#       license='MIT',
#       ext_modules=[
#
          ),
          Extension(
              "kadmin_local",
              libraries=["krb5", "kadm5srv", "kdb5"],
              include_dirs=include_dirs,
              sources=[
                  "src/kadmin.c",
                  "src/PyKAdminErrors.c",
                  "src/PyKAdminObject.c",
                  "src/PyKAdminIterator.c",
                  "src/PyKAdminPrincipalObject.c",
                  "src/PyKAdminPolicyObject.c",
                  "src/PyKAdminCommon.c",
                  "src/PyKAdminXDR.c",
                  "src/getdate.c"
                  ],
              extra_compile_args=["--std=gnu89"],
              define_macros=[('KADMIN_LOCAL', '')]
              )
          ],
      classifiers=[
          "Development Status :: 4 - Beta",
          "Environment :: Console",
          "Intended Audience :: System Administrators",
          "Intended Audience :: Developers",
          "Operating System :: POSIX",
          "Programming Language :: C",
          "Programming Language :: Python",
          "Programming Language :: YACC",
          "License :: OSI Approved :: MIT License",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: System :: Systems Administration :: Authentication/Directory",
          ]
      )

