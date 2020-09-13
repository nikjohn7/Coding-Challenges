def surfaceArea(A):
    matrix=[[0]*(len(A[0])+2)]
    for r in A:
        matrix.append([0]+r+[0])
    matrix.append([0]*(len(A[0])+2))

    price=2*len(A)*len(A[0])

    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[i])):
            price+=abs(matrix[i][j]-matrix[i-1][j])
            price+=abs(matrix[i][j]-matrix[i][j-1])
    return price




if __name__ == '__main__':

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    print(str(result) + '\n')