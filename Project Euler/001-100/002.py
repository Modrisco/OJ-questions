def fibonacci(n):
    if n <= 2:
        return 1
    if n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)
L = []
result = 0
for i in range(1,34):
    L.append(fibonacci(i))
for i in range(len(L)):
    if L[i] % 2 == 0:
        result += L[i]

print(result)
