f = open('p022_names.txt', 'r')
array = f.read()
array = array.replace('"','')
array = array.split(',')
array = sorted(array)
result = 0
def letter_product(s):
    p = 0
    for i in range(len(s)):
        p += ord(s[i])-64
    return p

for i in range(len(array)):
    result += (i+1) * (letter_product(array[i]))
print(result)
print(array.index('COLIN'))

