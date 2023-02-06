"""
                                               SET COMPREHENSION


Lembre-se que set não guarda ordenação e não aceita repetição de valores.
"""

# Exemplo

numeros = {num for num in range(1, 7)}  # Note que no List Comprehension usamos colchetes, aqui usamos chaves
print(numeros)
print('----')

# Outro

res = {num**3 for num in range(10)}
print(res)
print('-----')

# Gerando um dicionário

resp = {num: num**3 for num in range(10)}
print(resp)
print('-----')

# Exemplo com string

letras = {letra for letra in 'Francisco Araújo'}
print(f'O set de letras: {letras}')
