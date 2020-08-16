from collections import defaultdict
def check_repeat(li):
  res=[]
  for i in li:
    x=defaultdict(int)
    c=[]
    for j in i:
      x[j]+=1
      c.append(x[j])
    print(c)
    res.append(c)
  print(res)
  return res

t = int(input())
 
for _ in range(t):
    inp = input().split()
    n = int(inp[0])
    parties = inp[1:]
    inp = input().split()
    v = int(inp[0])
    passwords = inp[1:]
    parties_data = check_repeat(parties)
    voters_data = check_repeat(passwords)
 
    votes = [0]*n
 
    for itr1,i in enumerate(parties_data):
        for itr2,j in enumerate(voters_data):
            if i==j:
                votes[itr1]+=1	
    maximum = max(votes)
    winners = []

    if(maximum==0):
        print("stalemate")
        continue

    for itr,i in enumerate(votes):
        if i==maximum:
            winners.append(parties[itr])

    winners.sort()
    print(*winners)