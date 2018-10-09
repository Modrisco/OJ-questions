# 1000-digit Fibonacci number

# def fib(n):
# 	a = 1
# 	b = 0
# 	while n > 1:
# 		a, b = a+b, a
# 		n-=1
# 	return a

# def binetFibFormula(n):
# 	n = decimal.Decimal(10)
# 	return len(str(int((((1+sqrt(5))**n - (1-sqrt(5))**n)/(2**n*sqrt(5))))))

# print(binetFibFormula(100))

flag = 0
l = [1, 1]
i = 1
while (flag == 0):
	if (len(str(l[i]))) >= 1000:
		flag = 1
		print(i+1)
	else:
		l.append(l[i] + l[i-1])
		i+=1
