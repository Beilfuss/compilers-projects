import sys
from parser import parser
from parsingTable import PARSING_TABLE

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py pathToInputFile.lsi")
        sys.exit(1)

    input_file_path = sys.argv[1]

    try:
        with open(input_file_path, 'r') as file:
            w = file.read()
        parser(w, PARSING_TABLE)
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado no path '{input_file_path}'.")
        sys.exit(1)
    except Exception as e:
        print(f"Erro: {e}")
        sys.exit(1)