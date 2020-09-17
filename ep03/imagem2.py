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

#-------------------------------------------------------------------------- 

class Imagem:
    '''
    Implementação da classe Imagem que tem o mesmo comportamento descrito 
    no enunciado.
    '''

    # COPIE AQUI OS MÉTODOS DO EP02
    def __init__(self, nlin, ncol, valor=0):
        self.nlin = nlin
        self.ncol = ncol
        self.valor = valor
        self.img = [[self.valor for i in range(self.ncol)] for i in range(self.nlin)]

    def __str__(self):
        s = ''
        for i in self.img:
            s += f'{str(i)[1:-1]} \n'
        return s

    def size(self):
        return (self.nlin, self.ncol)

    def get(self, lin, col):
        return self.img[lin][col]

    def put(self, lin, col, val):
        self.img[lin][col] = val
        return None

    def crop(self, left=0, top=0, right=0, bottom=0):
        if right == 0:
            right = self.ncol
        if bottom == 0:
            bottom = self.nlin

        a = 0
        recorte = Imagem(bottom - top, right - left)

        for i in range(top, bottom):
            recorte.img[a] = self.img[i][left:right]
            a += 1
        return recorte

    # escreva aqui os NOVOS métodos da classe Imagem que fazem parte do EP03

    def __add__(self, other):
        imgsoma = Imagem(self.nlin, self.ncol)

        for i in range(len(self.img)):
            for j in range(len(self.img[i])):
                imgsoma.put(i, j, self.img[i][j] + other.img[i][j])

        return imgsoma

    def __mul__(self, other):
        other = float(other)
        imgmult = Imagem(self.nlin, self.ncol)

        for i in range(len(self.img)):
            for j in range(len(self.img[i])):
                imgmult.put(i,j, self.img[i][j]*other)

        return imgmult

    def __rmul__(self, other):
        return self * other

    def paste(self, imgn, tlin, tcol):
        mlin = max(self.nlin, imgn.nlin)
        mcol = max(self.ncol, imgn.ncol)
        tlin += mlin
        tcol+= mcol

        if tlin + imgn.nlin < mlin or 2*mlin < tlin:
            return None
        if tcol + imgn.ncol < mcol or 2*mcol < tcol:
            return None

        inula = Imagem(3*mlin, 3*mcol)
        a,b,c,d = 0,0,0,0

        for i in range(mlin, mlin+self.nlin):
            for j in range(mcol, mcol+self.ncol):
                inula.put(i,j, self.img[a][b])
                b+=1
            b=0
            a+=1


        for i in range(tlin, (tlin+imgn.nlin)):
            for j in range(tcol, (tcol+imgn.ncol)):
                inula.put(i, j, imgn.img[c][d])
                d+=1
            d=0
            c+=1

        final = inula.crop(mcol, mlin, mcol + self.ncol, mlin + self.nlin)
        self.img = final.img

        return None
