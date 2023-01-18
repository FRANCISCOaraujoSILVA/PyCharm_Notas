"""
                                                    TIPO BOOLEANO


- Esse tipo vem da álgebra booleana, criada por George Boole
- Para o tipo booleano temos duas constantes, verdadeiro ou falso
    True: verdadeiro
    False:falso

Nota:
Não podemos usar letras minúsculas para representar "True" ou "False".
Usado também para operações básicas.
"""

ativo = False

print(ativo)
print('-----')

# Operações básicas

# Negação (not)

"""
Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso,
se for falso o resultado será verdadeiro. Ou seja, sempre ao contrário.
"""

print(not ativo)
print('-----')

# Ou (or)

"""
Retorna um valor verdadeiro:

True or True: True
True or False: True
False or False: False
"""

logado = False
print(ativo or logado)
print('-----')

# E (and)

"""
Ambos os valores devem ser verdadeiros, mas a recíproca não é verdadeira. Confira no último boobleano (False and False).

True and True: True
True and False: False
False and False: False
"""

print(ativo and logado)
print('-----')
