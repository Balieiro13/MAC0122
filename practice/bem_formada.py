def bem_formada(s):
    abre = ['(', '[', '{']
    fecha = ['}', ']', ')']
    pares = ['()', '{}', '[]']
    pilha=[]
    for i in s:
        if i in abre:
            pilha.append(i)
        if i in fecha:
            if len(pilha) == 0:
                return False
            if pilha[-1]+ i in pares:
                pilha.pop()

    return (len(pilha)==0)

def main ():
    testes = [
            '()',
            '[()]',
            '[{()}]',
            '() [{}][(])',
            ']',
            '((({}{}{{{}}})))',
            ']((({}{}{{{}}})))'

            ]
    for t in range(len(testes)):
        resp = bem_formada( testes[t])
        print (resp)

main()
