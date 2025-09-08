N = int(input())
arr = [0] * (N+1)

dp = [[0] * 2 for _ in range(N+1)]

for i in range(1, N+1):
    arr[i] = int(input())

# dp[i][0]이 다음걸 선택할 수 있는 것
# dp[i][1]이 다음걸 선택할 수 없는 것

if N >= 1:
    dp[1][0] = dp[1][1] = arr[1]

if N >= 2:
    dp[2][0] = arr[2]
    dp[2][1] = arr[1] + arr[2]

for i in range(3, N+1):

    # dp[i][0] 은 다음 것을 선택할 수 있는 것이기 때문에 i-1 의 포도주를 더하면 안됨.
    # 포도주를 여러개 마시지 않고 이번 포도주를 마실 수도 있기 때문에 i-3 까지 고려함.
    dp[i][0] = max(dp[i-2][0], dp[i-2][1], (max(dp[i-3][0], dp[i-3][1]))) + arr[i]
    
    # dp[i][1] 은 다음 것을 선택할 수 없기 때문에 dp[i-1][0] + arr[i] 으로 갱신
    dp[i][1] = dp[i-1][0] + arr[i]

if N == 1:
    ans = arr[1]
else:
    ans = 0

for i in range(1, N + 1):
    ans = max(ans, dp[i][0], dp[i][1])
print(ans)