def paper(y, x, n):
    global cnt_0
    global cnt_1
    value = my_list[y][x]
    m = n // 2
    for i in range(y, y + n):
        for j in range(x, x + n):
            if my_list[i][j] != value:
                for r in range(2):
                    for c in range(2):
                        paper(y + r * m, x + c * m, m)

                return
    if value == 1:
        cnt_1 += 1
    else:
        cnt_0 += 1


N = int(input())
my_list = [list(map(int, input().split())) for _ in range(N)]
cnt_0 = 0
cnt_1 = 0
paper(0, 0, N)

print(cnt_0)
print(cnt_1)
