n = int(input())
k = 1  # 테케 번호
while n != 0:  # 0이면 종료
    arr = [[0] * 3 for _ in range(n)]
    dp = [[0] * 3 for _ in range(n)]
    for i in range(n):
        a, b, c = map(int, input().split())
        arr[i][0] = a
        arr[i][1] = b
        arr[i][2] = c
    for i in range(n):
        for j in range(3):
            if i == 0:  #첫번째줄은 미리 초기화, 경우의 수가 하나밖에 없기 때문
                dp[i][0] = float('inf')  # 0으로 하니까 답 안나옴
                dp[i][1] = arr[i][1]
                dp[i][2] = arr[i][1] + arr[i][2]
            elif i >= 1:  # 각 경우의 수들의 최적화 값 중 가장 작은 값을 찾고 거기에 자기 자신의 값을 더함
                dp[i][0] = arr[i][0] + min(dp[i - 1][0], dp[i - 1][1])  # 왼쪽으로 올수있는 경우의 수가 2개
                dp[i][1] = arr[i][1] + min(dp[i][0], dp[i - 1][0], dp[i - 1][1], dp[i - 1][2])  # 가운데로 올수있는 경우의 수가 4개
                dp[i][2] = arr[i][2] + min(dp[i][1], dp[i - 1][1], dp[i - 1][2])  # 오른쪽으로 올수있는 경우의 수가 3개
    print(f"{k}. {dp[n - 1][1]}")  # 도착요소의 인덱스의 최적화값이 곧 정답
    k += 1
    n = int(input())