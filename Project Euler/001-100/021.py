result = 0
def sum_divisor(n):
    sum = 0
    for i in range(1, n//2+1):
        if n % i == 0:
            sum += i
    return sum
for i in range(10):
    result += sum_divisor(i)
print(result)
