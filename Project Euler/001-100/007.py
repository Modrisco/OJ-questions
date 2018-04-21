from math import sqrt
l = [[0] for _ in range(10001)]

def isPrime(n):
    flag = 1
    for j in range(2, int(sqrt(n)) + 1):
        if n % j == 0:
            flag = 0
    if flag == 1:
        return True

num = 2
i = 0
while i <= 10000:
    if isPrime(num):
        l[i] = num
        num += 1
        i += 1
    else:
        num += 1

print(l[-1])
