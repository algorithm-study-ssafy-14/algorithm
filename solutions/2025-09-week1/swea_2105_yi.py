def dfs(sx, sy, x, y, d, cnt, eaten):
    global result
    dx = [1, 1, -1, -1]
    dy = [1, -1, -1, 1]

    for i in range(d, 4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if nx == sx and ny == sy and cnt >= 4:
                result = max(result, cnt)
                return

            if arr[nx][ny] not in eaten:
                dfs(sx, sy, nx, ny, i, cnt + 1, eaten + [arr[nx][ny]])


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = -1

    for i in range(N):
        for j in range(N):
            dfs(i, j, i, j, 0, 1, [arr[i][j]])

    print(f"#{tc} {result}")
