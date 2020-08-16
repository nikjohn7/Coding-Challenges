def fairRations(B):
    if len(B)==2:
        arr=[x%2 for x in B]
        if sum(arr)==0:
            return 0
        elif sum(arr)==1:
            return 'NO'
        elif sum(arr)==2:
            return 2
    loaves=0
    for i in range(len(B)-1,0,-1):
        if B[i]%2==1:
            B[i]+=1
            B[i-1]+=1
            loaves+=2
    B=[x%2 for x in B]
    if sum(B)==0:
        return loaves
    else:
        return 'NO'