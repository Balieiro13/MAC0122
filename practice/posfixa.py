def posfixa(lista):
    pilha = []
    nums = '1234567890'
    operadores = '+-*/'

    for i in lista:
        if i in nums:
            pilha.append(i)
        if i in operadores:
            if i == '+':
                resultado = int(pilha[-2]) + int(pilha[-1])
            if i == '-':
                resultado = int(pilha[-2]) - int(pilha[-1])
            if i == '*':
                resultado = int(pilha[-2]) * int(pilha[-1])
            if i == '/':
                resultado = int(pilha[-2]) / int(pilha[-1])
            pilha.pop()
            pilha.pop()
            pilha.append(str(resultado))

    return pilha[0]

teste = ['2', '3', '+', '4', '*']

print(posfixa(teste))
