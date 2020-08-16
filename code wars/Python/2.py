def iq_test(numbers):
    #your code here
    arr=[x%2 for x in list(map(int,numbers.split()))]
    if arr.count(0)>1:
        return arr.index(1)+1
    else:
        return arr.index(0)+1