"""
POLIMORFISMO

- Objetos que podem se comportar de formas diferentes

Poli: muitas
Morfis: formas
"""


class Animal(object):

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):  # método ainda não implementando, pois cada animal fala de uma maneira
        raise NotImplementedError('A classe filha que deve implementar este método')
        # uma exceção, caso alguma classe filha não implemente este método

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


class Rato(Animal):  # veja o erro: um método abstrato não foi implementado

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
    - overrides (estamos alterando o comportamento de determinado objeto)
        - é a melhor representação do polimorfismo
    
"""




