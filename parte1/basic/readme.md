# Lexer básico

Este projeto é um analisador léxico básico baseado em Autômatos Finitos Determinísticos (AFDs ou DFAs) anotados, construído utilizando Python.

## Alunos

Carolina Pacheco da Silva
Matheus Antunes Monteiro
Matheus Beilfuss

## Funcionalidades

- Geração de lista de tokens a partir de um arquivo de código-fonte;
- Criação de uma tabela de símbolos contendo os tokens únicos encontrados.

## Arquivos

1. DFA.py

Este arquivo define uma classe genérica para DFAs e cria DFAS específicos para:

- Identificadores (por exemplo, nomes de variáveis, palavras reservadas);
- Números (por exemplo, inteiros);
- Operadores (por exemplo, operadores relacionais como ==, >=, etc.).

2. lexAnalyzer.py

Este arquivo contém a classe Analyzer, que:

- Lê o input caractere por caractere;
- Usa DFAs para identificar e categorizar tokens;
- Lida com palavras reservadas como if, else, int, float, etc.;
- Gera dois tipos de saída:
    - Lista de Tokens: uma lista de tokens encontrados no arquivo de entrada.
    - Tabela de Símbolos: uma tabela de símbolos com informações como o valor do token, linha, coluna e tipo.

3. main.py

É o ponto de entrada para executar o analisador léxico. Executa as seguintes operações:

- Lê um arquivo de entrada contendo o código fonte;
- Processa o conteúdo do arquivo e gera tokens utilizando o lexer;
- Exibe a lista de tokens encontrados e a tabela de símbolos única.

4. correct.txt e incorrect.txt

Arquivos sem erros e com erros, respectivamente, para teste do lexer.

## Como usar

### Pré-requisitos

- Possuir ambiente de execução Python 3 instalado.

### Execução do lexer

1. Clonar o repositório. Se optar por download, manter os todos os arquivos no mesmo diretório.

2. Criar um arquivo de código-fonte para teste. Por exemplo, codigo.txt:

```
int x = 42;
float y = 105;
x == y;
```

3. Executar o arquivo main.py passando o caminho de código-fonte como argumento. Por exemplo, se o arquivo estiver no mesmo diretório que o script main.py:

> python main.py codigo.txt

Para utilizar os arquivos correto e incorreto de teste fornecidos com o trabalho, os comandos são:

> python main.py correct.txt

> python main.py incorrect.txt

