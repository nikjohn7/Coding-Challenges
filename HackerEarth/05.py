mods=1000000007
n=int(input())
temp,ans=1,1
for i in range(2,n):
    temp=(temp+ans)%mods
    temp,ans=ans,temp
print(ans%mods)