#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
    Goto Lexer
"""

from setuptools import setup

entry_points = """
[pygments.lexers]
gotolex = gotolex:GotoLex
"""

setup(name = 'pygments-gotolex',
  version  = '0.1',
  description  = __doc__,
  author       = "Vincent",
  packages     = ['gotolex'],
  entry_points = entry_points)

