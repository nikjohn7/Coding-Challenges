for _ in range(int(input())):
    req_amount = int(input())
    arr = list(map(int, input().split()))
    N = arr.pop(0)
    l = []
    for i in range(N):
        l.append(arr[i]/(2**i))
    lst = sorted(l)
    i = 0
    energy = 0
    while req_amount:
        t = l.index(lst[i])
        while req_amount >= 2 ** t:
            energy += arr[t]
            req_amount -= 2 ** t
        i += 1
    print(energy)




