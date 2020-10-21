from queue import Queue

def dist(c, rede):
    n = len(rede)

    # inicia queue
    q = Queue()
    q.push(c)

    # inicia dist
    d = [n] * n
    d[c] = 0 

    while not q.vazio():
        i = q.dd()
        for j in range(n):
            if rede[i][j] == 1 and d[j] > d[i]+1:
                d[j] = d[i]+1
                q.push(j)
    return d

def main():

    mat = [
            [0,0,1,1,1,0],
            [0,0,0,0,0,0],
            [0,1,0,0,1,0],
            [0,0,0,0,1,1],
            [0,1,0,0,0,1],
            [0,1,0,0,0,0]
            ]

    origem = 3 

    d = dist(origem,mat)
    for i in range(min(len(d),20)):
        print(" ",i, ":",d[i])
    
    print(d)
main()        
