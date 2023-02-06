"""
                                                    MIN E MAX


- Min e max: retorna o menor/maior valor em um iterável ou o menor/maior de dois ou mais elementos
- Funciona da seguinte forma:
    - lista
    - tupla
    - set
    - dicionário. Esse precisa de cuidado

Exemplo com lista:
    lista = [1, 8, 4, 99, 34, 129]
    print(max(lista))

Exemplo com dicionário:
    dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
    print(max(dicionario)) --> Retorna 'f', a maior chave
    print(max(dicionario.values())) --> Retorna 129, o maior valor

Nota:
Observe como é fácil no Python, nem precisamos de estrutura condicional para obter esse tipo de informação.
"""

# Construir um código que recebe dois valores do usuário e retorna o maior

# valor1 = int(input('Digite o primeiro valor: '))
# valor2 = int(input('Digite o segundo valor: '))
# print(f'O maior valor: {max(valor1, valor2)}')
# print('-----')

# Ou

print(max('a', 'b', 'g'))  # Retorna o maior em relação a posição no alfabeto
print(max('a', 'ab', 'abc', 'abcd'))  # Retorna o maior em relação a quantidade de elementos
print(max(1.3344, 1.3343))
print('-----')

# Outros exemplos

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivandader']

print(max(nomes))  # Vai localizar o 'Tim', pois está levando em consideração a ordem alfabética
print(min(nomes))  # Vai licalizar o 'Arya', pois está levando em consideração a ordem alfabética
print('-----')

# Como encontrar o maior nome? Vamos alterar o comportamento padrão do max()

print(max(nomes, key=lambda nome: len(nome)))  # Vai buscar o que possui mais caracteres
print('-----')

"""
O que estamos fazendo é: Para cada nome, na lista de nomes, vamos ordenar pelo tamanho dos nomes.

E como saber se posso fazer essas alterações?
Faça no terminal:
help(max): lá temos um parâmetro que recebe uma função

Ou, use o CTRL na função max(). Considero esse como sendo o meio mais recomendado.
"""

musicas = [
    {"título": 'Rap', "tocou": 3},
    {"título": 'MPB', "tocou": 32},
    {"título": 'Sertanejo', "tocou": 21},
    {"título": 'Rock', "tocou": 80},
    {"título": 'Serenata', "tocou": 17}]

print(f"A música que mais tocou:\n{max(musicas, key=lambda nome: nome['tocou'])}")
print(f"A música que menos tocou:\n{min(musicas, key=lambda nome: nome['tocou'])} ")
print('-----')

# Desafio 1: Imprimir apenas o título da música mais/menos tocada

print(f"O título da música mais tocada: {max(musicas, key=lambda nome: nome['tocou'])['título']}")
print(f"O título da música menos tocada: {min(musicas, key=lambda nome: nome['tocou'])['título']}")

# Essa sacada de enxergar a própria função como objeto, e pedir a chave, foi muito boa

# Desafio 2: Como encontrar a música mais/menos tocada sem o max/min e sem o lambda?

max = 0

for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(f"O título da música que mais tocou com o loop for: {musica['título']}")

# Note que dá muito mais trabalho sem o max e as expressões lambdas.
