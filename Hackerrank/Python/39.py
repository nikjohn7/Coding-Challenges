def happyLadybugs(b):
    if len(b)==1:
        if b[0]=='_':
            return 'YES'
        else:
            return 'NO'
    if list(set(b))==['_']:
        return 'YES'
    if '_' not in b:
        if len(b)==2:
            if b[0]==b[1]:
                return 'YES'
            else:
                return 'NO'
        else:
            if b[0]!=b[1] or b[-1]!=b[-2]:
                return 'NO'
            else:
                for i in range(1,len(b)-1):
                    if b[i]!=b[i-1] and b[i]!=b[i+1]:
                        return 'NO'
                return 'YES'
    else:
        setb=set(b)
        b=list(b)
        for i in setb:
            if i!='_':
                if b.count(i)<2:
                    return 'NO'
        return 'YES'

    

if __name__ == '__main__':

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        print(result)