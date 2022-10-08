def bin(array,start,end):
    sum1 = 0
    sum2 = 0
    i = 0
    length = end-start+1
    if length == 1:
        return start
    elif length%2==1:
        for i in range(start,start+length//2):
            sum1+=array[i]
        for i in range(end+1-length//2,end+1):
            sum2+=array[i]
        if sum1 == sum2:
            return start+length//2
        elif sum1 < sum2:
            return bin(array,start,start+length//2-1)
        else:
            return bin(array,end+1-length//2,end)
    else:
        for i in range(start,start+length//2):
            sum1+=array[i]
        for i in range(end+1-length//2,end+1):
            sum2+=array[i]
        if sum1 < sum2:
            return bin(array,start,start+length//2-1)
        else:
            return bin(array,end+1-length//2,end)
list = [2,2,2,2,2,2,1,2,2,2,2,2,2,2,2]
print(bin(list,0,len(list)-1))