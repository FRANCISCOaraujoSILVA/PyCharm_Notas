"""
ABSTRAÇÃO E ENCAPSULAMENTO

- Não é pré-requisito para resolver qualquer problema
- O diferencial está na forma de como resolvemos os mais diversos problemas
- Deve-se pensar sobre qual estilo de programação usar para resolver determinado problema
- O grande objetivo da POO é encapsular o código dentro de um grupo lógico e hierárquico de classes

Encapsular / cápsula:

             Classe
------------------------------------
|       Atributos e métodos        |
-----------------------------------

- É o agrupamento de atributos e métodos (públicos e privados), fazendo com a abstração seja possível

Relembre, atributos e métodos privados

Imagine que temos uma classe chamdda Pessoa, contendo um atributo privado chamado __nome e um método privado chamado
__falar().

Esses elementos privados só devem/deveriam ser acessados dentro da classe. Mas o Python não bloqueia esse acesso fora
da classe. Pois o Python possui um fenômeno chamdo Name Mangling, que faz uma alteração na forma de acessar os elementos
privados, veja:

_Classe__elemento

Exemplo: acessando elementos privados fora da classe (não recomendado, haja visto que sempre há um motivo para definir
um atributo com sendo privado).

instancia._Pessoa__nome
instancia._Pessoa__falar()


---------------

ABSTRAÇÃO EM POO: ato de expor apenas dados relevantes de uma classe, no qual escondemos atributos e métodos privados
que o usuário não precisa ter conhecimento a priori. Lembrar do exemplo da máquina de café;
 - não precisamos como a máquina funciona internamente. Queremos apenas o dado relevante, o café pronto e botões
 para escolher qual o tipo de café queremos. Ou seja, dados irrelevantes são removidas, abstraídas.
"""

# exemplo:


class Conta:

    contador = 400  # atributo de classe

    def __init__(self, titular, saldo, limite):  # atributos de classe
        self.numero = Conta.contador
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        Conta.contador += 1

    def extrato(self):  # métodos de instância
        print(f'Saldo de {self.saldo} do titular {self.titular} com limite de {self.limite}')

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor


# testando

conta1 = Conta('Francisco', 150.00, 1500)
print(conta1)  # imprimie o endereço de memória


# Problema: Atributos públicos (fazemos acesso direto). Com o acesso direto podemos alterar os dados
print(conta1.numero)
print(conta1.titular)
print(conta1.saldo)
print(conta1.limite)
print('-----')

# Imagine
conta1.numero = 42
conta1.titular = 'Outra pessoa'
conta1.saldo = 999999
conta1.limite = 8888888888

print(conta1.__dict__)  # os dados mudaram, isso não é legal, não tem segurança.
print('-----')
conta1.extrato()


# Para resolver este problema, devemos encapsular (manter seguro) os dados. Veja:

class ContaRefatorada:

    contador = 400  # atributo de classe

    def __init__(self, titular, saldo, limite):  # atributos de classe
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):  # métodos de instância
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor


conta2 = ContaRefatorada('Francisco', 150.00, 1500)

"""
As linhas de código abaixo não funcionam mais.

print(conta2.numero)
print(conta2.titular)
print(conta2.saldo)
print(conta2.limite)
print('-----')

conta2.numero = 42
conta2.titular = 'Outra pessoa'
conta2.saldo = 999999
conta2.limite = 8888888888
"""
print('-----')

print(conta2.__dict__)
print('-----')
conta2.extrato()
print('-----')

# Os atributos estão seguros (privados). Mas o Python ainda permite o acesso a estes dados
print(conta2._ContaRefatorada__titular)  # Name Mangling (não recomendado)

conta2._ContaRefatorada__titular = 'Outra pessoa'
print(conta2.__dict__)
conta2.depositar(150)
print(conta2.__dict__)


# Nota: Nesse caso, nossos métodos não precisam ser privados. Pois precisamos fazer acesso a eles fora da classe
