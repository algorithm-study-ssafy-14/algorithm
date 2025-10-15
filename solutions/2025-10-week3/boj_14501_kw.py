N = int(input())

arr = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]  # 계산하기 편하게 0 부터

dp = [0] * (N + 1)

if arr[-1][0] == 1:                                             # 마지막 날에 잡혀있는 상담이 하루 걸린다면
    dp[-1] = arr[-1][1]

for i in range(N-1, 0, -1):                                     # N - 1 부터 순회
    if arr[i][0] + i - 1 > N:                                   # 당일에 잡혀 있는 상담이 N 일을 벗어난다면 패스
        dp[i] = dp[i + 1]
        continue

    if i + arr[i][0] > N:                                       # 상담이 마지막 날에 끝나는 경우
        dp[i] = max(arr[i][1], dp[i + 1])
    else:                                                       # 추가 상담을 할 수 있는 경우
        dp[i] = max(arr[i][1] + dp[i + arr[i][0]], dp[i + 1])

print(dp[1])