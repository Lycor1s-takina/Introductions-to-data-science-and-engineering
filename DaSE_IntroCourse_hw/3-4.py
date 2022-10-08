import math
import random
s = 100
n = 1000000
count = 0
for i in range(n):
    x=random.uniform(2.0,3.0)
    y=random.uniform(0.0,100.0)
    if y <= x**2+4*x*math.sin(x):
        count+=1
print(count/n*s)
