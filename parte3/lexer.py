'''
Carolina Pacheco da Silva
Matheus Antunes Monteiro
Matheus Beilfuss
'''

import sys
import ply.lex as lex


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

tokens = ['ID', 'ID_LPAR', 'NUMBER', 'LOWER', 'LOWEREQUAL', 'GREATER', 'GREATEREEQUAL', 'EQQUAL', 'NOTEQUAL',
          'ASSIGN', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAR', 'RPAR', 'LBRACE', 'RBRACE',
          'COMMA', 'SEMICOLON'] + list(reserved.values())

# regex para reconhecimento dos tokens simples
t_LOWER = r'<'
t_LOWEREQUAL = r'<='
t_GREATER = r'>'
t_GREATEREEQUAL = r'>='
t_EQQUAL = r'=='
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

# função de utilidade para cálculo da coluna em que um token foi encontrado
def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1



def t_ID_LPAR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*\('
    t.type = 'ID_LPAR'  
    t.value = "id("
    return t

# Definição de handler para identificadores
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*' #regex para identificadores
    t.type = reserved.get(t.value, 'ID') # confere se o identificador não é uma palavra reservada
    
    if t.type == "ID":
        t.value = "id"

    return t

# Definição de handler para números
def t_NUMBER(t):
    r'\d+'
    t.value = "num"
    return t

# Definição de handler para novas linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Definição de caracteres para ignorar
t_ignore = ' \t'

# Definição de handler para erros
def t_error(t):
    column = find_column(t.lexer.lexdata, t) # Calcula a coluna do erro
    print(f"Erro léxico: '{t.value[0]}' na linha {t.lineno} e coluna {column}") # Imprime mensagem de erro
    sys.exit(1) # Interrompe a execução do lexer

# Constrói o lexer com base nas definições anteriores
lexer = lex.lex()