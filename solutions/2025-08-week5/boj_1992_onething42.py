n = int(input())
arr = [list(map(int, input())) for _ in range(n)]

white, blue = 0, 0
result = []


def check(x, y, n):
    global white, blue
    color = arr[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != color:
                result.append("(")
                size = n // 2
                check(x, y, size)
                check(x, y + size, size)
                check(x + size, y, size)
                check(x + size, y + size, size)
                result.append(")")
                return
    if color == 0:
        result.append(0)
    elif color == 1:
        result.append(1)


check(0, 0, n)
print(*result, sep='')
