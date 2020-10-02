import numpy as np

def algum_menor(idade):
    idade = idade.reshape(idade.size)
    for i in idade:
        if i < 18:
            return True
    return False

def algum_menorv2(idade):
    menor = idade < 18
    return np.any(menor)

a = np.array([[21,19,20,21],[19,20,18,20]])

print(algum_menorv2(a))
print(algum_menor(a))