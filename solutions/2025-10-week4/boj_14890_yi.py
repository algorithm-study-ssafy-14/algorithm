n,l = map(int, input().split())
road_map = [list(map(int, input().split())) for _ in range(n)]
res = 0
row_same = 0
col_same = 0

# 가로 확인(같은 숫자만 있는지)
for i in range(n):
    same = True
    for j in range(1, n):
        if road_map[i][j] != road_map[i][0]:
            same = False
            break
    if same:
        res += 1
        row_same += 1


# 세로 확인(같은 숫자만 있는지)
for i in range(n):
    same = True
    for j in range(1, n):
        if road_map[j][i] != road_map[0][i]:
            same = False
            break
    if same:
        res += 1
        col_same += 1


# 가로 경사로 검사
for i in range(n):
    used = [False] * n
    flag = True
    for j in range(n-1):
        if road_map[i][j] == road_map[i][j+1]:
            continue
        if road_map[i][j] + 1 == road_map[i][j+1]:
            for k in range(j, j - l, -1):
                if k < 0 or road_map[i][k] != road_map[i][j] or used[k]:
                    flag = False
                    break
                used[k] = True
        elif road_map[i][j] - 1 == road_map[i][j+1]:
            for k in range(j+1, j+1 + l):
                if k >= n or road_map[i][k] != road_map[i][j+1] or used[k]:
                    flag = False
                    break
                used[k] = True
        else:
            flag = False

        if not flag:
            break
    if flag:
        res += 1

res = res - row_same


# 세로 경사로 검사
for i in range(n):
    used = [False] * n
    flag = True
    for j in range(n-1):
        if road_map[j][i] == road_map[j+1][i]:
            continue
        if road_map[j][i] + 1 == road_map[j+1][i]:
            for k in range(j, j - l, -1):
                if k < 0 or road_map[k][i] != road_map[j][i] or used[k]:
                    flag = False
                    break
                used[k] = True
        elif road_map[j][i] - 1 == road_map[j+1][i]:
            for k in range(j+1, j+1 + l):
                if k >= n or road_map[k][i] != road_map[j+1][i] or used[k]:
                    flag = False
                    break
                used[k] = True
        else:
            flag = False

        if not flag:
            break
    if flag:
        res += 1

res = res - col_same

print(res)
