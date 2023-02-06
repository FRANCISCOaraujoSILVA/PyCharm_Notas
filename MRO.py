"""
Aula 88
                                        MRO - METHOD RESOLUTION ORDER


- É a ordem de execução, ou seja, os métodos são executados na ordem
- Fenômeno que ocoore quando temos herança mútlipla
- Nesse caso, o super() funciona para a classe que tem apenas uma herança, no caso a classe Aquatico

Podemos conferir a ordem de execução dos métodos de três formas:
    - via propriedade da classe __mro__
    - via método mro()
    - via help
"""


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando.'

    def cumprimentar(self):  # Sobrescrevendo o método cumprimentar()
        return f'Eu sou {self._Animal__nome} do mar!'


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra!'


class Pinguim(Aquatico, Terrestre):
    def __init__(self, nome):
        super().__init__(nome)

    def cumprimentar(self):
        return 'Comprimentar Pinguim'


# Caso 1: class Pinguim(Terrestre, Aquatico)

shef = Pinguim('shef')
print(shef.cumprimentar())
"""
Eu sou shef da terra!
"""

# Caso 2: class Pinguim(Aquatico, Terrestre)

"""
Eu sou shef do mar!
"""

# No terminal, faça:

"""
from MRO import Pinguim

------------via propriedadde------------

Pinguim.__mro__

Ou seja, a ordem de execução seria:

1°: <class 'MRO.Pinguim'>
2°: <class 'MRO.Aquatico'>
3°: <class 'MRO.Terrestre'>
4°: <class 'MRO.Animal'>
5°: <class 'object'>


------------via método------------
Pinguim.mro()

------------via help------------EU GOSTEI MAIS DESSE
help(Piguim)
"""
