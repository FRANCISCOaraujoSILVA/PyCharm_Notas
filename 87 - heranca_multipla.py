"""
HERANÇA MÚLTIPLA

    Enquando que no java conseguimos herdar diretamente apenas de uma classe, aqui no Python conseguimos herdar de múltiplas
classes.

Nota:
    A herança múltipla pode ser feita de duas maneiras:
        - Multiderivação Direta
        - Multiderivação Indireta

Class Cliente(Pessoa) -> A classe Cliente DERIVA (classe que herda de outra classe) de Pessoa. Ou seja, multiderivação é
a herança múltipla.


Obs.:
- Não importa se a derivação é direta ou indireta. A classe que realizar a herança herdará todos os atributos e
métodos das super classes.


class Pessoa:
    pass

é equivalente a

class Pessoa(object):
    pass




"""

# Exemplo 1 - Multiderivação Direta


class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class MultiDerivada(Base1, Base2, Base3):  # herda 3 classes
    pass


# Exemplo 2 - Multiderivação Indireta


class Base4:
    pass


class Base5(Base4):
    pass


class Base6(Base5):  # herda diretamente a Base5 e indiretamente a Base4
    pass


class MultiDerivadaBases(Base6):  # herda diretamente a Base6 e indiretamente a Base5 e Base4
    pass


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

    def cumprimentar(self):  # sobrescrevendo o método cumprimentar()
        return f'Eu sou {self._Animal__nome} do mar!'


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra!'


class Pinguim(Terrestre, Aquatico):  # herança múltipla. Herdando diretamente Terrestre e Aquatico e indiretamente de
    # Animal. Pinguim anda, nada e cumprimenta. A pergunta que fica é: Quando o pinguim tiver que cumprimentar, qual dos
    # três métodos ele irá executar?

    def __init__(self, nome):
        super().__init__(nome)


# Testando

baleia = Aquatico('Sara')
print(baleia.nadar())
print(baleia.cumprimentar())
print('-----')


tatu = Terrestre('Gaspar')
print(tatu.andar())
print(tatu.cumprimentar())
print('-----')

son = Pinguim('Son')
print(son.andar())
print(son.nadar())
print(son.cumprimentar())  # qual dos metodos cumprimentar() será executado? A escolha é feita por:
# Method Resolution Order - MRO.
print('------')

"""
Vai executar o método cumprimentar() da classe Terrestre, pois é o primeiro da ordem de herança: Eu sou Son da terra!. 
Se o primeiro da ordem de herança fosse Aquatico, o método cumprimentar() seria: Eu sou Son do mar!

"""


# Descobrindo de qual instância é determinado objeto:

print(f'son é instância de Pinguim? {isinstance(son, Pinguim)}')  # retorna um booleano
