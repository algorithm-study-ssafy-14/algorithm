N = int(input())
dp = [0] * (N + 1)

for i in range(2, N+1):
    dp[i] = dp[i - 1] + 1  # -1, +1이 cnt느낌
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)  # 3으로 나누기
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)  # 2로 나누기

print(dp[N])