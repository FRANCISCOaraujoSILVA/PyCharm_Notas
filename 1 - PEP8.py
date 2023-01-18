"""
                                    PEP8 - PROPOSTAS DE MELHORIAS PARA A LINGUAGEM PYTHON


Faça no terminal:
    - python
    - import this (veja o poema do programador)

- A ideia da pep8 é que possamos escrever códigos de forma pythônica, ou seja, visualmente bonitas

Dicas:
 - Utilizar Camel Case para nome de classes. Ou seja, NomeSobrenome: Observe as letras maiúsculas
 - Perceba que duas linhas em branco são necessárias para evitar a cobrinha
 - Para tirar erros de palavras, modifique em: file,settings,slelling,desativar typo
 - Utilizar nome minúsculo, separados por underline para funções ou variáveis


Veja abaixo como nomeamos classes e funções de forma pythônica.

class Calculadora:
    pass


class CalculadoraCientífica:
    pass


def soma():
    pass


def soma_dois():
    pass


Notas:
    - Use "#" para escrever comentários apenas de uma linha: # comentário
    - Observe o espaço entre "#" e "comentário". Ele é necessário
    - Use aspas triplas para comentários maiores que uma linha. Segue como exemplo este local onde estou colocando as
informações
    - Há uma linha à direita na vertical, para evitar cobrinhas não ultrapasse essa linha
    - Se o comentário for logo após um dado (na mesma linha), uma classe, uma função etc... é necessário deixar dois
    espaços entre esse dado e a cerquilha "#"
"""

numero = 4
numero_impar = 5

"""
    - Utilize 4 espaços para identação! se a regra não for seguida, não conseguiremos programar
    - Os dois pontos no fim da classe, função... indica que um novo bloco vai começar, por isso precisamos de 4 espaços
    - Não é recomendado usar o TAB do teclado para dar os espaços, muito embora ele esteja (em algumas máquinas)
    programado com 4 espaços da tecla space
    - Essa linguagem de programação é completamente dependente de indentação, por isso, tenha muito cuidado e fique
     atento
"""

if 'a' in 'banana':
    print('tem')

"""
    - Precisamos de duas linhas de espaço entre funções e definições de classes
    - Métodos dentro de uma classe devem ser separados com uma única linha em branco

Imports devem "sempre" ser feitos em linhas separadas.

Import errado
    - import sys. os

Import certo
    - import sys
    - import os

Podemos importar partes de uma biblioteca, e não há problema em fazer isso. Ideal para no máximo 3 módulos.

from types import StringType, ListType

Para mais de 3, fazemos assim:
from types import (
    StringTupe,
    ListType,
    SetType,
    OutroType
)

imports devem ser colocadas no topo do arquivo, logo depois de qualquer comentário ou docstring e antes de constantes 
ou variáveis globais.
"""

# Espaços em expressões e instruções

"""
Observe os espaços desnecessários (erro de indentação)

Não faça: 
    funcao( algo[ 1 ],{outro: 2})

Faça:
funcao(algo[1],{outro:2})

Não faça:
algo (1)

Faça:
algo(1)

Não faça:
dict ['chave'] = list [indice]

Faça:
dict['chave'] = list[indice]

Não faça (observe a falta de espaço):
x=1
y=3

Faça:
x = 1
y = 3

Notas:
- Podemos fazer comentários com três aspas simples também ('''texto'''). Mas é preferível usar três aspas duplas!
- Sempre termine uma instrução com uma NOVA linha
"""
