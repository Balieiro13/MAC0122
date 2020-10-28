# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
# NÃO INCLUA NENHUM import ...
#------------------------------------------------------------------

'''

    Nome: André Balieiro
    NUSP: 9365810

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa (EP)
    foram desenvolvidas e implementadas por mim e que portanto não 
    constituem desonestidade acadêmica ou plágio.
    Declaro também que sou responsável por todas as cópias desse
    programa e que não distribui ou facilitei a sua distribuição.
    Estou ciente que os casos de plágio e desonestidade acadêmica
    serão tratados segundo os critérios divulgados na página da 
    disciplina.
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
    assim, poderão ser punidos por desonestidade acadêmica.

    Abaixo descreva qualquer ajuda que você recebeu para fazer este
    EP.  Inclua qualquer ajuda recebida por pessoas (inclusive
    monitores e colegas). Com exceção de material de MAC0110 ou MAC0122, 
    caso  você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na 
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte:

'''
from percolation import Percolation
from itertools import product
import numpy as np
import random
import math
                 
class PercolationStats:
    def __init__(self, shape, T):
        if type(shape) == int:
            self.shape = (shape,shape)
        if type(shape) == tuple:
            self.shape = shape
        self.T = T
        self.exper = []
        for i in range(T):
            self.test()

    def test(self):
        m = max(self.shape)
        rand = list(product(range(m), repeat =2))
        random.shuffle(rand)
        perco = Percolation(self.shape)
        for i in rand:
            l,c = i
            if not (perco.percolates()):
                try:
                    perco.open(l,c)
                except IndexError:
                    pass
        self.exper.append(perco)
        return None

    def no_abertos(self):
        T = self.T
        arr = np.array([0]*T)
        for i in range(T):
            arr[i] = self.exper[i].no_open()
        return arr
    
    def mean(self):
        mean_arr = np.array([self.no_abertos()])
        mean_arr = mean_arr / (self.shape[0]*self.shape[1])
        media = mean_arr.mean()
        return media

    def stddev(self):
        std = np.array([self.no_abertos()])
        std = std / (self.shape[0]*self.shape[1])
        stddev = std.std(ddof=1)
        return stddev

    def confidenceLow(self):
        mean = self.mean()
        std = self.stddev()
        raizT = math.sqrt(self.T)
        cLow = mean - (std/raizT)
        return cLow

    def confidenceHigh(self):
        mean = self.mean()
        std = self.stddev()
        raizT = math.sqrt(self.T)
        cHigh = mean + (std/raizT)
        return cHigh

