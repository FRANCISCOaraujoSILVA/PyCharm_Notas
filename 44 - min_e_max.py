"""
MIN E MAX:

max e min: retorna o maior/menor valor em um iterável ou o maior/menor de dois ou mais elementos.
funciona para:
- lista
- tupla
- set
- dicionário. Esse precisa de cuidado
"""
"""
# Exemplos
lista = [1, 8, 4, 99, 34, 129]
print(max(lista))
print('-----')

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario))  # Vai retorna "f", a maior chave
print(max(dicionario.values()))  # Vai retorna 129, o maior valor
"""

# Olha como é fácil no Python, nem precisamos de estrutura condicional para obter um dado
# Construir um código que recebe dois valores do usuário e retorna o maior

# valor1 = int(input('Digite o primeiro valor: '))
# valor2 = int(input('Digite o segundo valor: '))
# print(f'O maior valor: {max(valor1, valor2)}')

# or
print(max('a', 'b', 'g'))  # retorna o maior em relação a posição no alfabeto
print(max('a', 'ab', 'abc', 'abcd'))  # retorna o maior em relação a quantidade de elementos
print(max(1.3344, 1.3343))
print('-----')

# Outros exemplos:
nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivandader']
print(max(nomes))  # Vai localizar o 'Tim', pois está levando em consideração a ordem alfabética
print(min(nomes))  # Vai licalizar o 'Arya', pois está levando em consideração a ordem alfabética
print('-----')

# Como encontrar o maior nome? Vamos alterar o comportamento padrão do max()
print(max(nomes, key=lambda nome: len(nome)))  # Vai buscar o que possui mais caracteres
print('-----')

"""
O que estamos fazendo é:
Para cada nome, na lista de nomes, vamos ordenar pelo tamanho dos nomes.

E como saber se posso fazer essas alterações?
Faça no terminal:
help(max): lá temos um parâmetro que recebe uma função

Ou, use o ctrl na função max(). Acho que esse meio mais recomendado
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

# Desafio: imprimir apenas o título da música mais/menos tocada
print(f"O título da música mais tocada: {max(musicas, key=lambda nome: nome['tocou'])['título']}")
print(f"O título da música menos tocada: {min(musicas, key=lambda nome: nome['tocou'])['título']}")

# Essa sacada de enxergar a própria função como objeto, e pedir a chave, foi muito bom

# Desafio: como encontrar a música mais/menos tocada sem o max/min e sem o lambda?

max = 0

for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(f"O título da música que mais tocou com o loop for: {musica['título']}")

"""
Veja que dá muito mais trabalho sem o max e as expressões lambdas.
"""