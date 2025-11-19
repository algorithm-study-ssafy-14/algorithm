## 미생물 격리

T = int(input())
dir_r = [-1, 1, 0, 0]
dir_c = [0, 0, -1, 1]

for tc in range(1, T + 1):
    # n이 행렬 크기, m이 격리 시간, k가 미생물 군집의 갯수
    n, m, k = map(int, input().split())
    matrix = [[[] for _ in range(n)] for _ in range(n)]
    # print(matrix)
    basket = []

    # 좌표, 개체 수, 방향
    for _ in range(k):
        r, c, nums, dir = map(int, input().split())
        dir -= 1
        basket.append((r, c, nums, dir))

    storage = []

    # 1초에 벌어지는 일
    for time in range(1, m + 1):
        storage.clear()

        for r, c, nums, dir in basket:
            nr = r + dir_r[dir]
            nc = c + dir_c[dir]

            # 매트릭스에 (개체 수, 방향, 시간)으로 등록
            if 1 <= nr < n - 1 and 1 <= nc < n - 1:
                if matrix[nr][nc] and matrix[nr][nc][0][2] == time:
                    matrix[nr][nc].append((nums, dir, time))

                else:
                    matrix[nr][nc].clear()
                    matrix[nr][nc].append((nums, dir, time))
                    storage.append((nr, nc))

            elif nr == 0 or nr == n - 1 or nc == 0 or nc == n - 1:
                if dir == 0 or dir == 2:
                    dir += 1
                elif dir == 1 or dir == 3:
                    dir -= 1

                if nums // 2 > 0:
                    matrix[nr][nc].clear()
                    matrix[nr][nc].append((nums // 2, dir, time))
                    storage.append((nr, nc))

        basket = []
        for p, q in storage:
            if len(matrix[p][q]) < 2:
                # (r / c / 숫자 / dir)
                basket.append((p, q, matrix[p][q][0][0], matrix[p][q][0][1]))

            else:
                a_max = -1
                mini_cnt = 0
                for i in range(len(matrix[p][q])):
                    mini_cnt += matrix[p][q][i][0]

                    if a_max < matrix[p][q][i][0]:
                        a_max = matrix[p][q][i][0]

                        idx = i
                basket.append((p, q, mini_cnt, matrix[p][q][idx][1]))

    cnt = 0
    for i in basket:
        cnt += i[2]
    print(f"#{tc} {cnt}")