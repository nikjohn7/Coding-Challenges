from collections import deque

def validate_bounds(i, j, n):
    return 0 <= i < n and 0 <= j < n

def bfs(a, b, n):
    q = deque([(0, 0, 0)])
    dirs = [[a, b], [-a, b], [-a, -b], [a, -b],
            [b, a], [-b, a], [-b, -a], [b, -a]]
    visited = [[False]*n for _ in range(n)]

    visited[0][0] = True
    while q:
        curr_r, curr_c, length = q.popleft()

        length += 1

        for dir_r, dir_c in dirs:
            new_r = curr_r + dir_r
            new_c = curr_c + dir_c
            if validate_bounds(new_r, new_c, n) and not visited[new_r][new_c]:
                if new_r == n-1 and new_c == n-1:
                    return length

                q.append((new_r, new_c, length))
                visited[new_r][new_c] = True

    return -1 

def knightL():
    n = int(input())

    answer = [[0]*(n-1) for _ in range(n-1)]

    for i in range(1, n):
        for j in range(i, n):
            answer[i-1][j-1] = bfs(i, j, n)
            answer[j-1][i-1] = answer[i-1][j-1]

    for ans in answer:
        print(*ans)


knightL()