"""
PROPRIEDADES (PROPERTIES)

- sempre criamos nossos atributos de forma privada. Como consequência, as propriedades getters() e setters() de acordo
como tal.
"""


class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor


conta1 = Conta('Francisco', 3000, 5000)
conta2 = Conta('Lara', 5000, 8000)

print(conta1.extrato())
print(conta2.extrato())
print('------')


# Como somar o saldo das duas contas?
"""
Não faça isso, não acesse um elemento privado se ele foi criado para ser privado:

soma = conta1._Conta__saldo + conta2._Conta__saldo
print(soma)
"""

"""
Crie métodos gettters() e setters() quando se deseja minupular os atributos privados de uma classe. Esses métodos 
públicos são criados quando temos atributos privados em nossas classes. Onde, getters retornam valor do atributo 
enquanto que os setters alteram o valor do mesmo.

Por definição, o nome do método deve ser:
    - get_atributo  (geralmente fazemos este, menos perigoso)
    - set_atributo  (geralmente não fazemos este, mais perigoso - pois pode alterar o valor de um atributo)
"""


class NovaConta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = NovaConta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        NovaConta.contador += 1

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):  # recebe o valor do atributo e faz alteração do mesmo
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite


conta3 = NovaConta('Francisco', 3000, 5000)
conta4 = NovaConta('Lara', 5000, 8000)
print(conta3.extrato())
print(conta4.extrato())
print(conta3.get_saldo() + conta4.get_saldo())
print('------')
print(conta3.__dict__)
print(conta3.set_limite(10_000))
print(conta3.__dict__)  # Veja que o valor do limite será alterado de 5000 para 10000
print('-----')

"""
Até aqui aplicamos muito bem os conceitos e vimos que os métodos getters() e setters() funcionam muito bem. Todavia,
essa nomenclatura não é muito amigável, por vezez, até se parece com a nomenclatura aplicada na linguagem java. Há outra
tipo de nomenclatura, usando propreidades (property):

- O @property faz o papel do método getter()
- E se você quiser criar um setter()?:
    @nomeDaPropriedade.setter no lugar de @property
"""


class OutraConta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = OutraConta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        OutraConta.contador += 1

    @property  # Um decorador. Palavra chave para criar as propriedades. Geralmente logo abaixo de método construtor
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):  # método de instância
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    @property
    def valor_total(self):
        return self.__saldo + self.__limite


conta5 = OutraConta('Francisco', 3000, 5000)
conta6 = OutraConta('LarA', 5000, 8000)
print(conta5.extrato())
print(conta6.extrato())
print(conta5.saldo + conta6.saldo)

print('------')
print(conta5.__dict__)
conta5.limite = 767676  # não é mais um método, é uma propriedade chamada limite. Funciona como o método setter()
print(conta5.__dict__)
print(conta5.limite)
print('-----')


# Além disso, é possível criar métodos como propriedades
"""
@property
def valor_total(self):
    return self.__saldo + self.__limite  
"""

print(conta5.valor_total)  # veja que não é uma função, pois: conta5.valor_total é diferente de conta5.valor_total(),
# com os parênteses
print(conta6.valor_total)
