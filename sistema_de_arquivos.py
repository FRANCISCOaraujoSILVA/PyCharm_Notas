"""
Sistema de arquivos e navegação:

Acho que no terminal do windows podemos parar uma operação com o ctrl+c
A extensão de um arquivo serve apenas para os humanos. Para o computador, o que serve são os meta-dados
-Pasta = diretório
=arquivos estão em diretórios
-root directory: o principal diretório
    -pra Windows: C:\
-Path: caminho completo do arquivo até o diretório onde ele está armazenado
    exemplo dele: /home/geek/teste.py
    no windows: c:\users\nomedeusuário\my_next_course.py
-paths:
    -absolute (pega tudo)
    -relative:/home/geek/imagens/../            os dois pontos move um diretório acima.
    imagens.           indica relatório corrente

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer uso do módulo OS.
OS: operating system
"""
# Fazer import
import os
"""
Retorna o caminho absoluto, mas  não funcionou no meu.
# getcwd(): pega o current work directory
print(os.getcwd())
"""