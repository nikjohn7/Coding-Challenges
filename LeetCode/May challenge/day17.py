from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        dict_p=Counter(p)
        dict_s=Counter(s[:len(p)])
        output=[]
        i=0
        n=len(p)
        
        while n<=len(s):
            if dict_s==dict_p:
                output.append(i)

            dict_s[s[i]]-=1
            if dict_s[s[i]]<=0:
                dict_s.pop(s[i])
                
            if n<len(s):    
                 dict_s[s[n]]+=1
            n+=1
            i+=1
            
        return output  