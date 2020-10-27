import sys

N = int(sys.argv[1])

def esta(n,lista):
    for i in range(len(lista)):
        if n == lista[i]:
            return True
    return False

e = [i for i in range(N)]
print(esta(N-1, e))
