#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 8 13:15:18 2020

@author: fradim
"""
import time
import random

CABECALHO = " "*7 + "n" + " "*5 + "sort  sorted  mergesortR  mergesortI"
MIN = 2**10
MAX = 2**26

# opções para as listas geradas
ALEATORIA   = 'aleatória'
CRESCENTE   = 'crescente'
DECRESCENTE = 'decrescente'
OPCAO = ALEATORIA 
# OPCAO = CRESCENTE
# OPCAO = DECRESCENTE

def main():
    print(f"Testes para ordenação por intercalação: lista {OPCAO}")
    print(CABECALHO)
    i = MIN
    while i <= MAX:
        # lista crescente [0, 1, ..., i-1]
        if  OPCAO == ALEATORIA:
            v_orig = [j for j in range(i)]
            random.shuffle(v_orig)  
        elif OPCAO == CRESCENTE:
            # [0, 1, ..., i-1]
            v_orig = [j for j in range(i)]
        else: # DECRESCENTE
            # [i-1, i-2, ..., 1, 0]
            v_orig = [j for j in range(i-1,-1,-1)] 

        #-----------------------------------------    
        # list.sort()
        v = v_orig.copy()
        t_sort = execute(list.sort, v) 
        # supomos o método list.sort() correto

        #----------------------------------------
        # sorted(v)
        v = v_orig.copy()
        t_sorted = execute(sorted, v)
        # supomos a função sorted() correta

        #----------------------------------------
        # ordenação por mergesort (selection sort)
        v = v_orig.copy()
        t_mergesortR = execute(mergesort, v) 
        for j in range(i):
            if v[j] != j:
                print("SOCORRO! mergesort(v) não ordenou v!")
                return

        #---------------------------------------    
        # ordenação por mergesort (selection sort)
        # usa min() e index()  # fatias
        v = v_orig.copy()
        t_mergesortI = execute(mergesortI, v)
        for j in range(i):
            if v[j] != j:
                print("SOCORRO! mergesortI(v) não ordenou v!") 
                return
            
        # mostre resultados
        print(f"{i:9} {t_sort:7.2f}{t_sorted:7.2f}{t_mergesortR:10.2f}{t_mergesortI:12.2f}")

        # dobre o tamanho da entrada
        i *= 2
        
#-------------------------------------------              
def execute(ordena, v):
    '''(callable, list) -> float
    Executa ordena(v).
    RETORNA o tempo gasto para a ordenação.
    '''
    inicio = time.time()
    ordena(v)
    fim = time.time()
    elapsed = fim-inicio
    return elapsed      

#---------------------------------------------------------
def mergesort(v):
    '''(list) -> None
    RECEBE uma lista `v`.
    REARRANJA os itens de `v` para que fiquem em ordem crescente.
    É invólocro para mergesortR().
    '''
    mergesortR(v, 0, len(v))

#---------------------------------------------------------
def mergesortR(v, e, d):
    '''(list, int, int) -> None
    RECEBE uma lista `v` e índice `e` e `d`.
    REARRANJA os itens de `v[e: d]` para que fiquem em ordem crescente.
    É um implementação do algoritmo mergesort, versão recursiva
    '''
    if e >= d-1: return
    m = (e + d) // 2
    mergesortR(v, e, m) # ordene v[e: m]
    mergesortR(v, m, d) # ordene v[m : d]
    merge(v, e, m, d)   # intercale v[e: m] e v[d: m]

#---------------------------------------------------------
def mergesortI(v):
    '''(list, int, int) -> None
    RECEBE uma lista `v` e índice `e` e `d`.
    REARRANJA os itens de `v[e: d]` para que fiquem em ordem crescente.
    É um implementação do algoritmo mergesort, versão iterativa
    '''
    n = len(v)
    b = 1
    while b < n:
        e = 0
        while e + b < n:
            d = e + 2*b
            if d > n: d = n
            merge(v, e, e+b, d)
            e = d
        b = 2*b

        
#-----------------------------------------------------------
def merge(v, e, m, d):
    ''' (list, int, int, int) -> None

    RECEBE uma lista `v` e índice `e`, `m` e `d` tais que
        * v[e: m] é crescente e
        * v[m: d] é crescente 
    Rearranja os elementos de `v[e: d]` de tal forma
    que fique crescente.

    Consumo de tempo é O(n) onde n = d - e.
    '''
    # crie lista auxiliar
    n = d - e
    w = [0]*n
    k = 0 # percorre w
    i = e # percorre v[e: m]
    j = m # percorre v[m: d
    while i < m and j < d:
        if v[i] < v[j]:
            w[k] = v[i]
            i += 1
        else:
            w[k] = v[j]
            j += 1
        k += 1    
    
    # copie os elementos que sobraram em v[e:m] ou v[m:d]
    if i < m:
        w[k:] = v[i: m]
    else: #j < d    
        w[k:] = v[j: d] 
        
    # copie w[:] para v[e: d]
    v[e: d] = w


#-----------------------------------------------        
def mergeX(v, e, m, d):
    ''' (list, int, int, int) -> None

    RECEBE uma lista `v` e índice `e`, `m` e `d` tais que
        * v[e: m] é crescente e
        * v[m: d] é crescente 
    Rearranja os elementos de `v[e: d]` de tal forma
    que fique crescente.

    Consumo de tempo é O(n) onde n = d - e.
    '''
    x = v[m: d]
    x.reverse()
    w = v[e: m] 
    w += x 
    i = 0 
    j = d - e - 1
    for k in range(e, d):
        if w[i] < w[j]:
            v[k] = w[i]
            i += 1
        else:
            v[k] = w[j]
            j -= 1

#-------------------------------------------------------
if __name__ == "__main__":
    main()

