mul_3 = 0
mul_5 = 0
mul_15 = 0
for i in range(1, 1000):
    if i % 3 == 0:
        mul_3 += i
    if i % 5 == 0:
        mul_5 += i
    if i % 15 == 0:
        mul_15 += i
print(mul_3 + mul_5 - mul_15)
