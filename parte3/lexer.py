'''
Carolina Pacheco da Silva
Matheus Antunes Monteiro
Matheus Beilfuss
'''

import sys
import ply.lex as lex

# Simbolos para tipos:

symbolic_types = {
    'LOWER': '<',
    'LOWEREQUAL': '<=',
    'GREATER': '>',
    'GREATEREQUAL': '>=',
    'EQUAL': '==',
    'NOTEQUAL': '<>',
    'ASSIGN': ':=',
    'PLUS': '+',
    'MINUS': '-',
    'TIMES': '*',
    'DIVIDE': '/',
    'LPAR': '(',
    'RPAR': ')',
    'LBRACE': '{',
    'RBRACE': '}',
    'COMMA': ',',
    'SEMICOLON': ';',
    'ID_LPAR': 'id(',
    'NUMBER': 'num',
    'END': '$',
    'ID': 'id'
}

# Definição das palavras reservadas, conforme gramática
reserved = {
    'int': 'int',
    'if': 'if',
    'else': 'else',
    'def': 'def',
    'print': 'print',
    'return': 'return'
}

# Definição dos tokens, conforme palavras reservadas

tokens = [
    'ID', 'ID_LPAR', 'NUMBER', 'LOWER', 'LOWEREQUAL', 'GREATER', 'GREATEREQUAL',
    'EQUAL', 'NOTEQUAL', 'ASSIGN', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAR', 'RPAR', 'LBRACE', 'RBRACE', 'COMMA', 'SEMICOLON', 'END'
] + list(reserved.values())

# regex para reconhecimento dos tokens simples
t_LOWER = r'<'
t_LOWEREQUAL = r'<='
t_GREATER = r'>'
t_GREATEREQUAL = r'>='
t_EQUAL = r'=='
t_NOTEQUAL = r'<>'
t_ASSIGN = r':='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAR = r'\('
t_RPAR = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_SEMICOLON = r';'
t_END = r'\$'

# função de utilidade para cálculo da coluna em que um token foi encontrado


def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


def t_ID_LPAR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*\('

    identifier = t.value[:-1]
    if identifier in reserved:
        t.lexer.lexpos -= 1
        t.type = reserved[identifier]
        t.value = identifier
        return t

    t.type = 'ID_LPAR'
    return t

# Definição de handler para identificadores


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'  # regex para identificadores
    # confere se o identificador não é uma palavra reservada
    t.type = reserved.get(t.value, 'ID')

    return t

# Definição de handler para números


def t_NUMBER(t):
    r'\d+'
    return t

# Definição de handler para novas linhas


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Definição de caracteres para ignorar
t_ignore = ' \t'

# Definição de handler para erros


def t_error(t):
    column = find_column(t.lexer.lexdata, t)  # Calcula a coluna do erro
    # Imprime mensagem de erro
    print(f"Erro léxico: '{t.value[0]}' na linha {t.lineno} e coluna {column}")
    sys.exit(1)  # Interrompe a execução do lexer


# Constrói o lexer com base nas definições anteriores
lexer = lex.lex()


def symbolic_lexer(input_text):
    lexer.input(input_text)
    tokenList = []
    while True:
        token = lexer.token()
        if not token:
            break

        token.type = symbolic_types.get(token.type, token.type)
        tokenList.append(token)
    return tokenList
