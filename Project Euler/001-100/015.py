'''
def f(N):
    if N == 1:
        return 1
    if N > 1:
        total = 1
        for i in range(1, N + 1):
            total *= i
        return total

def paths(N):
    a = f(N ** 2)
    b = f(N) * 2
    return int(a / b)
'''

    
