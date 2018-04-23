for i in range(1, 500):
    for j in range(i + 1, 500):
        mul = i ** 2 + j ** 2
        k = int(1000 - i - j)
        if i ** 2 + j ** 2 == k ** 2:
            print(f'{i * j * k}')
