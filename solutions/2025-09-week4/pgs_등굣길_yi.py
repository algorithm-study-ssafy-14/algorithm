def solution(m, n, puddles):
    key = 1000000007
    grid = [[0] * n for _ in range(m)]
    grid[0][0] = 1

    for x, y in puddles:
        grid[x - 1][y - 1] = -1

    status = 1
    for j in range(1, n):
        if grid[0][j] == -1:  
            status = 0
        grid[0][j] = status

    status = 1
    for i in range(1, m):
        if grid[i][0] == -1:
            status = 0
        grid[i][0] = status

    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j] == -1: 
                grid[i][j] = 0
            else:
                grid[i][j] = (grid[i - 1][j] + grid[i][j - 1]) % key

    return grid[m - 1][n - 1]
