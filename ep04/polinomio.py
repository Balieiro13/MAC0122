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

        Encontrei a funcão "enumerate()" que não conhecia para fazer a multiplicaćão de
        polinômios na página "https://stackoverflow.com/questions/5413158/multiplying-polynomials-in-python"

'''
class Polinomio:

    def __init__(self, coefs):
        coefs = tiraz(coefs)
        if coefs == None:
            coefs = [0]
        self.coefs = coefs[:]
        self.gral = len(coefs)-1

    def __str__(self):
        co = self.coefs
        str = ''
        sig = ['+','-' ]
        for i in range(len(co)):
            if co[i] >= 0:
                s = sig[0]
            else:
                s = sig[1]
            str +=  s + f' {abs(co[i])}*x^{i} '

        return str

    def __eq__(self, other):
        if isinstance(other, Polinomio):
            return self.coefs == other.coefs
        else:
            return len(self.coefs) == 1 and self.coefs[0] == other


    def __call__(self, args):
        result = 0
        for i in range (self.gral +1):
            result += self.coefs[i]*(args**i)

        return result


    def __add__(self, other):
        padd = [0]*(self.gral+1)

        if type(other) == int or type(other) == float:
            padd = self.coefs[:]
            padd[0] += other
            return Polinomio(padd)

        if self.gral < other.gral:
            return other.__add__(self)

        cother = other.coefs[:]
        for i in range(len(self.coefs)):
            cother.append(0)
            padd[i] = self.coefs[i] + cother[i]

        return Polinomio(padd)

    def __sub__(self, other):
        if type(other) == int or type(other) == float:
           return self + (other *-1)
        if self == other:
            return 0

        cother = [-i for i in other.coefs]

        return self + Polinomio(cother)


    def __rsub__(self, other):
        return (-1)*self + other

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        pmul = [0]*(self.gral+1)

        if type(other) == int or type(other) == float:
            for i in range(len(self.coefs)):
                pmul[i] = self.coefs[i]* other
            return Polinomio(pmul)

        pxp = [0]*(self.gral + other.gral + 1)
        for i1,i2 in enumerate(self.coefs):
            for j1,j2 in enumerate(other.coefs):
                pxp[i1+j1] += i2*j2
        return Polinomio(pxp)


    def __rmul__(self, other):
        return self * other


    def derive(self):
        derivado = [0]*(self.gral+1)
        for i in range(self.gral):
            derivado[i] = self.coefs[i+1]*(i+1)

        return Polinomio(derivado)

    def grau(self):             #não entendi pra que esse método
        return self.gral

    def coeficientes(self):         #nem esse.
        coeficiente = self.coefs[:]
        return coeficiente


'''
Funćões auxiliares
'''

def tiraz(lis):
    for i in range(len(lis)-1, -1, -1):
        if lis[i] !=0 :
            return lis[:i+1]