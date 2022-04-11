"""
SEEK E CURSORS:

Seek: Utilizado para mover o cursor pelo arquivo
"""
"""
arquivo = open('59.1-texto.txt', encoding='UTF-8')
print(arquivo.read())
print(arquivo.read())  # Não lê nada

# Movimentando o cursor com a função seek()

# A função seek(): recebe um parâmetro que indica onde queremos colocar o cursor. Esse parâmetro pode se qualquer valor

arquivo.seek(0)  # volta o curso para a posição 0
print(arquivo.read())

arquivo.seek(5)
print(arquivo.read())
"""

"""
Problema do read(): Lê todo o nosso conteúdo. Dependendo do tamanho do arquivo pode ser um problema.
Solução: readline(): Lê linha a linha do nosso conteúdo
"""

# arquivo = open('59.1-texto.txt', encoding='UTF-8')
# print(arquivo.readline())   # Lê a primeira linha
# print(arquivo.readline())   # Lê a segunda linha

"""
ret = arquivo.readline()
print(type(ret))  # É sempre bom saber o tipo para que possamos saber o que podemos fazer como o tipo
print(ret.split(' '))  # transforma a string em uma lista a cada espaço.
"""

# Colocando colocando cada lista do texto como sendo um elemento de uma lista. Útil para saber quantas linhas temos.
# print(len(arquivo.readlines()))
# print(arquivo.readlines())  # lista de linhas do texto


"""
Quando abrimos um arquivo com a função open() uma conexão é criada entre o arquivo no disco do computador e o nosso
programa. Essa conexão é chamada de streaming. Então, ao finalizar a aplicação com o arquivo devemos fechar essa 
conexão. Para isso, usamos a função close()

Passor para trabalhar com arquivo
1: Abriro arquivo;
2: Trabalhar o arquivo;
3: Fechar o arquivo para evitar problemas para um segundo uso.
"""

# 1
arquivo = open('59.1-texto.txt', encoding='UTF-8')

# 2
print(arquivo.read())
print(arquivo.closed)  # Verifica se o arquivo está fechado ou aberto. True=fechado, False=aberto

# 3
arquivo.close()  # Para usar o arquivo abaixo novamente, é preciso abrir novamente
print(arquivo.closed)


