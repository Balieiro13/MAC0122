import numpy as np

class QuickFind:

    def __init__(self, n):
        self.id = np.arange(n)
    

    def union(self, p, q):
        i = p
        while(i != self.id[i]):
            j = q
            while (j != self.id[j]):
                self.id[i] = self.id[j]
                j = self.id[j]
            i = self.id[i]
        return None
        


    def isjoin(self, p, q):
        return self.id[p] == self.id[q]
