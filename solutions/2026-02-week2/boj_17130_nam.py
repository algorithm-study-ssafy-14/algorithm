<<<<<<< HEAD
import sys
sys.stdin = open('17130_rabbit_island.txt', 'r')
input = sys.stdin.readline

T = int(input())

for i in range(1, T + 1):

    N, M = map(int, input().split())
    arr = list(input().strip() for _ in range(N))

    for r in range(N):
        for c in range(M):  
            if arr[r][c] == 'R':
                start = r, c

    max_carrot = -1
    dp = [[-1] * M for _ in range(N)]

    dr = [0, 1, -1]
    dc = [1, 1, 1]

    def recur(start, C_cnt):
        global max_carrot
        r, c = start

        if dp[r][c] >= C_cnt:
            return
        dp[r][c] = C_cnt

        for dir in range(3):
            nr = r + dr[dir]
            nc = c + dc[dir]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != '#':
                pos = arr[nr][nc]

                if pos == 'O':
                    max_carrot = max(max_carrot, C_cnt)
                    continue

                if pos == 'C':
                    recur((nr, nc), C_cnt + 1)
                else:
                    recur((nr, nc), C_cnt)

    recur(start, 0)
=======
import sys
sys.stdin = open('17130_rabbit_island.txt', 'r')
input = sys.stdin.readline

T = int(input())

for i in range(1, T + 1):

    N, M = map(int, input().split())
    arr = list(input().strip() for _ in range(N))

    for r in range(N):
        for c in range(M):  
            if arr[r][c] == 'R':
                start = r, c

    max_carrot = -1
    dp = [[-1] * M for _ in range(N)]

    dr = [0, 1, -1]
    dc = [1, 1, 1]

    def recur(start, C_cnt):
        global max_carrot
        r, c = start

        if dp[r][c] >= C_cnt:
            return
        dp[r][c] = C_cnt

        for dir in range(3):
            nr = r + dr[dir]
            nc = c + dc[dir]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != '#':
                pos = arr[nr][nc]

                if pos == 'O':
                    max_carrot = max(max_carrot, C_cnt)
                    continue

                if pos == 'C':
                    recur((nr, nc), C_cnt + 1)
                else:
                    recur((nr, nc), C_cnt)

    recur(start, 0)
>>>>>>> 280e96fcda6729f8af56bedf8d028218ba919eff
    print(max_carrot)