from collections import deque

# 8방향(상,하,좌,우 + 대각선) 이동을 위한 방향 벡터
# (r, c)에서 각각 더해주며 주변 칸을 탐색한다.
dir_r = [1, 1, 1, 0, 0, -1, -1, -1]
dir_c = [1, 0, -1, 1, -1, 1, 0, -1]

def bfs(r, c):
    """
    (r, c)가 '0칸(주변 지뢰가 하나도 없는 칸)'일 때,
    한 번 클릭했을 때 연쇄적으로 열리는 칸들을 모두 방문 처리하는 BFS 함수
    """
    basket = deque([(r, c)])   # BFS를 위한 큐(덱), 시작 좌표를 넣고 시작
    while basket:
        p, q = basket.popleft()
        # 현재 칸(p, q) 기준으로 8방향 탐색
        for i in range(8):
            np = p + dir_r[i]
            nq = q + dir_c[i]
            # 범위 안이고 아직 방문하지 않은 칸만 고려
            if 0 <= np < n and 0 <= nq < n and not visited[np][nq]:
                visited[np][nq] = 1   # 방문 처리
                # 주변 지뢰 개수가 0인 칸('.')이면 큐에 넣어서 계속 퍼뜨리기
                if matrix[np][nq] == '.':
                    basket.append((np, nq))


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    # 지뢰판 입력 받기: '*'는 지뢰, '.'는 아직 숫자 계산 전의 빈 칸
    matrix = [list(input()) for _ in range(n)]

    # 1단계: 각 칸에 대해 주변에 지뢰가 있는지 확인해서
    #       지뢰가 하나라도 있으면 그 칸을 1(숫자칸)로 바꾼다.
    #       주변 지뢰가 하나도 없으면 그대로 '.'(0칸)으로 남겨둔다.
    for r in range(n):
        for c in range(n):
            # 지뢰가 아닌 빈 칸에 대해서만 주변 지뢰 존재 여부 확인
            if matrix[r][c] == '.':
                for i in range(8):
                    nr = r + dir_r[i]
                    nc = c + dir_c[i]
                    if 0 <= nr < n and 0 <= nc < n:
                        # 주변에 지뢰('*')가 하나라도 있으면 숫자칸으로 표시(여기서는 그냥 1로 통일)
                        if matrix[nr][nc] == '*':
                            matrix[r][c] = 1
                            break
    # print(matrix)  # 디버깅용

    # 방문 여부를 기록할 배열
    visited = [[0] * n for _ in range(n)]
    cnt = 0   # 최소 클릭 횟수

    # 2단계: 주변 지뢰가 0개인 칸('.')부터 먼저 처리
    #   -> 이 칸을 한 번 클릭하면 BFS로 주변의 '.'과 그 인접 숫자칸까지 한 번에 열린다.
    for r in range(n):
        for c in range(n):
            # 아직 방문하지 않은 0칸('.')을 발견하면 새로운 클릭이 필요
            if matrix[r][c] == '.' and not visited[r][c]:
                cnt += 1               # 이 칸을 한 번 클릭
                visited[r][c] = 1      # 방문 처리
                bfs(r, c)              # 연쇄적으로 열리는 칸들 모두 방문

    # print용 디버깅 코드
    # for i in matrix:
    #     print(*i)
    # print()
    # for i in visited:
    #     print(*i)

    # 3단계: 아직 열리지 않은 숫자칸(1)은
    #        인접한 0칸이 없어서 자동으로 안 열렸으므로
    #        각각 개별적으로 한 번씩 클릭해줘야 한다.
    for r in range(n):
        for c in range(n):
            if matrix[r][c] == 1 and not visited[r][c]:
                cnt += 1

    # 테스트 케이스 번호와 함께 정답 출력
    print(f"#{tc} {cnt}")
