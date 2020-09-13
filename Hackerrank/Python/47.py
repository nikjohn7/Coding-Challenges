def beautifulPairs(a, b):
    sums=0
    for i in a:
        if i in b:
            b.remove(i)
            sums+=1
    if sums<len(a):
        return sums+1
    else:
        return sums-1

if __name__ == '__main__':

    n = int(input())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)

    print(str(result))