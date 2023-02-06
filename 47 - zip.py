"""
                                                    ZIP


- Zip(): cria um iterável (Zip Object) que agrega elementos em pares de cada um dos iteráveis passados como entrada
- O dado fica em memória, e portanto podemos usar apenas uma vez. Na segunda utilização já não existe mais

Nota:
Muito legal, gostei dessa função.
"""

lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]
zip1 = zip(lista1, lista2)  # Poderíamos ter mais iteráveis como argumento do zip
print(zip1)
print(type(zip1))
print('-----')

# Vamos visualizar esses agrupamento?

print(list(zip1))  # Gera uma lista contendo tuplas para cada par
print(tuple(zip1))  # Vazio
print(set(zip1))  # Vazio
print(dict(zip1))  # Vazio
print('-----')

# Poderíamos ter:

zip2 = zip(lista1, 'abc')  # Veja que esse tipo de dado fica apenas em memória, temos que colocar antes de cada print.
print(zip2)  # Veja que é um objeto do tipo zip: <zip object at 0x000001B44B210240>
print(' ')  # Para dar um espaço
print(list(zip2))

zip2 = zip(lista1, 'abc')
print(tuple(zip2))  # Veja que temos tupla dentro de tupla

zip2 = zip(lista1, 'abc')
print(set(zip2))

zip2 = zip(lista1, 'abc')  # Vai gerar apenas chave e valor
print(dict(zip2))

"""
Veja abaixo o que acontece se o tamanho dos iteráveis no argumento do zip forem difentes... note que o 16 e o 17 não 
entram, pois essa função leva em conta o iterável de menor tamanho, que no caso são 'lista1' e 'lista2'.
"""

lista3 = [10, 11, 12, 13, 15, 16, 17]
zip3 = zip(lista1, lista2, lista3)  # Veja o que acontece se mudar a ordem dos elementos
print(list(zip3))
print('-----')

# Podemos usar para diferentes iteráveis

tupla = 1, 2, 3, 4
lista = [1, 2, 3, 4]
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
zt = zip(tupla, lista, dicionario.values())
print(list(zt))
print('-----')

# Veja isso, vamos desempacotar com o asterisco. Lembra dele? Lá do *args e **kwargs

dados = [(1, 2), (3, 4), (5, 6), (7, 8)]
zp = zip(*dados)
print(list(zp))
print('-----')

# Veja esse exemplo mais complexo, no qual precisamos gerar um dicionário com a maior nota de cada estudante

prova1 = [80, 91, 78]
prova2 = [70, 92, 75]
alunos = ['Raissa', 'Luiza', 'Francisco']

# Implementando apenas o zip

print(list(zip(alunos, prova1, prova2)))
print('-----')

# Lembra dessa estrutura de compreensão: dictionary comprehension?

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)
print('-----')

"""
Veja que dado[0] é a chave, ou seja, o nome de cada estudante.
O max vai pegar a maior nota entre a nota 1 e a nota 2, ou seja, será o valor do nosso dicionário.
"""

# Veja outra forma de fazer esse mesmo procedimento. Lembre-se que o Map() recebe uma função e um iterável

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final))

"""
Veja que o zip vai criar pares entre alunos e map.
Veja que map vai gerar as maiores notas. Perceba que map() recebe uma função e um iterável.
"""
