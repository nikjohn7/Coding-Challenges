def repeatedString(s, n):
    mul=n//len(s)
    rem=n%len(s)
    if rem>0:
        rem_string=s[:rem]
    s= list(s)
    num=s.count('a')
    num*=mul
    if rem>0:
        num+=rem_string.count('a')