import math
import random
s = 5
n = 1000000
count = 0
for i in range(n):
    x=random.uniform(0.0,1.0)
    y=random.uniform(0.0,5.0)
    if y <= x**3+x**2:
        count+=1
print(count/n*s)