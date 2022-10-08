min=0.0
max=2.0
g=(min+max)/2
while abs(g**2-2)>0.0001:
    if g**2-2>0:
        max=g
    else:
        min=g
    g=(max+min)/2
print(g)