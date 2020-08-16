def countHens(numheads,numlegs):

    ns=-1
    for i in range(numheads+1):
        j=numheads-i
        if (2*i)+(4*j)==numlegs:
            return i
    return ns

t=int(input())
for _ in range(t):
    head,leg = map(int, input().split())
    ans=countHens(head, leg)
    print(ans)