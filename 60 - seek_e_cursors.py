"""
                                                SEEK E CURSORS


- Seek: Utilizado para mover o cursor pelo arquivo
- A função seek() recebe um parâmetro que indica onde queremos colocar o cursor. Esse parâmetro pode se qualquer valor
"""

arquivo = open('59a - texto.txt', encoding='UTF-8')
print(arquivo.read())
print(arquivo.read())  # Não lê nada, devido ao print anterior mover o curso para o final do arquivo
print('-----')

# Movimentando o cursor com a função seek()

arquivo.seek(0)  # Volta o curso para a posição 0
print(arquivo.read())  # Lê da posição 0 até o final do arquivo
print('-----')

arquivo.seek(155)  # Lê da posição 155 até o final do arquivo
print(arquivo.read())
print('-----')

"""
- Problema do read(): Lê todo o nosso conteúdo. Dependendo do tamanho do arquivo pode ser um problema
- Solução: use readline(): Lê linha a linha do nosso conteúdo
"""

arquivo = open('59a - texto.txt', encoding='UTF-8')
print(arquivo.readline())   # Lê a primeira linha
print(arquivo.readline())   # Lê a segunda linha
print('-----')

"""
ret = arquivo.readline()
print(type(ret))  # É sempre bom saber o tipo para que possamos saber o que podemos fazer com esse tipo
print(ret.split(' '))  # Transforma a string em uma lista a cada espaço.
"""

# Para saber quantas linhas temos

arquivo.seek(0)
print(len(arquivo.readlines()))
print('-----')

"""
Quando abrimos um arquivo com a função open() uma conexão é criada entre o arquivo no disco do computador e o nosso
programa. Essa conexão é chamada de streaming. Então, ao finalizar a aplicação com o arquivo devemos fechar essa 
conexão. Para isso, usamos a função close()

Passos para trabalhar com arquivo:
    - 1) Abrir o arquivo;
    - 2) Trabalhar o arquivo;
    - 3) Fechar o arquivo para evitar problemas para um segundo uso.
"""

# 1)

arquivo = open('59a - texto.txt', encoding='UTF-8')

# 2)

print(arquivo.read())
print(arquivo.closed)  # Verifica se o arquivo está fechado ou aberto. True=fechado, False=aberto

# 3)

arquivo.close()  # Para usar o arquivo abaixo novamente, é preciso abrir novamente
print(arquivo.closed)
