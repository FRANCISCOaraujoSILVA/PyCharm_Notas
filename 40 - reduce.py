"""
                                                    REDUCE


- A função reduce() recebe dois parâmetros: a função e o iterável
- É viável para um teste de programação, pois demonstra conhecimento avançado
- É um pouco mais confuso
- Reduce: a partir do Python 3.0 a função reduce() não é mais uma função integrada (built-in). Agora temos que
importar e utilizar a partir do módulo 'functools'
- Guido van Rossum: Utilize a função reduce() se você realmente precisa dela. Em todo caso, 99% das vezes um loop for
é mais legível

Imagine a situação:
dados = [a1, a2, a3, a4, ..., an]

A função a ser usada precisa de dois parâmetros:
def func(x, y)
    return x*y

reduce(func, dados)

Funcionamento do reduce:
Passo 1: res1 = f(a1, a2) --> Aplica a função no dois primeiros elementos da coleção e guarda o resultado
Passo 2: res2 = f(res1, a3) --> Aplica a função passando o resultado do passo 1 + o terceiro elemento e guarda o
resultado. E assim por diante até obter o resultado final.


Forma alternativa para o reduce:
funcao(funcao(funcao(a1, a2), a3), a4), ...), an)
"""

from functools import reduce

# Na prática. Aplicando reduce para multiplicar todos os valores de uma lista

dados = [2, 3, 4, 7, 11, 13, 19, 23, 29]

# Vamos usar a função lambda recebendo dois parâmetros

res = reduce(lambda x, y: x * y, dados)
print(f'O resultado com o reduce:\n {res}')

# Fazendo a mesma operação com laço for
res = 1
for n in dados:
    res = res * n

print(f'O resultado com o for:\n {res}')
