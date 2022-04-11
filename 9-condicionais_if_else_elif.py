"""
ESTRUTURAS CONDICIONAIS:

if
else
elif > para mais de duas estruturas de condição. elif= else+if
"""

idade = 15

if idade < 18:  # veja que o dois pontos cria o bloco. Estrutura condicional na frente.
    print('Menor de idade!')
    print(f'{idade} anos')
elif idade == 18:  # Podemos ter vários "elfis"
    print('Tem 18 anos')
else:  # Estrutura condicional em baixo
    print('Maior de idade!')
    print(f'{idade} anos')

# veja que no python é muito mais limpo para escrever estruturas condicionais.
# Poderíamos ter vários if também, mas não é legal, fica muito poluído visualmente
