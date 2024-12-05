'''
Carolina Pacheco da Silva
Matheus Antunes Monteiro
Matheus Beilfuss
'''

# Define classe genérica de DFAs 
class DFA:
    def __init__(self, accepting_states, transitions):

        self.initial_state = 0 # estado inicial do DFA
        self.accepting_states = accepting_states # Estados de aceitação
        self.transitions = transitions # Funções de transição

        self.current_state = self.initial_state # estado atual

    # Função para resetar o estado atual do DFA
    def reset(self):
        self.current_state = self.initial_state

    # Executa uma transição conforme as funções de transição definidas na inicialização
    def transit(self, char):
        self.current_state = self.transitions[self.current_state](char)

    # Retorna verdadeiro caso o DFA esteja em estado de aceitação ou falso caso não esteja
    def accepts(self):
        return self.current_state in self.accepting_states

# Inicializa um DFA para identificadores
identifier_dfa = DFA({1}, {
    0: lambda char: 1 if char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' else "ERROR",
    1: lambda char: 1 if char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' else "ERROR",
    "ERROR": lambda char: "ERROR"
})

# Inicializa um DFA para números
numbers_dfa = DFA({1}, {
    0: lambda char: 1 if char in '0123456789' else "ERROR",
    1: lambda char: 1 if char in '0123456789' else "ERROR",
    "ERROR": lambda char: "ERROR",
})

# Inicializa um DFA para operadores relacionais
operators_dfa = DFA({1, 2}, {
    0: lambda char: 1 if char in '><=' else 3 if char == "!" else "ERROR",
    # State after reading '>, <, = or !', check for '='
    1: lambda char: 2 if char == '=' else "ERROR",
    2: lambda char: "ERROR",
    3: lambda char: 2 if char == '=' else "ERROR",
    "ERROR": lambda char: "ERROR",
})

'''
input = "!"

for char in input:
    operators_dfa.transit(char)

print(operators_dfa.accepts())
'''
