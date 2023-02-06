"""
                        RECEBENDO DADOS DO USUÁRIO - TODO DADO RECEBDIDO VIA INPUT É DO TIPO STRING


Outros exemplos de string:
- aspas simples
    'Palavra'
- aspas duplas
    "Palavra"
- aspas simples triplas
    '''Palavra'''
- aspas duplas triplas
    ""Palavra""     # Só não coloquei as três aspas duplas, de fato, para não dar erro aqui no python, haja vista já ter
aspas duplas e triplas logo abaixo
"""

# Entrada de dados

# Podemos fazer esse input apenas em uma linha. Muito mais elegante

# print("Qual é o seu nome?")
# nome = input()

nome = input('Qual o seu nome? ')

# Exemplo de print antigo

# print('seja bem vindo(a) %s' % nome)

# Exemplo de print moderno

# print('seja bem-vindo(a) {0}'.format(nome))

# Exemplo de print 'mais atual'. Perceba que o f é de >>format. Eu prefiro usar este

print(f'Seja bem-vindo(a) {nome}!')

# Podemos fazer esse input apenas em uma linha. Muito mais elegante

# print('Qual sua idade?')
# idade=input()

idade = input('Qual a sua idade? ')

# Saída

# Exemplo de print antigo

# print('O %s tem %s anos' % (nome,idade))

# Exemplo de print moderno

# print('O(a) {0} tem {1} anos'.format(nome,idade))

# Exemplo de print 'mais atual'. Percebe que o f é de >>format

print(f'O(a) {nome} tem {idade} anos, ou seja, nasceu em {2021-int(idade)}.')

"""
- O int(idade) => cast
- Cast é a conversão de um tipo de dado. Ou seja, conseguimos subtrair uma string de um número (percebeu?)
- Podemos fazer cálculos dentro das chaves
- É importante notar que eu poderia tirar esse int aqui de baixo e colocar lá no input da idade, antes do input, para
transformar em inteiro logo no início

Nota:
Achei o jeito atual muito mais maneiro e profissional. A coisa está ficando boa.
"""
