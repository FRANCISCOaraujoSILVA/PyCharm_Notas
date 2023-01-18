"""
SET COMPREHENSION:

Lembrar que set não guarda ordenação e não aceita repetição de valores.
"""
# exemplo

numeros = {num for num in range(1, 7)}
print(numeros)
print('----')

# outro
res = {num**3 for num in range(10)}
print(res)
print('-----')

# gerando um dicionário
resp = {num: num**3 for num in range(10)}
print(resp)
print('-----')

# exemplo com string
letras = {letra for letra in 'Francisco Araújo'}
print(f'O set de letras: {letras}')
