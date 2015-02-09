maxnumber = 0
for i in range(100, 1000):
	for j in range(100, 1000):
		product = i * j
		str(product)
		# product -> integer
		if str(product)[::-1] == str(product):
			if product > maxnumber:
				maxnumber = product

print(maxnumber)



