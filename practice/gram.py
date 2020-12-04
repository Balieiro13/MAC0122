import numpy as np
from numpy import linalg as LA

def gramsch(matrix):
    arr = np.transpose(matrix)
    q = np.zeros(arr.shape)
    r = np.zeros((arr.shape[0],arr.shape[0]))

    for j in range(arr.shape[0]):
        q[j] = arr[j]
        for k in range(j):
            r[k,j] = np.inner(q[k],arr[j])
            q[j] = q[j] - (r[k,j] * q[k])

        r[j,j] = LA.norm(q[j])
        if (r[j,j] == 0):
            continue
        else:
            q[j] /= r[j,j]
    q = np.transpose(q)

    return (q,r)

def vecze(arr, barr):
    Q = gramsch(arr)
    qt = np.transpose(Q[0])
    z = np.dot(qt, barr)
    return z

def main():
    a = np.array([[1,2,-1,3], [2,3,9,16], [-2,0,4,-1], [2,11,5,3], [0,2,-1,4], [1,-3,1,7]])
    b = gramsch(a)
    c = np.dot(np.transpose(b[0]), b[0])
    print(c)
main()    
