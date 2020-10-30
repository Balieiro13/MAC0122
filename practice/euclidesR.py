def mdclides(m, n):
    if n == 0:
        return m
    
    return mdclides(n, m%n)

print(mdclides(34765, 93847))
