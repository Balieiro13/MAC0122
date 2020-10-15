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
import numpy as np

#-------------------------------------------------------------------------- 

class NumPymagem:
    '''
    Implementação da classe NumPymagem que tem o mesmo comportamento descrito 
    no enunciado.
    '''

    # escreva aqui os métodos da classe Pymagem

    def __init__(self, nlins, ncols, val=0):
        valores =[[val] * ncols] * nlins
        imagem = np.array(valores)

        if type(val) == int or type(val) == float:
            self.data = imagem
        else:
            self.data = np.copy(val)
        if type(val) == type(imagem):
            self.nlins, self.ncols = self.data.shape
        else:
            self.nlins = nlins
            self.ncols = ncols

        self.val = val
        self.shape = self.data.shape
        self.str = [list(i) for i in self.data]

    def __str__(self):
        s = ''
        for i in self.data:
            s += f'{str((i))[1:-1]} \n'
        return s

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value
        return None

    def __add__(self, other):
        soma = self.data + other.data
        return NumPymagem(0,0,soma)

    def __mul__(self, other):
        mult =  self.data * other
        return NumPymagem(0,0,mult)

    def __rmul__(self, other):
        return self*other

    def crop(self, left=0, top=0, right=0, bottom=0):
        if right == 0:
            right = self.ncols
        if bottom == 0:
            bottom = self.nlins

        sharingan = np.copy(self.data[top:bottom, left:right])

        return NumPymagem(0,0,sharingan)

    def paste(self, imgn, tlin, tcol):
        mlin = min(self.nlins, imgn.nlins + tlin)
        mcol = min(self.ncols, imgn.ncols + tcol)
        slin = max(0,tlin)
        scol = max(0,tcol)
        array = np.copy(imgn.data)
        if tlin < 0:
            if imgn.nlins + tlin <=0:
                return None
            array = np.delete(array, np.s_[:-tlin],0)
            array = np.delete(array, np.s_[self.nlins:], 0)
        if tcol <0:
            if imgn.ncols +tcol <=0:
                return None
            array = np.delete(array, np.s_[:-tcol],1)
            array = np.delete(array, np.s_[self.ncols:],1)

        if tlin > self.nlins or tcol > self.ncols:
            return None
        
        

        self[slin:mlin, scol:mcol] = array[:self.nlins - tlin, :self.ncols - tcol]

        return None

    def pinte_disco(self, val, raio, clin, ccol):
        for i in range(self.nlins):
            for j in range(self.ncols):
                if (i-clin)**2 + (j-ccol)**2 - raio**2 < 0:
                    self[i,j] = val
        return None

    def pinte_retangulo(self, val, left, top, right, bottom):
        retang = NumPymagem(bottom - top, right - left, val)
        self.paste(retang, top, left)

        return None
