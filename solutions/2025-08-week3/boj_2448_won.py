N = int(input())
my_list = [[' '] * 2*N for _ in range(N)]


def star(n, y, x):
    if n == 3:
        my_list[y][x] = '*'
        my_list[y+1][x-1] = my_list[y+1][x+1] = '*'
        for i in range(-2, 3):
            my_list[y + 2][x - i] = "*"
        return

    new_n = n // 2
    star(new_n, y, x)
    star(new_n, y + new_n, x - new_n)
    star(new_n, y + new_n, x + new_n)


star(N, 0, N-1)
for s in my_list:
    print("".join(s))
