# -*- coding: utf-8 -*-
#-----------------------------------------------------------
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.rating = []

    def __str__(self):
        l = self.rating
        s = self.nome + "\n"
        for i in range(len(l)):
            s += f"{i}: {l[i]} \n"
        return s

    def get_nome(self):
        return self.nome

    def put_classificacao(self, filmes):
        self.rating = filmes[:]

    def get_classificacao(self):
        return self.rating[:]

    def distancia(self, other):
        whr = where(self.get_classificacao(), other.get_classificacao())
        if (len(whr) < 3):
            return None
        d = insertSort(whr)
        return d

    def distanciaY(self, other):
        whr = where(self.get_classificacao(), other.get_classificacao())
        if (len(whr) < 3):
            return None
        d = mergesortX(whr)
        return d

    def distanciaX(self, other):
        whr = self.em_comum(other)
        if (len(whr) < 3):
            return None
        return mergesortX(whr, 0, len(whr))

    def em_comum(self, other):
        indice = whereX(self.get_classificacao(), other.get_classificacao())
        return indice

###################################funções auxiliares##################################
#-------------------------------------------------------------------
def mergeX(v, e, m, d):
    n = d - e
    w = [0]*n
    k, i, j = 0, e, m
    cont = 0
    while (i < m and j < d):
        if (v[i] < v[j]):
            w[k] = v[i]
            i += 1
        else:
            w[k] = v[j]
            j += 1
            cont += m - i
        k += 1
    if (i < m):
        w[k:] = v[i:m]
    else:
        w[k:] = v[j:d]
    v[e:d] = w

    return cont

def mergesortX(v, e=None, d=None):
    c = 0
    if (e is None):
        e = 0
    if (d is None):
        d = len(v)
    if (e < d - 1):
        m = (e + d) // 2
        c += mergesortX(v, e, m)
        c += mergesortX(v, m, d)
        c += mergeX(v, e, m, d)

    return c

def insertSort(arr):
    d = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while (j >= 0 and arr[j] > key):
            arr[j + 1] = arr[j]
            j -= 1
            d += 1
        arr[j + 1] = key
    return d

def ltodi(v):
    ind = {v[i] : i for i in range(len(v))}
    return ind

def whereX(v, w):
    dv = ltodi(v)
    whr = []
    for i in w:
        x = dv.get(i)
        if x != None:
            whr.append(dv[i])
    return whr

def where(w, v):
    whr =[]
    for i in range(len(v)):
        for j in range(len(w)):
            if (v[i] == w[j]):
                whr.append(j)
    return whr

