"""
                                                        MAPAS


- Em Python são conhecidos como dicionários
- Dicionários são representados por chaves
"""

receita = {'jan': 100, 'fev': 250, 'mar': 400}

# Iterar sobre dicionários

# Pegando a chave

for chave in receita:
    print(chave)
print('-----')

# Ou, pegando o valor

for chave in receita:
    print(receita[chave])  # Aqui estamos querendo o valor da receita. Isso é muito importante
print('-----')

print(receita)
print('-----')

for chave in receita:
    print(f'Em {chave}: recebi o valor de {receita[chave]} R$')  # Outro exemplo muito útil. Importante
print('-----')

# Podemos pedir todas as chaves em um dicionário

print(receita.keys())

# Podemos acessar todos os valores em um dicionário

print(receita.values())
print('-----')

# Modo pythônico de trabalhar

for chave in receita.keys():
    print(receita[chave])
print('-----')

# Desempacotamento de dicionário. Outro detalhe importante

for chave, valor in receita.items():
    print(f'Chave={chave}\nValor={valor}\n')  # Gostei dessa manipulação
print('-----')


# Soma, valor máximo, valor mínimo, tamanho

# Se os valores forem todos inteiros ou reais, daí a importância de usar a propriedade "values()"

print(f' Soma dos valores: {sum(receita.values())}')
print(f' Valor máximo: {max(receita.values())}')
print(f' Valor mínimo: {min(receita.values())}')
print(f' O tamanho do dicionário: {len(receita)}')
