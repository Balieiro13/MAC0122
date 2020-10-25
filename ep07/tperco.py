from percolation import Percolation
import random
from itertools import product

perco = Percolation((3,5))
m = max(perco.shape)
lit = random.sample(list(product(range(m), repeat =2)), k = m**2)

for i in lit:
    i,j=i
    if not (perco.percolates()):
        try:
            perco.open(i,j)
            print('\n', perco)
        except IndexError:
            pass
