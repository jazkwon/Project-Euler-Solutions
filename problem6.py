a = 0
b = 0
sum = 0
sqre = 0
for i in range(1, 101):
    a = i * i
    sum = sum + a
for i in range(1, 101):
    b = i
    sqre = sqre + b
sqre = sqre ** 2
print (sqre - sum)


