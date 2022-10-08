s = input()
max_count = 1
for i in range(1,len(s)):
    count=1
    while s[i-1]==s[i]:
        count+=1
        i+=1
        if i>=len(s):
            break
    if count>max_count:
        max_count=count
if max_count==1:
    print("no")
else:
    print(max_count)