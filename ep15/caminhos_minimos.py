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

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na 
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

        Minha colega Maria me explicou o funcionamente da busca em largura.

    Descrição de ajuda ou indicação de fonte:

'''

from grafo import Grafo

# pode ser utilizado para clonar o grafo dado: grafo = copy.deepcopy(grafo_dado)
import copy 

class Caminhos_Minimos:
    def __init__(self, graph, orig):
        if orig not in graph.vertices():
            print(f"Caminhos.__init(): '{orig}' não é vertice do grafo")
            return
        
        self.orig = orig
        self.distance, self.previous = ssspp(graph=graph, orig=orig)

    def __str__(self):
        s = ''
        for node in self.distance.keys():
            s += f'{node}: ' + str(self.distancia(node)) + \
                ", " + str(self.anterior(node)) + '\n'
        return s

    def distancia(self, node):
        return self.distance[f'{node}']
    
    def anterior(self, node):
        return self.previous[f'{node}']
    
    def caminho(self, node):
        path = [node]
        p = self.anterior(node)
        while p != None:
            path.append(p)
            p = self.anterior(p)
        return path[::-1]
            


#---------------------------------aux-----------------------------------#

def ssspp(graph, orig):
    q = []
    d = {}
    prev = {}
    
    for i in graph.vertices(): 
        d[f'{i}']    = graph.V()
        prev[f'{i}'] = None

    d[f'{orig}']    = 0

    q.append(orig)
    while len(q) != 0:
        i = q.pop(0)
        edges = graph.adjacentes(i)
        for node in edges:
            if d[f'{node}'] > d[f'{i}'] + 1:
                prev[f'{node}'] = i
                d[f'{node}']    = d[f'{i}'] + 1
                q.append(node)
    return d, prev
    