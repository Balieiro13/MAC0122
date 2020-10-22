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
    monitores e colegas). Com exceção de material de MAC0110 e MAC0122, 
    caso você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na 
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte:

'''
import numpy as np
from queue import Queue

#-------------------------------------------------------------------------- 
# constantes
BLOCKED = 0  # sítio bloqueado
OPEN    = 1  # sítio aberto
FULL    = 2  # sítio cheio

class Percolation:
    '''
    Representa uma grade com todos os sítios inicialmente bloqueados.
    '''
    def __init__(self, shape):
        if type(shape) == int:
            self.shape = (shape,shape)
            self.data = np.array([[0]*shape]*shape)
        if type(shape) == tuple:
            self.shape=shape
            self.data = np.array([[0]*shape[1]]*shape[0])
        self.rede = [[0 for i in range(self.data.size)] for i in range(self.data.size)]
    
    def __str__(self):
        return str(self.data)
    
    def is_open(self, lin, col):
        return self.data[lin, col] == OPEN or self.data[lin, col] == FULL
    
    def is_full(self, lin, col):
        return self.data[lin, col] == FULL
    
    def percolates(self):
        if FULL in self.data[-1]:
            return True
        return False
    
    def no_open(self):
        sum = 0
        for i in np.reshape(self.data, self.data.size):
            if i == OPEN or i == FULL:
                sum += 1
        return sum

    def open(self, lin, col):
        if self.data[lin, col] == BLOCKED:
            if lin == 0:
                self.data[lin, col] = FULL
                return None
            self.data[lin, col] = OPEN
        
        for i in range(self.shape[0]):
            for j in range(self.shape[1]-1):
                if self.is_open(i,j) and self.is_open(i,j+1):
                    self.rede[i*self.shape[1] + j][i*self.shape[1] + j+1] = 1
                    self.rede[i*self.shape[1] + j+1][i*self.shape[1] + j] = 1

        for i in range(self.shape[0]-1):
            for j in range(self.shape[1]):
                if self.is_open(i,j) and self.is_open(i+1,j):
                    self.rede[i*self.shape[1] + j][(i+1)*self.shape[1] + j] = 1
                    self.rede[(i+1)*self.shape[1] + j][i*self.shape[1] + j] = 1
         
        d = distancia(lin*self.shape[1] + col, self.rede)
        for i in range(self.shape[1]):
            if d[i] != self.data.size and d[i] != 0:
                for i in range(self.data.size):
                    if d[i] != self.data.size:
                        self.data[i//self.shape[1], i%self.shape[1]] = FULL
                        
        return None
    
    def get_grid(self):
        return self.data.copy()

#-------------------------------------------------------------------------- 
# funções auxiliares

def distancia(c, rede):
    n = len(rede)
  
    # inicia queue
    q = Queue()
    q.put(c)
 
    # inicia dist
    d = [n] * n
    d[c] = 0
  
    while not q.empty():
        i = q.get()
        for j in range(n):
            if rede[i][j] == 1 and d[j] > d[i]+1:
                d[j] = d[i]+1
                q.put(j)
    return d