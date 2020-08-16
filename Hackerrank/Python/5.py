def hourglassSum(arr):
    sums=[]
    for i in range(4):
        for j in range(4):
            r1=arr[i][j:j+3]
            r2=arr[i+2][j:j+3]
            sums.append(sum(r1)+sum(r2)+(arr[i+1][j+1]))
    return max(sums)
