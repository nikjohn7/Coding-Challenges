def merge_the_tools(string, k):
    arr=[]
    n=len(string)
    part=n//k
    a=0
    for i in range(part):
        inp=list(string[a:a+k])
        inp=list(dict.fromkeys(inp))
        print("".join(inp))
        a+=k

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)