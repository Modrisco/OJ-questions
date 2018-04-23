from math import sqrt

def isPrime():
    sum = 2
    for i in range(3, 2000000, 2):
        flag = 1
        for j in range(2, int(sqrt(i)) + 1):
            if i % j == 0:
                flag = 0
        if flag == 1:
            sum += i
    print (sum)

isPrime()
'''
marked = [0] * 2000000
value = 3
s = 2
while value < 2000000:
    if marked[value] == 0:
        s += value
        i = value
        while i < 2000000:
            marked[i] = 1
            i += value
    value += 2
print (s)
'''
