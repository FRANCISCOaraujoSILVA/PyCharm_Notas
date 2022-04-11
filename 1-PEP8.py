"""
PEP8 - SÃO PROPOSTAS DE MELHORIAS PARA A LINGUAGEM PYTHON.

import this

A ideia da pep8 é que possamos escrever códigos de forma pythônica, ou seja, visualmente bonita.
[1] utilizar Camel Case para nome de classes;
ou seja, NomeSobrenome: Observe as letras maiúsculas.
Perceba que duas linhas em brancos são necessárias para evitar o traço em baixo.
Para tirar erros de palavras, mude: file,settings,slelling,desatiar typo
[2] Utilizar nome minúsculo, separados por underline para funções ou variáveis;



class Calculadora:
    pass


class CalculadoraCientífica:
    pass


def soma():
    pass


def soma_dois():
    pass

numero=4
numero_impar=5

[3] utilize 4 espaços para identação!, se não seguir, não conseguimos programar.
Os dois pontos no fim indica que um novo bloco vai começar, por isso precisamos de 4 espaços.
Não é recomendado usar o tab para dar os espaços.
Essa linguagem de programação é completamente dependente da indentação.


if 'a' in 'banana':
    print('tem')

[4] linhas em branco.
-Precisamos das duas linhas de espaço, entre funções e definições de classe.
-Métodos dentro de uma classe devem ser separados com uma única linha em branco.

[5] Imports devem ser sempre feitos em linhas separadas.

#Import errado

import sys. os

#import certo

import sys
import os

#Podemos importar partes de uma biblioteca, não há problema em fazer isso. Serve para no máximo 3

from types import StringType,ListType

#para mais de 3, fazemos assim:

from types import (
    StringTupe,
    ListType,
    SetType,
    OutroType
)

# imports devem ser colocadas no topo do arquivo, logo depois de qualquer comentário ou docstringr
# e antes de constantes ou variáveis globais.

[6] Espaços em expressões e instruções

# Não faça:

funcao( algo[ 1 ],{outro: 2})

# faça:

funcao(algo[1],{outro:2})

# não faça:

algo (1)

# faça:

algo (1)

# não faça:

dict ['chave'] = list [indice]

# faça:

dict['chave'] = list[indice]

# não faça:

x = 1
y = 3

# faça:

x=1
y=3

[7] Sempre termine uma instrução com uma nova linha

obs.: podemos fazer comentários com três aspas simples também. Mas é preferível usar três aspas duplas.
"""
