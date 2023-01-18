"""
                                                    DOCSTRINGS


- Documentando funções com Docstring: São as aspas para comentários
- É importante documentar apenas o que é essencial
- Faça: print(help(print)) no terminal do Python. Note que lá existem documentações docstrings
help() or .__doc__
A aparência do help é melhor!
"""

# Exemplos


def diz_oi():
    """A documentação de uma função simples"""
    return 'Olá!'

# No terminal, faça: from docstring import diz_oi
# help(diz_oi) or print(diz_oi.__doc__)


# O próprio Python cria uma documentação automática

def exponencial(numero, potencia=2):
    """
    A função retorna o quadrado de outro, e para qualquer potência informada.
    :param numero:  Base, obrigatório
    :param potencia: Expoente, opcional
    :return: Rertono a potênica de um número
    """
    return numero ** potencia
