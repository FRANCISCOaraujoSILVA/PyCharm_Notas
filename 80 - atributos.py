"""
POO - Atributos
Recomendação: ver esta aula mais de uma vez

Atributos - Representam as características do objeto. Ou seja, pelos atributos conseguimos representar
computacionalmente os estados de um objeto.

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de instância;
    - Atributos de classe;
    - Atributos dinâmicos


# Atributos de instância: São atributos declarados dentro do método construtor.

Obs.: Método construtor (__init__): método especial utilizado para a construção do objeto

Em java: Veja como é muito mais complicado

public class Lampada(){
    private int voltagem;
    public String cor;
    pretected Boolean ligada = false;

    public Lampada(int voltagem, String cor){
        this.Voltagem = voltagem;
        this.cor = cor;
    }

}


Agora, vamos fazer o equivalente, veja que é muito mais simples em python.
"""

# CLASSES COM ATRIBUTOS PÚBLICOS ---------------------------------------------------------------------------------------


class Lampada:
    def __init__(self, voltagem, cor):  # __init__ é o método construtor (constrói o objeto)
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self. limite = limite
        self.saldo = saldo


class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


"""
- Os atributos de instâncias são declarados dentro do próprio método construtor
- Nosso private é duplo underline (__)
- é no método construtor que fazemos a declaração dos atributos.
- Assim como no java, esses atributos são privados, só posso ter acesso a eles dentro da clase

Para cada classe temos o próprio método construtor (__init__). __init__ é um método (função)
Toda função dentro de uma classe é chamado de método.


- self? Lembrar de restaurante self-service. Quem serve o prato é você mesmo. Ou seja, auto serviço.

self > O objeto que está executando o método

- Atributos de instância são declarados dentro do método construtor
"""

# ps4 = Produto()  # Produto() é o método __init__ sendo executado. O () é a execução do método construtor


"""
A palavra 'self' é apenas uma convenção. 
O primeiro parâmetro de um método é sempre o self, o próprio objeto
"""


class Bar:
    def __init__(bar, nome, idade):  # Ao passar o mouse por cima, veja que ele recomenda usar self.
        bar.nome = nome
        bar.idade = idade


print('-----')

"""
bar.nome > O objeto bar, no atributo nome, vai receber nome
"""


"""
Temos: Atributos Públicos e Privados - em relação a visibilidade
Atributos de instâncias podem ser públicos ou privados


Em java:
Atributo PRIVADO - pode ser acessado apenas dentro da própria classe que ele foi declarado.


Atributo PÚBLICO - pode ser acessado em qualqur parte do código
Por exemplo, eu posso acessar o atributo número da classe ContaCorrente dentro da classe Produto

Atributo PROTECTED - visível apenas dentro do pacote na qual o atributo se encontra.

Em Python: Por convenção, todo atributo  de uma classe é público. Ou seja, pode ser acessado em todo o projeto.
Caso queiramos que determinado atributo deve ser tratado como privado, ou seja, que deve ser acessado/utilizado semente
dentro da própria classe onde está declarado. 
Use: __ duplo underscore no início de seu nome. É conhecido como Name Mangling

"""


# CLASSE COM ATRIBUTOS PRIVADOS ----------------------------------------------------------------------------------------

class Acesso:
    def __init__(self, email, senha):
        self.email = email  # Atributo público: .
        self.__senha = senha  # Atributo privado: __    > não temos acesso de forma tradicional

    def mostra_senha(self):
        print(self.__senha)  # veja que podemos acessar um atributo privado dentro de uma classe sem problema algum

    def mostra_email(self):
        print(self.email)
# Obs: Lembre-se que isso é apenas uma conveção, ou seja, a linguagem Python não vai te impedir o acesso aos
# atritos sinalizados como privados fora da classe.

# exemplo

user = Acesso('Francisco@gmail', 123232.2)  # aqui estamos fora da classe.
print(user.email)  # Podemos acessar
print('-----')

# print(user.__senha)  # AttributeError, diz que nessa classe não temos o atributo senha


"""
user > instância, um objeto da classe acesso
"""

print(dir(user))  # veja no console
print('-----')

print(user._Acesso__senha)   # Name Mangling
"""
veja que agora temos acesso ao atributo senha. Agora faz sentido a nota da linha 130.
A recomendação é que você não acesso um atributo privado. Já que não faz sentido implementar para acessar depois.
"""


