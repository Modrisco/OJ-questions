f = open('1.txt', 'r')
array = f.readlines()

for i in range(len(array)):
    array[i] = int(array[i])

total = sum(array)
total = str(total)
print(total[0:10])
