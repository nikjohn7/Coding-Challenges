import re 

lowervow=['a','e','i','o','u']
uppervow=['A','E','I','O','U']

for _ in range(int(input())):
    v=0
    string=input()
    string=list(string)
    if len(string)>=3:  
        for i in range(len(string)-2):
            subs=string[i:i+3]
            #print(subs)
            if (all(x in lowervow for x in subs)) or (all(x in uppervow for x in subs)):
                v+=1
    temp = re.findall(r'\d', str(string))
    temp=[int(x) for x in list(temp)]
    sums=sum(temp)
    print(v%sums)