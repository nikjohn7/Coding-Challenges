def chocolateFeast(n, c, m):
    choc=0
    wrap=0
    initial=n//c
    choc+=initial
    wrap+=choc
    while(True):
        if wrap>=m:
            a=wrap//m
            rem=wrap%m
            choc+=a
            wrap=a+rem
        else:
            break
    return choc
