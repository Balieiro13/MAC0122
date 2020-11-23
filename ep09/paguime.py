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

        Minha colega Maria me explicou que eu devia utilizar a função int() 
        quando fazemos leitura de números inteiros.

        No fórum escreveram para usar a função ...

        A minha solução foi baseada na descrição encontrada na 
        página https://stackoverflow.com/questions/15976333/

    Descrição de ajuda ou indicação de fonte:
'''
import numpy as np
#------------------------------------------------------------
class Paguime:
    ''' Recebe um array com pares (fcoin, quantidade) indicando
        o tipo e quantidade disponíveis de cada fcoin e atende os 
        pagamentos quando possível.
    '''

    def __init__(self, saldo):
        self.saldo = saldo
        self.valor = saldo[:,0]
        self.quant = saldo[:,1]
        self.cache = self.valor.copy()
        self.pay = np.zeros(self.valor.size, int)

    def __str__(self):
        s = str(self.saldo)
        return s

    def pague(self, valor):

        if valor == 0 and np.all(self.pay ==0):
            return np.vstack((self.valor, self.pay)).T
        if valor == 0: return None

        if valor in self.valor:
            c = np.where(self.cache == valor)
            if self.quant[c[0][0]] != 0:
                self.quant[c[0][0]] -= 1
                self.pay[c[0][0]] += 1
                sharingan = self.pay.copy()
                self.pay *= 0
                return np.vstack((self.valor, sharingan)).T
            else:
                self.cache[c[0][0]] = 0

        n = np.where(np.logical_and(self.cache < valor, self.quant > 0))
        self.quant[n[0][0]] -= 1
        self.pay[n[0][0]] += 1
        return self.pague(valor%self.valor[n[0][0]])


