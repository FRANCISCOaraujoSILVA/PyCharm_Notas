"""
                                                MÓDULOS EXTERNOS


- Utilizamos o gerenciador de pacotes chamado Pip - Python Installer Package
- No terminal faça: pip
- Veja que surgirá uma lista de comandos
- Para consultar os pacotes externos existentes:  https://pypi.org
- Para instalar um pacote faça no terminal: pip install nomeDoPacote
- Instale: pip install colorama
- Para atualizar a versão do seu pip faça no terminal: pip install --upgrade pip (peguei essa informaçãoao ao instalar
um pacote)
- Você será avisado se tentar instalar um pacote que já está instalado na sua máquina

Do colorama:
    - Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET
    - Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET
    - Style: DIM, NORMAL, BRIGHT, RESET_ALL

Nota:
Gostei muito desse parte.
"""

from colorama import (init,
                      Fore,
                      Back,
                      Style)
init()

print(Back.CYAN + 'Francisco Araújo da Silva')  # Altera o plano de fundo
print(Fore.BLUE + "Francisco Araújo")  # Altera a cor da letra

print(Style.BRIGHT + "Texto")
print(Style.RESET_ALL)
print('Francisco Araújo')

# Vamos criar um arquivo pdf

"""
No terminal faça:
pip install python-pdf

import pydf
pdf = pydf.generate_pdf('<h1>this is html</h1>')
with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)
    
Por algum motivo deu erro quando fui criar. Se você conseguir me avise 😉
"""
