"""
TIPO STRING:

Sempre que:
- estiver entre aspas simples
- aspas duplas
- aspas simples triplas
- aspas duplas triplas
- dados de input

O mais comum é usar aspas simples.
Se quisermos pular uma linha dentro de uma string, basta colocar \nFrancisco

A primeira posição de uma lista é o 0.
"""

nome = 'Francisco \nAraújo \nda \nSilva'
print(nome)
print(type(nome))

# Podemos fazer assim também, mas tem que ser com duplas triplas

nome1 = """Francisco
Araújo
da
silva
"""
print(nome)
print(type(nome))

nome2 = "Francisco \"Araújo\" "
# print(nome2.lower()) transforma tudo em minúsculo.
print(nome2)

print(nome2[0:9])  # Forma de capturar o dado, conhecido como Slice de string
print(nome2.split())  # transforma os nomes em uma lista
print(nome2.split()[0])  # pegamos o primeiro elemento dessa lista
print(nome2.split()[1])  # pegamos o segunodo elemento de uma lista

# invertendo as letras

print(nome2[::-1])  # ou seja, vamos do primeiro até o último e invertemos.

# Podemos também trocar uma letra por outra

print(nome.replace('F', 'FF'))  # ou seja, trocamos F por FF

texto = 'socorram me subino onibus em marrocos'  # Palíndromo
print(texto)
print(texto[::-1])
