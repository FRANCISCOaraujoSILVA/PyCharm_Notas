"""
LAMBDAS:

Utilizando lambdas:
    - São funções sem nome, anônima
    - Palavra reservada: lambda
    - Podemos ter múlitplas entradas

Obs.: Só aceita a quantidade de argumentos esperados
"""


def fucao(x):
    return 3 * x + 1


print(f'O retorno: {fucao(2)}')
print('-----')

# Expressão lambda
lambda x: 3 * x + 1

"""
x-> Parâmetros de entrada
Como não tem nome, vamos direto para o retorno: 3 * x + 1
"""

# Como utilizar a expressão lambda? Podmeos dar um nome a ela
calc = lambda x: 3 * x + 1  # Não é a forma correta de utilização dessas expressões.


print(f'O valor do cálculo: {calc}')
print('-----')

# Imagine um formulário, com nome e sebrenome em campos diferentes, com múltiplas entradas. Mas precisamos do nome
# e sobrenome.

"""
Entradas: logo após a palavra reservada "lambda" e antes dos dois pontos.
nome e sobrenome: são duas entradas

strip(): nome = ' Francisco '; nome.strip() = 'Francisco'. Ou seja, remove espaços no início e no fim.
title(): Transforma a primeira letra em caixa alta
"""

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo(' francisco', ' araújo   '))
print('-----')


# lambda sem entrada
like = lambda: 'Como não gostar do Python?'
love = lambda x: 3 * x
avenue = lambda x, y: x * y

print(like())
print(love(4))
print(avenue(1, 4))
print('-----')


# lista de autores

autores = ['Francisco Araújo', 'Senhora lendy', 'Senhora alquimista', 'Os três', 'O grande êxodo', 'L. G. Almeida']
print(autores)
print('-----')

# E se precisar ordenar pelo sobrenome? Usando o lambda de forma Pythônica
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())  # [-1] pega o útlimo elemento da lista, RODA
# sort(). faz a ordenação
print(autores)
print('-----')

# split(): gera lista a cada espaço
# lower(): transforma tudo em minúsculo

"""
Agora, uma aplicação muito interessante.
Vamos criar uma função quadrática, recebendo as constantes e o valor da variável x.
"""


def geradora_quadratica(a, b, c):
    return lambda x: a*x**2+b*x+c


Teste = geradora_quadratica(2, 4, 4)
print(Teste(2))
print(Teste(-1))
print(Teste(25))
print('-----')

# ou

print(f'O valor da função quadrática: {geradora_quadratica(2, 4, 4)(2)}')
print(f'O valor da função quadrática: {geradora_quadratica(2, 4, 4)(-1)}')
print(f'O valor da função quadrática: {geradora_quadratica(2, 4, 4)(25)}')
print('-----')

"""
E onde aplicamos as expressões lambdas?
Geralmente: 
    -filtragem
    -ordenação de dados
"""
