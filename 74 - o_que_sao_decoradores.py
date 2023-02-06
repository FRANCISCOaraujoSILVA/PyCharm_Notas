"""
                                                DECORADORES (DECORATORS)


O que são decoradores?
    - São funções
    - Envolvem outras funções e aprimoram (decoram o que você já tem) seu comportamento
    - São exemplos de Higher Order Function
    - Possui sintaxe própria, usando "@" (Syntact Sugar / Açucar Sintático)
    - Geralmente, uma função decorator recebe como parâmetro uma função, pois estamos decorando a função que está sendo
    passada como parâmetro

...........................................
|           Function Decorator            |
-------------------------------------------

...........................................
|                Function                 |
-------------------------------------------

Nota:
Não confunda Decorator com Decorator Function
    - Decorator
                        @seja_educado_mesmo
    - Decorator function:
                        def seja_educado_mesmo(funcao):
                            def sendo_mesmo():
                            print('Foi um prazer conhecer você!')
                            funcao()
                            print('Tenha um excelente dia.')
                        return sendo_mesmo

"""

# Decoradores como funções - Sintaxe não recomendada / Sem açucar Sintático


def seja_educado(funcao):  # Função principal que tem como argumento outra função
    def sendo():  # Função interna
        print('Foi um prazer conhecer você!')
        funcao()  # Executa a função
        print('Tenha um ótimo dia.')
    return sendo  # Retorna a função interna, e não a execução da função


def saudacao():
    print('Seja bem-vido(a) à programação!')


# Testando 1

saudacao()
print('-----')

teste = seja_educado(saudacao)
teste()
# Estamos decorando a função saudacao com a função seja_educado. Estamos aprimorando o comportamento da função saudacao
print('-----')

# Testando 2


def raiva():
    print('EU TE ODEIO!')


raiva_educada = seja_educado(raiva)
raiva_educada()
print('-----')


# Decoradores como funções - Sintaxe recomendada /  açucar Sintático. É muito melhor de enxergar


def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia.')
    return sendo_mesmo


@seja_educado_mesmo  # Forma recomendada e mais utilizada. Vemos que '@seja_educado_mesmo' decora 'apresentando'
def apresentando():
    print('Meu nome é Francisco.')


# Testando 3

apresentando()
print('-----')

# Testando 4


@seja_educado_mesmo
def dormir():
    print('Quero dormir.')


dormir()
