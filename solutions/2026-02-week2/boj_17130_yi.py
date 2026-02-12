n, m = map(int, input().split())
island = [list(input()) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]

## 토끼 찾기
rab_x, rab_y = 0, 0
find = False
for i in range(n):
    for j in range(m):
        if island[i][j] == "R":
            rab_x = i
            rab_y = j
            dp[rab_x][rab_y] = 0
            find = True
            break
    if find:
        break

## 토끼 움직이는 방향
move_x = [1, 0, -1]
move_y = [1, 1, 1]

## 토끼 있는 열부터 마지막 열까지 이동
for i in range(rab_y, m - 1):
    for j in range(n):
        if dp[j][i] == -1:
            continue
        for k in range(3):
            mx = i + move_y[k]
            my = j + move_x[k]
            if 0 <= mx < m and 0 <= my < n:
                carrot = 0
                if island[my][mx] != "#":
                    if island[my][mx] == "C": ## 당근 찾음
                        carrot = 1
                    else:
                        carrot = 0
                    dp[my][mx] = max(dp[my][mx], dp[j][i] + carrot)

res = -1
for i in range(n):
    for j in range(m):
        if island[i][j] == "O": ## 쪽문마다 당근 최댓값 확인
            if res < dp[i][j]:
                res = dp[i][j]

print(res)