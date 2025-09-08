
N = int(input())
num_list = list(map(int, input().split()))


#memo 기록
memo = [1] * N


#O(N)으로 해결하려고 하다가 고생 많이함. 다른 방법이 있을까?

for i in range(N):
    for j in range(i):
        if num_list[j] < num_list[i]:
            memo[i] = max(memo[i], memo[j] + 1)

print(max(memo))