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

    def __init__(self, nlins, ncols, val):
        imagem = np.array([[val] * ncols] * nlins)

        if type(val) == int or type(val) == float:
            self.img = imagem
        else:
            self.img = val
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

        recorte = self.img[top:bottom, left:right]

        return NumPymagem(0,0,recorte)

    #def paste(self, img, tlin, tcol):


