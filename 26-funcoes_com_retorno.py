""""
FUNÇÕES COM RETORNO:

Obs.: Não precisamos criar uma variável para receber a variável de retorno. Podemos passar a
execução da função para outra função ou para o próprio print.

Posso importar minha função direto no terminal:
"from nomeDoArquivo import nomeDafunção"
nomeDafunção

O import abaixo será usado no fim do código.
"""
from random import random

numeros = [1, 2, 3]
ret_por = numeros.pop()  # pop remove e retorna o último elemento de uma lista. Mas nesse caso, não retorna diretamente.
print(f'Retorno de pop: {ret_por}')  # mostrando o elemento removido.
print('-----')

ret_pr = print(numeros)  # veja o erro (cobrinha).
print(f'O retorno de print: {ret_pr}')  # veja que a função print não retorna nada, daí o aviso.
print('-----a')


def quadrado_de_7():
    print(7 * 7)
    # só estamos imprimindo, mas não retornando. Muito cuidado com isso.  É diferente.


print('-----a')

rettt = quadrado_de_7()
print(f'O retorno do print: {rettt}')  # Veja que não retornamos nada com o print. É None. veja o erro (cobrinha).
print('-----')

# REFATORANDO (reescrevendo) o  problema. Ou seja, vamos dar uma melhorada no código.


def quadrado_de_8():
    return 8*8  # o return retorna o resultado.


rett = quadrado_de_8()  # veja que agora não temos mais erro. Já que agora possui retorno.

# diferentes formas de usar aquele resultado.
print(f'O retorno de 8 é: {rett}')
print(f'O retorno de 8 é: {quadrado_de_8()}')
print(f'O retorno de 8 é: {quadrado_de_8()*2}')
print('-----')

# veja que a grande sacada é o "return". Ou seja, o que retornamos agora é o valor do quadrado, e o erro desaparece.


def diz_oi():
    return 'Olá'
# Se fosse com um print não dava para somar lá em baixo, já que seria none.
# Se fosse print, não iriamos conseguir fazer cálculos com ele.


alguem = ' Lara!'
print(diz_oi() + alguem)  # Veja que o return oferece mais flexibilidade para usar variáveis.

"""
Notas:
1 - o return finaliza a função, ou seja, ela sai da execução da função.
2 - podemos ter diferentes return para a mesma função, mas apenas um é executado.
3 - podemos, em uma função, retornar qualquer tipo de dado e até múltiplos valores.
"""
print('-----')

# Exemplo 1 - Finalizando com return.


def diz_ola():
    print('Executado antes do return')  # executa
    return 'Olá'  # retorna
    print('Estou sendo executado? Não, pois está após o return')  # nunca será executado e retornado.


print(diz_ola())
print('-----a')

# Exemplo 2 - Diferentes returns.


def nova_funcao():
    variavel = None  # iniciando a variável.
    if variavel:  # se a variável for True, retorna 4, se for None, retorna 3.2, se for falso retorna 'Última opção'.
        return 4
    elif variavel is None:
        return 3.2
    return 'Última opção'


# veja que temos diferentes returns.
print(nova_funcao())
print('-----b')

# Exemplo 3 - retornando múltiplos valores.


def outra_funcao():  # número separado por vírgula são tuplas.
    return 2, 3, 4, 5


num1, num2, num3, num4 = outra_funcao()
# Seria tipo um desempacotamento de função. MUITO IMPORTANTE ISSO AQUI.

print(num1, num2, num3, num4)
print(type(print(num1, num2, num3, num4)))  # Veja que está sem tipo.
print('-----c')

# or
print(outra_funcao())  # retorna no formato tupla como foi definido na def.
print('-----d')

# vamos criar uma função para jogar a moeda.

# No terminal, dá para importar nosso script (o pacote) e qualquer função desse script, da mesma maneira.


def joga_moeda():
    # gera um número pseudo randômico entre zero e um. Pseudo, pois pode repetir.

    if random() > 0.5:
        return 'Cara'
    return 'Coroa'  # já tá fazendo o papel do else. IMPORTANTE ISSO AQUI.


print(joga_moeda())  # Para cada run, retornamos cara ou coroa
print('-----')


# codificações DESNECESSÁRIAS no return:
# %: verifica o resto da divisão
# !=: diferente


def e_impar():
    numero = 4
    if numero % 2 != 0:
        return True
    else:  # esse else é desnecessário
        return False


print(e_impar())
