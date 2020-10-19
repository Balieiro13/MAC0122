# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
#------------------------------------------------------------------

'''

    Nome:
    NUSP:

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
ALTURA  = 120
LARGURA = 160
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

    video.append(preto)
    while cor < WHITE:  
        D1['vetor'] = change_vetor(D1['raio'], D1['lin'], D2['col'], LARGURA, ALTURA, D1['vetor'])

        cor +=1
        dcor = (dcor-1)%WHITE
        cinza = NumPymagem(ALTURA, LARGURA, cor)

        D1['lin'] += D1['vetor'][0]
        D1['col'] += D1['vetor'][1]

        cinza.pinte_disco(dcor, D1['raio'], D1['lin'], D1['col']) 

        video.append(cinza)

    for i in range(60): # mostra 2s de fundo branco
        D1['vetor'] = change_vetor(D1['raio'], D1['lin'], D2['col'], LARGURA, ALTURA, D1['vetor'])
        branco = NumPymagem(ALTURA, LARGURA, WHITE)
        D1['lin'] += D1['vetor'][0]
        D1['col'] += D1['vetor'][1]

        branco.pinte_disco(BLACK, D1['raio'], D1['lin'], D1['col'])
        video.append(branco)

    while cor > BLACK:
        D1['vetor'] = change_vetor(D1['raio'], D1['lin'], D2['col'], LARGURA, ALTURA, D1['vetor'])
        cor -= 1
        dcor = (dcor+1)%WHITE
        cinza = NumPymagem(ALTURA, LARGURA, cor)
        
        D1['lin'] += D1['vetor']
        D1['col'] += D1['vetor']

        cinza.pinte_disco(dcor, D1['raio'], D1['lin'], D1['col'])
        video.append(cinza)

    mostre = True
    if mostre:
        mostre_video(video)

    salve = False
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
    if col <= 0:
        vetor[1] *= -1
    if lin + raio >= alt:
        vetor[0] *= -1
    if lin <= 0:
        vetor[0] *= -1
    return vetor

def randisco(ALT,LARG):
    raio = random.randint(5,10)
    lin = random.randint(raio, ALT - raio)
    col = random.randint(raio, LARG - raio)
    vetor = [1 + random.random(), 1+ random.random()]
    valores = {'raio':raio, 'lin':lin, 'col':col, 'vetor':vetor}
    return valores


#-------------------------------------------------------------------------- 
if __name__ == '__main__':
    main()
