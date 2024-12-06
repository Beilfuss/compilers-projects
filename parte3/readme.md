# Parser preditivo para a linguagem LSI-2024-2

Este projeto é um parser preditivo para a linguagem LSI-2024-2, construído utilizando Python.

## Alunos

Carolina Pacheco da Silva
Matheus Antunes Monteiro
Matheus Beilfuss

## Funcionalidades

- Geração de lista de produções utilizadas pelo parser
- Geração da lista ordernada de matches realizados pelo parser
- Em caso de erro, indicação do token terminal ou não terminal que gerou o erro

## Arquivos

1. lexer.py

Contém a implementação do lexer (analisador léxico). Inclui a definição dos tokens da linguagem e suas respectivas expressões regulares. Foi baseado no lexer utilizado na parte 1 do trabalho, mas ligeiramente adaptado para as necessidades desta parte do trabalho.

2. parser.py

Contém a imeplementação do parser propriamente dito, exatamente conforme o algoritmo visto em aula e produzindo as saídas definidas na especificação do trabalho.

3. parsingTable.py

Contém a tabela de reconhecimento sintático utilizada pelo parser em formato de dicionário

4. main.py

É o ponto de entrada para executar o parser. Executa as seguintes operações:

- Importa a tabela de parsing definida em parsingTable.py
- Lê um arquivo de entrada contendo o código fonte;
- Repassa o conteúdo do arquivo lido para o parser, assim como a parsingTable;

5. correto1.lsi, correto2.lsi, incorret1.lsi, incorreto2.lsi (diretório exemplos)

São os arquivos contendo os programas para teste, conforme requisito do trabalho

## Instruções de uso

### Pré-requisitos

- Possuir ambiente de execução Python 3 instalado;
- Instalar a biblioteca PLY com o seguinte comando:

> pip install ply

Atenção: a dependender da configuração do ambiente de execução, pode ser necessário utilizar o seguinte comando, em vez do comando acima:

> pip3 install ply

### Execução do parser

1. Clonar o repositório. Se optar por download, manter os arquivos lexer.py e main.py no mesmo diretório.
2. Criar um arquivo de código fonte para teste. Por exemplo, codigo.lsi:

```
  def func1(int A, int B) {
      int C, D, R;
      C := A + B;
      D := A + B * C;
      R := C - D;
      return R;
  }
```

3. Executar o arquivo main.py passando o caminho de código-fonte como argumento. Por exemplo, se o arquivo estiver no mesmo diretório que o script main.py:

> python main.py codigo.lsi

Para utilizar os arquivos correto e incorreto de teste fornecidos com o trabalho, os comandos são:

> python main.py exemplos/correto1.lsi

> python main.py exemplos/correto2.lsi

> python main.py exemplos/incorreto1.lsi

> python main.py exemplos/incorreto2.lsi

## Observações

### Tabela de reconhecimento sintático

Iniciou-se a execução deste trabalho com a tabela de reconhecimento sintático produzido no T2. No entanto, a referida tabela possuía ambiguidade com relação às produções if/else. Para remoção dessa ambiguidade, a equipe substituiu as produções

IFSTMT ::= if ( EXPR ) STMT IFSTMT’
IFSTMT’ ::=  else STMT
IFSTMT’ ::= ''

Pelas produções

IFSTMT ::= if ( EXPR ) { STMTLIST } ELSEPART
ELSEPART ::= else { STMTLIST }
ELSEPART ::= ''

Dessa forma, eliminou-se a ambiguidade referente ao IF/ELSE através do uso de chaves. Foi gerada nova tabela de reconhecimento sintático para utilização na versão definitiva do trabalho. A versão final da tabela de reconhecimento sintática está disponível entre os arquivos do projeto com o nome "nova tabela de reconhecimento sintático".


### Exemplo de saída para input sem erro

A saída para inputs corretos inclui:

- Lista de produções geradas pelo parser
- Lista ordenada dos matches gerados pelo parser
- Lista completa de matches


```
Produção: S → MAIN
Produção: MAIN → FLIST
Produção: FLIST → FDEF FLIST’
Produção: FDEF → def id( PARLIST ) { STMTLIST }
Produção: PARLIST → ε
Produção: STMTLIST → STMT STMTLIST’
Produção: STMT → PRINTST ;
Produção: PRINTST → print EXPR
Produção: EXPR → NUMEXPR EXPR’
Produção: NUMEXPR → TERM NUMEXPR′
Produção: TERM → FACTOR TERM′
Produção: FACTOR → ( NUMEXPR )
Produção: NUMEXPR → TERM NUMEXPR′
Produção: TERM → FACTOR TERM′
Produção: FACTOR → num
Produção: TERM′ → ε
Produção: NUMEXPR′ → ε
Produção: TERM′ → ε
Produção: NUMEXPR′ → ε
Produção: EXPR’ → ε
Produção: STMTLIST’ → ε
Produção: FLIST’ → ε

Sucesso!

Lista ordenada de matchs:

Match 1: def
Match 2: id(
Match 3: )
Match 4: {
Match 5: print
Match 6: (
Match 7: num
Match 8: )
Match 9: ;
Match 10: }
['def', 'id(', ')', '{', 'print', '(', 'num', ')', ';', '}']
```

### Exemplos de saída para input com erro

As saídas de inputs com erros incluem as produções geradas até a detecção do erro seguidas de uma mensage de erro como:


```
Erro: Produção não encontrada: 

Não-terminal fora da tabela de reconhecimento sintático: STMTLIST’ - Valor do input: else 
```

Ou

```
Erro: Terminal incorreto (sem match): 

Terminal esperado: { - Terminal encontrado: id

```