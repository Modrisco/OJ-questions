def lcm(a, b):
    mul = a * b
    while a % b != 0:
        a, b = b, a % b
    return mul / b
answer = 1
for i in range(1, 21):
    answer = lcm(answer, i)
print(int(answer))
    
