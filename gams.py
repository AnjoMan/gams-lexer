from pygments.lexer import RegexLexer
from pygments.lexer import (
    words,
)
from pygments.token import (
    Comment,
    Keyword,
    Name,
    Operator,
)


class CustomLexer(RegexLexer):
    name = 'GAMS'
    aliases = ['gams']
    filenames = ['*.gms']

    tokens = {
        'root': [
            (r'\*.*', Comment.Single),
            (words((
                'abs', 'acos', 'acosh', 'alias', 'asin', 'asinh', 'atan', 'atan2',
                'atanh', 'ceil', 'ctime', 'cos', 'exp', 'floor', 'log', 'log10',
                'max', 'min', 'precision', 'round', 'sin', 'sinh', 'sqrt', 'tan',
                'tanh', 'time', 'trunc', 'Beta', 'Cauchy', 'Exponential', 'Gamma',
                'Irand224', 'Normal', 'Normal01', 'Poisson', 'Uniform', 'Uniform01',
                'num', 'num0', 'ichar', 'char', 'length', 'substr', 'sprintf',
                'match', 'sub', 'gsub', 'print', 'printf', 'next', 'nextw', 'prev',
                'prevw', 'first', 'last', 'ord', 'ord0', 'card', 'arity',
                'indexarity'), prefix=r'\b', suffix=r'\b'), Name.Builtin),
            (r'(Parameter|Parameters|Variable|Variables)',
                Keyword.Declaration),
            (words((
                'Equation', 'Equations',
                'Model',
                'Variable', 'Variables',
                'Parameter', 'Parameters',
                'Set', 'Sets',
            ), prefix=r'\b', suffix=r'\b'), Keyword.Declaration),
            (words((
                'solve', 'Solve',
                'using', 'USING',
                'minimizing',
                'maximizing',
            ), prefix=r'\b', suffix=r'\b'), Keyword.Reserved),
            (r'=e=|=l=|=g=', Operator),
        ]
    }
