for _ in range(int(input())):
    r,g=map(int,input().split())
    if r==0 or g==0:
        print('1.000000')
        continue
    dp=[0 for i in range(g+1)]
    dp[0]=1.000000
    for i in range(1,g+1):
        dp[i]=(r/(r+i))+(i/(i+r))*(1.0-dp[i-1])
    print("{:f}".format(dp[g]))