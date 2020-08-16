def countWays(arr, N): 
    count=[]
    count = [0 for i in range(N + 1)] 
    count[0] = 1
    for i in range(1, N + 1): 
        for j in range(len(arr)): 
            if (i >= arr[j]): 
                count[i] += count[i - arr[j]]
    #print(count[N])
    return count[N]
lis=[1,2,3,4]
for _ in range(int(input())):
    n=int(input())
    print(countWays(lis,n))