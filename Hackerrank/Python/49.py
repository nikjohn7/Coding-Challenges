def connectedCell(matrix):
    mx = 0
    filled = [(i, j) for i, row in enumerate(matrix) for j,n in enumerate(row) if n]
    while filled:
        region = [filled.pop()]
        count = 0
        while region:
            
            n = region.pop()
            count += 1
            for f in list(filled):
                if abs(n[0] - f[0]) <= 1 and abs(n[1]-f[1]) <= 1:
                    region.append(f)
                    filled.remove(f)
        else:
            mx = max(mx, count)
    return mx

if __name__ == '__main__':

    n = int(input())

    m = int(input())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    print(str(result))
