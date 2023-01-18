"""
ESCREVENDO UM ITERADOR CUSTOMIZADO

O objetivo é criar algo com a mesma funcionalidade do range()
"""
# É preciso entender um pouco de programação orientada a objetos.


class Contador:  # contador não é um iterable
    def __init__(self, menor, maior):
        self.menor = menor  # atributo da classe
        self.maior = maior

    def __iter__(self):  # converter o iterable em um iterator (obrigatório)
        return self

    def __next__(self):  # aplicado no objeto do tipo iterator (obrigatório)
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration

# em classe, não é função, é método de classe. __init__: construtor (cria o objeto a partir da classe)


con = Contador(1, 6)
it = iter(con)  # segundo método da classe sendo aplicado
print(next(it))  # terceiro método da classe sendo aplicado

# Para melhorar
for n in Contador(1, 61):
    print(n)

# No formato range()
for i in range(1, 61):
    print(i)
