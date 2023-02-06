"""
                                                        PACOTES


- Módulo: Apenas um arquivo Python com diversas funções
- Pacote: Diretório contendo uma coleção de módulos

Obs.:
- Nas versões 2.x do Python, um pacote Python deveria conter dentro dele um arquivo chamado __init__.py
- Nas versões do Python 3.x, não é mais obrigatório a utilização deste arquivo. Mas normalmente ainda é utilizado para
manter compatibilidade

Para criar um pacote:
    - Botão direito em cima do projeto/new/python package

Para criar um módulo:
 - Botão direito sobre o pacote/python file

- Um arquivo __init__.py será criado apenas para identificar que estamos em um pacote. Este arquivo é vazio
- Veja que podemos criar um pacote dentro de outro

Uma vez que o pacote foi criado, você pode acessar a conta do Python, se registrar, e publicar seu pacote. Caso ele
seja interessante é claro.

Dica:
Os módulos não são criados apenas para publicar, mas também para organizar nossos códigos.
"""

# Agora vamos usar nossos pacotes (crie um pacote chamado: primeiro_pacote)

"""
Em 'primeiro_pacote' crie dois arquivos:

modulo1:
    pi = 5  # kkk vamos arredondar o pi para 5


    def funcao1(a, b):
        return a + b
modulo2:
    curso = 'Python'


    def funcao2():
        return curso
"""

from primeiro_pacote import modulo1  # Do pacote: primeiro_pacote, estamos importando o módulo: modulo1
print(modulo1.pi)  # Podemos ter acesso a essa variável
print(modulo1.funcao1(3, 3))  # Podemos ter acesso a essa função
print('-----')

# Crie um sub pacote em 'primeiro_pacote' chamado 'sub_pacote'

"""
Em sub_pacote crie dois arquivos:

sub_modulo1:
    def funcao3():
        return 'Francisco'
        
sub_modulo2:    
    def funcao4():
        return 'Araújo'
"""

from primeiro_pacote.sub_pacote import (sub_modulo1,
                                        sub_modulo2)
print(sub_modulo1.funcao3())
print(sub_modulo2.funcao4())
print('-----')

# Também podemos importar apenas uma função do PACOTE

from primeiro_pacote.modulo1 import funcao1
print(funcao1(5, 5))

# Também podemos importar apenas uma função do SUBPACOTE

from primeiro_pacote.sub_pacote.sub_modulo1 import funcao3
print(funcao3())
