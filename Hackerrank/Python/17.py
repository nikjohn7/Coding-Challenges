def makingAnagrams(s1, s2):
    s1,s2=list(s1),list(s2)
    set1,set2=set(s1),set(s2)
    common=list(set1.intersection(set2))
    i=0
    while i<len(common):
        if common[i] in s1 and common[i] in s2:
            s1.remove(common[i])
            s2.remove(common[i])
        else:
            i+=1
    return len(s1)+len(s2)