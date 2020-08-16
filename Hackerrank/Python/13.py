def sherlockAndAnagrams(s):
    count=0
    dict={}
    n=len(s)
    for i in range(n):
        for j in range(n-i):
            sub=''.join(sorted(s[j:j+i+1]))
            try:
                dict[sub]+=1
            except:
                dict[sub]=1
    for i in dict:
        count+=dict[i]*(dict[i]-1)//2
    return count
