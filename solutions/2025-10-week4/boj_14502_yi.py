from itertools import combinations
from copy import deepcopy
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(temp):
    q = deque(virus)
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx,ny = a+dx[i],b+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    q.append((nx,ny))

def count(temp):
    res = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                res += 1
    return res


n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
zero = []
virus = []
real_res = -1
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            zero.append((i,j))
        if graph[i][j] == 2:
            virus.append((i,j))

# 3개 벽 세우기
for x in combinations(zero, 3):
    temp = deepcopy(graph)
    for i,j in x:
        temp[i][j] = 1
    bfs(temp)
    res_temp = count(temp)
    real_res = max(res_temp, real_res)

print(real_res)