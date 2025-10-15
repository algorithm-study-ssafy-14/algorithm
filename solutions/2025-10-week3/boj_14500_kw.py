tetrominoss = [
    [(0, 1), (0, 2), (0, 3)], [(1, 0), (2, 0), (3, 0)],  # -
    [(0, 1), (1, 0), (1, 1)],  # ㅁ
    [(1, 0), (2, 0), (2, 1)], [(0, 1), (0, 2), (1, 0)],  # ㄴ
    [(0, 1), (1, 1), (2, 1)], [(0, 1), (0, 2), (-1, 2)],
    [(1, 0), (2, 0), (2, -1)], [(0, 1), (0, 2), (1, 2)],
    [(1, 0), (2, 0), (0, 1)], [(1, 0), (1, 1), (1, 2)],
    [(1, 0), (1, 1), (2, 1)], [(0, -1), (1, -1), (1, -2)],  # ㄹ
    [(1, 0), (1, -1), (2, -1)], [(0, 1), (1, 1), (1, 2)],
    [(1, 0), (1, 1), (1, -1)], [(1, 0), (1, 1), (2, 0)],  # ㅗ
    [(0, -1), (1, 0), (0, 1)], [(0, 1), (-1, 1), (1, 1)],
]


def solve(y, x, p_t):
    res = arr[y][x]

    for dy, dx in p_t:
        ny = y + dy
        nx = x + dx

        # 범위 밖으로 나가게 되면 0 리턴
        if nx < 0 or nx >= M or ny < 0 or ny >= N:
            return 0

        res += arr[ny][nx]
    return res


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

result = 0
for i in range(N):
    for j in range(M):
        for tetrominos in tetrominoss:
            cur = solve(i, j, tetrominos)
            result = max(cur, result)

print(result)