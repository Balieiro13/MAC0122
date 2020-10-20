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
    print(f"Está compatível com numpymutil: {type(preto.data) is np.ndarray}")
    cor = BLACK
    
    for i in range(90):
        preto = NumPymagem(ALTURA, LARGURA, BLACK)    
        cor = (cor+2)%WHITE
        preto.pinte_disco(cor, 5, ALTURA/2, LARGURA/2)
        video.append(preto)


    elip = preto.crop()
    for lin in range(ALTURA):
        elip=elip.crop()
        for col in range(LARGURA):
            if 28 <= ((lin - ALTURA/2)/2.5)**2 + ((col - LARGURA/2)/10)**2  <= 30:
                elip[lin, col] = 250
                video.append(elip)

    elip2 = elip.crop()
    for lin in range(ALTURA):
        elip2=elip2.crop()
        for col in range(LARGURA):
            if 28 <= ((lin - ALTURA/2)/10)**2 + ((col - LARGURA/2)/2.5)**2 <=30:
                elip2[lin, col] = 250
                video.append(elip2)

    elip3 = elip2.crop()
    theta = np.radians(45)
    for i in range(ALTURA):
        elip3=elip3.crop()
        for j in range(LARGURA):
            if 28 <= (((j-LARGURA/2)*np.cos(theta) - (i-ALTURA/2)*np.sin(theta))/10)**2 + (((j-LARGURA/2)*np.sin(theta) + (i-ALTURA/2)*np.cos(theta))/2.5)**2 <= 30:
                elip3[i,j] = 250
                video.append(elip3)

    elip4 = elip3.crop()
    theta = np.radians(135)
    for i in range(ALTURA):
        elip4=elip4.crop()
        for j in range(LARGURA):
            if 28 <= (((j-LARGURA/2)*np.cos(theta) - (i-ALTURA/2)*np.sin(theta))/10)**2 + (((j-LARGURA/2)*np.sin(theta) + (i-ALTURA/2)*np.cos(theta))/2.5)**2 <= 30:
                elip4[i,j] = 250
                video.append(elip4)
    
    elip_preto = elip4.crop()*(-1/250)
    fundo_branco = elip_preto.crop()
    for i in range(ALTURA):
        for j in range(LARGURA):
            if fundo_branco[i,j] == 0:
                fundo_branco[i,j] = 1
            if fundo_branco[i,j] == -1:
                fundo_branco[i,j] = 0
    

    for i in range(250):
        elip4 += elip_preto + fundo_branco
        video.append(elip4)
        
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


#-------------------------------------------------------------------------- 
if __name__ == '__main__':
    main()
