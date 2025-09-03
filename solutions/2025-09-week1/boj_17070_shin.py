# 입력값 크기를 보고 DP로 접근해야겠다는 생각, 판을 잘 깔면 +로 해결할 수 있겠다는 생각.
def DP(level, r, c):

    #-1 인덱스 값을 참조할 것에 대비
    if r < 0 or c < 0:
        return 0

    #메모이제이션 판단, -1일 경우 메모, 아닐 경우 해당 값을 참조
    if memo[level][r][c] != -1:
        return memo[level][r][c]

    #메모이제이션 / 점화식 시작

    #벽이 있을 경우 해당 모든 차원의 메모를 0으로 입력
    if matrix[r][c] == 1:
        memo[0][r][c] = memo[1][r][c] = memo[2][r][c] = 0
        return 0

    # 0일경우 파이프가 수직 방향, 1일 경우 대각선 방향, 2일 경우 수평 방향
    if level == 0:
        memo[0][r][c] = DP(0, r - 1, c) + DP(1, r - 1, c)

    # 대각선 방향일 경우 양쪽 벽 확인, 벽 있을시 0으로 메모 및 리턴
    elif level == 1:
        if matrix[r][c-1] == 1 or matrix[r-1][c] == 1:
            memo[1][r][c] = 0
            return 0
        memo[1][r][c] = DP(0, r - 1, c - 1) + DP(1, r - 1, c - 1) + DP(2, r - 1, c - 1)

    #0의 경우와 동일
    else:
        memo[2][r][c] = DP(1, r, c - 1) + DP(2, r, c - 1)

    return memo[level][r][c]


N = int(input())
dirs = [(0, 1), (1, 1), (1, 0)]
matrix = [list(map(int, input().split())) for _ in range(N)]
counter = [[0] * N for _ in range(N)]
#메모판, 3차원
memo = [[[-1] * N for _ in range(N)] for _ in range(3)]

#파이프가 깔린 방향, 시작점.
memo[2][0][1] = 1

print(DP(0, N - 1, N - 1) + DP(1, N - 1, N - 1) + DP(2, N - 1, N - 1))