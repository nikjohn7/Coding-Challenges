def alternatingCharacters(s):
    count,i=0,0
    if len(s)==1:
        return 0
    s=list(s)
    while i<len(s):
        if s[i]==s[i+1]:
            del s[i+1]
            count+=1
        else:
            i+=1
        if i==len(s)-1:
            return count

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        print(str(result))