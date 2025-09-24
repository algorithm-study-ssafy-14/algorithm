def solution(triangle):
    n = len(triangle)

    # 트리 구성
    dp = [[0] * (i + 1) for i in range(n)]

    # 0번째와 1번째 트리를 만듦
    dp[0] = triangle[0]
    dp[1][0] = dp[0][0] + triangle[1][0]
    dp[1][1] = dp[0][0] + triangle[1][1]

    for i in range(2, n):
        for j in range(i):
            # j 가 0이라면 좌측이므로 현재 값과 dp[i-1][0] 을 더해줌
            if j == 0:
                dp[i][j] = dp[i - 1][j] + triangle[i][j]
                continue
            # 가운데 값들은 비교해서 가장 큰 값을 넣어줌
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + triangle[i][j], dp[i - 1][j] + triangle[i][j])
        # 우측 값은 좌측 값과 동일하게 dp[i-1][i-1] 를 더해줌
        dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]

    # 마지막 리스트에서 가장 큰 값을 출력함
    return max(dp[n - 1])