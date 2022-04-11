"""
ESTRUTURAS CONDICIONAIS:

Operadores binários
    and(e) - ambos precisam ser verdadeiros
    or(ou) - ou um ou outro precisa ser verdaderio
Operadores unários
    not(não) - o valor do boolenao é invertido, ou seja, se for True, vira False, se for False, vira True. É uma negação
    operador de negação
    is(é) - é muito usado para comparação como forma de pergunta, retorna True ou False

o "if" verifica se a expressão é verdadeira ou falsa

obs.: quanto mais alto o nível da programação, mais próximo da linguagem humana, quanto mais baixo, mais
próximo das máquinas

temos os is nas iniciais de algumas expressões quando consultamos o "dir"
no terminal:
nome = 'Francisco'
dir(nome)      > veja que lá temos várias propriedades começando com o "is"

faça:
nome.isupper()
nome.title()
"""
ativo = True
logado = False

# if ativo or logado:
#     print('Bem vindo usuário!')
# else:
#    print('Você precisa ativar sua conta, Por favor, cheque seu email')
print('-----')
if not ativo:  # se não for ativo
    print('Você precisa ativar sua conta. Por favor, cheque seu email')
else:  # se for ativo
    print('Bem-vido usuário')
print('-----')

print(not True)
print(not False)
print('-----')

if ativo is False:  # jeito redunte de analisar
    print('Você precisa ativar sua conta')
else:
    print('Bem-vido usuário')
print('-----')

if not ativo:  # jeito pythônico de fazer a análise, se não está ativo você prescisa ativar sua conta
    print('Você precisa ativar sua conta')
else:
    print('Bem-vido usuário')
print('-----')

# ativo é True?
print(ativo is True)
# ativo é False?
print(ativo is False)
