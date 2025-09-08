n = int(input())
arr = list(map(int, input().split()))
dp = [1] * (n + 1)  # dp배열 1로 초기화, 자신 포함하기 때문
for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)  # 자기 자신의 최적화 값이랑 자기보다 작은 값의 최적화값에다가 1더한거 중 큰값을 다시 자기자신의 최적화값으로 초기화
print(max(dp))