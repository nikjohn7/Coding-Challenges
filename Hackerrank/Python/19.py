def encryption(s):
    s=s.replace(' ','')
    n=len(s)
    c=math.ceil(math.sqrt(n))
    l,count=0,0
    res=[]
    while True:
        if l==n:
            break
        st=''
        i=count
        while(i<n):
            st+=s[i]
            l+=1
            i+=c
        res.append(st)
        count+=1
    return ' '.join(res)