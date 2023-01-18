"""
                                MÓDULO COLLECTIONS - COUNTER (CONTADOR)


- Temos que importar
- Não confundir com o count() usado na aula de LISTA
- Collections: Conhecido como high-performance container datetypes
- Todas as coleções são containers

Counter: Recebe um iterável como parâmetro e cria um OBJETO do tipo Collections Counter que é parecido com um
dicionário, contendo como chave o ELEMENTO da lista e, como VALOR, a quantidade de ocorrências desse elemento.

Nota:
Esse tema é importante para trabalhar com alguns framework
"""

# Podemos usar qualquer iterável. Mas para este exemplo vamos usar uma lista

from collections import Counter  # Estamos importando uma biblioteca

lista = [1, 1, 1, 2, 2, 3, 5, 6, 7, 7, 7, 7, 8, 9, 99, 100, 120, 150, 200, 400, 400, 400]

# Utilizando o Counter()

res = Counter(lista)  # Se parece muito com um dicionário, mas não é
print(type(res))
print(lista)
print(res)  # Observe a falta de ordenação
print('-----')

"""
O que ele faz é: ELEMENTO: OCORRÊNCIA
<class 'collections.Counter'>
Counter({7: 4, 1: 3, 400: 3, 2: 2, 3: 1, 5: 1, 6: 1, 8: 1, 9: 1, 99: 1, 100: 1, 120: 1, 150: 1, 200: 1})

Ou seja, criou uma chave e colocou como valor a ocorrência dos elementos no iterável. É importante notar que poderia ser 
uma string também.
"""

# Imprimindo direto

print(Counter('Francisco'))  # Observe a falta de ordenação lá no console. Vai contar a ocrrência de cada letra
print('-----')

print(Counter(['Francisco', 'Araújo', 'da', 'Silva']))  # Vai contar a ocorrência de nome
print('-----')

# Exemplo mais completo

texto = """
Quem aspira se graduar na Engenharia de Petróleo precisa ter espírito arrojado, colaborativo e cooperativo e, sobretudo, 
entender a importância da cooperação e colaboração nas atividades cotidianas tendo em vista a promoção de ambientes 
propositivos alinhados na consecução de objetivos comuns. Ademais, deve estar preparado para ampliar o entendimento da 
realidade através do manuseio do repertório das ciências exatas e das engenharias.
"""

# Vamos separar as palavras numa lista. O separador padrão é o espaço entre as palavras, mas posso mudar no split(' ')

palavras = texto.split()  # Separando por espaço
print(palavras)
resp = Counter(palavras)
print(resp)

# Encontrando as 3 palavras com mais ocorrência no texto acima

print('-----')
print(resp.most_common(5))
# Esse comando é muito interessante. Nesse caso, vai encontrar as 5 palavras/letras com maior n° de ocorrências

"""
Posso ler a explição via terminal:
from collections import Counter
help(Counter)
"""
