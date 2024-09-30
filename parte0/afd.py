class AFD:
  def __init__(self):
    self.estados = {0, 1, 2, 3}
    self.alfabeto = {'a', 'b'}
    self.estado_inicial = 0
    self.estados_finais = {3}
    self.transicoes = {
      (0, 'a'): 1,
      (0, 'b'): 0,
      (1, 'a'): 1,
      (1, 'b'): 2,
      (2, 'a'): 1,
      (2, 'b'): 3,
      (3, 'a'): 1,
      (3, 'b'): 0
    }

    self.estado_atual = self.estado_inicial

  def processar_string(self, input):
    self.estado_atual = self.estado_inicial
    for simbolo in input:

      if simbolo not in self.alfabeto:
        return False
      
      self.estado_atual = self.transicoes[(self.estado_atual, simbolo)]

    return self.estado_atual in self.estados_finais # Verifica se terminou em um estado final
  
def testar_afd():
    automato = AFD()

    # Exemplos de strings aceitas
    aceitas = ["abb", "bbabb", "baababb"]
    # Exemplos de strings rejeitadas
    rejeitadas = ["aab", "bbbb", "abba"]
    
    print("Strings Aceitas:")
    for string in aceitas:
        
        resultado = automato.processar_string(string)
        print(f"{string}: {'Aceita' if resultado else 'Rejeitada'}")
    
    print("\nStrings Rejeitadas:")
    for string in rejeitadas:
        
        resultado = automato.processar_string(string)
        print(f"{string}: {'Aceita' if resultado else 'Rejeitada'}")

testar_afd()
