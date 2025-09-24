def solution(triangle):
    n = len(triangle)

    res = []
    for row in triangle:
        n_row = [0] + row + [0]
        res.append(n_row)

    for i in range(1, n):
        for j in range(1, i + 2):
            lt = res[i - 1][j - 1]
            rt = res[i - 1][j]
            res[i][j] += max(lt, rt)

    answer = max(res[-1])
    return answer
