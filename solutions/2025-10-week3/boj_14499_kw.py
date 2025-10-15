def roll(move):
    if move == 1:  # 동쪽
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[4], dice[2], dice[1], dice[6], dice[5], dice[3]
    elif move == 2:  # 서쪽
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[3], dice[2], dice[6], dice[1], dice[5], dice[4]
    elif move == 3:  # 북쪽
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[5], dice[1], dice[3], dice[4], dice[6], dice[2]
    elif move == 4:  # 남쪽
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[2], dice[6], dice[3], dice[4], dice[1], dice[5]


N, M, y, x, K = map(int, input().split())  # 좌표를 (x,y) 로 줌. 그래서 반대로 받음
arr = [list(map(int, input().split())) for _ in range(N)]

dice_move = list(map(int, input().split()))

dice = [0] * 7  # 1 ~ 6 사용
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in dice_move:
    nx = x + dx[i - 1]
    ny = y + dy[i - 1]

    if nx < 0 or nx >= M or ny < 0 or ny >= N:
        continue

    roll(i)

    if arr[ny][nx] == 0:  # 0 일 때
        arr[ny][nx] = dice[6]
    else:
        dice[6] = arr[ny][nx]
        arr[ny][nx] = 0

    print(dice[1])

    x, y = nx, ny