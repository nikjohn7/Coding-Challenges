a, b = map(int, input().split())
current = 1
nums = 0
 
while True:
  if b <= current:
    print(nums)
    exit(0)
  current += (a - 1)
  nums += 1