import sys
from copy import deepcopy
try:
    filename = input('Which data file do you want to use?: ')
    f = open(filename,'r')
    if not filename:
        raise FileNotFoundError
except FileNotFoundError:
    print ('Incorrect input, giving up.')
    sys.exit()
# 1-D list
array = f.read()
array = array.replace('\n',' ')
array = array.split(' ')
while '' in array:
    array.remove('')
old_len = len(array)
# 2-D list
for i in range(len(array)):
    element = []
    element.append(array[i])
    array.append(element)
del array[0:old_len]
# 3-D list
array_2 = deepcopy(array)
for i in range(len(array)):
    array[i].append(1)
    array[i][0] = int(array[i][0])
start_item = end_item = 0
line = 1
while end_item < old_len:
    end_item = start_item + line
    array.append(array[start_item:end_item])
    start_item = end_item
    line += 1
del array[0:old_len]

for i in range(len(array_2)):
    array_2[i][0] = int(array_2[i][0])
start_item = end_item = 0
line = 1
while end_item < old_len:
    end_item = start_item + line
    array_2.append(array_2[start_item:end_item])
    start_item = end_item
    line += 1
del array_2[0:old_len]

def find_sum_and_pathes(array):
    largest_sum = 0
    num_of_paths = 1
    row_num = len(array)-1
    for row in range(0,row_num):
        col = 0
        while col < row_num - row:
            if array[row_num-row-1][col][0] + array[row_num-row][col][0] > array[row_num-row-1][col][0] + array[row_num-row][col+1][0]:
                array[row_num-row-1][col][-1] = array[row_num-row][col][-1]
                array[row_num-row-1][col][0] = array[row_num-row-1][col][0] + array[row_num-row][col][0]
            elif array[row_num-row-1][col][0] + array[row_num-row][col][0] == array[row_num-row-1][col][0] + array[row_num-row][col+1][0]:
                array[row_num-row-1][col][-1] = array[row_num-row][col][-1] + array[row_num-row][col+1][-1]
                array[row_num-row-1][col][0] = array[row_num-row-1][col][0] + array[row_num-row][col][0]
            else:
                array[row_num-row-1][col][-1] = array[row_num-row][col+1][-1]
                array[row_num-row-1][col][0] = array[row_num-row-1][col][0] + array[row_num-row][col+1][0]
            col += 1

    largest_sum = array[0][0][0]
    num_of_paths = array[0][0][-1]
    print (f'The largest sum is: {largest_sum}')
    print (f'The number of paths yielding this sum is: {num_of_paths}')

def find_the_largest_path(array):
    path = result = []
    row_num = len(array)-1

    for row in range(0,row_num):
        col = 0
        while col < row_num - row:
            if array[row_num-row-1][col][-1] + array[row_num-row][col][-1] > array[row_num-row-1][col][-1] + array[row_num-row][col+1][-1]:
                if row_num-row != row_num:
                    array[row_num-row-1][col] += (array[row_num-row][col][0:-1])
                else:
                    array[row_num-row-1][col].append(array[row_num-row][col][-1])
                array[row_num-row-1][col].append(array[row_num-row-1][col][0] + array[row_num-row][col][-1])

            elif array[row_num-row-1][col][-1] + array[row_num-row][col][-1] == array[row_num-row-1][col][-1] + array[row_num-row][col+1][-1]:
                if row_num-row != row_num:
                    array[row_num-row-1][col] += (array[row_num-row][col][0:-1])
                else:
                    array[row_num-row-1][col].append(array[row_num-row][col][-1])
                array[row_num-row-1][col].append(array[row_num-row-1][col][0] + array[row_num-row][col][-1])
            else:
                if row_num-row != row_num:
                    array[row_num-row-1][col] += (array[row_num-row][col+1][0:-1])
                else:
                    array[row_num-row-1][col].append(array[row_num-row][col+1][-1])
                array[row_num-row-1][col].append(array[row_num-row-1][col][0] + array[row_num-row][col+1][-1])
            col += 1

    path = array[0][0]
    for n in range(0,len(path)-1):
        result.append(int(path[n]))

    print (f'The leftmost path yielding this sum is: {result}')
find_sum_and_pathes(array)
find_the_largest_path(array_2)
