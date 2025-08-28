def quad(y, x, n):
    value = my_list[y][x]

    for i in range(y, y+n):
        for j in range(x, x+n):
            if value != my_list[i][j]:
                m = n // 2
                result.append('(')

                for r in range(2):
                    for c in range(2):
                        quad(y + m * r, x + m * c, m)

                result.append(')')
                return

    result.append(value)


N = int(input())

my_list = [list(map(int, input().strip())) for _ in range(N)]

result = []

quad(0, 0, N)

print(''.join(map(str, result)))
