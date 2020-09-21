string=input()
count=0
for i in string:
    if int(i)%2==0:
        count+=1
for i in string:
    print(count, end=' ')
    if int(i)%2==0:
        count-=1