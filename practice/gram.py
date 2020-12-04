import numpy as np

def gramsch(matrix):
    arr = np.transpose(matrix)
    q = np.zeros(arr.shape)
    r = np.zeros((arr.shape[0],arr.shape[0]))

    for j in range(arr.shape[0]):
        q[j] = arr[j]
        for k in range(j):
            r[k,j] = np.inner(q[k],arr[j])
            q[j] = q[j] - (r[k,j] * q[k])

        r[j,j] = np.linalg.norm(q[j])
        if (r[j,j] == 0):
            continue
        else:
            q[j] /= r[j,j]
    q = np.transpose(q)

    return (q,r)

def calcula_ze(Q, b):
    z = np.dot(np.transpose(Q), b)
    return z

def resolve_sistema(R, z):
    ans = z.copy()

    for i in range(len(z)-1, -1, -1):
        ans[i] = ans[i] / R[i,i]
        for s in range(i-1, -1, -1):
            ans[s] -= R[s,i] * ans[i]

    return ans

def residuo(A, x, b):
    d = b - A.dot(x)
    return np.linalg.norm(d)

def main():
    a = np.array([[1,2,-1,3], [2,3,9,16], [-2,0,4,-1], [2,11,5,3], [0,2,-1,4], [1,-3,1,7]])
    b = np.array([1,0,1,0,-1,1])
    
    Q, R = gramsch(a)
    QR = Q.dot(R)
    z = calcula_ze(Q,b)
    ans = resolve_sistema(R,z)
    res = residuo(a, ans, b)

    print('Matrix A:')
    print(a, '\n')
    print('Matrix b:')
    print(b, '\n')
    print('Fatoração A = QR:')
    print('Matrix Q:\n')
    print(Q, '\n')
    print('Matrix R:\n')
    print(R, '\n')
    print('Matrix QR sendo um aprox de A: \n')
    print(QR, '\n')
    print('Matrix z = Q.transpose * b:\n')
    print(z, '\n')
    print('Solução aproximada do sistema linear Ax = b:\n ')
    print(ans, '\n')
    print('Resíduo da solução: \n')
    print(res, '\n')

main()
