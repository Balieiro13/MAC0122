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
    
    def __str__(self):
        return str(self.data)
    
    def is_open(self, lin, col):
        return self.data[lin, col] == OPEN
    
    def is_full(self, lin, col):
        return self.date[lin, col] == FULL
    
    def percolates(self):
        for i in self.data[-1]:
            if i == FULL: return True
    
    def no_open(self):
        sum = 0
        for i in np.reshape(self.data, self.data.size):
            if i == OPEN:
                sum += 1
        return sum

    def open(self, lin, col):
        if self.data[lin, col] == BLOCKED:
            self.data[lin, col] = 1
        return None
    
    def get_grid(self):
        return self.data

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
  
    while not q.vazio():
        i = q.get()
        for j in range(n):
            if rede[i][j] == 1 and d[j] > d[i]+1:
                d[j] = d[i]+1
                q.put(j)
    return d