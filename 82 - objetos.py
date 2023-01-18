"""
OBJETOS

- Objeto e instância é a mesma coisa.
- Objetos são instâncias da classe. Após mapear o objeto do mundo real para sua representação computacional, podemos
criar quantos objetos forem necessários. Instâncias são variáveis do tipo definido na classe.

- Para instanciar um objeto é preciso informar os parâmetros (atributos) que ele possui no método construtor
"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False  # toda lâmpada quando for construída terá o atributo ligada como falso

    def checa_lampada(self):  # um método que checa se lâmpda está ligada ou desligada
        return self.__ligada

    def ligar_desligar(self):  # se o método for executado: se a lâmpada tiver ligada, vamos desliga, e vice-versa.
        if self.__ligada:  # se o atributo ligada for True
            self.__ligada = False
        else:
            self.__ligada = True


class Cliente:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f'O cliente {self.__nome} diz oi.')


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O cliente é: {self.__cliente._Cliente__nome}')  # fazendo acesso a self.__cliente e acesso ao atributo
                                                                # privado ._Cliente__nome


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


# instânica do tipo lâmpada
# lamp1 = Lampada()  # Gera erro, temos que inserir os argumentos do método construtor
lamp1 = Lampada('branca', 110, 60)
lamp1.ligar_desligar()  # inicialmente, a lâmpada está desligada. Quando o método for executado, ela será ligada
# lamp1.ligar_desligar() # desligaria a lâmpada
print(f'A lâmpada está ligada? {lamp1.checa_lampada()}')
print('-----')


# instânica do tipo conta corrente
cliente1 = Cliente('Francisco Araújo',  '1111.1111.1111.95')
cc1 = ContaCorrente(500, 10000, cliente1)  # veja que o teceiro atributo é o objeto Cliente
cc1.mostra_cliente()  # veja que temos acesso ao nome do cliente
cc1._ContaCorrente__cliente.diz()  # Forma incorreta. De dentro de ContaCorrente tenho acesso a métodos e atrinutos da
# classe Cliente.
print('-----')


# instância do tipo usuário
user1 = Usuario('Francisco', 'Araújo', 'franciscoaraujo2016f2@outlook.com', '111111')
