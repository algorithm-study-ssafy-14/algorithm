from itertools import combinations
from collections import deque

n, a = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

virus = [(r, c) for r in range(n) for c in range(n) if matrix[r][c] == 2]
dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def bfs(active):
    q = deque(active)
    visited = [[-1] * n for _ in range(n)]
    for r, c in active:
        visited[r][c] = 0

    spread_cnt = 0
    max_time = 0

    while q:
        r, c = q.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                if matrix[nr][nc] != 1 and visited[nr][nc] == -1:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))
                    if matrix[nr][nc] == 0:
                        spread_cnt += 1
                        max_time = max(max_time, visited[nr][nc])

    if spread_cnt == zero_cnt:
        return max_time
    else:
        return 1000

zero_cnt = sum(row.count(0) for row in matrix)

min_result = 10**9
for case in combinations(virus, a):
    min_result = min(min_result, bfs(case))

print(-1 if min_result == 1000 else min_result)
