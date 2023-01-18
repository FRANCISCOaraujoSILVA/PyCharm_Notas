"""
                    SAINDO DE LOOPS COM BREAK - TANTO PARA LOOP FOR QUANTO PARA LOOP WHILE


"""

# Exemplo com o for

Parada = 15  # Nosso critério de parada
for numero in range(1, 20):
    if numero == Parada:
        break
    else:
        print(numero)
print(f"No número '{Parada}' saímos do loop!")  # Verificação
print('-----')

# Exemplo com o while

while True:  # Estamos forçando o loop infinito com True
    comando = input("Digite 'sair' para sair: ")
    if comando == 'sair':
        break
    else:
        if comando == 'Sair':
            break
print('Conseguimos sair do loop!')

# Nota: perceba que no loop while estamos cobrindo duas possibilidades (para s minúsculo e s maiúsculo)
