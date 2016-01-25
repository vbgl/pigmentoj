#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
    Grey-scale style
"""

from setuptools import setup

entry_points = """
[pygments.styles]
gs = gs:GS
"""

setup(name = 'pygments-gs',
  version  = '0.1',
  description  = __doc__,
  author       = "Vincent",
  packages     = ['gs'],
  entry_points = entry_points)

