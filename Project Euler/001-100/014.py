def chain(num):
    times = 1
    while num != 1:
        if num % 2 == 0:
            num = num // 2
            times += 1
        else:
            num = 3 * num + 1
            times += 1
    return times

max_times = 0
for i in range(1, 1000000):
    j = chain(i)
    if j > max_times:
        max_times = j
# print(max_times)

i = 100000
while i <= 1000000:
    if chain(i) == max_times:
        print(i)
        break
    i += 1
    
