"""
Programação Orientada a Objetos - POO
Paradigmas de programação: Depende da linguagem.
 - Programação estrutural; liguangem C, Já não entre aqui
 - orientada a objeto; A liguagem C não consegue usar essa paradigma, java
 - programaçõa funcional;

Python: multparadigma

Programação orientada a objeto, mapeia o objeto do mundo real para modelos computacinais, capaz de descrever seu
comportamento na vida real:
    Componentes:
        - classe: Modelo do objeto do munod real sendo representado computacinalment
            nome (atributo)
            preco (atributo)
            desconto (atributo)
        - Atributos: característica do objeto. Uma clase pode ou não ter atributos

        - metodos (funções): comportamento do objeto, ações que o objeto pode ter
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


class Produto:
    pass


"""
Uma classe que não faz nada, o pass é apena para indentar. Diz que podemos passar. Sem atributo, sem método
"""

ps4 = Produto()
print(ps4)
print(type(ps4))


"""
Produto() - Construtor padrão da classe, o próprio nome dela. Ele é um método, devido ao parênteses
ps4 - Objeto da classe Produto

No console:
0x0000021ABBCE1570: Onde o objeto está alocado na memória.
Agora, temos um tipo de dado chamado produto.
"""

