def theLoveLetterMystery(s):
    if len(s)==1:
        return 0
    c=0
    i,j=0,len(s)-1
    if len(s)%2==0:
        while i<j:
            c+=abs(ord(s[i])-ord(s[j]))
            i+=1
            j-=1
    else:
        while i<=j:
            c+=abs(ord(s[i])-ord(s[j]))
            i+=1
            j-=1
    return c


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        print(str(result))
