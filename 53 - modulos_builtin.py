"""
TRABALHANDO COMO MODULOS BUILTIN

- São módulos integrados que já vem instalados no python

Quando o Python é instalado:
 ________________________
|Python|Múdulos Builtins|
------------------------

No entanto, quando estamos usando a linguagem Python, o módulos builtins não carregados.
No terminal faça:
Python
dir()

E veja que lá tem o módulo builtins. Depois, faça:
dir(__builtins__)

Vejá que lá já tem todas as funções instaladas. Para carregar algumas delas para nosso uso, devemos importar
(import random, por exemplo)

Dica: Uma boa prática, seria pesquisar pela documentação no site do python.org/módulos. Lá tem bastante exemplo. Vale
muito apena pesquisar.

site: https://docs.python.org/3/py-modindex.html
"""

# Utilizando alias (apelidos) para módulos/funções
import random as rdm
print(rdm.random())
print('-----')

# Podemos importar todas as funções de um módulo utilizando o *

from random import *
print(random())
print('-----')
"""
Importante: veja que pressupõe-se que você já saiba o nome da função (random()). Além disso, a chamada da função é 
diferente, pois do outro modo:

import random
print(random.random())
"""

# Podemos dar um apelido para função também
from random import randint as rdi
print(rdi(5, 89))
print('-----')

# Importando duas funções e dando apelido para as duas

from random import randint as rdi, random as rdm
print(rdi(5, 89))
print(rdm())
print('------')

# Às vezes, a partir de um módulo queremos fazer vários imports

"Maneira confução"
from random import random, randint, uniform, shuffle, choice

"Maneira profissional, utilizando tuple para vários imports. Um import em cada linha seria o ideal"
from random import (random,
                    randint,
                    uniform,
                    shuffle,
                    choice)

print(random())
print(randint(1, 2))
print(uniform(2, 6))
lista = ['a', 'b', 'd']
shuffle(lista)
print(lista)
print(choice('Francisco Araújo'))





