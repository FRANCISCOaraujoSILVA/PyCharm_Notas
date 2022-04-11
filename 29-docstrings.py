"""
DOCSTRINGS:

Documentando funções com Docstring: São as aspas para comentários.
É importante documentar apenas o que é essencial

- Faça: print(help(print)) no terminal do Python, lá existem documentações docstring
help() or .__doc__
A aprência do help é melhor!
"""


# Exemplos:
def diz_oi():
    """A documentação de uma função simples"""
    return 'Olá!'

# No terminal, faça: from docstring import diz_oi
# help(diz_oi) or print(diz_oi.__doc__)


# o Próprio Python cria documentação automática
def exponencial(numero, potencia=2):
    """
    A função retorna o quadrado de outro, ou a qualquer potência informada
    :param numero:  Base, obrigatório
    :param potencia: Expoente, opicinal
    :return: Rertono a potênica de um número
    """
    return numero ** potencia
# Por algum motivo não estou conseguindo importar essa função no terminal
