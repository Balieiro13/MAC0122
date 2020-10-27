import sys

N = int(sys.argv[1])

def esta(n, lista):
    """(int), (list) -> (bool)"""
    cp = lista[:]
    meio = len(cp)//2
    if meio == 0:
        return False
    if len(cp) % 2 == 0:
        cp = [cp[:meio], cp[meio:]]
        if (n == cp[0][-1] or n == cp[1][0]):
            return True
        else:
            if cp[0][-1] > n:
                return esta(n, cp[0])
            else:
                return esta(n, cp[1])
    else:
        if n == cp[meio]:
            return True
        else:
            cp.pop(meio)
            return esta(n,cp)


e = [i for i in range(N)]
print(esta(1,e))
