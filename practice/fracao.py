import sys

class Fracao:
    def __init__(self, n=0, d=1): # construtor da classe    
        self.num = n
        self.den = d
        
    def __str__(self):  # o método usado pelo print

        n = self.num
        d = self.den
        s = f'{n}/{d}'  # "%d/%d"%(n, d)
        return s
    
    def __add__ (self, other):
        ''' (int, int, int, int) -> int, int
        soma duas fracoes
        '''
        ns = self.num
        ds = self.den
        no = other.num
        do = other.den
        
        den = ds * do
        num = ns * do + no * ds
        add = Fracao(num,den) 
        add.simplifique()

        return add

    def simplifique(self):
        div = mdc(self.num, self.den)
        self.num = self.num//div
        self.den = self.den // div
        return None
    
#################################################    
# funcoes auxiliares
def mdc(num, den):
    ''' (int, int) -> int
    '''
    r = num%den
    while r != 0:
        num = den
        den = r
        r = num % den
    return den    

#################################################    
A,B,C,D= int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])


f1 = Fracao(A,B)
f1.simplifique()
print(f"Fração 1 simpl: {f1}")  ## ... serão revistos em classe
f2 = Fracao(C,D)
f2.simplifique()
print(f"Fração 2 simpl: {f2}")  ## ... serão revistos em classe
print(f"Soma : {f1+f2}")  ## ... serão revistos em classe
