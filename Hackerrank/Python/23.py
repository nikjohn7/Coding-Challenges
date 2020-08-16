def flatlandSpaceStations(n, c):
    arr=[0]*n
    m=0
    c.sort()
    if c[0]>0:
            a=len(arr[:c[0]])
            if a>m:
                m=a
    for i in range(len(c)-1):
        a=math.ceil((len(arr[c[i]+1:c[i+1]]))/2)
        if a>m:
            m=a
    if c[-1]!=n-1:
        a=len(arr[c[-1]+1:])
        if a>m:
            return a
    return m
