PAREDE = '+'
PEGADA = '*'
BECO   = 'b'
INICIO = 'I'

def main():
    # um corredor sem saidas
    lab = [
        [' ',' ',' ',' ',' ',' ','+','+','+','+','+'],
        [' ',' ',' ',' ',' ',' ','+','+','+',' ','+'],
        [' ',' ',' ',' ',' ',' ','+',' ','+',' ','+'],
        [' ',' ',' ',' ',' ',' ','+',' ','+',' ','+'],
        [' ',' ',' ',' ',' ',' ','+',' ','+',' ','+'],
        ['+','+','+','+','+','+','+',' ','+',' ','+'],
        ['+',' ',' ',' ',' ',' ',' ',' ',' ',' ','+'],
        ['+','+','+','+','+','+','+','+','+','+','+']
    ]
    lab[6][2] = INICIO
    print(to_string(lab))
    pause()
    anda(lab, 6, 2)
    print(to_string(lab))
          
#---------------------------------------------------------------            
def anda(lab, i, j):
    ''' (list, int, int) -> None
    RECEBE um `lab` sem saídas e uma posição [i][j].
    RECURSIVAMENTE, anda para pelo labirinto marcando as posições com PEGADA.
    Procura andar para "cima" e em seguida andar para a direita.
    Volta trocando as suas pegadas por BECO.

    NOTA: essa função altera `lab`.
    '''
    print(f"posição = [{i}][{j}]")
    print(to_string(lab))
    pause()
    
    if lab[i][j] == '+':
        return
    
    lab[i][j] = '*'
    anda(lab, i-1, j)
    anda(lab, i, j+1)
    
    lab[i][j] = 'b'
    print('VOLTADO!')
    print(to_string(lab))
    pause()
    
    
    
#-----------------------------------------------------------
# COSMÉTICO: exibe o labirinto
#
#-----------------------------------------------------------            
def to_string(lab):
    '''(list) -> string 
    '''
    s = ''
    nlins = len(lab)
    ncols = len(lab[0])
    linha = "  " + "+---"*ncols + "+\n"
    regua = " "
    for j in range(ncols):
        regua += f"  {j:2}"
            
    s += regua + '\n'
    for i in range(nlins):
        s += linha
        s += f"{i:2}"
        for j in range(ncols):
            s += f"| {lab[i][j]} "
        s += '|\n'
    s += linha    
    return s

def pause():
    input("Tecle ENTER para continuar.")      
            
main()
