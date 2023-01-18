"""
HERANÇA (INHERITANCE)

- Tema muito legal
- É a possibilidade de reaproveitar o código (ato de herdar atributos e métodos para uma nova classe)
- Extender as classes

Pense nas seguintes entidades:

    Cliente
        - nome;
        - sobrenome;
        - cpf;
        - renda;

    Funcionario
        - nome
        - sobrenome
        - cpf
        - matrícula;



Nota:
- Perceba que quando uma herança é criada, a IDE do PyCharm indica com os sinalizadores que está rolando uma herança
em algum lugar do código - os sinalizadores (azuis) do lado lado direito da número das linhas.

- Quando uma classe herda de outra classe, todos os atributos e métodos dessa classe sõa herdados.
- Quando uma classe herda de outra classe, a classe herdada (no nosso caso a classe PESSOA) é conhecida como:
    - super classe ----------------------------------------------------- foque nessa nomenclatura
    - classe mãe
    - classe pai
    - classe base
    - classe genérica

- Quando uma classe herda de outra classe (no nosso caso, a classe NovoCliente e NovoFuncionário), é conhecida por:
    - sub classe
    - classe filha
    - classe específica




Com o método super() podemos fazer acesso a qualquer atrbuto é método de uma Super Classe. Em nosso caso, estamos
fazendo acesso ao método construtor da super classe.
"""


class Cliente:
    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


cliente1 = Cliente('Francisco', 'Araújo', '1111.1111.1111.11', 5000)
funcionario1 = Funcionario('Francisco', 'Araújo', '1111.1111.1111.11', 1212121212)
print(cliente1.__dict__)
print(funcionario1.__dict__)

"""
Veja a quantidade de atributos repetidos nas duas classes.
A pergunta que deve ser feita:Existe alguma entidade genérica o suficiente para encapsular os atributos e métodos comuns a outras entidades?
"""


# Vamos refatorar as classes anteriores criando uma nova classe.


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):  # atributos privados
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):  # método público
        return f'{self.__nome} {self.__sobrenome}'


# Criando a herança
class NovoCliente(Pessoa):  # NovoCliente herda de Pessoa
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)  # é precisso criar este método super().__init__
        # Pessoa.__init__(self, nome, sobrenome, cpf)  # Tabém poderia ser assim, mas não é a forma comum de acessar os
        # dados da super classe
        self.__renda = renda


class NovoFuncionario(Pessoa):  # NovoFuncionario herda de Pessoa
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())  # super() acessa a super classe; nome_completo() acessa esse método contido lá.
        return f'Funcionário: {self.__matricula} Nome: {self._Pessoa__nome}'  # overriding


# Veja a quantidade de códigos que foi economizado
# Testando

print('------')
cliente2 = NovoCliente('Francisco', 'Araújo', '123.123.123-22', 10000)
funcionario2 = NovoFuncionario('Clarice', 'Savi', '111.111.111-11', '1213213212')

print(cliente2.nome_completo())  # veja que o método nome_completo() é da super classe
print(funcionario2.nome_completo())
print('-----')

print(cliente2.__dict__)  # conseguimos observar a qual classe cada atributo pertence
print(funcionario2.__dict__)

"""
Tratando de outro tema: Sobrescrita de Métodos (Overriding): veja o método reimplementado (nome_completo()) na classe 
NovoFuncionario. Observe também a bolinha com um vetor vermelho nesse método e passe o mouse sobre ele. Passe o mouse 
também sobre a bolinha do método nome_completo() na classe Pessoa.

    - ocorre quando reescrevemos/reimplementamos um método presente na super classe em classes filhas. Veja o exemplo
    abaixo:
"""
