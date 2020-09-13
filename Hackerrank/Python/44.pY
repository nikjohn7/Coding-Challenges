def strangeCounter(t):
    init=3
    while t>init:
        t-=init
        init*=2
    
    return init-t+1


if __name__ == '__main__':

    t = int(input())

    result = strangeCounter(t)

    print(str(result))