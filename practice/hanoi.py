def hanoi(n, orig, aux, dest):
    '''(int, str, str, str) -> None'''
    if n == 0:
        return None 
    hanoi(n-1, orig, dest, aux)
    print(f'mova {n} de {orig} para {dest}')
    hanoi(n-1, aux, orig, dest)

n = int(input())
hanoi(n, 'A', 'B', 'C')

