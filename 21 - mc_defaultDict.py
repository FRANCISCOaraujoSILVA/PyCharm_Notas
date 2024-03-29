"""
                                    MÓDULO COLLECTIONS - DEFAULT DICT


Observe a diferença:
    recapitulando dicionários;
        dicionário = {'Curso': 'Engenharia de Petróleo'}
        print(dicionário)
        print(dicionário['Curso'])
        print(dicionário['Nome'])  # gera um keyError, já que essa chave não existe

    Default Dict;
        - Informamos um valor default, para não gerar erro se a chave não existe
        - Podemos usar o lambda para isso. Ou seja, sempre que não exisir um valor definido
        - Ao tentar utilizar uma chave que não existe, essa chave será criada e o valor default será atribuído

Nota:
Lambdas são funções sem nome, que podem ou não receber parâmetros de entrada e retornar valores. Não se preocupe pois
vamos estudar as funções lambdas mais adiante.
"""

# Importando

from collections import defaultdict
print(' ')
dicionario = defaultdict(lambda: 0)  # Uma função lambda que não recebe argumento mas retorna zero. Va
print(dicionario)  # Imprime no estilo objeto
print(dict(dicionario))  # Imprime o objeto convertido em dicionário
print('-----')

dicionario['Curso'] = 'Petróleo'  # Criando a primeira chave e valor
print(dicionario)  # Imprime no estilo defaultdict
print('-----')

print(dicionario['outro'])  # Mesmo não existindo, não gera KeyError, mas atribui o valor do lambda
print('-----')

print(dicionario)  # Agora vai atribuir a chave 'outro' com o valor '0' no dicionário.
