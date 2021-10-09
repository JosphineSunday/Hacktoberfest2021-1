a = 0
b = 1
for x in range(0,int(input())):
	print(a, end = ",")
	c = a+b
	a = b
	b = c
