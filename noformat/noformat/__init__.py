# -*- coding: utf-8 -*-

"""
    Not a formatter, for further processing.
"""

from pygments.formatter import Formatter

class NoFormat(Formatter):
    u"""
    Format tokens as pairs type⋅content separated by a single
    tabulation.
    """

    name = 'NoFormat'
    aliases = ['noformat']

    def format_unencoded(self, tokensource, outfile):
        for ttype, value in tokensource:
            lines = value.split('\n')
            for line in lines[:-1]:
                outfile.write(str(ttype))
                outfile.write('\t')
                outfile.write(unicode(line))
                # .replace('\\', '\\\\').replace('\n', '\\n'))
                outfile.write('\n')
                outfile.write('Token.Newline\t\n')
            outfile.write(str(ttype))
            outfile.write('\t')
            outfile.write(unicode(lines[-1]))
            outfile.write('\n')
