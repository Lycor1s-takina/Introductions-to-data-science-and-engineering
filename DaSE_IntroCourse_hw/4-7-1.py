import random
n=1000000
count=0
for i in range(n):
    x=random.uniform(-1.0,1.0)
    y=random.uniform(-1.0,1.0)
    if x**2+y**2<=1:
        count+=1
print(count/n*4)