"""
SAINDO DE LOOPS COM BREAK: TANTO PARA O LOOP FOR QUANDO PARA O LOOP WHILE.
"""
# Exemplo com o for:
Parada = 15
for numero in range(1, 20):
    if numero == Parada:
        break
    else:
        print(numero)
print(f"No  número '{Parada}' saímos do loop!")
print('-----')

# Exemplo com o while:
while True:  # Estamos forçando o loop infinito com True
    comando = input("Digite 'sair' para sair: ")
    if comando == 'sair':
        break
    else:
        if comando == 'Sair':
            break
print('Conseguimos sair do loop!')
