palindrome = []
for i in range(100, 999):
    for j in range(100, 999):
        num = i * j
        if len(str(num)) == 5:
            continue
        if len(str(num)) == 6:
            if num % 10 == num // 100000 % 10 and num // 10 % 10 == num // 10000 % 10 and num // 100 % 10 == num // 1000 % 10:
                palindrome.append(num)

print(sorted(palindrome)[-1])
