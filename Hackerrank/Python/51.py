from heapq import heappop, heapify

def getMinimumCost(k, c):
    if k>=len(c):
        return sum(c)
    c=[-1*i for i in c]
    heapify(c)
    temp=k
    ans=0
    print(c)
    while temp:
        ans+=((-1)*heappop(c))
        temp-=1
    start=1
    temp=k
    print(c)
    while c:
        if temp>0:
            ans+=(start+1)*(-1*heappop(c))
        else:
            start+=1
            temp=k
            ans+=(start+1)*(-1*heappop(c))
        temp-=1
    return ans
    

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    print(str(minimumCost))