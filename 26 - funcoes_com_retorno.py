""""
                                            FUNÇÕES COM RETORNO


Obs.: Não precisamos criar uma variável para receber a variável de retorno. Podemos passar a execução da função para
outra função ou para o próprio print.

Posso importar minha função direto no terminal:

from nomeDoArquivo import nomeDafunção
nomeDafunção

O import abaixo será usado no fim do código.
"""

from random import random

numeros = [1, 2, 3]
ret_por = numeros.pop()  # O pop remove e retorna o último elemento da lista. Mas nesse caso, não retorna diretamente
print(f'Retorno de pop: {ret_por}')  # Mostrando o elemento removido
print('-----')

ret_pr = print(numeros)
# Veja o erro (cobrinha) acima, pois estamos criando uma variável para receber uma variável de retorno
print(f'O retorno de print: {ret_pr}')  # Veja que a função print não retorna nada, daí o aviso
print('-----')


def quadrado_de_7():
    print(7 * 7)
    # Só estamos imprimindo, mas não retornando. Muito cuidado com isso.  É diferente


print('-----')


rettt = quadrado_de_7()
print(f'O retorno do print: {rettt}')  # Veja que não temos com retornar algo com o print. É None. veja o aviso
print('-----')

# REFATORANDO (reescrevendo) o problema. Ou seja, vamos dar uma melhorada no código


def quadrado_de_8():
    return 8*8  # O return retorna o resultado


rett = quadrado_de_8()  # Observe que agora não temos mais o erro. Já que agora a função possui retorno

# Diferentes formas de usar aquele resultado

print(f'O retorno de 8 é: {rett}')
print(f'O retorno de 8 é: {quadrado_de_8()}')
print(f'O retorno de 8 é: {quadrado_de_8()*2}')
print('-----')

# Note que a grande sacada é o "return". Ou seja, o que retornamos agora é o valor do quadrado, e o erro desaparece


def diz_oi():
    return 'Olá'
# Se fosse com um print não dava para somar lá em baixo, já que seria None
# Se fosse print, não iríamos conseguir fazer cálculos com ele


alguem = ' Lara!'
print(diz_oi() + alguem)  # Veja que o return oferece mais flexibilidade para usar variáveis

"""
Notas:
- O return finaliza a função, ou seja, ela sai da execução da função
- Podemos ter diferentes returns para a mesma função, mas apenas um é executado
- Podemos, em uma função, retornar qualquer tipo de dado e até múltiplos valores
"""
print('-----')

# Exemplo 1: Finalizando com return


def diz_ola():
    print('Executado antes do return')  # Executa
    return 'Olá'  # Retorna
    print('Estou sendo executado? Não, pois está após o return.')  # Essa linha nunca será executada e retornada


print(diz_ola())
print('-----')

# Exemplo 2: Diferentes returns


def nova_funcao():
    variavel = None  # Iniciando a variável
    if variavel:  # Se a variável for True retorna 4, se for None retorna 3.2, e se for falso retorna 'Última opção'
        return 4
    elif variavel is None:
        return 3.2
    return 'Última opção'


# Veja que temos diferentes returns

print(nova_funcao())
print('-----')

# Exemplo 3: Retornando múltiplos valores


def outra_funcao():  # Lembre-se que números separados por vírgulas são tuplas
    return 2, 3, 4, 5


num1, num2, num3, num4 = outra_funcao()
# Seria tipo um desempacotamento de função. MUITO IMPORTANTE ISSO AQUI

print(num1, num2, num3, num4)
print(type(print(num1, num2, num3, num4)))  # Veja que está sem tipo
print('-----')

# Ou

print(outra_funcao())  # Retorna no formato tupla como foi definido na def
print('-----')

# Vamos criar uma função para jogar a moeda

# No terminal, dá para importar nosso script (módulo) e qualquer função desse script


def joga_moeda():
    # Gera um número pseudo randômico entre zero e um. Pseudo, pois o número pode se repetir

    if random() > 0.5:
        return 'Cara'
    return 'Coroa'  # Observe que já está fazendo o papel do else. IMPORTANTE ISSO AQUI


print(joga_moeda())  # Para cada run, retornamos cara ou coroa
print('-----')


# Codificações DESNECESSÁRIAS no return

# % --> Verifica o resto da divisão
# != --> Diferente


def e_impar():
    numero = 4
    if numero % 2 != 0:
        return True
    else:  # Este else é desnecessário
        return False


print(e_impar())
