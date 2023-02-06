"""
                                                    MÉTODOS


- Métodos (funções): Representam o comportamento do objeto. Ou seja, as ações que este objeto pode realizar no seu
sistema

Em Python, dividimos os métodos, assim como os atributos, em 2 grupos:
    - Método de instânica
    - Método de classe

Nota:
Vamos criar atributos privados para ter segurança. Ou seja, acessar os atributos apenas dentro daquela classe.
"""

# Método de instância

"""
- O método dunder __init__ é um método especial chamado de construtor e sua função é construir o objeto a partir da 
classe
- Todo elemento em Python que inicia e finaliza com duplo underline é chamado de dunder (Double UNDERline)
- Os métodos/funções dunder em Python são chamados de métodos mágicos
- Não é recomendado que nós, programadores, criemos métodos dunders. Já que podemos dar o azar de criar um dunder que já
existe internamente (vários dunders)
- Quando uma função está contida dentro de uma classe ela é chamada de método, ou método de instância
    - Métodos de instância: pois precisamos de uma instância da classe para utilizá-los
- Métodos são escritos em letras minúsculas. Se o nome for composto, esse nome terá as palavras separadas por underline
"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):  # __init__ é o método construtor, o objetivo é construir o objeto
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.id

    def desconto(self, porcentagem):
        """
        :param porcentagem: Porcentagem de desconto
        :return: Retorna o valor do produto com o desconto
        """
        return (self.__valor * (100 - porcentagem))/100


class Usuario:
    def __init__(self, nome, sobrenome, email, senha):  # __init__  Método interno do Python
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.senha = senha

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


"""
p1 = Produto('Playstation 4', 'Video Game', 2300)
print(p1.desconto(20))  # Veja que precisamos de uma instância para acessar o método

# print(Produto.desconto(20))  -> Gera erro, assim não conseguimos. Precisamos da instância
print(Produto.desconto(p1, 40))  # Outra maneira de fazer. Mas ainda precisamos da instância
"""

user1 = Usuario('Francisco', 'Araújo', 'Franciscoaraujo2016f2@outlook.com', '123')
user2 = Usuario('Lara', 'Siqueira', 'LaraSiqueira2016f2@outlook.com', '456')

print(f'Nome completo: {user1.nome_completo()}')
print(Usuario.nome_completo(user1))
print('-----')

print(f'Nome completo: {user1.nome_completo()}')
print(Usuario.nome_completo(user2))

"""
Método de instânicia: é um método que está dentro de uma classe.
"""

# print(f'Senha user 1: {user1._Usuario__senha}')  # Acesso de forma errada de um atributo de classe
# print(f'Senha user 1: {user1._Usuario__senha}')  # Acesso de forma errada de um atributo de classe
print('-----')

from passlib.hash import pbkdf2_sha256 as cryp  # Esse é um pacote de criptografia extramente poderoso


class Usuario:
    def __init__(self, nome, sobrenome, email, senha):  # __init__  Método interno do Python
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.__hash__(senha, rounds=200000, salt_sizer=16)
        # 'senha' é a string que quer encriptar. 'Rounds', número de embaralhamento. 'salt_sizer' é o tamanho do texto
        # que deve se juntar com outro para gerar o embaralhamento

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):  # Recebe a senha, e verifica se a senha recebida é = a senha do objeto instanciado
        if cryp.verify(senha, self.__senha):  # Verifica se senha = self.senha
            return True
        return False


"""
Deu um erro aqui:

# Para criar um usuário
nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o e-mail: ')
senha = input('Informe a senha: ')
confirma_senha = input('Confirme a senhaa: ')

if senha == confirma_senha:  # se a senha for igual, vamos instanciar
    user = Usuario(nome, sobrenome, email, senha)  # usa as variáveis anteriores
else:
    print('Senha não confere...')
    exit(1)

print('Usuário criado com sucesso!')

senha = input('Informe a senha para acesso: ')

if user.checa_senha(senha):
    print('Acesso permitido.')
else:
    print('Acesso negado.')

print(f'Senha User Criptografada: {user.Usuario_senha}')

Métodos de instancia, então, trabalham com valores da instancia do objeto
"""

"""
Métodos de classe.
- Não estão vinculados a nenhuma instancia da classe, mas sim, diretamento a ela.
- Usamos decoradores.
"""


class Usuarios:

    contador = 0

    @classmethod  # Decorador. Necessário para usar um método de classe
    def conta_usuarios(cls):  # Argumento cls, é a própria classe
        print(f'Temos {cls.contador} usuário(s) no sistema.')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuarios.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha
        Usuarios.contador = self.__id

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def ver(self):  # Veja que, como esse método não faz acesso a nenhum atributo de instância, ele recomenda usar
        print('ver')      # método de classe


# Antes, para acessar o contador:
# Usuarios.contador

# Agora

user = Usuarios('Francisco', 'Araújo', 'gmail', '123')
user4 = Usuarios.conta_usuarios()  # Forma correta, nome_da_classe.metodo_de_classe. Via nome da classe
user.conta_usuarios()  # Possível, mas incorreto. Via instância da classe

"""
Quando usar método de classe e método de instancia? Basta olhar na estrutura acima.
- Métodos de instâncias: Quando o método precisa fazer acesso a atributos de instância
- Método de classe: Não fazemos acesso à métodos de instância, e nem teria como fazer. Pois não temos acesso ao self. Ou
seja, a instância
- Métodos de classe, aqui no Python, são conhecidos como métodos estáticos em outras linguagens

def ver(self):  # Veja que, como esse método não faz acesso a nenhum atributo de instância, ele recomenda usar
    print('ver')      # método de classe
"""

# Métodos privados (duplo __ no começo do método): Refatorando a classe usuarios:

# Assim como temos atributos públicos e privados, também temos métodos públicos e privados


class Usuarios:

    contador = 0

    @classmethod  # Decorador. Necessário para usar um método de classe
    def conta_usuarios(cls):  # Argumento cls, é a própria classe
        print(f'Temos {cls.contador} usuário(s) no sistema.')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuarios.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha
        Usuarios.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def __gera_usuario(self):
        return self.__email.split('@')[0]  # Separa o email no '@', gera uma lista, retorna o 1° elemento da lista
    # split e slice de string.


"""
user5 = Usuarios('Francisco', 'Araújo', 'Francisco@gmail.com','123')  # Só tenho acesso à classe __gera_usuario dentro
# da classe

# print(user5.__gera_usuario())  # Veja que ele não imprime. Pois não temos acessso a esse método fora da classe.
print(user5._Usuarios__gera_usuario())  # Tenho acesso, mas não é recomendado
"""

# Métodos estáticos aqui no Python: Muito parecidos com métodos de classe

# Sem acesso a classe e sem acesso a instâncias


class Usuarios:

    contador = 0

    @classmethod  # Decorador. Necessário para usar um método de classe
    def conta_usuarios(cls):  # Argumento cls, é a própria classe
        print(f'Temos {cls.contador} usuário(s) no sistema.')

    @staticmethod
    def definicao():  # Sem acesso a classe e a instâncias
        return 'UXR344'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuarios.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha
        Usuarios.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def __gera_usuario(self):
        return self.__email.split('@')[0]


print('-----')
print(Usuarios.contador)  # 0 porque ainda não instanciamos nenhum usuario
print(Usuarios.definicao())
user6 = Usuarios('Francisco', 'Araújo', 'Francisco@gmail.com', '123')
print(user6.contador)
print(user6.definicao())
