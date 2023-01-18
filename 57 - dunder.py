"""
DUNDER NAME E DUNDER MAIN

Dunder: Doble Under
Dunder Name: __name__
Duncer Main: __main__

- Os Dunders são criados para não gerar conflitos com variáveis, atributos ou funções criados criadas por nós aqui no
Python. Pois, veja que se executarmos um módulo em Python diretamente na linha de comando, internamente o Python
atribuirá à variável __name__ o valor __main__ indicando que este módulo é o módulo de execução principal.

Faça no terminal:
dir(): perceba que lá tem vários dunders. Além disso, vejá que lá tem __name__
faça: print(__name__), veja que será retornado __main__
"""
from funcoes_com_parametro import soma_impares

print(soma_impares([1, 2, 3, 5]))  # os dois prints estão sendo executados apenas pelo import da linha 13 e 16.
# perceba que mesmo o print sendo comentado ainda assim executamos os dois prints apenas pelo import (isso naõ deveria
# acontecer em um programa real do python. É agora que o método dunder entre.
"""
Para corrigir, faça:
if __name__ == '__main__':  se o nome do arquivo for main (principal), execute o arquivo diretamente, e não pelo import.
    lista = [1, 2, 3, 4, 5, 6, 7]
    print(soma_impares(lista))

    tupla = (1, 2, 3, 4, 5, 6, 7)
    print(soma_impares(tupla))
    
Todo arquivo python python contém a variável __name__, se a função for executada na linha de comando, a variável 
__name__ vai ter o valor __main__ e então executamos os prints. 

Assim, agora temos um módulo (funcoes_com_parametro) real do Python.
Veja que agora temos apenas o print que nos interessa


Agora, veja que os dunders são muito usados no módulos python. Vá ao final da documentação do módulo random da aula
52:

if __name__ == '__main__': se o módulo está sendo executado diretamente (é uma verificação)
    _test()
    
Ou seja, essa verifica diz se o módulo foi feito para se executado diretamente ou não.

- Veja que lá não tem nenhum print.
- Os dois prints do módulo são executados apenas quando executados no próprio módulo.

Resumo:
se o arquivo foi executado diretamente vai se chamar: __main__ 
se o arquivo for importado vai se chamar __name__: proprioNomeDoArquivo
"""



