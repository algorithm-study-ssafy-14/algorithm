n = int(input())

stars = [[" " for _ in range(n)] for _ in range(n)]

def draw_star(x, y, size):
    if size == 1:
        stars[x][y] = "*"
        return
    div = size // 3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            draw_star(x + i * div, y + j * div, div)

draw_star(0, 0, n)

for i in stars:
    print("".join(i))
