#벌통의 최댓값을 구하기 위한 과정

def dfs(a_list, start, First=False):
    if First:
        First = False
        global a_max, a_sum, mini_sum
        mini_sum = 0
        a_sum = 0
        a_max = 0

    #M값이 됐을 경우 탈출(
    if start >= len(a_list):
        return

    #dfs 재귀 시작, 중복 탐색을 피하기 위해서 start로 시작값 한정
    for i in range(start, len(a_list)):

        #C를 초과하지 않는 한에서 dfs 시작
        if mini_sum + a_list[i] <= C:
            mini_sum += a_list[i]
            a_sum += a_list[i] ** 2

            #max값 최신화
            if a_max <= a_sum:
                a_max = a_sum

            #재귀 호출
            dfs(a_list, i + 1)

            #재귀 종료 후 복귀
            mini_sum -= a_list[i]
            a_sum -= a_list[i] ** 2

T = int(input())
dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

for tc in range(1, T + 1):
    N, M, C = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    #여기에 값을 적어둠.
    memo = [[0] * N for _ in range(N)]


    for r in range(N):
        for c in range(N - M + 1):

            #벌통 후보를 담음
            a_list = []
            for distortion in range(M):
                a_list.append(matrix[r][c + distortion])

            #메모에 값을 기록하기 위한 dfs
            dfs(a_list, 0, True)
            memo[r][c] = a_max

    total_max = 0
    # 작업자 A
    for r in range(N):
        for c in range(N):
            num1 = memo[r][c]

            #작업자 B
            #중복순열을 약간이라도 피하기 위한 (r,N)
            for n in range(r,N):
                for m in range(N):

                    #A가 수집하는 곳을 B가 수집하지 않게 하기 위한 방어장치
                    if r == n and m < c + M:
                        continue
                    num2 = memo[n][m]
                    if total_max < memo[r][c] + memo[n][m]:
                        total_max = memo[r][c] + memo[n][m]

    print(f"#{tc} {total_max}")