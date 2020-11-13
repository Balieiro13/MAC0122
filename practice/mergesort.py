def merge(v, e, m, d):
    n = d - e
    w = [0]*n
    k, i, j = 0, e, m
    while (i < m and j < d):
        if (v[i] < v[j]):
            w[k] = v[i]
            i += 1
        else:
            w[k] = v[j]
            j += 1
        k += 1
    if (i < m):
        w[k:] = v[i:m]
    else:
        w[k:] = v[j:d]
    v[e:d] = w

def mergesort(v, e, d):
    if (e >= d-1): return
    m = (e + d) // 2
    mergesort(v, e, m)
    mergesort(v, m, d)
    merge(v, e, m, d)


def main():
    a = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    mergesort(a, 0, len(a))

    print(a)

main()
