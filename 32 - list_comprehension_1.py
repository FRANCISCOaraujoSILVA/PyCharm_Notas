"""
                                        LIST COMPREHENSION - PARTE 1


- COMPREHENSION: Poderoso. Apenas na linguagem python

Parte 1:
    - Utilizando o List Comprehension, podemos gerar novas listas com dados processados a partir de outro iterável

Sintaxe:

[dado for dado in iterável]: Para cada dado na coleção, precesse o dado. Veja que lemos de trás para frente
    - Dado: variável
    - Iterável: coleção
"""

# Exemplo 1

numeros = [10, 20, 30, 40, 50, 60]
res = [dado/10 for dado in numeros]  # Ou seja, estamos dividindo cada dado da coleção por 10
print(f'A funcionalidade da List Comprehension: {res}')
print('-----')

"""
Conclusão:
    - Parte 1: for dado in numeros --> Para cada número na lista
    - Parte 2: dado/10 --> O que queremos fazer com o dado
"""

# Exemplo 2


def uma_funcao(numer):
    return numer*numer


print(uma_funcao(2))
print('-----')


listao = [1, 2]
resp = [uma_funcao(dado) for dado in listao]
print(f' A função aplicada numa lista qualquer trabalhando com o list comprehension: {resp}')  # Muito legal!
print('-----')

# Loop Convencional versus List Comprehension

# loop: Para quem conhece o Python

umalista = [10, 20, 30, 40]
umaListaVazia = []

for N in umalista:
    num_dobrado = N*2
    umaListaVazia.append(num_dobrado)

print(f' A lista original: {umalista}')
print(f' A lista dobrada: {umaListaVazia}')
print('-----')

# List Comphension: Para quem conhece o Python Avançado. Observe que economizamos Várias linhas de código

print(f' A lista dobrada com List Comprehension: {[numero*2 for numero in umalista]}')
print('-----')
