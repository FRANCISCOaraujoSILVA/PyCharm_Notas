"""
                                                    POLIMORFISMO


- Objetos que podem se comportar de formas diferentes

Poli: Muitas
Morfis: Formas
"""


class Animal(object):

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):  # Método ainda não implementando, pois cada animal fala de uma maneira
        raise NotImplementedError('A classe filha que deve implementar este método')
        # Uma exceção, caso alguma classe filha não implemente este método

    def comer(self):
        print(f'{self.__nome} está comendo...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala wau wau!')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala miau!')


class Rato(Animal):  # Veja o erro: Um método abstrato não foi implementado

    def __init__(self, nome):
        super().__init__(nome)


# Testando

felix = Gato('felix')
felix.comer()
felix.falar()
print('-----')

pluto = Cachorro('pluto')
pluto.comer()
pluto.falar()
print('-----')

mickey = Rato('mickey')
mickey.comer()  # OK
mickey.falar()  # Erro: NotImplementedError
print('-----')

"""
O que acontece quando sobrescrevemos um método contido na classe pai:
    - Overrides (estamos alterando o comportamento de determinado objeto)
        - É a melhor representação do polimorfismo    
"""
