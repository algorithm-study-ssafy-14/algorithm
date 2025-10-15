from collections import deque

N = int(input().strip())
K = int(input().strip())

apples = set()
for _ in range(K):
    s, e = map(int, input().split())
    apples.add((s - 1, e - 1))

L = int(input().strip())
turns = deque()
for _ in range(L):
    s, e = input().split()
    turns.append((int(s), e))

# 우, 하, 좌, 상
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dir_idx = 0

snake = deque([(0, 0)])
arr = [[0] * N for _ in range(N)]
arr[0][0] = 1

time = 0
y, x = 0, 0

while True:
    dy, dx = dirs[dir_idx]
    ny, nx = y + dy, x + dx
    time += 1

    # 벽 충돌
    if ny < 0 or ny >= N or nx < 0 or nx >= N:
        print(time)
        break

    # 꼬리 충돌
    if arr[ny][nx] == 1:
        print(time)
        break

    # 일단 머리를 이동시킴. 만약 이동한 곳에 사과가 있다면 꼬리는 유지, 없으면 꼬리를 제거
    snake.append((ny, nx))
    arr[ny][nx] = 1

    if (ny, nx) in apples:
        apples.remove((ny, nx))
    else:
        # 이동할 곳에 사과가 없으면 꼬리를 제거
        ty, tx = snake.popleft()
        arr[ty][tx] = 0

    if turns and turns[0][0] == time:
        i, d = turns.popleft()
        if d == 'D':
            dir_idx = (dir_idx + 1) % 4
        else:
            dir_idx = (dir_idx + 3) % 4

    y, x = ny, nx
