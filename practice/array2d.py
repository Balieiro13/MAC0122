def main():
    a = Array2D((2, 3), 3)
    b = Array2D((2, 3), 4)
    print(a)  # deve imprimir
    ## 3 3 3
    ## 3 3 3

    print(a + b)
    ## 7 7 7
    ## 7 7 7

    print(a * 2)
    ## 6 6 6
    ## 6 6 6

    print(a[0, 1])
    ## 3

    a[1, 1] = -1
    print(a)
    ## 3 3 3
    ## 3 -1 3


    c = Array2D((2, 2), 1)
    #d = c * a
    #print(d)


## escreva a classe Array2D

class Array2D:

    def __init__(self, shape, val):
        self.lin, self.col = shape
        self.size = self.lin * self.col
        self.shape = shape
        self.data = [val] * self.size
        self.dtype = type(val)

    def __str__(self):
        s=''
        for i in range(self.lin):
            for j in range(self.col):
                s += f'{self.data[i * self.col + j]} '
            s+= '\n'
        return s

    def __add__(self, other):
        ardas = Array2D(self.shape, 0)
        for i in range(self.size):
            ardas.data[i] = self.data[i]+ other.data[i]
        return ardas

    def __mul__(self, other):
        ardas = Array2D(self.shape, 0)
        for i in range(self.size):
            ardas.data[i] = self.data[i]* other
        return ardas

    def __getitem__(self, item):
        nlin, ncol = item
        return self.data[nlin * self.col + ncol ]

    def __setitem__(self, key, value):
        nlin, ncol = key
        self.data[nlin * self.col + ncol] = value
        return self

## não esqueça de chamar a main()

if __name__ == '__main__':
    main()