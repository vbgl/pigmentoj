#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
    Coq Lexer
"""

from setuptools import setup

entry_points = """
[pygments.lexers]
coqlex = coqlex:CoqLex
"""

setup(name = 'pygments-coqlex',
  version  = '0.1',
  description  = __doc__,
  author       = "Vincent",
  packages     = ['coqlex'],
  entry_points = entry_points)

