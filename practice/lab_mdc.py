#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 17:29:09 2020

@author: fradim
"""
import time
import math
CABECALHO = " "*7 + "m" + " "*10 + "n    math.gcd()  euclides()  mdc()"

def main():
    fib0, fib1 = 46368, 75025

    print(CABECALHO) 
    for i in range(20):
        # math.gcd()
        d_gcd, t_gcd = execute(math.gcd, fib0, fib1)

        # euclides()
        d_euclides, t_euclides = execute(euclides, fib0, fib1)

        # mdc() MAC0110
        d_mdc, t_mdc = execute(mdc, fib0, fib1)

        # mostre resultados
        print(f"{fib0:10} {fib1:10} {t_gcd:8.2f}   {t_euclides:8.2f} {t_mdc:10.2f}")

        # proximos valores
        fib0, fib1 = fib1, fib0+fib1
    

#-------------------------------------------              
def execute(f, m, n):
    '''(callable, int, int) -> int, float
    Executa f(m,n).
    RETORNA valor retornado por f() e tempo gasto.
    '''
    inicio = time.time()
    d = f(m, n)
    fim = time.time()
    elapsed = fim-inicio
    return d, elapsed      
              

#-----------------------------------------
def mdc(m, n):
    """ (int, int) -> int
    RECEBE dois inteiros m e n.
    RETORNA o mdc de m e n.
    
    Se m = 0 = n retorna 0 indicando erro.
    """
    if n <  0: n = -n    
    if m <  0: m = -m
    if m > n: n, m = m, n
    if n == 0: return m
    d = n
    while m%d != 0 or n%d != 0:
        d -= 1
    return d

#-----------------------------------------
def euclides(m,n):
    """ (int, int) -> int
    RECEBE dois inteiros m e n.
    Retorna o mdc de m e n.
    
    Se m = 0 = n retorna 0 indicando erro.
    """
    if n <  0: n = -n    
    if m <  0: m = -m
    if n == 0: return m
    return euclidesI(m, n) # mude para euclidesR() se desejar

#-----------------------------------------
def euclidesI(m, n):
    """ (int, int) -> int
    RECEBE dois inteiros m e n.
    RETORNA o mdc de m e n.
    
    PRÉ-CONDIÇÃO: m >= 0 e  n > 0
    """
    r = m%n
    while r != 0:
        m = n
        n = r
        r = m % n
    return n

#-----------------------------------------
def euclidesR(m, n):
    """ (int, int) -> int
    RECEBE dois inteiros m e n.
    Retorna o mdc de m e n.
    
    PRÉ-CONDIÇÃO: m >= 0, n >=0
    """
    if n == 0: return m
    return euclidesR(n, m%n)

if __name__ == "__main__":
    main()
