from pygments.lexer import RegexLexer, words, include, bygroups, default
from pygments.token import (
    Text,
    Comment,
    Operator,
    Keyword,
    Name,
    String,
    Number,
    Punctuation,
)

from pygments import unistring as uni

__all__ = ("PortuscriptLexer",)


class PortuscriptLexer(RegexLexer):
    name = "Portuscript"
    aliases = ["portuscript", "ptst"]
    filenames = ["*.ptst"]

    uni_name = "[%s][%s]*" % (uni.xid_start, uni.xid_continue)

    tokens = {
        "root": [
            (r"\s+", Text),
            (r"#.*$", Comment.Single),
            (r'"[^"]*"', String),
            include("keywords"),
            (r'(func)((?:\s|\\\s)+)', bygroups(Keyword, Text), 'funcname'),
            include("expr"),
        ],
        'funcname': [
            (uni_name, Name.Function, '#pop'),
            default('#pop'),
        ],
        "keywords": [
            (
                words(
                    (
                        "var",
                        "const",
                        "se",
                        "senao",
                        "enquanto",
                        "retorne",
                        "pare",
                        "continue",
                        "para",
                        "de",
                        "importe",
                    ),
                    suffix=r"\b",
                ),
                Keyword,
            ),
            (words(("Verdadeiro", "Falso", "Nulo"), suffix=r"\b"), Keyword.Constant),
        ],
        "builtins": [
            (words(("int", "imprima", "texto", "int", "doc", "tamanho", "leia"), prefix=r"(?<!\.)", suffix=r"\b"), Name.Builtin),
        ],
        "expr": [
            include("numbers"),
            (r"!=|==|<<|>>|[-~+/*%=<>&^|.]", Operator),
            (r"[]{}:(),;[]", Punctuation),
            (r"(em|e|ou|nao)\b", Operator.Word),
            (words(("Verdadeiro", "Falso", "Nulo"), suffix=r"\b"), Keyword.Constant),
            include("builtins"),
            include("name"),
        ],
        "funcparams": [
            (r"[^()\n]+", Name.Function),
            (r"\(", Punctuation, "#push"),
            (r"\)", Punctuation, "#pop"),
            (r"[()]|\n", Text),
        ],
        "numbers": [
            (
                r"(\d(?:_?\d)*\.(?:\d(?:_?\d)*)?|(?:\d(?:_?\d)*)?\.\d(?:_?\d)*)"
                r"([eE][+-]?\d(?:_?\d)*)?",
                Number.Float,
            ),
            (r"\d(?:_?\d)*", Number.Integer),
        ],
        "name": [
            (uni_name, Name),
        ],
    }
