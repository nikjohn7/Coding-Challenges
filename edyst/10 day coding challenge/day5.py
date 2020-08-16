t=int(input())
for _ in range(t):
    n,limit=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort(reverse=True)
    s1=[0]*n
    res=0
    if l[0]>limit:
        print('impossible')
    else:
        for i in range(n):
            s=0
            if s1[i]==0:
                s1[i]=1
                s+=l[i]
                j=i+1
                while j<n:
                    if s1[j]==0 and s+l[j]<=limit:
                        s+=l[j]
                        s1[j]=1
                        for k in range(j+1,n):
                            s1[k]=1
                    j+=1
                    break
                res+=1
        print(res)