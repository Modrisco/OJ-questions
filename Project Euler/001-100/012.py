def list_factors(num):
    L = []
    for i in range(1, (int(num ** 0.5))+1):
        if num % i==0:
            L.append(i)
            L.append(num // i)
    return len(L)

i = 1
while True:
    num = int(i * (i + 1) / 2)
    if list_factors(num) >= 500:
        print(num)
        break
    i += 1
