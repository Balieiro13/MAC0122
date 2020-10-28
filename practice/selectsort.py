def ssort(arr, init):
    if (init == (len(arr)-1)): return 0
    old = arr[init]
    m = min(arr[init:])
    for i in range(init, len(arr)):
        if m == arr[i]:
            arr[init] = m
            arr[i] = old
            return ssort(arr, init+1)

v = [-10, 0, 3, 6, 2, 3, 10, 6, -2, 2]
ssort(v, 0)
print(v)
