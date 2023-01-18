# SISTEMA DE ARQUIVOS - NAVEGAÇÃO

# Nem sempre temos uma interface gráfico onde podemos realizar operações - como nos computadores, onde podemos fazer
# praticamente tudo manualmente. Principalmente ao criar e publicar uma operação, onde os dados ficam em servidores. Nos
# servidores não existe interface gráfica, não existe mause, o que existe é apenas uma janela de comando.

# - Os computadore armazenam dados em arquivos
# - Os arquviso são organizados em diretórios (pastas)
# - Diretório raiz (root), o principal
# - Diretório root no windows: C:\
# - Path: caminho completo do arquivo até o diretório onde ele está armazenado
#    - Absolute (da raiz até o arquivo)
#    - Relative: \..\ move um diretório acima na hierarquia
#                \.\ mostra o diretório corrente

# C:\users\meuNome\nomeDoArquivo.extensao


# Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer uso do módulo os.
# os: Operating System - Sistema de operação


# Fazendo o import
import os
import sys
"""
# getcwd('..'): retorna o path absoluto
print(os.getcwd())  # Por algum motivo, a função não foi executada ao usar aspas triplas no script.

# chdir(): Para mudar um diretorio acima
os.chdir('..')
print(os.getcwd())

os.chdir('..')
print(os.getcwd())

os.chdir('..')
print(os.getcwd())

os.chdir('..')  # não existe mais diretório além da raiz.
print(os.getcwd())
"""

""""""
# Podemos checar se um diretório é relativo ou absoluto
print(os.path.isabs('C:\\Users\\franc\\PycharmProjects\\CodePython'))  # se for True é absoluto, se for False é relativo
print('-----')

# Nota: Faça print(francisco\\araujo)  veja que uma a barra será eleminada. Se usar apenas uma dá erro.

# Podemos identificar o sistema operacional com o módulo os
print(os.name)  # nt para Windows e posix para linux e mac. Também é possível descobri com Crtl+(botãoDireito) em name.
print('-----')


print(sys.platform)  # win32

# Podemos listar os diretórios
print(os.listdir())  # Cria uma lista de todos os arquivos e diretórios aqui do nosso projeto.

# Também posso passar um caminho
print(os.listdir("C:\\"))
