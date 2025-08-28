n = int(input())
stars = [[" " for _ in range(2*n)] for _ in range(n)]

def draw(x, y, size):
    if size == 3:
        stars[x][y] = "*"
        stars[x+1][y-1] = "*"
        stars[x+1][y+1] = "*"
        for i in range(-2, 3):
            stars[x+2][y+i] = "*"
        return
    
    temp = size // 2
    draw(x, y, temp)
    draw(x+temp, y-temp, temp)
    draw(x+temp, y+temp, temp)

draw(0, n-1, n)

for i in stars:
    print("".join(i))
