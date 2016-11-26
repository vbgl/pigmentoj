#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
    Not a formatter, for further processing.
"""

from setuptools import setup

entry_points = """
[pygments.formatters]
noformat = noformat:NoFormat
"""

setup(name = 'pygments-noformat',
  version  = '0.1',
  description  = __doc__,
  author       = "Vincent",
  packages     = ['noformat'],
  entry_points = entry_points)

