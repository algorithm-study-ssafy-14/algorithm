N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

dice = [0] * 6

dirs = {
    1: (0, 1),   # 동
    2: (0, -1),  # 서
    3: (-1, 0),  # 북
    4: (1, 0),   # 남
}

def roll(dice, cmd):
    if cmd == 1: 
        tmp = dice[0]
        dice[0] = dice[5]
        dice[5] = dice[1]
        dice[1] = dice[4]
        dice[4] = tmp
    elif cmd == 2: 
        tmp = dice[0]
        dice[0] = dice[4]
        dice[4] = dice[1]
        dice[1] = dice[5]
        dice[5] = tmp
    elif cmd == 3:  
        tmp = dice[0]
        dice[0] = dice[3]
        dice[3] = dice[1]
        dice[1] = dice[2]
        dice[2] = tmp
    elif cmd == 4: 
        tmp = dice[0]
        dice[0] = dice[2]
        dice[2] = dice[1]
        dice[1] = dice[3]
        dice[3] = tmp

for cmd in commands:
    dx, dy = dirs[cmd]
    nx, ny = x + dx, y + dy
    if not (0 <= nx < N and 0 <= ny < M):
        continue  
    x, y = nx, ny
    roll(dice, cmd)
    if board[x][y] == 0:
        board[x][y] = dice[1]
    else:
        dice[1] = board[x][y]
        board[x][y] = 0
    print(dice[0])
