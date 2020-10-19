# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
#------------------------------------------------------------------

'''

    Nome: André Balieiro Pereira da Silva
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
import random
from numpymagem import NumPymagem
from numpymutil import mostre_video
from numpymutil import salve_video

# Escreva aqui outras constantes que desejar
ALTURA  = 240  
LARGURA = 300
BLACK = 0
WHITE = 250

#-------------------------------------------------------------------------- 

def main():
    ''' (None) -> None
    Escreva o seu programa que cria o vídeo como descrito no enunciado.
    
    O código abaixo serve para ilustrar como usar a função mostre_video()
    que recebe uma lista com NumPymagens e as mostra em um vídeo na tela
    do seu computador usando PyGame. Por isso lembre-se de seguir as 
    instruções para instalar PyGame no seu computador.

    Remova ou altere o código para gerar o seu próprio vídeo. Não se esqueça
    de criar funções para facilitar o entendimento do seu vídeo.

    Você pode (mas não precisa!) salvar o seu vídeo em um formato mp4, para
    mostrar sua obra no fórum da disciplina. Para isso, antes de salvar, 
    você deve instalar o software ffmpeg que você pode baixar de 
    https://ffmpeg.org/download.html. 
    '''
    
    video = []
    preto = NumPymagem(ALTURA, LARGURA, BLACK)    
    branco = NumPymagem(ALTURA, LARGURA, WHITE)
    print(f"Está compatível com numpymutil: {type(preto.data) is np.ndarray}")
    cor = BLACK
    dcor = WHITE
    
    D1 = randisco(ALTURA, LARGURA)
    D2 = randisco(ALTURA, LARGURA)

    
    for i in range(120):
        D1['vetor'] = change_vetor(D1['raio'], D1['lin'], D1['col'], LARGURA, ALTURA, D1['vetor'])
        D2['vetor'] = change_vetor(D2['raio'], D2['lin'], D2['col'], LARGURA, ALTURA, D2['vetor'])
        preto = NumPymagem(ALTURA, LARGURA, BLACK)

        D1['lin'], D1['col'] = soma_vetor(D1['lin'], D1['col'], D1['vetor'])
        D2['lin'], D2['col'] = soma_vetor(D2['lin'], D2['col'], D2['vetor'])

        preto.pinte_disco(WHITE, D1['raio'], D1['lin'], D1['col'])
        preto.pinte_disco(WHITE, D2['raio'], D2['lin'], D2['col'])
        video.append(preto)

    while cor < WHITE:  
        D1['vetor'] = change_vetor(D1['raio'], D1['lin'], D1['col'], LARGURA, ALTURA, D1['vetor'])
        D2['vetor'] = change_vetor(D2['raio'], D2['lin'], D2['col'], LARGURA, ALTURA, D2['vetor'])

        cor +=1
        dcor = (dcor-1)%WHITE
        cinza = NumPymagem(ALTURA, LARGURA, cor)

        D1['lin'], D1['col'] = soma_vetor(D1['lin'], D1['col'], D1['vetor'])
        D2['lin'], D2['col'] = soma_vetor(D2['lin'], D2['col'], D2['vetor'])

        cinza.pinte_disco(dcor, D1['raio'], D1['lin'], D1['col']) 
        cinza.pinte_disco(dcor, D2['raio'], D2['lin'], D2['col']) 

        video.append(cinza)

    for i in range(120): 
        D1['vetor'] = change_vetor(D1['raio'], D1['lin'], D1['col'], LARGURA, ALTURA, D1['vetor'])
        D2['vetor'] = change_vetor(D2['raio'], D2['lin'], D2['col'], LARGURA, ALTURA, D2['vetor'])
        branco = NumPymagem(ALTURA, LARGURA, WHITE)

        D1['lin'], D1['col'] = soma_vetor(D1['lin'], D1['col'], D1['vetor'])
        D2['lin'], D2['col'] = soma_vetor(D2['lin'], D2['col'], D2['vetor'])

        branco.pinte_disco(BLACK, D1['raio'], D1['lin'], D1['col'])
        branco.pinte_disco(BLACK, D2['raio'], D2['lin'], D2['col'])
        video.append(branco)

    while cor > BLACK:
        D1['vetor'] = change_vetor(D1['raio'], D1['lin'], D1['col'], LARGURA, ALTURA, D1['vetor'])
        D2['vetor'] = change_vetor(D2['raio'], D2['lin'], D2['col'], LARGURA, ALTURA, D2['vetor'])
        cor -= 1
        dcor = (dcor+1)%WHITE
        cinza = NumPymagem(ALTURA, LARGURA, cor)
        
        D1['lin'], D1['col'] = soma_vetor(D1['lin'], D1['col'], D1['vetor'])
        D2['lin'], D2['col'] = soma_vetor(D2['lin'], D2['col'], D2['vetor'])

        cinza.pinte_disco(dcor, D1['raio'], D1['lin'], D1['col'])
        cinza.pinte_disco(dcor, D2['raio'], D2['lin'], D2['col'])
        video.append(cinza)

    for i in range (160):
        D1['vetor'] = change_vetor(D1['raio'], D1['lin'], D1['col'], LARGURA, ALTURA, D1['vetor'])
        D2['vetor'] = change_vetor(D2['raio'], D2['lin'], D2['col'], LARGURA, ALTURA, D2['vetor'])
        preto = NumPymagem(ALTURA, LARGURA, BLACK)

        D1['lin'], D1['col'] = soma_vetor(D1['lin'], D1['col'], D1['vetor'])
        D2['lin'], D2['col'] = soma_vetor(D2['lin'], D2['col'], D2['vetor'])

        preto.pinte_disco(WHITE, D1['raio'], D1['lin'], D1['col'])
        preto.pinte_disco(WHITE, D2['raio'], D2['lin'], D2['col'])
        video.append(preto)


    mostre = False
    if mostre:
        mostre_video(video)

    salve = True
    if salve:
        print("Salvando vídeo")
        salve_video(video)
#-------------------------------------------------------------------------- 
#
# ESCREVA OUTRAS FUNÇÕES E CLASSES QUE DESEJAR
#
#-------------------------------------------------------------------------- 
def change_vetor(raio, lin, col, larg, alt, vetor):
    if col + raio >= larg:
        vetor[1] *= -1
    if col - raio <= 0:
        vetor[1] *= -1
    if lin + raio >= alt:
        vetor[0] *= -1
    if lin - raio <= 0:
        vetor[0] *= -1
    return vetor

def randisco(ALT,LARG):
    raio = random.randint(5,10)
    lin = random.randint(raio, ALT - raio)
    col = random.randint(raio, LARG - raio)
    vetor = [1 + random.random(), 1+ random.random()]
    valores = {'raio':raio, 'lin':lin, 'col':col, 'vetor':vetor}
    return valores

def soma_vetor(lin, col, vetor):
    return [lin+vetor[0], col+vetor[1]]


#-------------------------------------------------------------------------- 
if __name__ == '__main__':
    main()
