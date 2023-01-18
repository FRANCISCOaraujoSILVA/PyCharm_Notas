"""
DICTIONARY COMPREHENSION:

Pense:
se quisermos criar:
lista = [1, 2, 3, 4]
tupla = (1, 3, 5, 5) ou 1, 3, 5, 5,
conjunto = {1, 3, 5, 5}
dicionário {'a': 1, 'b': 2}

# sintaxe
{chave: valor for valor in interável}: dictionary comprehension
[valor for valor in iterável]: list comprehension
"""

# exemplo
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e':5}
quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
"""
 Ou seja, vamos elevar todos os valores ao quadrado. Mas não modificamos a chave
 """

print(f'O dicionário ao quadrado: {quadrado}')
print('-----')


"""
Imagine que você tem uma lista de números, e deseja elevar esses números ao quadrado e colocar em um dicionário:
"""

numeroListas = [1, 3, 5, 6]
# numeroListas = {1, 3, 5, 6}  # Poderíamos também usar esse set
quadrad = {valor: valor**3 for valor in numeroListas}  # lembrar que dicionário não aceita chave repetida.
print(f'O cubo dos valores da lista em um dicionário: {quadrad}')
print('-----')

# Criando chaves e valores a partir de uma string e uma lista

chavesss = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chavesss[i]: valores[i] for i in range(0, len(valores))}
print(f'Juntando as chaves: {mistura}')
print('-----')

# Exemplo com estrutura condicional
numpe = [1, 2, 3, 4, 5, 6]
res = {num: ('par' if num % 2 == 0 else 'ímpar') for num in numpe}
print(f'O dicionário com as específicações: {res}')