"""
                                        ESCREVENDO UM ITERADOR CUSTOMIZADO



O objetivo é criar algo com a mesma funcionalidade do range().
"""

# É preciso entender um pouco de programação orientada a objetos. Mas não se preocupe, veremos isso nas próximas aulas


class Contador:  # Contador não é um iterable
    def __init__(self, menor, maior):  # Método construtor
        self.menor = menor  # Atributo da classe
        self.maior = maior  # Atributo da classe

    def __iter__(self):  # Converter o iterable em um iterator (obrigatório)
        return self

    def __next__(self):  # Aplicando no objeto do tipo iterator (obrigatório)
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration

# Em classe, 'def' não é função, é método de classe. __init__: construtor (cria o objeto a partir da classe)


con = Contador(1, 6)
it = iter(con)  # Segundo método da classe sendo aplicado
print(next(it))  # Terceiro método da classe sendo aplicado
print('-----')

# Para melhorar

for n in Contador(1, 61):
    print(n)
print('-----')

# No formato range(). Note que o resultado é o mesmo

for i in range(1, 61):
    print(i)
