def decentNumber(n):
    if n%3==0:
        print('5'*n)
        return
    init5=n-(n%3)
    ans=''
    while init5>0:

        if (n-init5)%5==0:
            ans+='5'*init5
            ans+='3'*(n-init5)
            print(ans)
            return
        else:
            init5-=3
    if n%5==0:
        print('3'*n)
    else:
        print ('-1')
    return



if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)