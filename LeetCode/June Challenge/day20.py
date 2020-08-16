from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        d=1
        arr=[]
        if(n==1):
            return "1"
        for i in range(1,n):
            d*=i
            arr.append(str(i))
        arr.append(str(n))
        ans=""
        temp=k
        y=n-1
        print(arr)
        while(y!=0 and temp!=0):
            a=math.ceil(temp/d)
            #print(a,l[a-1])
            ans+=arr[a-1]
            arr.pop(a-1)
            temp=temp%d
            d=d//y
            y-=1
        if(temp==0):
            ans+="".join(arr[::-1])
        
        return ans