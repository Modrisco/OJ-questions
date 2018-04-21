from math import sqrt

n = 600851475143 

i = 2
while i < sqrt(n):
    while n % i == 0:
        n //= i
    i += 1

print(f'{n}')
