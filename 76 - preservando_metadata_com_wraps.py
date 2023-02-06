"""
                                    PRESERVANDO METADATA COM WRAPS


- Metadados: São dados intrínsecos em arquivos
- Wraps: Funções que envolvem elementos com diferentes finalidades
"""

# Problema


def ver_log(funcao):  # Função decoradora
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'Você está chamando {funcao.__name__}')  # __name__: Retorna o nome da função
        print(f'Aqui a documentação: {funcao.__doc__}')  # __doc__: Retorna a documentação da função
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois números"""
    return a + b


# print(soma(10, 30))

# Veja o problema. Em um projeto real, isso gera muita dor de cabeça por alguns dias até encontrar a fonte de erro

print(soma.__name__)  # O nome deveria ser 'soma'
print(soma.__doc__)  # A documentação deveria ser 'Soma dois números'
print('-----')

"""
Pense no seguinte caso: Você resolve publicar uma biblioteca com essa fonte de erro, o que aconteceria se outra pessoa
resolvesse consultar a documentação do seu código? Ou seja, não basta que o código execute corretamente. É preciso 
que a documentação também esteja de acordo.
"""


# Para resolver este problema precisamos importar um decorator da própria linguagem Python

# Resolução do problema

from functools import wraps


def ver_log(funcao):  # Função decoradora
    @wraps(funcao)  # Resolvendo o problema com apenas essa linha de código. Wraps preserva os metadatas das funções -
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'Você está chamando {funcao.__name__}')  # __name__: Retorna o nome da função
        print(f'Aqui a documentação: {funcao.__doc__}')  # __doc__: Retorna a documentação da função
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois números"""
    return a + b


print(soma.__name__)  # O nome deveria ser 'soma'
print(soma.__doc__)  # A documentação deveria ser 'Soma dois números'
