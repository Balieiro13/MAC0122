def pivo(v, e, d):
    x = v[d-1]
    i = e - 1 
    for j in range(e, d):
        if (v[j] <= x):
            i += 1
            v[i], v[j] = v[j], v[i]
    return i

def quicksort(v):
    quicksortR(v, 0, len(v))

def quicksortR(v, e, d):
    if (e >= d - 1): return
    m = pivo(v, e, d)
    quicksortR(v, e, m)
    quicksortR(v, m+1, d)

def main():
    v = [33,99,11,22,55,88,33,77,66,44]
    quicksort(v)
    print(v)
    return 0

main()
