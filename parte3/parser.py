from lexer import lexer
from parsingTable import PARSING_TABLE

TERMINALS = [
    "id", "num",
    "<", ">", "<=", ">=", "<>", "=",
    "int", "if", "else", "def", "print", "return",
    "+", "-", "*", "/", ":=", "(", ")", "{", "}", ",", ";",
    "id("
]


w = '''
if (x > 0)
    if (y > 0)
        z := 1;
'''


def parser(w, parsingTable):

    # variável para guardar os elementos em que ocorreu match
    matchList = list()

    # Prepara buffer com string de texto + $ ao final

    lexer.input(w)
    found_tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        found_tokens.append(tok.value)

    print(found_tokens)

    buffer = found_tokens
    buffer.append("$")

    currentSymbolIndex = 0

    # prepara a pilha com S$
    stack = ['$'] + ["S"]

    # a = primeiro símbolo de W
    a = buffer[currentSymbolIndex]
    # X = símbolo do topo da pilha
    X = stack[-1]

    # Enquanto a pilha não estiver fazia

    while X != "$":

        # Se X == a, realiza o match
        if X == a:

            matchList.append(a)

            # remove X da pilha
            stack.pop()

            # a = próximo símbolo de W
            currentSymbolIndex += 1
            a = buffer[currentSymbolIndex]

        # Se X é um terminal
        elif X in TERMINALS:

            # É terminal, mas não corresponde ao input
            print("Terminal incorreto")
            print(X)
            print(a)
            print(X == a)
            return "Erro"

        # M[X, a] é uma entrada de erro
        elif (X, a) not in parsingTable:

            print("Produção não encontrada")
            print(X)
            print(a)
            print(("TERM′", "(") in parsingTable)
            return "Erro"

        # X não é terminal, aciona a produção em M
        elif ((X, a) in parsingTable):

            production = parsingTable[(X, a)]

            # Imprime a produção
            print(
                f"Produção: {X} → {''.join(production) if production else 'ε'}")

            # remove X da pilha
            stack.pop()

            # Empilha a produção
            stack.extend(reversed(production))

        X = stack[-1]
        print("Sucesso")
        print(f"Pilha: {stack}")
        print(f"Match: {matchList}")


parser(w, PARSING_TABLE)
