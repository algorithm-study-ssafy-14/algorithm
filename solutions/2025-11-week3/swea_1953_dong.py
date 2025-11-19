## 탈주범 검거

from collections import deque

# bfs 탐색
def bfs(start):
    basket = deque([start])
    check_mat[start[0]][start[1]] = 1
    
    # T 시간동안의 경로 추적
    for _ in range(T):
        a_len = len(basket)
        for _ in range(a_len):
            r, c = basket.popleft()
            for dr, dc in dir_mat[matrix[r][c]]:
                nr = r + dr
                nc = c + dc

                # 이동하고자 하는 방향에 따라서 그 방향을 갈 수 있는지 결정
                # 가는 방향, 가고자 하는 방향 2개를 판별하며 진행.
                if 0 <= nr < N and 0 <= nc < M and not check_mat[nr][nc]:
                    if dr == 1:
                        if matrix[nr][nc] in (1, 2, 4, 7):
                            check_mat[nr][nc] = 1
                            basket.append([nr, nc])
                    elif dr == -1:
                        if matrix[nr][nc] in (1, 2, 5, 6):
                            check_mat[nr][nc] = 1
                            basket.append([nr, nc])
                    elif dc == 1:
                        if matrix[nr][nc] in (1, 3, 6, 7):
                            check_mat[nr][nc] = 1
                            basket.append([nr, nc])
                    elif dc == -1:
                        if matrix[nr][nc] in (1, 3, 4, 5):
                            check_mat[nr][nc] = 1
                            basket.append([nr, nc])

    sum_a = 0
    for i in check_mat:
        sum_a += i.count(1)

    return sum_a - len(basket)


# ======================================================================

# 테트리스처럼 모양을 직접 좌표로 만듦.
dir_mat = [[],
           [(1, 0), (-1, 0), (0, 1), (0, -1)],
           [(1, 0), (-1, 0)],
           [(0, 1), (0, -1)],
           [(-1, 0), (0, 1)],
           [(1, 0), (0, 1)],
           [(0, -1), (1, 0)],
           [(0, -1), (-1, 0)]]

T = int(input())
for tc in range(1, T + 1):
    # 맵크기NM / 맨홀위치RC, 소요 시간
    N, M, R, C, T = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 방문 표시
    check_mat = [[0] * M for _ in range(N)]
    result = bfs([R, C])

    print(f"#{tc} {result}")