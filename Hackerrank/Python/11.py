def climbingLeaderboard(scores, alice):
    d={}
    pos=1
    for i in scores:
        if i not in d:
            d[i]=pos
            pos+=1
    key=list(d.keys())
    print(key)
    res=[]
    rank=0
    alice.reverse()
    for i in alice:
        f=0
        while rank<len(key):
            if i >= key[rank]:
                res.append(d[key[rank]])
                f=1
                break
            else:
                rank+=1
        if f==0:
            res.append(len(key)+1)
    return reversed(res)