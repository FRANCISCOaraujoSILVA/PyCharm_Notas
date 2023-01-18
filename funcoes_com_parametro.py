"""
Esse é apenas uma parte do script da aula 27. Foi criado para analisar o método dunder da aula 57.
"""
def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total  # veja que se dermos mais um tab, o if itera apenas uma vez, já que o return finaliza o passo


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7]
    print(soma_impares(lista))

    tupla = (1, 2, 3, 4, 5, 6, 7)
    print(soma_impares(tupla))
