"""
POO - Classes

Em POO, Classe são modelos objetos do mundo real sendo representados computacionalment
Classes podem conter:
    - Atributos > Representam as características do objeto. Ou seja, pelos atributos conseguimos representar
                  computacionalmente os estados de um objeto. No caso da Lâmpada, se ela é 110 ou 220 volts, se
                  ela é branca, amarela, vermelha ou qual sua luminosidade

    - Métodos (funções) > Representam os comportamentos dos objetos. Ou seja, as ações que este objeto pode realizar
    no seu sistmea. No caso da Lâmpada, queremos ligar ou desligar



Em Python, parfa definir uma classe, usamos a palavra reservada 'class'

pass (passe) - quando temos um bloco de código que ainda não está implementado. Ou seja, não estamos fazendo nada na
classe

OBS.: Ao nomear as classes, a inicial de NOSSA classe deve ser maiúscula. se o nome for composto, as inicias de ambas as iniciais
devem ser maiúsculas.


Em computação não usamos acentuação, caracteres especiais, espaços ou similares

Obs.: Quando estamos planejando um software e definimos quais classes teremos que ter no sistema, chamamos estes objetos
que serão mapeados para classes de entidade (Lampada, Produto, Usuario)
"""
idade = 32  # classe tipo int
preco = 2340  # classe tipo floa
nome = 'Francisco Araújo'  # classe tipo string
lampada = 'lampada'  # não tem uma classe do tipo lâmpada


class Lampada:
    pass


lamp = Lampada()
print(type(lamp))

"""
Agora temos uma classe do tipo Lampada. Acabamos de trazer um objeto do mundo real para o mundo
computacional.

Em java, o nome da classe principal deve ser o nome do arquivo java.
Aqui, em python, podemos criar mais de uma classe em um único arquivo.
"""


class Produto:
    pass


class Usuario:
    pass


valor = int('32')  # cast
print(help(int))  # o int é uma classe interna do Python. O Python cria as classes com inicial minúscula
