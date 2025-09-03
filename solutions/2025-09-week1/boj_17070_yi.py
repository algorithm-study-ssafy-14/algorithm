# from collections import deque

# n = int(input())
# graph = [list(map(int, input().split())) for _ in range(n)]

# queue = deque()
# queue.append((0, 1, 0))

# count = 0

# while queue:
#     x, y, direction = queue.popleft()
    
#     if x == n-1 and y == n-1:
#         count += 1
#         continue
    
#     if direction == 0 or direction == 2:
#         nx, ny = x, y + 1
#         if ny < n and graph[nx][ny] == 0:
#             queue.append((nx, ny, 0))
    
#     if direction == 1 or direction == 2:
#         nx, ny = x + 1, y
#         if nx < n and graph[nx][ny] == 0:
#             queue.append((nx, ny, 1))
    
#     nx, ny = x + 1, y + 1
#     if nx < n and ny < n:
#         if graph[x][y+1] == 0 and graph[x+1][y] == 0 and graph[nx][ny] == 0:
#             queue.append((nx, ny, 2))

# print(count)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[[0]*3 for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1

for i in range(n):
    for j in range(2, n):
        if graph[i][j] == 0:
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
            if i > 0:
                dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]
            if i > 0 and graph[i-1][j] == 0 and graph[i][j-1] == 0:
                dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]

result = sum(dp[n-1][n-1])
print(result)

