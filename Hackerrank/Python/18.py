def cavityMap(grid):
    if len(grid)>2:
        lis=[]
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid)-1):
                x=[int(grid[i-1][j]),int(grid[i+1][j]),int(grid[i][j-1]),int(grid[i][j+1])]
                print(x)
                if int(grid[i][j])>max(x):
                    lis.append((i,j))
        for i in lis:
            grid[i[0]]=grid[i[0]][:i[1]]+'X'+grid[i[0]][i[1]+1:]
    return grid