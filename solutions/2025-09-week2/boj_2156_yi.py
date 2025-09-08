n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
dp = [0] * (n + 1)
if n == 1:
    ans = arr[0]
elif n == 2:
    ans = arr[0] + arr[1]
elif n == 3:
    ans = max(arr[1] + arr[0], arr[1] + arr[2], arr[0] + arr[2])
else:
    dp[0] = arr[0]
    dp[1] = arr[1] + arr[0]
    dp[2] = max(arr[1] + arr[0], arr[1] + arr[2], arr[0] + arr[2])
    for i in range(3, n):
        a = dp[i - 1]
        b = dp[i - 2] + arr[i]
        c = dp[i - 3] + arr[i] + arr[i - 1]
        dp[i] = max(a, b, c)
    ans = max(dp)
print(ans)