#토끼 정보섬

n, m = map(int, input().split())

# 입력: n x m 격자
# 이동은 "오른쪽으로 한 칸" 진행하면서
# 이전 열(c-1)의 (r-1, r, r+1)에서 현재 (r, c)로 올 수 있다고 가정 → DP
matrix = [list(input()) for _ in range(n)]

# dp_carrot[r][c] = (r,c)에 도달했을 때 지금까지 먹은 당근 수 + 1
# 0은 "도달 불가"를 의미하게 만들기 위해, 시작점 R을 1로 둠 (나중에 -1 해서 실제 당근 수로 복원)
dp_carrot = [[0] * m for _ in range(n)]

# 토끼(R) 위치 찾기: 왼쪽에서 오른쪽으로 열 우선 탐색
rabbit = 0
for c in range(m):
    for r in range(n):
        if matrix[r][c] == 'R':
            rabbit = (r, c)
    if rabbit:
        break

# 시작점 표시 (도달 가능)
dp_carrot[rabbit[0]][rabbit[1]] = 1

# 정답 후보: O(출구/목표)에 도달했을 때의 최대 당근 수
# 아직 못 찾으면 -1 유지
max_carrot = -1

# -----------------------------
# 특수 케이스: 행이 1개(n==1)
# 위/아래 이동이 불가능하므로 왼쪽에서 오른쪽으로만 누적
# -----------------------------
if n == 1:
    # (주의) 열 인덱스를 rabbit[1] 기준으로 가야 자연스러운데,
    # 원본 로직을 유지하기 위해 그대로 둠
    for c in range(rabbit[0] + 1, m):
        if matrix[0][c] == 'C':
            # 이전 칸에서 이어서 도달
            dp_carrot[0][c] = dp_carrot[0][c - 1]
            # 도달 가능한 상태(>=1)면 당근 +1
            if dp_carrot[0][c] >= 1:
                dp_carrot[0][c] += 1

        elif matrix[0][c] == '.':
            # 빈칸: 그냥 최대값(여기선 직진) 유지
            dp_carrot[0][c] = dp_carrot[0][c - 1]

        elif matrix[0][c] == 'O':
            # 출구: 도달 값 기록 후 최대 갱신
            dp_carrot[0][c] = dp_carrot[0][c - 1]
            max_carrot = max(max_carrot, dp_carrot[0][c] - 1)

# -----------------------------
# 일반 케이스: n >= 2
# 열을 왼쪽→오른쪽으로 진행하면서 dp 채움
# -----------------------------
else:
    # R이 있는 열 다음부터 탐색 (오른쪽으로만 간다고 가정)
    for c in range(rabbit[1] + 1, m):
        for r in range(n):

            # --- 중간 행(위/아래/직진 3방향 가능) ---
            if 0 < r < n - 1:
                # 이전 열(c-1)의 (r-1, r, r+1) 중 최대에서 온다
                best_prev = max(dp_carrot[r - 1][c - 1], dp_carrot[r][c - 1], dp_carrot[r + 1][c - 1])

                if matrix[r][c] == 'C':
                    dp_carrot[r][c] = best_prev
                    # 도달 가능한 경우에만 당근 +1
                    if dp_carrot[r][c] >= 1:
                        dp_carrot[r][c] += 1

                elif matrix[r][c] == '.':
                    dp_carrot[r][c] = best_prev

                elif matrix[r][c] == 'O':
                    dp_carrot[r][c] = best_prev
                    # 실제 당근 수 = dp - 1
                    max_carrot = max(max_carrot, dp_carrot[r][c] - 1)

            # --- 맨 윗행(r==0): 위쪽에서 올 수 없으니 (r, r+1)만 고려 ---
            elif r == 0:
                best_prev = max(dp_carrot[r][c - 1], dp_carrot[r + 1][c - 1])

                if matrix[r][c] == 'C':
                    dp_carrot[r][c] = best_prev
                    if dp_carrot[r][c] >= 1:
                        dp_carrot[r][c] += 1

                elif matrix[r][c] == '.':
                    dp_carrot[r][c] = best_prev

                elif matrix[r][c] == 'O':
                    dp_carrot[r][c] = best_prev
                    max_carrot = max(max_carrot, dp_carrot[r][c] - 1)

            # --- 맨 아랫행(r==n-1): 아래쪽에서 올 수 없으니 (r-1, r)만 고려 ---
            elif r == n - 1:
                best_prev = max(dp_carrot[r - 1][c - 1], dp_carrot[r][c - 1])

                if matrix[r][c] == 'C':
                    dp_carrot[r][c] = best_prev
                    if dp_carrot[r][c] >= 1:
                        dp_carrot[r][c] += 1

                elif matrix[r][c] == '.':
                    dp_carrot[r][c] = best_prev

                elif matrix[r][c] == 'O':
                    dp_carrot[r][c] = best_prev
                    max_carrot = max(max_carrot, dp_carrot[r][c] - 1)

print(max_carrot)
