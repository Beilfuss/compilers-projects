# Lexer para Linguagem LSI-2024-2

Este projeto é um analisador léxico para a linguagem LSI-2024-2, construído usando a biblioteca PLY (Python Lex-Yacc).

## Alunos

Carolina Pacheco da Silva
Matheus Antunes Monteiro
Matheus Beilfuss

## Funcionalidades

- Geração de lista de tokens a partir de um arquivo de código-fonte;
- Criação de uma tabela de símbolos contendo os tokens únicos não-triviais.

## Arquivos

1. lexer.py

Contém a implementação do lexer (analisador léxico). Inclui a definição dos tokens da linguagem e suas respectivas expressões regulares, além de funções para processar e armazenar os tokens em uma tabela de símbolos.

2. main.py

É o ponto de entrada para executar o analisador léxico. Executa as seguintes operações:

- Lê um arquivo de entrada contendo o código fonte;
- Processa o conteúdo do arquivo e gera tokens utilizando o lexer;
- Exibe a lista de tokens encontrados e a tabela de símbolos única.

3. correct_test.lsi e incorrect_test.lsi

Arquivos sem erros e com erros, respectivamente, para teste do lexer.

## Como usar

### Pré-requisitos

- Possuir ambiente de execução Python 3 instalado;
- Instalar a biblioteca PLY com o seguinte comando:

> pip install ply

Atenção: a dependender da configuração do ambiente de execução, pode ser necessário utilizar o seguinte comando, em vez do comando acima:

> pip3 install ply

### Execução do lexer

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

> python main.py correct_test.lsi

> python main.py incorrect_test.lsi