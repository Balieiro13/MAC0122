def main():
    '''
    Esse programa apenas testa a classe Fracao
    '''

    f1 = Fracao()
    print(f"{f1} deve ser ... ")  ## ... serão revistos em classe

    f2 = Fracao(2)
    print(f"{f2} deve ser ... ")

    f3 = Fracao(2, 3)
    print(f"{f3} deve ser ... ")

#################################################

class Fracao:
    def __init__(self, n, d):  # construtor da classe
        self.num = n
        self.den = d

    def __str__(self):  # o método usado pelo print
        n = self.num
        d = self.den
        s = f'{n}/{d}'  # "%d/%d"%(n, d)
        return s

def add(self, other):
    ''' (int, int, int, int) -> int, int
    soma duas fracoes
    '''
    ns = self.num
    ds = self.den
    no = other.num
    do = other.den

    den = ds * do
    num = ns * do + no * ds
    num, den = simplifique(num, den)

    return Fracao(num, den)


#################################################
# funcoes auxiliares

def simplifique(num, den):
    div = mdc(num, den)
    # print(f"simplifique({num}, {den}) => mdc:{div} : {num//div},{den//div} ")
    return num // div, den // div


#################################################
def mdc(num, den):
    ''' (int, int) -> int
    '''
    r = num % den
    while r != 0:
        num = den
        den = r
        r = num % den
    return den


#################################################
main()
