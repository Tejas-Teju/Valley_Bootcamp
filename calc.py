
x = input('Enter the expression: ')
lst = ['*','/','+','-']

aa = []
indx = 0

opr = 0

num1 = ''
a = 0

num2 = ''
b = 0

for i in x:
	aa.append(i)
	if i in lst:
		opr = i

indx = aa.index(opr)

for i in range(indx):
	num1 = num1 + aa[i]
a = int(num1)

for i in range(indx + 1,len(aa)):
	num2 = num2 + aa[i]

b = int(num2)


# for i in x:
# 	if i in lst:
# 		operator = i
# 		flag == 1
# 	if flag == 0:
# 		if i not in lst:
# 			a.append(i)
# 	if flag == 1:
# 		b.append(i) 
# print(a,b)


def multiply(a,b):
	return a*b
def divide(a,b):
	if b == 0:
		return 'Divide by zero error'
	return a/b
def add(a,b):
	return a+b
def sub(a,b):
	return a-b


if opr == '*':
	print(multiply(a,b))
elif opr == '/':
	print(divide(a,b))
elif opr == '+':
	print(add(a,b))
elif opr == '-':
	print(sub(a,b))
else:
	print('operation not defined')
	

