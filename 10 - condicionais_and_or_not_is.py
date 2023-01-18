"""
                                             ESTRUTURAS CONDICIONAIS


Operadores binários:
    - and (e): ambos precisam ser verdadeiros
    - or (ou): ou um ou o outro precisa ser verdadeiro

Operadores unários:
    - not (não): o valor do booleano é INVERTIDO, ou seja, se for True, vira False, se for False, vira True. É uma
    negação, um operador de negação
    - is (é): é muito usado para COMPARAÇÃO como forma de pergunta, retorna True ou False

Obs.:
- É importante notar que o "if" verifica se uma expressão é verdadeira ou falsa
- Quanto mais alto o nível da programação, mais próximo da linguagem humana. Por outro lado, quanto mais baixo, mais
próximo da linguagem das máquinas

Veja, quando usamos a função integrada dir() no console do Python, temos "is" nas iniciais de algumas expressões.
Faça no seu terminal:
nome = 'Francisco'
dir(nome)  --> veja que lá temos várias propriedades começando com o "is"

faça:
nome.isupper()
nome.title()
"""

ativo = False
logado = False

if ativo or logado:  # O que ele está dizendo é: se ativo ou logado for True: Executa a ação. Lembrar da prop. de "or"
    print('Bem vindo usuário!')
else:
    print('Você precisa ativar sua conta, Por favor, cheque seu email.')
    print('-----')
if not ativo:  # Se ativo não for True
    print('Você precisa ativar sua conta. Por favor, cheque seu email!!!')
else:  # Se ativo for True
    print('Bem-vindo usuário!')
print('-----')

print(not True)
print(not False)
print('-----')

if ativo is False:  # Uma maneira redundante de fazer a análise
    print('Você precisa ativar sua conta.')
else:
    print('Bem-vnido usuário!')
print('-----')

if not ativo:  # Uma maneira pythônica de fazer a análise: se não está ativo você prescisa ativar sua conta
    print('Você precisa ativar sua conta.')
else:
    print('Bem-vindo usuário!')
print('-----')

# Ativo é True?

print(ativo is True)

# Ativo é False?

print(ativo is False)
