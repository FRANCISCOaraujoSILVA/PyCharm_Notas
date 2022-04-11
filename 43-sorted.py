"""
SORTED:

ELE SEMPRE IRÁ RETORNAR UMA LISTA (por padrão, mas posso mudar) COM OS ELEMENTOS DO ITERÁVEL
Sorted: Serve para ordenar, mas funciona além das listas, inclusive, para elas, também. Além disso, ele cria uma nova
lista ordenada, diferente do sort() - que ordena a própria lista
Obs.: Nâo confundir com a função sort() que já estudamos. Além disso, lembrar que sort() funciona APENAS em listas:
lembrar como usar:
dado_lista = [3, 2, 1]
dado_lista.sort()
>> [1, 2, 3]
"""
numeros = [6, 1, 8, 2]
print(numeros)  # Sem ordenação
print(sorted(numeros))  # Com ordenação e com uma nova lista
print(numeros)  # Sem ordenação, mesma distribuição dos dados originais
print('-----')
numeros1 = 6, 1, 8, 2,
print(sorted(numeros1))  # Retorna essa tupla em formato de lista ordenada

# Adicionando parâmetros ao sorted()
print(sorted(numeros1, reverse=True))  # Ordena e inverte a lista

# Convertendo o serted()
print(tuple(sorted(numeros1, reverse=True)))
print('-----')
# Exemplo mais complexo com o sorted()
usuarios = [
    {"username": "Samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "Carla", "tweets": ["Eu amo gatos"]},
    {"username": "Larissa", "tweets": []},
    {"username": "Pedro", "tweets": []},
    {"username": "Eliza", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "Anna", "tweets": []}
]


print(f'Os usuários do twitter:\n {usuarios}')
print('-----')
# print(sorted(usuarios))  # não vai funcionar, ele não itera em dicionário assim
print(sorted(usuarios, key=lambda usuario: usuario["username"]))  # Na chave, podemos passar até uma função para odern.
print('-----')
"""
Estamos ordenando pelo nome de usuário, mas podemos pelo tweets
"""

# Ordenando pela quantidade de tweets do usuário (do maior para o menor)
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets']), reverse=True))
print('-----')

# Imagine a lista de músicas, com seus respectivos títulos e quantidade de vezez que ela tocou.
musicas = [
    {"título": 'Rap', "tocou": 3},
    {"título": 'MPB', "tocou": 32},
    {"título": 'Sertanejo', "tocou": 21},
    {"título": 'Rock', "tocou": 80},
    {"título": 'Serenata', "tocou": 17}]

# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda mus: mus['tocou']))

# Ordena da mais tocada para a menos tocada
print(sorted(musicas, key=lambda mus: mus['tocou'], reverse=True))
