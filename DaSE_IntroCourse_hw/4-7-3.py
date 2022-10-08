n=1000000
sum=0.0
for i in range(1,n):
    sum+=1/i**4
print((sum*90)**(1/4))