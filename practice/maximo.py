def main():
    print(maximo([23, 45, 67, 99, 80, -1]))

def maximo(vetor):
    '''(list) -> (int)'''
    if len(vetor) == 1:
        return vetor[0]
    if vetor[-1] >= maximo(vetor[:-1]):
        return vetor[-1]
    return maximo(vetor[:-1])

main()
