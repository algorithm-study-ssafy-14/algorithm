def dfs(start_r, end_r, start_c,end_c):
    global w_count, b_count

    default = matrix[start_r][start_c]
    for r in range(start_r, end_r):
        for c in range(start_c, end_c):
            if matrix[r][c] != default:
                print('(',end='')
                dfs(start_r, (start_r + end_r)//2, start_c, (start_c + end_c)//2)
                dfs( start_r, (start_r + end_r) // 2,(start_c + end_c) // 2, end_c)
                dfs((start_r + end_r) // 2, end_r, start_c, (start_c + end_c) // 2)
                dfs((start_r + end_r) // 2, end_r, (start_c + end_c) // 2, end_c)
                print(')', end='')
                return

    else:
        print(default,end='')

N = int(input())
matrix = [list(map(int, list(input()))) for _ in range(N)]
dfs(0, N, 0, N)