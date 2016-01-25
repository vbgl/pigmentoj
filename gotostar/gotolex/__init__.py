# -*- coding: utf-8 -*-

"""
    A Goto lexer
"""

from pygments.lexer import RegexLexer
from pygments.token import Comment, Keyword, Name, Punctuation, String, Text

class GotoLex(RegexLexer):
    """
        A Goto lexer
    """
    name = 'Goto'
    aliases = ['goto']
    filenames = ['*.gts']
    mimetypes = ['text/x-goto']

    tokens = {
        'root': [
            (r'\s+', Text),
            (r'\(\*', Comment, 'comment'),
            (r'([^.\s]+|\.\S)+', Text),
        ],
        'comment': [
            (r'[^(*)]+', Comment),
            (r'\(\*', Comment, '#push'),
            (r'\*\)', Comment, '#pop'),
            (r'[(*)]', Comment),
        ],
    }
