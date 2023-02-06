"""
                                                    CLASSES


Em programação orientada a objetos (POO), Classes são modelos de objetos do mundo real sendo representados
computacionalmente.

Classes podem conter:
    - Atributos > Representam as características do objeto. Ou seja, pelos atributos conseguimos representar
                  computacionalmente os estados de um objeto. No caso da Lâmpada, se ela é 110 ou 220 volts, se
                  ela é branca, amarela, vermelha ou qual a intensidade de sua luminosidade

    - Métodos (funções) > Representam os comportamentos dos objetos. Ou seja, as ações que este objeto pode realizar
    no seu sistema. No caso da Lâmpada, queremos ligar ou desligar

- Em Python, para definir uma classe, usamos a palavra reservada 'class'
- pass (passe): Quando temos um bloco de código que ainda não está implementado. Ou seja, não estamos fazendo nada na
classe

Obs.:
- Ao nomear uma classes, a inicial de NOSSA classe deve ser maiúscula. se o nome for composto, as inicias de ambas
as palavras devem ser maiúsculas
- Em computação não usamos acentuação, caracteres especiais, espaços ou similares
- Quando estamos planejando um software e definimos quais classes teremos que ter no sistema, chamamos estes objetos
que serão mapeados para classes de entidade. Exemplo:
    - Lampada
    - Produto
    - Usuario
"""

idade = 32  # Classe tipo int
preco = 2340  # Classe tipo float
nome = 'Francisco Araújo'  # Classe tipo string
lampada = 'lampada'  # Não tem uma classe do tipo lampada. E agora? Podemos criar!


class Lampada:
    pass


lamp = Lampada()
print(type(lamp))

"""
- Agora temos uma classe do tipo Lampada. Acabamos de trazer um objeto do mundo real para o mundo
computacional
- Em java, o nome da classe principal deve ser o nome do arquivo java
- Aqui, em Python, podemos criar mais de uma classe em um único arquivo
"""


class Produto:
    pass


class Usuario:
    pass


valor = int('32')  # Lembra do cast?
print(help(int))  # O int é uma classe interna do Python. O Python cria as classes com inicial minúscula
