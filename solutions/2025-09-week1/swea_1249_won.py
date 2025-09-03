from collections import deque
T = int(input())
 
for test_case in range(1, T + 1):
    N = int(input())
 
    my_list = [list(map(int, input().strip())) for _ in range(N)]
 
    Q = deque()
 
    result_list = [[-2] * N for _ in range(N)]
 
    result_list[0][0] = 0
    result_list[N-1][N-1] = -1
 
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
 
    Q.append((0, 0))
 
    while Q:
        y, x = Q.popleft()
 
        cur_value = result_list[y][x]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
 
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
 
            if result_list[ny][nx] == -1:                        # 목적지면 값만 옮기고 continue
                result_list[ny][nx] = cur_value
                continue
 
            if result_list[ny][nx] == -2 or result_list[ny][nx] > cur_value + my_list[ny][nx]:   # 첫 방문이거나 원래 값이 더 크다면 갱신
                result_list[ny][nx] = cur_value + my_list[ny][nx]
                Q.append((ny, nx))
 
    print(f"#{test_case} {result_list[N-1][N-1]}")
