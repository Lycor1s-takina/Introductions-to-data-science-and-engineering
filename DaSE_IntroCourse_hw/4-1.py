i = 0
c = 1
while i <= 100:
    if i%2==1:
        print(i)
        if i<50:
            c*=i
    i+=1
print(c)
