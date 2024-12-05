'''
Carolina Pacheco da Silva
Matheus Antunes Monteiro
Matheus Beilfuss
'''

import sys
from lexer import lexer, find_column, symbol_table


def main():

    # Previne execução sem argumentos
    if len(sys.argv) != 2:
        print("Usage: python main.py <inputfile>")
        sys.exit(1)

    # Obtém caminho para arquivo de código fonte
    input_file = sys.argv[1]

    try:
        # lê arquivo de código fonte
        with open(input_file, 'r') as file:
            data = file.read()

        # transmite o conteúdo do arquivo para o lexer
        lexer.input(data)

        # Roda o lexer, armazenando cada token encontrado em uma lista
        found_tokens = []
        while True:
            tok = lexer.token()
            if not tok:
                break
            column = find_column(data, tok)
            found_tokens.append(
                f"LexToken({tok.type},'{tok.value}',{tok.lineno},{column})")

        # Printa lista de tokens
        print("Lista de tokens: \n")

        print(found_tokens)
        for tok in found_tokens:
            print(tok)

        # Printa tabela de símbolos
        print("\nTabela de símbolos:\n")
        for entry in symbol_table.values():
            print(
                f"Type: {entry['type']}, Value: '{entry['value']}', Line: {entry['line']}, Column: {entry['column']}")

    # handler para erro caso o arquivo de código fonte não seja encontrado
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)


if __name__ == '__main__':
    main()
