

def solution(m, n, puddles):
    memo = [[-1] * m for _ in range(n)]
    memo[0][0] = 1
    for i, j in puddles:
        memo[j - 1][i - 1] = 0

    for c in range(1, m):
        if memo[0][c]:
            memo[0][c] = memo[0][c - 1]

    for r in range(1, n):
        if memo[r][0]:
            memo[r][0] = memo[r - 1][0]

    for r in range(1, n):
        for c in range(1, m):
            if memo[r][c]:
                memo[r][c] = (memo[r - 1][c] + memo[r][c - 1]) % 1000000007

    answer = memo[r][c]
    return answer