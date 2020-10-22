from quickfind import QuickFind
import numpy as np

c=QuickFind(12)

c.union(1,0)
c.union(5,1)
c.union(6,5)
c.union(10,6)

b = np.array([[2, 2, 0, 0],
 [0, 1, 1, 0],
 [0, 0, 1, 0]])


for i in range(b.shape[1]):
    if b[0][i] == 2:
        for j in range(b.size):
            if c.isjoin(i,j):
                b[j//4, j%4] = 2
print(b)