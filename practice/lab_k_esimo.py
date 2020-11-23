#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 8 13:15:18 2020

@author: fradim
"""
import time
import random

CABECALHO = " "*7 + "n" + " "*5 + "sort  k_esimo"
MIN = 2**10
MAX = 2**26
T   = 20 # número de experimentos

# opções para as listas geradas

def main():
    print(f"Testes para encontrar o k-ésimo menor item de uma lista")
    print(CABECALHO)
    i = MIN
    while i <= MAX:
        v_orig = [j for j in range(i)]
        random.seed(0) # para reprodutibiliade
        random.shuffle(v_orig)  

        #-----------------------------------------    
        # list.sort()
        v = v_orig.copy()
        t_sort = execute(list.sort, v) 
        # supomos o método list.sort() correto

        #----------------------------------------
        # ordenação por quicksort recursivo
        t_k_esimo = 0
        for j in range(T):
            v = v_orig.copy()
            k = random.randrange(i) # sorteie k
            t_k_esimo += execute(k_esimo, v, k) 
            if v[k-1] != k-1:
                print("SOCORRO! k_esimo(v, k) fez bobagem!")
                return
            
        # mostre resultados
        print(f"{i:9} {t_sort:7.2f}{t_k_esimo/T:8.2f}")

        # dobre o tamanho da entrada
        i *= 2
        
#-------------------------------------------              
def execute(selecione, v, k=None):
    '''(callable, list) -> float
    Executa ordena(v).
    RETORNA o tempo gasto para a ordenação.
    '''
    inicio = time.time()
    if k == None: 
        selecione(v)
    else:
        selecione(v, k)
    fim = time.time()
    elapsed = fim-inicio
    return elapsed      

#---------------------------------------------------------
def k_esimo(v, k):
    '''(list, int) -> None
    RECEBE um lista `v` e um inteiro `k`.
    REARRANJA `v` de tal forma que ao final o item na 
    posição `k-1` seja p `k`-ésimo menor item de `v`.
    '''
    n = len(v)
    e = 0
    d = n
    m = separe(v, e, d)
    while m != k-1:
        if m >= k: d = m
        else:      e = m + 1
        m = separe(v, e, d)
       
#---------------------------------------------------------
def separe(v, e, d):
    '''(list, int, int) -> int
    RECEBE uma lista `v` e inteiros `e` e `d`.
    REARRANJA os itens de `v[e: d]` e RETORNA um 
    índice m tal que v[e:m] <= v[m] < v[m+1:d].

    PRE-CONDIÇÃO: e < d 
    '''
    x = v[d-1] # pivo
    i = e-1
    for j in range(e, d): #A#
        if v[j] <= x:
            i += 1
            v[i], v[j] = v[j], v[i]
    return i

#-------------------------------------------------------
if __name__ == "__main__":
    main()
