def findSum(n) : 
    if (n % 2 == 0) : 
        return (n / 2) * (n + 1) 
   
   # If n is odd, (n+1) must be even 
    else : 
        return  ((n + 1) / 2) * n 

t=int(input())
for i in range(t):
    n,p=map(int,input().split())
    norm=int(findSum(n))
    arr=[0]*n
    add=1
    iterlevel=0
    f=0
    itr=0
    count=0
    while(True):
        if count<norm:
            if p>0:
                arr[itr]+=1
            else:
                break
            
            p-=1
            if itr==n-1:
                itr=add
                add+=1
            else:
                itr+=1
            count+=1
        else:
            f=1
            break
    if f==1:
        arr[0]+=p
    for k in arr:
        print(k,end=" ")
    print()