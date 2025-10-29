from itertools import combinations
from collections import deque

N, M = map(int, input().split())

boards = [list(map(int, input().split())) for _ in range(N)]

v_pos = []                                  # 바이러스 위치
empty_cnt = 0                               # 빈 칸. 모든 칸이 채워졌는지를 확인하기 위함.

for i in range(N):
    for j in range(N):
        if boards[i][j] == 2:
            v_pos.append((i, j))
        elif boards[i][j] == 0:
            empty_cnt += 1

if not empty_cnt:                           # 빈 칸이 없다면 0 출력
    print(0)
    exit(0)

result = 21e10
for viruss in combinations(v_pos, M):       # v_pos 에서 M 개 만큼을 뽑음
    q = deque()
    dist = [[-1] * N for _ in range(N)]

    max_time = 0
    filled_squares = 0                      # 모든 칸이 채워졌는지 체크하기 위함

    for virus in viruss:                    # 뽑은 바이러스들을 큐에 넣고, dist 도 0으로 갱신
        q.append(virus)
        dist[virus[0]][virus[1]] = 0

    while q:
        y, x = q.popleft()

        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = y + dy, x + dx

            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue
            if dist[ny][nx] != -1:                              # 이전에 방문한 곳이면 패스
                continue
            if boards[ny][nx] == 1:                             # 벽이면 패스
                continue

            dist[ny][nx] = dist[y][x] + 1                       # dist 갱신
            q.append((ny, nx))

            if boards[ny][nx] == 0:
                filled_squares += 1

                if dist[ny][nx] > max_time:                     # dist 가 max_time 보다 크다면 max_time 갱신
                    max_time = dist[ny][nx]                     # 빈 칸에 바이러스를 퍼뜨리는 최소 시간이라 boards == 0 일 때만 갱신함.

    if filled_squares == empty_cnt:                             # 모든 칸이 채워졌을 때만 result 갱신
        result = min(result, max_time)

print(-1 if result == 21e10 else result )