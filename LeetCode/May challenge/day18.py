class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1)>len(s2):
            return False
        
        d1 = {}
        for l in s1:
            if l in d1:
                d1[l] += 1
            else:
                d1[l] = 1
    
        d2 = {}
        for l in s2[:len(s1)]:
            if l in d2:
                d2[l] += 1
            else:
                d2[l] = 1
                
        if d1 == d2:
            return True
        
        for i in range(len(s2)-len(s1)):
            v_out = s2[i]
            if d2[v_out] == 1:
                del d2[v_out]
            else:
                d2[v_out] -=1

            v_in = s2[i+len(s1)]
            if v_in in d2:
                d2[v_in] += 1
            else:
                d2[v_in] = 1
            if d1 == d2:
                return True
                
        return False