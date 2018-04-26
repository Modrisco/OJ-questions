def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n * f(n - 1)

print(sum(map(int, str(f(100)))))    
