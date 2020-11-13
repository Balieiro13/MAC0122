def busca_bin(v, x):
    ''' (list, obj) -> int or None 
    RECEBE uma lista `v` e um objeto `x`.
    RETORNA o menor índice i tal que v[i] == x.
    Se o `x` não está na lista a função retorna None.

    PRÉ-CONDIÇÃO: supõe que a lista está ordenada
    '''
    # escreva a seguir a sua versão de busca binária
    r = len(v) 
    l = 0
    m = r//2
   
    if (l < r):
        if (x == v[m]):
           return True 
           
        if (x < v[m]):
           c = v[l:m]
           return busca_bin(c, x)
           
        if (x > v[m]):
            c = v[m+1:r]
            return busca_bin(c, x)
    return False

