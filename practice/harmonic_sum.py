#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 10:12:34 2020

@author: balieiro
"""


def MDC(n,m):
    while m!= 0:
        r = n % m
        n = m
        m = r
    return n
    
    
def simplifique (n,m):
    div = MDC(n,m)
    
    return (n//div,m//div)

''' soma de harmônicos '''

def soma_frac(n1,d1,n2,d2):
    
    fracn = d2*n1 + d1*n2
    fracd = d1*d2
    return simplifique(fracn, fracd)

def soma_har(n):
    s = (1, 1)
    for i in range(2, n+1):
        s = soma_frac(s[0], s[1], 1, i )
    return simplifique(s[0],s[1])


def harm(n):
    summ = soma_har(n)
    
    return summ[0]/summ[1]
    