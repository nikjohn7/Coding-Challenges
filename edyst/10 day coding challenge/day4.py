t=int(input())
for q in range(t):
    inp=[int(x) for x in input().split()]
    n=inp[0]
    arr=inp[2:]
    i=0
    row=[]
    cols=[]
    rowcount=0
    colcount=0
    while i<=(n*n)-n:
        lis=arr[i:i+n]
        row.append(lis)
        i+=n
    for j in range(n):
        count=0
        lis=[]
        itr=j
        while(count<n):
            lis.append(arr[itr])
            itr+=n
            count+=1
        cols.append(lis)
    for j in range(n):
        if len(row[j])!=len(set(row[j])):
            rowcount+=1
        if len(cols[j])!=len(set(cols[j])):
            colcount+=1
    if rowcount==0 and colcount==0:
        print('SAFE')
    else:
        print('DANGER',rowcount,colcount)
