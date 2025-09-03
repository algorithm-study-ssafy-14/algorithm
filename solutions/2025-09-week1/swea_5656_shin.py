
# 전체적인 큰 틀
def dfs(depth, matrix):
    global min_a

    if min_a == 0:
        return

    #K번 발사 시 결과 확인
    if depth == K:
        count = 0
        for row in matrix:
            count += row.count(0)

        if min_a > N * M - count:
            min_a = N * M - count

        return

    #굳이 없어도 됨, 2 이상의 값 행렬에 없을 시 빠르게 계산하고 리턴
    check = False
    for p in range(N):
        if check:
            break

        for q in range(M):
            if matrix[p][q] > 1:
                check = True
                break
    # 2 주어진 판에 2 이상이 없다면 계산 후 함수 리턴
    if not check:
        mini_count = 0
        for p in range(N):
            mini_count += sum(matrix[p])

        if mini_count > K - depth:
            mini_count -= (K - depth)
        else:
            mini_count = 0

        if min_a > mini_count:
            min_a = mini_count

        return

    # 벽돌깨기 시작, 위부터 순회하며 1 이상인 값 마주치면 깨짐, 2 이상일경우 추가적인 재귀
    else:
        for c in range(M):
            for r in range(N):
                if matrix[r][c] != 0:
                    if matrix[r][c] == 1:
                        matrix[r][c] = 0
                        dfs(depth + 1, matrix)
                        matrix[r][c] = 1
                        break

                    else:
                        saved = [row[:] for row in matrix]

                        # 2 이상일 경우 explosion 재귀
                        explosion(r, c, saved)
                        gravity(saved)
                        dfs(depth + 1, saved)
                        break

# 크기 2 이상의 폭발
def explosion(r, c, matrix):

    #값을 바꿔주지 않으면 서로 폭발이 일어나 무한루프에 빠지게 됨, 따라서 미리 값 저장 후 재귀 시작
    power = matrix[r][c]
    matrix[r][c] = 0
    for dr, dc in dirs:
        for pow in range(1, power):
            nr = r + dr * pow
            nc = c + dc * pow
            if nr >= N or nc >= M or nr < 0 or nc < 0:
                break
            if matrix[nr][nc] != 0:
                if matrix[nr][nc] == 1:
                    matrix[nr][nc] = 0
                else:
                    explosion(nr, nc, matrix)

#중력 작용
def gravity(matrix):
    for c in range(M):
        #한 번에 내릴 수 있었는데 한 칸씩 내림.
        for r in range(N - 1, -1, -1):
            if matrix[r][c] == 0:
                dist = 1
                while r - dist >= 0:
                    if matrix[r - dist][c] == 0:
                        dist += 1
                    else:
                        matrix[r][c] = matrix[r - dist][c]
                        matrix[r - dist][c] = 0
                        break

#입력값, 메인명령
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
T = int(input())
for tc in range(1, T + 1):
    K, M, N = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    min_a = 200
    dfs(0, matrix)
    #min값 변경 x시 : 중간에 종료됐을 경우 min값 갱신이 되지 않으므로.
    if min_a == 200:
        min_a = 0
    print(f"#{tc} {min_a}")