from collections import deque


def bfs():
    visited = [[1000] * n for _ in range(n)]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 0

    while queue:
        a, b= queue.popleft()
        for i, j in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            ni, nj = a + i, b + j
            if 0 <= ni < n and 0 <= nj < n:
                new_cost = visited[a][b] + graph[ni][nj]
                if new_cost < visited[ni][nj]:
                    visited[ni][nj] = new_cost
                    queue.append((ni, nj))
    return visited[n-1][n-1]


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    graph = [list(map(int, input())) for _ in range(n)]
    print(f"#{test_case} {bfs()}")