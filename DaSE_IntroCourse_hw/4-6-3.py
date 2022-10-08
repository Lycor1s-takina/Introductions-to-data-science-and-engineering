g=1.0
while abs(g**2-2)>0.0001:
    g=(g+2/g)/2
print(g)