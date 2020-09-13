def balancedSums(arr):
    if len(arr)==1:
        return 'YES'
    if sum(arr[1:])==0 or sum(arr[:len(arr)-1])==0:
        return 'YES'
    l=arr[0]
    r=sum(arr)-l
    for i in range(1,len(arr)-1):
        curr=arr[i]
        r-=curr
        if l==r:
            return 'YES'
        l+=curr
    return 'NO'

if __name__ == '__main__':

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        print(result)