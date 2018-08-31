from math import *
def sum_of_divisor(n):
    divisor = []
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            divisor.extend([i, n//i])
    return sum(divisor)+1

def sum_of_amicable_numbers(n):
    result = []
    for i in range(10000):
        s = sum_of_divisor(i)
        if sum_of_divisor(s) == i and s != i:
            result.extend([i, s])
    return sum(set(result))

print(sum_of_amicable_numbers(10000))
