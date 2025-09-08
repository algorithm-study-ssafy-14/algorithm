n = int(input())
k = 1
while n != 0:
    arr = [[0] * 3 for _ in range(n)]
    dp = [[0] * 3 for _ in range(n)]
    for i in range(n):
        a, b, c = map(int, input().split())
        arr[i][0] = a
        arr[i][1] = b
        arr[i][2] = c
    for i in range(n):
        for j in range(3):
            if i == 0:
                dp[i][0] = float('inf')  # 0으로 하니까 답 안나옴
                dp[i][1] = arr[i][1]
                dp[i][2] = arr[i][1] + arr[i][2]
            elif i >= 1:
                dp[i][0] = arr[i][0] + min(dp[i - 1][0], dp[i - 1][1])
                dp[i][1] = arr[i][1] + min(dp[i][0], dp[i - 1][0], dp[i - 1][1], dp[i - 1][2])
                dp[i][2] = arr[i][2] + min(dp[i][1], dp[i - 1][1], dp[i - 1][2])
    print(f"{k}. {dp[n - 1][1]}")
    k += 1
    n = int(input())