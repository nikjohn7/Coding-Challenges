nd = input().split()

n = int(nd[0])

d = int(nd[1])

arr = list(map(int, input().rstrip().split()))
right=arr[:d]
left=arr[d:]
left.extend(right)
left=[str(x) for x in left]
print(" ".join(left))