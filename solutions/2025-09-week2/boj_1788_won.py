import math   # inf 를 위한 import

test_case = 0
while True:
    test_case += 1
    N = int(input())

    if N == 0:  # 0 이 나왔을 때 종료
        break

    arr = [list(map(int, input().split())) for _ in range(N)]

    dp = [[math.inf] * 3 for _ in range(N)]  # 열이 무조건 3개
    dp[0][0] = arr[0][1]
    dp[0][1] = arr[0][1]
    dp[0][2] = arr[0][1] + arr[0][2]         # (0,2) 는 (0,1) 에서 갈 수 있기 때문에 더해준다

    for i in range(1, N):  # 도착할 수 있는 모든 방향을 모두 고려해서 가장 작은 값으로 갱신시켜줌
        dp[i][0] = min(dp[i-1][0], dp[i-1][1]) + arr[i][0] 
        dp[i][1] = min(dp[i-1][0], dp[i-1][1], dp[i-1][2], dp[i][0]) + arr[i][1]
        dp[i][2] = min(dp[i-1][1], dp[i-1][2], dp[i][1]) + arr[i][2]

    print(f"{test_case}. {dp[N-1][1]}")
