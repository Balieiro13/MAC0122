# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
# NÃO INCLUA NENHUM OUTRO import ...
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
    monitores e colegas). Com exceção de material de MAC0122, caso
    você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função
        split(), strip(), map() e filter() para leitura dos dados
        no arquivo.

    Descrição de ajuda ou indicação de fonte:

'''

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.rating = []

    def __str__(self):
        l = self.rating
        s = self.nome + "\n"
        for i in range(len(l)):
            s += f"{i}: {l[i]} \n"
        return s

    def get_nome(self):
        return self.nome

    def put_classificacao(self, filmes):
        self.rating = filmes[:]

    def get_classificacao(self):
        return self.rating[:]

    def distancia(self, other):
        selfcp = self.get_classificacao()
        othercp = other.get_classificacao()
        selfcp = [i for i in selfcp if i in othercp]
        if (len(othercp) < 3):
            return None
        othercp = [i for i in othercp if i in selfcp]
        whr = where(othercp, selfcp)
        d = insertSort(whr)
        return d

################################ funções auxiliares #########################################

def insertSort(arr):
    d = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while (j >= 0 and arr[j] > key):
            arr[j + 1] = arr[j]
            j -= 1
            d += 1
        arr[j + 1] = key
    return d

def where(v, w):
    whr =[]
    for i in range(len(w)):
        for j in range(len(w)):
            if (v[i] == w[j]):
                whr.append(j)
    return whr
