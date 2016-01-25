# -*- coding: utf-8 -*-

"""
    Style gris
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic

class GS(Style):
    """
        A grey-scale style
    """
    default_style = ""
    styles = {
        Comment.Special:        '#444',
        Comment.Preproc:        '#000',
        Comment.Multiline:      'italic #444',
        Comment.Single:         'italic #444',
        Keyword:                '#444',
        Name.Builtin:           'bg:#eee #000',
        String:                 'italic #000'
    }
