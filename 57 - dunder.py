"""
                                            DUNDER NAME E DUNDER MAIN


- Dunder: Doble Under
- Dunder Name: __name__
- Duncer Main: __main__
- Os Dunders são criados para não gerar conflitos com variáveis, atributos ou funções criadas por nós aqui no Python.
Pois, veja que se executarmos um módulo em Python diretamente na linha de comando, internamente o Python atribuirá à
variável __name__ com o valor __main__ indicando que este módulo é o módulo de execução principal.

Faça no terminal:
dir(): Perceba que lá tem vários dunders. Além disso, vejá que lá tem __name__
faça: print(__name__), Veja que será retornado __main__
"""

"""
Crie um script chamado 'funcoes_com_parametro' com os seguinte comandos (pode copiar e colar):

# Essa é apenas uma parte do script da aula 27. Foi criado para analisar o método dunder da aula 57


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total  # Veja que se dermos mais um tab, o if itera apenas uma vez, já que o return finaliza o passo


lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))

tupla = (1, 2, 3, 4, 5, 6, 7)
print(soma_impares(tupla))
"""

from funcoes_com_parametro import soma_impares

print(soma_impares([1, 2, 3, 5]))  # Os dois prints estão sendo executados apenas pelo import
# Note que mesmo o print sendo comentado ainda assim executamos os dois prints apenas pelo import (isso naõ deveria
# acontecer em um programa real do python. É agora que o método dunder entre.

"""
Para corrigir, faça:
if __name__ == '__main__':  # Se o nome do arquivo for main (principal), execute diretamente, e não pelo import
    lista = [1, 2, 3, 4, 5, 6, 7]
    print(soma_impares(lista))

    tupla = (1, 2, 3, 4, 5, 6, 7)
    print(soma_impares(tupla))
"""

# Todo arquivo python contém a variável __name__, se a função for executada na linha de comando, a variável __name__
# vai ter o valor __main__ e então executamos os prints.

# Assim, agora temos um módulo (funcoes_com_parametro) real do Python. Veja que agora temos apenas o print que nos
# interessa.

# Veja que os dunders são muito usados no módulos python. Vá ao final da documentação do módulo random da aula 52

"""
if __name__ == '__main__': se o módulo está sendo executado diretamente (é uma verificação)
    _test()
    
Ou seja, essa verifica diz se o módulo foi feito para se executado diretamente ou não.

- Veja que lá não tem nenhum print.
- Os dois prints do módulo são executados apenas quando executados no próprio módulo

Resumo:
se o arquivo foi executado diretamente vai se chamar: __main__ 
se o arquivo for importado vai se chamar __name__: proprioNomeDoArquivo
"""
