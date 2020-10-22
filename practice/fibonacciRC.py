def fibonacci(n):
    cache = [0]*(n+1)
    cache[0] = 0
    cache[1] = 1
    return fibonacciRC(n,cache)

def fibonacciRC(n, cache):
    if cache[n] != 0:
        return cache[n]
    cache[n-1] = fibonacciRC(n-1, cache)
    cache[n] = cache[n-1]+cache[n-2]
    return cache[n]

