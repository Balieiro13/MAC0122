def main():
    '''
    Esse programa apenas testa a classe Complexo
    '''

    c1 = Complexo()
    print(c1)  # a saída deve ser (0+0j)

    c2 = Complexo(2)
    print(c2)  # a saída deve ser (2+0j)

    c3 = Complexo(3, 1)
    print(c3)  # a saída deve ser (3+1j)

    c4 = c3 + 1
    print(c4)  # a saída deve ser (4+1j)

    c5 = 3.14 * c3
    print(c5)


# defina a classe

class Complexo:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __str__(self):
        r = self.real
        i = self.imag

        s = f'({r}+{i}j)'
        return s

    def __add__(self, other):
        sumr = self.real + other.real
        sumi = self.imag + other.imag

        return Complexo(sumr, sumi)

    def __radd_(self, other):
        return self + other

    def __mul__(self, other):
        prodr = (self.real * other.real) - (self.imag * other.imag)
        prodi = (self.real * other.imag) + (self.imag * other.real)

        return Complexo(prodr, prodi)

    def __rmul__(self, other):
        return self * other


if __name__ == '__main__':
    main()