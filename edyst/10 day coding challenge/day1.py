t=int(input().strip())
for i in range(t):
    n=int(input().strip())
    n=n+1
    if n<=296:
        rem=n%10
        if rem==1:
            ans='sunday'
        elif rem==2:
            ans='monday'
        elif rem==3:
            ans='tuesday'
        elif rem==4:
            ans='wednesday'
        elif rem==5:
            ans='thursday'
        elif rem==6:
            ans='friday'
        elif rem==7:
            ans='saturday'
        elif rem==8:
            ans='kryptonday'
        elif rem==9:
            ans='coluday'
        elif rem==0:
            ans='daxamday'
    else:
        c = n//296
        n = n - c*296
        rem=n%10
        if rem==1:
            ans='sunday'
        elif rem==2:
            ans='monday'
        elif rem==3:
            ans='tuesday'
        elif rem==4:
            ans='wednesday'
        elif rem==5:
            ans='thursday'
        elif rem==6:
            ans='friday'
        elif rem==7:
            ans='saturday'
        elif rem==8:
            ans='kryptonday'
        elif rem==9:
            ans='coluday'
        elif rem==0:
            ans='daxamday'
    print(ans)