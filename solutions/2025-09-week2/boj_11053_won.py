N = int(input())

my_list = list(map(int, input().split()))

dp = [1] * N

for i in range(N):
    for j in range(i):               # i 밑의 인덱스에서 my_list[i] 보다 작은 값을 찾음.
        if my_list[j] < my_list[i]:
            dp[i] = max(dp[i], dp[j] + 1) # 갱신

print(max(dp))