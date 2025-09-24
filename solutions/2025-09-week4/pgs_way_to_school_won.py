def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]

    blocked = {(y-1, x-1) for x, y in puddles}

    if (0, 0) in blocked:
        return 0
    dp[0][0] = 1
    for r in range(n):
        for c in range(m):
            if (r, c) in blocked:
                dp[r][c] = 0
                continue

            if r == 0 and c == 0:
                continue
            up = dp[r-1][c] if r > 0 else 0
            left = dp[r][c-1] if c > 0 else 0
            dp[r][c] = (up + left) % 1000000007

    return dp[n-1][m-1]