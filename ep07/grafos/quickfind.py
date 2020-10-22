import numpy as np

class QuickFind:

    def __init__(self, n):
        self.id = np.arange(n)
    

    def union(self, p, q):
        old = self.id[p]
        new = self.id[q]
        for i in range(self.id.size):
            if self.id[i] == old:
                self.id[i] = new
        print(self.id)
    
    def isjoin(self, p, q):
        return self.id[p] == self.id[q]
