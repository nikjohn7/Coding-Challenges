def nseries(n,count,arr=[]):
    if count==0:
        return(arr)
    else:
        arr.append(n)
        count-=1
        return nseries((2*n)-1,count,arr)

t = int(input())
init=65
for a in range(t):
    h,m=map(int,input().split(':'))
    res=nseries(h,m+1,[])
    sums=sum(res)
    sums=[int(x) for x in list(str(sums))]
    ans=[]
    for i in sums:
        ans.append(chr(init+i))
    print("".join(ans))
