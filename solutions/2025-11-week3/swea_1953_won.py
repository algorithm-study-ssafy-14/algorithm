from collections import deque

T = int(input())

MOVES = [
    [],
    [(1, 0), (-1, 0), (0, 1), (0, -1)],  # 1, 상하좌우
    [(1, 0), (-1, 0)],  # 2, 상하
    [(0, 1), (0, -1)],  # 3, 좌우
    [(-1, 0), (0, 1)],  # 4
    [(1, 0), (0, 1)],  # 5
    [(1, 0), (0, -1)],  # 6
    [(-1, 0), (0, -1)],  # 7
]

OPPOSITE = {(-1, 0): (1, 0), (1, 0): (-1, 0), (0, 1): (0, -1), (0, -1): (0, 1)}  # 반대 방향

for test_case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())  # 세로, 가로, 맨홀 세로, 가로, 소요시간

    boards = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0] * M for _ in range(N)]
    q = deque()
    q.append((R, C, 1))
    result = 1  # 시간, 맨홀에 들어가는것부터 1시간
    visited[R][C] = 1

    while q:
        y, x, t = q.popleft()  # 좌표, 시간

        if t == L:
            continue

        pipe = boards[y][x]  # 현재 파이프
        for dy, dx in MOVES[pipe]:

            ny, nx = y + dy, x + dx

            if nx < 0 or nx >= M or ny < 0 or ny >= N:  # 범위 체크
                continue

            if boards[ny][nx] == 0:  # 파이프 가 없으면
                continue

            if OPPOSITE[(dy, dx)] not in MOVES[boards[ny][nx]]:  # 현재 파이프와 이동할 파이프와 연결되어 있는지
                continue

            if visited[ny][nx]:
                continue

            result += 1
            visited[ny][nx] = 1
            q.append((ny, nx, t + 1))

    print(f"#{test_case} {result}")