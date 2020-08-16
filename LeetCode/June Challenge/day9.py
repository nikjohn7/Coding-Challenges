class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)>len(t):
            return False
        if s=="":
            return True
        s=list(s)
        t=list(t)
        tset=set(s)
        #print(tset)
        cnt=f=0
        for i in range(len(t)):
            if t[i] in tset:
                if t[i]==s[cnt]:
                    #print(s[cnt])
                    cnt+=1
                    if cnt==len(s):
                        f+=1
                        break
        #print(f)
        if f==1:
            return True
        else:
            return False