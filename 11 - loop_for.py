"""
                                                    LOOP FOR


LOOP - repetição
FOR - umas das estruturas de repetição

- Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis
- Dica para abrir a documentação de qualquer função: ctrl + (clique em cima da função)
- Podemos multiplicar uma string pelo nome

Dicas para concatenar:
    nome = 'Francisco'
    nome + ' Araújo
"""

nome = 'Francisco Araújo'  # Faça: nome[0] e veja que o primeiro elemento (F) dessa lista de string será retornado
print(f'O primeiro elemento da lista: {nome[0]}.')
print('-----')

lista = [1, 3, 5, 7, 9]
print(f'O tipo da lista: {type(lista)}.')
numeros = range(1, 10)  # Não é uma lista, é um range. Depois veremos como transformar um range em uma lista
print(f'O tipo da lista: {type(numeros)}.')
print('-----')

# Exemplo de for 1: iterando em uma string

for letra in nome:
    print(f'Iterando em uma string: {letra}')
print('-----')

# Exemplo de for 2: iterando em uma lista

for numero in lista:
    print(f'Iterando em uma lista: {numero}')
print('-----')

# Exemplo de for 3: iterando em um range

for numero in range(1, 10):  # Isso lembra muito o linspace. Obs.: O range não inclui o último n°, vai até o elemento 9
    print(f'Iterando em um range: {numero}')
print('-----')

# Agora vamos iterar relacionando cada índice da lista, como uma forma de referência

"""
Enumerate: Retorna índice e valor
((1, 'F'), (2, 'r'), (3, 'a'), (4, 'n'), (5, 'c'), (6, 'i'), (7, 's'), (8, 'c'), (9, 'o'), (10, '')...)
"""

nome = 'Dua Lipa'
for letra, indice in enumerate(nome):
    print(f"Com o índice 'letra' estamos captando a letra: {nome[letra]}")
print('-----')

for _, letra in enumerate(nome):  # Outra forma, quando não precisamos do índice, descartamos com o underline
    print(letra)
print('-----')

for dado in enumerate(nome):  # Retorna índice e valor
    print(dado)
print('-----')

for valor in enumerate(nome):
    print(valor[0])  # Somente os índices

# Vamos agora para um exemplo prático de como usar o laço for aqui Python

quantidade = int(input('Quantas vezes esse loop deve rodar? '))  # Com o int garantimos que o número seja inteiro
for n in range(0, quantidade+1):
    print(f'Imprimindo: {n}')
print('-----')

Nome = 'Um novo nome!'

for letra in Nome:
    print(letra, end='/')

# O end='' faz com que as impressões sejam feitas na mesma linha com um espaçamento pré-especificado
