"""
                                                O BLOCO TRY/EXCEPT


- Try = tente
- Except = capture a exceção

Utilizamos o bloco try/except para tratar erros que podem ocorrer em nosso código. Prevenindo, assim, que o programa
pare de funcionar e o usuário recebe mensangens de erro inesperadas. Se o erro não for tratada, pode fazer o usuário
perder a confiança em nossa aplicação.

Forma mais simples de utilzar:
    try:
        //execução problemática (tente fazer isso)
    except:
        //o que deve ser feito em caso de problema
"""

# Exemplo 1: Tratando um erro genérico (qualquer tipo) - não é recomendado. O recomendado é tratar de forma específica

try:
    geek()
except:
    print('Deu Algum problema.')

# Em palavras: tente executar a funçõa geek(), caso encontre erros imprima: 'Deu Algum problema.'
print('Veja que conseguimos tratar o erro para que o código continue.')
print('-----')

# Exemplo 2: Tratando um erro específico

try:
    geek()  # Gera NameError
    # len(5) # Gera TypeError
except NameError:  # Ou seja, capturamos apenas o erro do tipo NameError. Se o erro for de outro tipo, não será tratado.
    print('Você está utilizando uma função inexistente')
print('-----')

# Exemplo 3: Podemos apelidar nossos erros

try:
    len(5)
except TypeError as err:  # err é um apelido padrão
    print(f'A aplicação gerou o seguinte erro: {err}')
print('-----')

# Exemplo 4: Diversos tratamentos de erros de uma única vez

try:
    len(5)
except NameError as erra:  # Veja que não temos erro. Mas se tivesse, seria detectado
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
print('-----')

# Exemplo 5: Criando uma função para capturar um erro dentro da função


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None


dic = {'nome': 'Francisco'}
print(pega_valor(dic, 'game'))  # Essa chave não existe
print(pega_valor(dic, 'nome'))  # Essa chave existe
