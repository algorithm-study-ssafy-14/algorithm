import itertools
from copy import deepcopy
from collections import deque
N, M = map(int, input().split())

boards = [list(map(int, input().split())) for _ in range(N)]

v_pos = []                                                # 바이러스
empty_pos = []                                            # 빈 공간 (combination 을 사용하기 위함)

for i in range(N):
    for j in range(M):
        if boards[i][j] == 2:
            v_pos.append((i, j))
        elif boards[i][j] == 0:
            empty_pos.append((i, j))

best = 0

for w1, w2, w3 in itertools.combinations(empty_pos, 3):  # 빈 공간에서 3곳을 뽑음
    temp = deepcopy(boards)                              # 조합마다 복사본을 만들어서 시뮬레이션함.
    for wy, wx in [w1, w2, w3]:
        temp[wy][wx] = 1                                 # 벽으로 만들어줌.

    q = deque(v_pos)

    while q:
        y, x = q.popleft()
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if temp[ny][nx] != 0:
                continue
            temp[ny][nx] = 2
            q.append((ny, nx))

    sub_res = 0

    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                sub_res += 1

    if best < sub_res:
        best = sub_res

print(best)