"""
                                                    O MÉTODO SUPER()


- O método super() faz referência a uma super classe
- Podemos usar esse método a partir do momento em que temos herança em nossas classes
- Podemos fazer acesso a qualquer elemento da classe pai
"""


class Animal:

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'O {self.__nome} fala {som}')


class Gato(Animal):  # É a classe filha, ou seja, a classe específica

    def __init__(self, nome, especie, raca):
        # Animal.__init__(self, nome, especie)
        super().__init__(nome, especie)
        super().faz_som('som de gato tipo cachorro')
        self.__raca = raca


felix = Gato('Felix', 'felino', 'Angorá')
felix.faz_som('som de gato')
