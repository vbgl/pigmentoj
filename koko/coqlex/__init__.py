# -*- coding: utf-8 -*-

"""
    A Coq lexer
"""

from pygments.lexer import RegexLexer
from pygments.token import Comment, Keyword, Name, Punctuation, String, Text

class CoqLex(RegexLexer):
    """
        A Coq lexer
    """
    name = 'Coq'
    aliases = ['coqq', 'koko']
    filenames = ['*.v']
    mimetypes = ['text/x-coq']

    tokens = {
        'root': [
            (r'\s+', Text),
            (r'\(\*', Comment.Special, 'comment'),
            (r'\.(?=\s)', Punctuation),
            (r'[()_,|=<>]', Punctuation),
            (r':=?', Punctuation),
            (r'({{|}})', Punctuation),
            (r'{\|?', Punctuation, 'record'),
            (r'Proof\s*\.', Keyword, 'proof'),
            (r'((Local|Set|Unset|Open|Scope|Close|Hint|Resolve|Unfold|Constructors|Eval|Compute)\s+)+', Keyword),
            (r'(Notation|Infix)', Keyword),
            (r'(Context|Variables?|Hypothes[ei]s)', Keyword),
            (r'(Require(\s+(Import|Export))?\s+)', Keyword, 'names'),
            (r'((Import|Export)\s+)', Keyword, 'names'),
            (r'((Module(\s+(Import|Export))?|Section|End|Transparent|Opaque|Arguments)\s+)+', Keyword, 'name'),
            (r'((Let|Example|Definition|Fixpoint|Inductive|Parameter|Lemma|Theorem|Corollary|Class|Existing|Instances?|Record|Canonical|Structure)\s+)+', Keyword, 'name'),
            (r'(match|let|in|if|then|else|return|with|end)(?=\b)', Keyword),
            (ur'[α-ωa-zA-Z_][₁₂₃₄₅₆₇₈₉₀α-ωa-zA-Z0-9._]*', Text),
            (ur'(⟨|⌊|⌈|⌉|⌋|⟩)', Text),
            (ur'(⊤|⊥|∅)', Text),
            (r'([^.\s]+|\.\S)+', Text),
        ],
        'comment': [
            (r'[^(*)]+', Comment.Multiline),
            (r'\(\*', Comment.Special, '#push'),
            (r'\*\)', Comment.Special, '#pop'),
            (r'[(*)]', Comment.Multiline),
        ],
        'name': [
            (ur'[α-ωa-zA-Z_][₁₂₃₄₅₆₇₈₉₀a-zA-Z0-9._]*', Name.Builtin, '#pop'),
        ],
        'names': [
            (r'\s+', Text),
            (ur'[a-zA-Z_][₁₂₃₄₅₆₇₈₉₀a-zA-Z0-9_]*', Name.Builtin),
            (ur'[a-zA-Z._]([₁₂₃₄₅₆₇₈₉₀a-zA-Z0-9_]*\.)*[₁₂₃₄₅₆₇₈₉₀a-zA-Z0-9_]+', Name.Builtin),
            (r'\.(?=\s)', Punctuation, '#pop'),
        ],
        'proof': [
            (r'(Qed|Defined)\s*\.', Keyword, '#pop'),
            (r'\(\*', Comment.Special, 'comment'),
            (r'\s+', String),
            (r'\.(?=\s)', Punctuation),
            (r'([^.]+|\.\S)+', String),
        ],
        'record': [
            (r'\(\*', Comment.Special, 'comment'),
            (ur'[α-ωa-zA-Z_][₁₂₃₄₅₆₇₈₉₀a-zA-Z0-9._]*', Name.Builtin, 'record-def'),
            (r'\s+', Text),
            ('', Text, '#pop'),
        ],
        'record-def': [
            (r'\(\*', Comment.Special, 'comment'),
            (r'\s+', Text),
            (r';', Punctuation, '#pop'),
            (r'({{|}})', Punctuation),
            (r'{\|?', Punctuation, 'record'),
            (r'}', Punctuation, '#pop'),
            (r':=?', Punctuation),
            (r'=>', Punctuation),
            (r'\'', Punctuation),
            (r'[(),<>=!?_|]', Punctuation),
            (r'(match|let|in|if|then|else|return|with|end)(?=\b)', Keyword),
            (ur'[α-ωa-zA-Z_][₁₂₃₄₅₆₇₈₉₀α-ωa-zA-Z0-9._]*', Text),
            (ur'(∀|∃|∈|→|∨|∧)', Text),
            (r'([^(]\*|[^(;}]|\([^*])+', Text),
        ],
    }
