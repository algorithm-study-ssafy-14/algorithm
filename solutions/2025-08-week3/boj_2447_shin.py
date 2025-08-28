def dp(length,start_r, start_c):
    if length == 3:
        matrix[start_r + 1][start_c + 1] = ' '
        return

    else:
        length //= 3
        for r in range(start_r + length, start_r + 2 * length):
            for c in range(start_c + length, start_c + 2 * length):
                matrix[r][c] = ' '

        for i in range(3):
            for j in range(3):
                if r == 1 and c == 1:
                    continue
                dp(length,start_r + length*i, start_c + length*j)

N = int(input())
matrix = [['*']*N for _ in range(N)]
dp(N,0,0)

trimmed = '\n'.join(''.join(i) for i in matrix)

print(trimmed)