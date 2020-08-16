def fact(n):
    if(n<=1):
        return 1
    else:
        return n*fact(n-1)

for _ in range(int(input())):
    (x1,y1)=map(int,input().split())
    (x2,y2)=map(int,input().split())
    d=input()
    if((x1>x2 and d[1]=='E') or (x1<x2 and d[1]=='W') or (y1>y2 and d[0]=='N') or (y1<y2 and d[0]=='S')):
        print('impossible')
    else:
        x=abs(x1-x2);y=abs(y1-y2);
        z=((fact(x+y))//(fact(x)*fact(y)))
        print('Total Ways:',z)