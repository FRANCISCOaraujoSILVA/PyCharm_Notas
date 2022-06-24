"""
PEP8 - SÃO PROPOSTAS DE MELHORIAS PARA A LINGUAGEM PYTHON.

Faça no terminal: import this (um poema)

A ideia da pep8 é que possamos escrever códigos de forma pythônica, ou seja, visualmente bonitas.
[1] Utilizar Camel Case para nome de classes;
ou seja, NomeSobrenome: Observe as letras maiúsculas.
Perceba que duas linhas em brancos são necessárias para evitar o traço em baixo.
Para tirar erros de palavras, mude: file,settings,slelling,desativar typo
[2] Utilizar nome minúsculo, separados por underline para funções ou variáveis;



class Calculadora:
    pass


class CalculadoraCientífica:
    pass


def soma():
    pass


def soma_dois():
    pass

Obs.: -use "#" para escrever comentários apenas de uma linha: # comentário

Observe o espaço entre "#" e "comentário". Ele é necessário!

- use aspas triplas para comentários maior que uma linha. Segue como exemplo o local onde estou colocando as
informações

- não ultrapasse essa linha na vertical à direita

- se o comentário for logo após um dado (na mesma linha) é necessário deixar dois espaços entre esse dado e a cerquilha
"#"
"""
numero = 4
numero_impar = 5

"""[3] Utilize 4 espaços para identação! se a regra não for seguida, não conseguiremos programar.
Os dois pontos no fim da classe, função... indica que um novo bloco vai começar, por isso precisamos de 4 espaços.
Não é recomendado usar o TAB do teclado para dar os espaços, muito embora ele esteja (em algumas máquinas) programado 
com 4 espaços.
Essa linguagem de programação é completamente dependente da indentação, por isso, tenha muito cuidado e fique atento.
"""

if 'a' in 'banana':
    print('tem')

"""[4] linhas em branco.
-Precisamos de duas linhas de espaço, entre funções e definições de classe.
-Métodos dentro de uma classe devem ser separados com uma única linha em branco.
"""

# [5] Imports devem ser sempre feitos em linhas separadas.

"""Import errado
import sys. os
"""

"""
# import certo
import sys
import os
"""

"""
Podemos importar partes de uma biblioteca, não há problema em fazer isso. Serve para no máximo 3
from types import StringType, ListType

# para mais de 3, fazemos assim:
from types import (
    StringTupe,
    ListType,
    SetType,
    OutroType
)

# imports devem ser colocadas no topo do arquivo, logo depois de qualquer comentário ou docstring
# e antes de constantes ou variáveis globais.
"""

# [6] Espaços em expressões e instruções

"""
Não faça: Observe os espaços desnecessários (erro de indentação)
funcao( algo[ 1 ],{outro: 2})

# faça:
funcao(algo[1],{outro:2})

# não faça:
algo (1)

# faça:
algo(1)

# não faça:
dict ['chave'] = list [indice]

# faça:
dict['chave'] = list[indice]

# faça:
x = 1
y = 3

# não faça (observe a falta de espaço):
x=1
y=3

[7] Sempre termine uma instrução com uma NOVA linha

obs.: podemos fazer comentários com três aspas simples também ('''texto'''). Mas é preferível usar três aspas duplas!
"""
