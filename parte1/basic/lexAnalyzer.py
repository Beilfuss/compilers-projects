'''
Carolina Pacheco da Silva
Matheus Antunes Monteiro
Matheus Beilfuss
'''
from DFA import identifier_dfa, numbers_dfa, operators_dfa

# Lista de keywords reservadas
RESERVED_KEYWORDS = {"if": "IF", "else": "ELSE",
                     "then": "THEN", "int": "INT", "float": "FLOAT", "return": "RETURN"}

# Classe do analizador
class Analyzer:

    def __init__(self):
        self.charPos = 0 # tracker da posição do caracter
        self.column = 0 # tracker da coluna
        self.line = 0 # tracker da linha
        self.tokenSize = 1 # tracker do tamanho do token em análise
        self.token_list = [] # lista de tokens encontrados
        self.symbol_table = {} # tabela de símbolos

    # Função para resetar o analisador
    def reset(self):
        self.charPos = 0
        self.column = 0
        self.line = 0
        self.token_list = []
        self.symbol_table = {}
        self.tokenSize = 1

    # Função para verificar se um token é válido
    # Recebe um DFA para fazer a análise, o tipo correspondente ao DFA e o INPUT para avaliar
    def verify_token(self, input, type, dfa):
        dfa.reset() # reseta o dfa
        token = "" # inicializa um token vazio
        startColumn = self.column # registra a coluna em que o token começa
        charPos = self.charPos # copia a posição do caracter
        keyword_type = type # registra o tipo do token correspondente ao DFA

        # itera pelo input, a partir da posição do caracter atual
        while (charPos < len(input)):
            char = input[charPos] # obtém o caracter da posição atual

            #interrompe o loop quando encontra um espaço ou um delimitador
            if (not char.isspace() and not char == ";"):
                token += char # incrementa o token com o caracter
                charPos += 1 # incrementa posição atual
                dfa.transit(char) # repassa o caracter para o DFA
            else:
                self.tokenSize = len(token) or 1 # guarda o tamanho do token avaliado
                break
        
        # após encontrar um espaço ou delimitador, verifica se o DFA aceitou o token
        if dfa.accepts():

            # verifica se o token é uma palavra reservada
            if token in RESERVED_KEYWORDS:
                # se o token for uma palavra reservada, atualiza o keyworkd type
                keyword_type = RESERVED_KEYWORDS[token]
            
            # formata os dados do token
            token_data = {
                'value': token, 'line': self.line, 'column': startColumn, "type": keyword_type}
            
            # Guarda o token na tabela de simbolos, se ele ainda não estiver lá
            if (token not in self.symbol_table):
                self.symbol_table[token] = token_data

            # Guardar o token na lista de tokens
            self.token_list.append(token_data)
            self.charPos = charPos # atualiza a posição global do token pela posição alcançada na análise
            self.column += self.tokenSize # atualiza a coluna atual global considerando o tamanho do token encontrado
            return True

        return False

    def print_symbol_table(self):

        print("\n Tabela de símbolos:\n")
        for key, token in self.symbol_table.items():
            print(
                f"Token: {token['value']}; Linha: {token['line']}; Coluna: {token['column']}; Tipo: {token['type']}\n")

    def print_token_list(self):
        print("\n Lista de tokens:\n")
        for token in self.token_list:
            print(token)

    def analyze(self, input):
        self.reset() #reseta o analizador

        # Itera pelos caracteres do input
        while (self.charPos < len(input)):
            char = input[self.charPos]

            # Atualiza linhas e colunas quando encontra um caracter de newline
            if (char == '\n'):
                self.line += 1
                self.column = 0
                self.charPos += 1
                continue

            # Pula espaços e delimitadores
            if char.isspace() or char == ";":
                self.charPos += 1
                self.column += 1
                continue

            # Verifica a validade do totem, passando pelos 3 DFAs
            isValidToken = (
                self.verify_token(input, "IDENTIFIER", identifier_dfa) or
                self.verify_token(input, "NUMBER", numbers_dfa) or
                self.verify_token(input, "OPERATOR", operators_dfa)
            )

            # se o token não é validado em nenhum DFA, reporta o erro e interrompe execução
            if not isValidToken:
                print(
                    f"Erro léxico: Token inválido na linha {self.line}, coluna {self.column}")
                exit(1)

        # Quando encerrar o input, printa os tokens encontrados e a tabela e símbolos
        self.print_token_list()
        self.print_symbol_table()


analyzer = Analyzer()
