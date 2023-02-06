"""
                                FORÇANDO TIPOS DE DADOS COM UM DECORADOR


- Sabemos que em Python, não definimos tipos de dados. O Python determina o tipo de acordo com o conteúdo da variável
- No entanto, em algums casos é preciso forçar o tipo de dado para evitar alguns problemas
"""

# Exemplo


def forca_tipo(*tipos):  # Veja que '*tipos' equivale ao '*args'
    def decorador(funcao):
        def converte(*args, **kwargs):  # O *args é imutável, por isso temos que criar uma nova variável
            novo_args = []
            for (valor, tipo) in zip(args, tipos):  # Zip: Une em pares os valores de um iterável
                novo_args.append(tipo(valor))  # str('Francisco'), int('3')
            return funcao(*novo_args, **kwargs)
        return converte
    return decorador


@forca_tipo(str, int)  # Estamos forçando 'msg' a ser uma string e 'vezes' a ser um inteiro
def repete_msg(msg, vezes):
    for vez in range(vezes):
        print(msg)


repete_msg('Francisco', '4')
print('-----')


@forca_tipo(float, float)
def dividir(a, b):
    print(a / b)


dividir('2', 4)
