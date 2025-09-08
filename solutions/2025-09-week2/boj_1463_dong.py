

n = int(input())
memo = [0] * (n+1)

#값 크게 넣어서 접근 못하게 설정
memo[0] = 1000001

#목표값
memo[1] = 0

# 나눠질 시 포함하여 memo에 적음,i부터 시작하여 bottom - up
for i in range(2, n+1):
    if memo[i] == 0:
        memo[i] = min(memo[i//3] if i%3 == 0 else 1000000, memo[i//2] if i%2 == 0 else 1000000, memo[i-1]) + 1

print(memo[n])