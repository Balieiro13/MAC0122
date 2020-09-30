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
        imagem = np.array([[val] * ncols] * nlins)

        if type(val) == int or type(val) == float:
            self.img = imagem
        else:
            self.img = np.copy(val)
        if type(val) == type(imagem):
            self.nlins, self.ncols = self.img.shape
        else:
            self.nlins = nlins
            self.ncols = ncols

        self.val = val
        self.shape = self.img.shape

    def __str__(self):
        s = ''
        for i in self.img:
            s += f'{str(i)[1:-1]} \n'
        return s

    def __getitem__(self, item):
        return self.img[item]

    def __setitem__(self, key, value):
        self.img[key] = value
        return None

    def __add__(self, other):
        soma = self.img + other.img
        return NumPymagem(0,0,soma)

    def __mul__(self, other):
        mult =  self.img * other
        return NumPymagem(0,0,mult)

    def __rmul__(self, other):
        return self*other

    def crop(self, left=0, top=0, right=0, bottom=0):
        if right == 0:
            right = self.ncols
        if bottom == 0:
            bottom = self.nlins

        sharingan = np.copy(self.img[top:bottom, left:right])

        return NumPymagem(0,0,sharingan)

    def paste(self, imgn, tlin, tcol):
        mlin = min(self.nlins, imgn.nlins + tlin)
        mcol = min(self.ncols, imgn.ncols + tcol)

        if tlin < 0:
            imgn = imgn.crop(0,-tlin,0,0)
        if tcol < 0:
            imgn = imgn.crop(-tcol,0,0,0)

        a,b = 0,0

        for i in range(max(0,tlin), mlin):
            for j in range(max(0,tcol), mcol):
                self[i,j] = imgn[a,b]
                b+=1
            b=0
            a+=1

        return None

    def pinte_disco(self, val, raio, clin, ccol):
        quad_circ = NumPymagem(2 * raio + 1, 2 * raio + 1)

        for i in range(len(quad_circ.img)):
            for j in range(len(quad_circ.img[i])):
                if (i + 1 - (raio + 1)) ** 2 + (j + 1 - (raio + 1)) ** 2 < (raio) ** 2:
                    quad_circ[i, j] = 1

        self.paste(quad_circ, (clin - raio), (ccol - raio))

        for i in range(len(self.img)):
            for j in range(len(self.img[i])):
                if self[i,j] == 0:
                    if type(self.val) == type(self.img):
                        self[i, j] = self.val[i, j]
                    else:
                        self[i,j] = self.val
                if self[i,j] == 1:
                    self[i, j] = val
        return None

    def pinte_retangulo(self, val, left, top, right, bottom):
        retang = NumPymagem(bottom - top, right - left, val)
        self.paste(retang, top, left)

        return None



