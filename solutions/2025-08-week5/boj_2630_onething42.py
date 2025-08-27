n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

white, blue = 0, 0


def check(x, y, n):
    global white, blue
    color = arr[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != color:
                size = n // 2
                check(x, y, size)
                check(x + size, y, size)
                check(x, y + size, size)
                check(x + size, y + size, size)
                return
    if color == 0:
        white += 1
    elif color == 1:
        blue += 1


check(0, 0, n)
print(white)
print(blue)
