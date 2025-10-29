N = int(input())

boards = [list(map(int, input().split())) for _ in range(N)]

total_population = sum(sum(row[:]) for row in boards[:])
result = 1e9

for y in range(N):           # 끝에 줄들은 마름모를 만들 수 없음
    for x in range(N):
        for d1 in range(1, N):  # d1, d2 는 1부터 시작
            for d2 in range(1, N):
                if y + d1 + d2 > N - 1:
                    continue

                if x - d1 < 0:
                    continue

                if x + d2 > N - 1:
                    continue

                num_boards = [[0] * N for _ in range(N)]

                # 5 경계선 채우기
                for i in range(d1 + 1):
                    num_boards[y + i][x - i] = 5               # 기준점에서 ↙
                    num_boards[y + d2 + i][x + d2 - i] = 5     # 기준점에서 ↘

                for j in range(d2 + 1):
                    num_boards[y + j][x + j] = 5               # 중간에서 ↘
                    num_boards[y + d1 + j][x - d1 + j] = 5     # 중간에서 ↙

                # 5 내부 채우기
                for r in range(y + 1, y + d1 + d2):            # y 는 채울게 없음. y + 1 부터 채울게 있음.
                    isIn = False
                    for c in range(N):
                        if num_boards[r][c] == 5:
                            isIn = not isIn
                        elif isIn:
                            num_boards[r][c] = 5

                population = [0, 0, 0, 0, 0]                   # 계산한 인구를 담을 리스트

                # 1 구역 인구 계산
                for r in range(y + d1):
                    for c in range(x + 1):
                        if num_boards[r][c] == 5:
                            break
                        population[0] += boards[r][c]

                # 2 구역
                for r in range(0, y + d2 + 1):
                    for c in range(N - 1, x, -1):              # 오른쪽에서 시작
                        if num_boards[r][c] == 5:
                            break
                        population[1] += boards[r][c]

                # 3 구역
                for r in range(y + d1, N):
                    for c in range(x - d1 + d2):
                        if num_boards[r][c] == 5:
                            break
                        population[2] += boards[r][c]

                # 4 구역
                for r in range(y + d2 + 1, N):
                    for c in range(N - 1, x - d1 + d2 - 1, -1):
                        if num_boards[r][c] == 5:
                            break
                        population[3] += boards[r][c]

                # 5 구역 인구 수 계산
                population[4] = total_population - sum(population[:4])

                # 이번 선거 구의 인구 차이
                sub_res = max(population) - min(population)

                if result > sub_res:
                    result = sub_res

print(result)