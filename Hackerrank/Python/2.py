def countingValleys(n, s):
    vcount=0
    level=0
    s=list(s)
    for i in s:
        if i=='U':
            level+=1
        elif i=='D':
            if level==0:
                vcount+=1
            level-=1
    return vcount