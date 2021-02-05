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

    Descrição de ajuda ou indicação de fonte:

'''

#-----------------------------------------------------------------
class Grafo:
    def __init__(self, graph=None, sep=' '):
        self.nodes           = []
        self.graph           = {}
        self.number_of_edges = 0

        if graph != None:
            if graph.endswith('.txt'):
                t = open('./'+graph)
                graph = t.read()

            edge = list(filter(lambda e: e != '', graph.split('\n')))

            for line in edge:
                nodes = line.split(sep)
                for vtx in range(1,len(nodes)):
                    self.insira_aresta(nodes[0], nodes[vtx])


    def __str__(self):
        s = ''
        vertices = sorted(self.nodes)
        for node in vertices:
            s += f'{node} | '
            edges = sorted(self.graph[node])
            for i in range(len(edges) - 1):
                s += f'{edges[i]}, '
            s+= edges[-1] + '\n'
        return s


    def insira_aresta(self, node1, node2):
        if node1 == '' or node2 == '':
            return    
        node1 = node1.strip()        
        node2 = node2.strip()        

        try:
            if node2 not in self.graph[node1]:
                self.graph[node1].append(node2)
                self.number_of_edges += 1
        except KeyError:
                self.graph[node1] = [node2]
                self.nodes.append(node1)
                self.number_of_edges += 1

        try:
            if node1 not in self.graph[node2]:
                self.graph[node2].append(node1)
        except KeyError:    
            self.graph[node2] = [node1]
            self.nodes.append(node2)
        

    def tem_vertice(self, node):
        return node in self.nodes
    
    def V(self):
        return len(self.nodes)

    def A(self):
        return self.number_of_edges

    def vertices(self):
        return sorted(self.nodes)
    
    def adjacentes(self, node):
        return sorted(self.graph[node])
    
    def grau(self, node):
        return len(self.graph[node])
    
    def tem_aresta(self, node1, node2):
        return node2 in self.graph[node1]