a = 2520
answerfound = 0
while answerfound==0:
        #things that find answer
        if a % 11 == 0 and a % 13 == 0 and a % 14 == 0 and a % 16 == 0 and a % 17 == 0 and a % 18 == 0 and a % 19 == 0 and a % 20 == 0:
                print(a)
                answerfound=1
        else:
                a = a + 1
        

