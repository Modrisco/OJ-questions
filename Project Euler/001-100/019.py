result = 0
day = 2 # 1901.01.01 is Tuesday
normal_year = [31,28,31,30,31,30,31,31,30,31,30,31]
leap_year = [31,29,31,30,31,30,31,31,30,31,30,31]

for year in range(1901, 2001):
    if year % 4 != 0:
        for i in range(len(normal_year)):
            day += normal_year[i]
            if day % 7 == 0:
                result += 1
    if year % 4 == 0:
        for i in range(len(normal_year)):
            day += normal_year[i]
            if day % 7 == 0:
                result += 1        

print("Result: ",result)
