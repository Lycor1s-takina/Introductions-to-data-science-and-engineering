n=1000000
sum=0.0
for i in range(n):
    sum+=(-1)**i/(2*i+1)
print(sum*4)