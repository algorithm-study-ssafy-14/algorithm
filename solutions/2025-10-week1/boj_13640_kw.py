from collections import deque


def roll(y, x, dy, dx, board):  # 벽까지 굴림.
    move_cnt = 0
    while True:
        ny, nx = y + dy, x + dx
        cell = board[ny][nx]
        if cell == '#':
            break
        y, x = ny, nx
        move_cnt += 1
        if cell == 'O':
            return y, x, move_cnt, True
    return y, x, move_cnt, False


def solve():
    N, M = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(N)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    ry = rx = by = bx = -1  # R, B
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':  # R, B 값만 저장하고 . 으로 밀어줌
                ry, rx = i, j
                board[i][j] = '.'
            elif board[i][j] == 'B':
                by, bx = i, j
                board[i][j] = '.'

    visited = [[[[False] * M for _ in range(N)] for __ in range(M)] for ___ in range(N)]
    visited[ry][rx][by][bx] = True

    q = deque()
    q.append((ry, rx, by, bx, 0))

    while q:
        cur_ry, cur_rx, cur_by, cur_bx, cnt = q.popleft()
        if cnt >= 10:
            continue

        for d in range(4):
            new_ry, new_rx, r_move, r_hole = roll(cur_ry, cur_rx, dy[d], dx[d], board)
            new_by, new_bx, b_move, b_hole = roll(cur_by, cur_bx, dy[d], dx[d], board)

            if b_hole:
                continue

            if r_hole and not b_hole:
                print(cnt + 1)
                return

            # R, B 가 같은 위치라면 더 많이 이동한 공이 뒤에서 출발한 것이므로 한 칸 뒤로 보냄
            if new_ry == new_by and new_rx == new_bx:
                if r_move > b_move:
                    new_ry -= dy[d]
                    new_rx -= dx[d]
                else:
                    new_by -= dy[d]
                    new_bx -= dx[d]

            if not visited[new_ry][new_rx][new_by][new_bx]:
                visited[new_ry][new_rx][new_by][new_bx] = True
                q.append((new_ry, new_rx, new_by, new_bx, cnt + 1))

    print(-1)


solve()
