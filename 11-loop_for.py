"""
LOOP - repetição
FOR - umas das estruturas

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Dica para ir na documentação da função: ctrl+clique na função
Podemos multiplicar uma string pelo nome

Dicas para concatenar:
nome = 'Francisco'
nome + ' Araújo

"""

print('-----')
nome = 'Francisco Araújo'  # faça: nome[1]
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # temos que tranformar em uma lista, ainda, vamos ver depois

print('-----')
# Exemplo de for 1 (iterando em uma string)
for letra in nome:
    print(letra)

print('-----')
# Exemplo de for 2 (iterando em uma lista)
for numero in lista:
    print(numero)

print('-----')
# Exemplo de for 3 (iterando em um range)
for numero in range(1, 10):  # lembra muito o linspace. Obs.: O range não inclui o último, nesse caso do python
    print(numero)

print('-----')
# E se quisermos os índices?

"""
Enumerate: trás dois valores
((1, 'F'), (2, 'r'), (3, 'a'), (4, 'n'), (5, 'c'), (6, 'i'), (7, 's'), (8, 'c'), (9, 'o'), (10, '')...)
Retorna o número e a letra.
"""

for indice, letra in enumerate(nome):
    print(nome[indice])
print('-----2')


for _, letra in enumerate(nome):  # é uma outra forma de fazer, quando não precisamos do número descartamos com o under.
    print(letra)

print('-----3')

for dado in enumerate(nome):  # Retorna o índice e valor
    print(dado)
print('-----4')

for valor in enumerate(nome):
    print(valor[0])  # Somente os índices


# Outras formas de usar o for aqui no python

quantidade = int(input('Quantas vezes esse loop deve rodar? '))
for n in range(1, quantidade+1):
    print(f'Imprimindo: {n}')
print('-----')

Nome = 'Um novo nome!'

for letra in Nome:
    print(letra, end='  ')  # o end='' faz com que as impressões sejam feitas na mesma linha com um espaçado pré-
# especificado
