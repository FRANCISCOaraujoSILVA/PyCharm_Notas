"""
DECORATORS COM DIFERENTES ASSINATURAS  (funções docoradoras com diferentes parâmetros de entrada)

Quando a funcão a ser decorada tiver mais de um argumento, como no caso da função ordenar:
    - usamos Decorator Pattern


- A assinatura de uma função é representada pelo seu retorno, nome e parâmetros de entrada.
"""

# Relembrando


def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()  # Aplicando caixa alta no resultado da função
    return aumentar


@gritar
def saudacao(nome):  # saudacao está decorado com a função gritar()
    return f'Olá, eu sou o {nome}'


@gritar
def ordenar(principal, acompanhamento):  # ordenar está decorado com a função gritar
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por  favor.'


# Testando
print(saudacao('Francisco'))
print('-----')

"""
print(ordenar('Picanha', 'Batata Frita')):
    vai gerar erro, temos que usar Decorator Pattern
"""

# Refatorando


def gritar_refatorado(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar_refatorado
def saudacao_refatorado(nome):
    return f'Olá, eu sou o {nome}'


@gritar_refatorado
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}. Por favor.'


print(saudacao('Francisco'))
print(ordenar('Picanha', 'Batata Frita'))
print('-----')

# também posso ter função sem argumento


@gritar_refatorado
def lol():
    return 'lol'


print(lol())
print('------')


# Obs.: Vale lembrar que podemos utilizar parâmetros nomeados

print(ordenar(acompanhamento='Salada', principal='Arroz'))  # quando nomeamos, não precisamos inserir na ordem.
print('-----')

# Decorator com argumentos


def verifica_primeiro_argumento(valor):  # Função decoradora
    def interna(funcao):  # recebe a função que está sendo decorada
        def outra(*args, **kwargs):  # realiza validações
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('pizza')  # pelas validações, obrigando o primeiro argumento a ser pizza
def comida_favorita(*args):
    return args


@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


# Testando
print(soma_dez(10, 20))  # vai somar
print(soma_dez(15, 15))  # não vai somar
print('-----')

print(comida_favorita('pizza', 'churrasco'))  # executa
print(comida_favorita('churrasco', 'pizaa'))  # não executa
