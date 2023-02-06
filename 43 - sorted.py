"""
                                                        SORTED


- Sorted: Serve para ordenar, mas funciona além das listas, inclusive, para elas, também. Além disso, ele cria uma nova
lista ordenada, diferente do sort() - que ordena a própria lista
- Ele sempre irá retornar uma lista (por padrão, mas posso mudar) com os elementos do iterável

Nota:
Não confundir com a função sort() que já estudamos. Além disso, lembrar que sort() funciona APENAS em listas.

Lembre-se como usar a função sort():
    dado_lista = [3, 2, 1]
    dado_lista.sort()
    >> [1, 2, 3]
"""

numeros = [6, 1, 8, 2]
print(numeros)  # Sem ordenação
print(sorted(numeros))  # Gera uma nova lista com ordenação
print(numeros)  # Sem ordenação, mesma configuração da lista 'numeros'
print('-----')

numeros1 = 6, 1, 8, 2,
print(sorted(numeros1))  # Retorna essa TUPLA em formato de LISTA ordenada

# Adicionando parâmetros ao sorted()

print(sorted(numeros1, reverse=True))  # Ordena e inverte a lista. Gostei dessa

# Convertendo o sorted() em tupla

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
# print(sorted(usuarios))  # não vai funcionar, ele não itera em dicionários dessa forma
print('-----')

print(sorted(usuarios, key=lambda usuario: usuario["username"]))  # Na chave, podemos passar até uma função para ordenar
print('-----')

# Estamos ordenando pelo nome de usuário, mas também podemos ordenar pelo tweets

# Ordenando pela quantidade de tweets do usuário (do maior para o menor)

print(sorted(usuarios, key=lambda usuario: len(usuario['tweets']), reverse=True))
print('-----')

# Imagine a lista de músicas, com seus respectivos títulos e quantidade de vezez que ela tocou

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
