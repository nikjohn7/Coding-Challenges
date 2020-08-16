def jumpingOnClouds(c):
    n=len(c)
    i,jump=0,0
    while(True):
        if i+2<n and c[i+2]==0:
            jump+=1
            i+=2
        elif i+1<n and c[i+1]==0:
            jump+=1
            i+=1
        elif (i+1<n and c[i+1]==1):
            continue
        elif i>=n-1:
            break
    return jump
