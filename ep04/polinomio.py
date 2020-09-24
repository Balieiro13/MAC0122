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
class Polinomio:

    def __init__(self, coefs):
        self.coefs = coefs
        self.grau = len(coefs)-1

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

    def __add__(self, other):
        padd = Polinomio([0 for i in range(len(self.coefs))])
        if type(other) == int or type(other) == float:
            padd.coefs = self.coefs[:]
            padd.coefs[0] += other
            return padd

        if len(self.coefs)<len(other.coefs):
            return self.__radd__(other)

        cother = other.coefs[:]

        for i in range(len(self.coefs)):
            cother.append(0)
            padd.coefs[i] = self.coefs[i] + cother[i]
        return padd

    def __radd__(self, other):
        return other + self

    def __mul__(self, other):
        pmul = Polinomio([0 for i in range(len(self.coefs))])
        if type(other) == int or type(other) == float:
            for i in range(len(self.coefs)):
                pmul.coefs[i] = self.coefs[i]* other
            return pmul
        

    def __rmul__(self, other):
        return other*self