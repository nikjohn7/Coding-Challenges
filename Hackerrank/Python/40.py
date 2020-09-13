def beautifulBinaryString(b):
    if ('010' not in b) or (len(b)<3):
        return 0
    b=list(b)
    sub=['0','1','0']
    count,i=0,0
    while i+3<=len(b):
        if b[i:i+3]==sub:
            count+=1
            i+=3
        else:
            i+=1
    return count



if __name__ == '__main__':

    n = int(input())

    b = input()

    result = beautifulBinaryString(b)

    print(str(result))