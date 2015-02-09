
def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	elif n == 2:
		return 1
	else:
		return fibonacci(n-2) + fibonacci(n-1)
sum = 0
fibValue = 0
n = 0
while fibValue < 4000000:
	fibValue = fibonacci(n)
	n = n + 1
	if (fibValue % 2 == 0):
		sum = sum + fibValue
print(sum)

