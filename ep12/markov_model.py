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
    monitores e colegas). Com exceção de material de MAC0110, caso
    você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na 
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte:

'''
from itertools import product

class MarkovModel:
    def __init__(self, k, s):
        self.corpus = s
        self.K = k
        self.alpha = letra(s)

        self.k_model = {''.join(p) : self.N(''.join(p)) 
                for p in product(self.alpha, repeat = k) 
                if self.N(''.join(p)) != 0}

        self.k1_model = {''.join(p) : self.N(''.join(p)) 
                for p in product(self.alpha, repeat = k+1) 
                if self.N(''.join(p)) != 0}

    def __str__(self): 
        s = f"alfabeto tem {len(self.alpha)} símbolos\n"
        for i,j in self.k_model.items():
            s += f"'{i}'" + '\t' + str(j) + '\n'
        for k,l in self.k1_model.items():
            s += f"'{k}'" + '\t' + str(l) + '\n'
        return s

    def alphabet(self):
        s = ''.join(self.alpha)
        return s

    def N(self, t):
        s = self.corpus
        if (len(t) > 0):
            s += s[:len(t) - 1]
        ans = sum (1 for i in range(len(s))
                if s.startswith(t, i))
        return ans

    def laplace(self, t):
        lap = (self.N(t) + 0.5) / (self.N(t[:-1]) + (0.5*len(self.alpha)))
        return lap
        

#########################################################################################################################

def letra(s):
    '''recebe uma (str) e retorna uma 
    (list) com os chars sem repetição'''
    alfa = set()
    for i in s:
        item = i
        alfa.add(item)
    lst = list(alfa)
    lst.sort()
    return lst
