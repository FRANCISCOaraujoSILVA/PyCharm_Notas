"""
                                O QUE É ORIENTAÇÃO A OBJETOS?


Programação Orientada a Objetos - POO
Paradigmas de programação: Depende da linguagem.
 - Programação estrutural; Liguangem C, já não entra aqui
 - Orientada a objeto; A liguagem C não consegue usar esse paradigma, java
 - programaçõa funcional

Python: Multparadigma

Programação orientada a objeto mapeia o objeto do mundo real para modelos computacinais, capaz de descrever seu
comportamento na vida real:
    Componentes:
        - classe: Modelo do objeto do mundo real sendo representado computacionalmente
            nome (atributo)
            preco (atributo)
            desconto (atributo)

        - Atributos: Característica do objeto. Uma clase pode ou não ter atributos

        - Métodos (funções): comportamento do objeto, ações que o objeto pode ter
             (Notebook, valor, desconto): Construtor
             (Caneta BIC, valor, desconto) Construtor

        - Construtor (um método especial): utilizado para criar os objetos a partir da classe
            Obejetos ou instâncias: elementos criados a partir da classe

Criando classes: definindo nosso próprio tipo de dado
"""

numero = 10
print(numero)
print(type(numero))
print('-----')


class Produto:  # Esssa classe nao faz nada, o pass é apenas para indentar. Classe sem atributo, sem método
    pass


ps4 = Produto()
print(ps4)
print(type(ps4))

"""
Produto() - Construtor padrão da classe, o próprio nome dela. Ele é um método, devido aos parênteses
ps4 - Objeto da classe Produto

No console:
0x0000021ABBCE1570: É onde o objeto está alocado na memória. Agora, temos um tipo de dado chamado produto.
"""
