from pygments.lexer import RegexLexer
from pygments.lexer import (
    words,
)
from pygments.token import (
    Comment,
    Keyword,
    Name,
    Operator,
    Punctuation,
)


class CustomLexer(RegexLexer):
    name = 'GAMS'
    aliases = ['gams']
    filenames = ['*.gms']

    tokens = {
        'root': [
            (r'^\*.*', Comment.Single),
            (words((
                "abs", "asc", "sigmoid", "sum",
                "acos", "acosh", "asin", "asinh", "atan", "atan2",
                "atanh", "ceil", "ctime", "cos", "cosh", "exp", "floor", "log", "log10",
                "max", "min", "precision", "round", "sin", "sinh", "sqrt", "tan", "tanh", "sqrt",
                "smax", "smin",
                "time", "trunc", "div",
                "beta", "betareg", "binomial", "edist", "entropy", "errorf", "fact",
                "gamma", "gammareg", "logbeta", "loggamma", "normal",
                "mapval", "mod", "ncpcm", "ncpf", "pi", "poly", "power",
                "sign", "signpower", "trunc", "uniform", "uniformint",
            ), prefix=r'\b', suffix=r'\b'), Name.Builtin),
            (r'^Set\s?\n?', Keyword.Declaration, 'value_declarations'),
            (words((
                'solve', 'Solve',
                'using', 'USING',
                'minimizing',
                'maximizing',
            ), prefix=r'\b', suffix=r'\b'), Keyword.Reserved),
            (words(("option"), prefix=r'\b', suffix=r'\b'), Name.Builtin),
            (r'^\$onText*', Keyword, 'onTextBlock'),
            (r'=e=|=l=|=g=', Operator),
        ],
        'onTextBlock': [
            (r'^\$offText*', Keyword, '#pop'),
            (r'[^\$]', Comment),
        ],
        'value_declarations': [
            (r';', Punctuation, '#pop'),
            (r'\s*\w+(?=[^;^\w])', Name.Variable, 'value_declaration'),
            (r'\s*\w+(?=;)', Name.Variable),
        ],
        'value_declaration': [
            (r'\n', Punctuation, '#pop'),
            (r'\(.*\)', Punctuation),
            (r'\'?[\w\s]\'?', Comment),
            (r'\s*\/.+\/\n?', Name.Entity, '#pop'),
        ]
    }
