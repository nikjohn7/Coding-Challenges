'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
temp=[]
arr=[]

def binsearch(l, r, ele):
    global temp
    global arr
    while (r-l)>1:
        mid=(r+l)//2
        if temp[mid]>=ele:
            r=mid
        else:
            l=mid
    return r

def solve(n):
    global temp
    global arr
    if n==1:
        return 1
    length=1
    temp[0]=arr[0]
    for i in range(1,n):
        if arr[i]<temp[0]:
            temp[0]=arr[i]
        elif arr[i]>temp[length-1]:
            temp[length]=arr[i]
            length+=1
        else:
            temp[binsearch(-1, length-1, arr[i])]=arr[i] 
    return length

n=int(input())
temp=[0 for i in range(n)]
arr=list(map(int,input().split()))
a1=n-solve(n)
arr.reverse()
a2=n-solve(n)
print('%d'%(min(a1,a2)%1000000007))