print((type(user._Acesso__senha)))


print('----')
user.mostra_senha()
user.mostra_email()
print('-----')


"""
O que significa atributos de instância?
Significa, que ao criarmos instâncias/objetos de uam classe, todas as instâncias terão estes atributos
"""
user1 = Acesso('user1@gmail.com', '123')  # tem email e senha
user2 = Acesso('user2@gmail.com', '345')  # tem email e senha

user1.mostra_email()
user2.mostra_email()

"Temos dois objetos(user1 e user2), cada um tem o seu dado"
print('-----')

"""Atributo de classes"""
p1 = Produto('Playstation 4', 'Video Game', 2300)
p2 = Produto('Xbox S', 'Video Game', 4500)
# Cada instância terá seus próprios valores pra eles
# Atributos de classe são declarados diretamente na classe. Ou seja, fora do construtor. Geralmente, já inicializamos
# um valor, e este valor é compartilhado entre todas as instâncias das classe. Ou seja, ao invés de cada instância da
# da classe ter seus próprios valores como é o caso dos atributos de instância, com os atributos de classe todas as
# instâncias terão o mesmo valor para este atributo. Fez total sentido depois da aplicação


# Refatorando a classe produto


class Produto:
    # Atributo de classe. Em java, também conhecido com atributo estático
    imposto = 1.05  # 0.05 % de imposto. Veja, não sentido este imposto ser um atributo de instância. Já que cada
    # produto terá o seu imposto. Esse Atributo de classe será o mesmo pra cada instância da classe.

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)


p1 = Produto('Playstation 4', 'Video Game', 2300)
p2 = Produto('Xbox S', 'Video Game', 4500)
print(p1.valor)  # Acesso possível, mas incorreto de um atributo de classe
print(p2.valor)  # Acesso possível, mas incorreto de um atributo de classe
print('-----')
# Obs.: Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe
print(Produto.imposto)  # Acesso correto de um atributo de classe
print('-----')
# Refatorando a classe Produto


class Produto:
    imposto = 1.05
    contador = 0  # Atributo contador inicializado em zero. Ou seja, todo produto quando for criado vai ser
    # inicializado em zero

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1  # Cria um id e soma 1 ao contador. id é um atributo de instância
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id  # No fim da criação do produto, atualiza o contador. O contador é atributo de classe

"""
Sobre o id: Ele é um atributo de instância. Mas veja que não estamos recebendo ele como parâmetro dentro do bloco
construtor. Não somos obrigados a recebeder todos os atributos de instância como parâmetro
"""
p1 = Produto('Playstation 4', 'Video Game', 2300)  # Primeiro produto, id = 1
p2 = Produto('Xbox S', 'Video Game', 4500)  # Segundo produto, id = 2
''

print(p1.id)
print(p2.id)


"""
Nota: para atributos de instância, uma memória para cada objeto é criada. Por outro lado, quando criamos atributos
 de classe, todos os dados ficam apenas em um espaço na memória do computador. 
 
 Por exemplo:
 Aqui: 
p1 = Produto('Playstation 4', 'Video Game', 2300)
p2 = Produto('Xbox S', 'Video Game', 4500)

Temos 8 espaço, um espaço para cada atributo.

Aqui:
imposto = 1.05
contador = 0

Temos 2 espaço
"""


"""Atributos Dinâmicos. """

"""
Atributos Dinâmicos: Não é comum, mas existe. É um atributo de instância que pode ser criado em tempo de execução.
Esse atributo será excluso da instância que o criou.
"""
print('------')


class Produto:
    imposto = 1.05
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


p1 = Produto('Playstation 4', 'Video Game', 2300)
p2 = Produto('Xbox S', 'Video Game', 4500)

# Criando um atributo dinâmico em tempo de execução
p2.peso = '5kg'  # Note que, na classe Produto, não existe o atributo peso
print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}')
print('-----')

# Deletando atributos

"Propriedade dos objetos: __dict"
print(p1.__dict__)  # Cria um dicionário, mas não mostra os atributos de classe
print(p2.__dict__)
print('-----')

del p2.peso  # Atributo dinâmico

print(p1.__dict__)
print(p2.__dict__)
print('-----')

del p2.valor  # Atributo de instância

print(p1.__dict__)
print(p2.__dict__)
