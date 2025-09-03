T = int(input())
 
 
# 방향, 현재 위치, 방문 노드 값 저장, 시작위치 인덱스
def dfs(d, c_y, c_x, p_list, val_list, s_idx_y, s_idx_x, turn):
    global result
 
    direction = [(1, 1), (1, -1), (-1, -1), (-1, 1)]  # 오른쪽 대각 아래, 왼쪽 대각 아래, 왼쪽 대각 위, 오른쪽 대각 위
 
    # 현재 위치에서 이동할 수 있는지 확인 후 이동하거나 아니면 return
    nx = c_x + direction[d][1]
    ny = c_y + direction[d][0]
 
    if nx < 0 or nx >= N or ny < 0 or ny >= N:
        return
 
    # 시작점 확인
    if nx == s_idx_x and ny == s_idx_y:
        if len(val_list) >= 4 and turn == 3:
            result = max(result, len(val_list))
     
    # 중복 확인
    for val in val_list:
        if val == p_list[ny][nx]:
            return
     
    # 방문
    val_list.append(p_list[ny][nx])
    dfs(d, ny, nx, p_list, val_list, s_idx_y, s_idx_x, turn)
     
    # 회전
    if turn < 3:
        nd = (d + 1) % 4
        dfs(nd, ny, nx, p_list, val_list, s_idx_y, s_idx_x, turn + 1)
 
    # 원상 복귀
    val_list.pop()
 
 
for test_case in range(1, T + 1):
 
    N = int(input().strip())
 
    my_list = [list(map(int, input().split())) for _ in range(N)]
 
    result = -1
 
    # 열에서 0 과 N-1 은 사각형을 만들 수 없으니까 제외
    # 행에서 N-2 는 사각형을 만들 수 없으니까 제외
 
    for i in range(N-2):
        for j in range(1, N-1):
            value_list = [my_list[i][j]]
            dfs(0, i, j, my_list, value_list, i, j, 0)
 
    print(f"#{test_case} {result}")
