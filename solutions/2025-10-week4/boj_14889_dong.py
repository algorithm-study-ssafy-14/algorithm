from itertools import combinations

N = int(input())

# 인접행렬로 표현
matrix = [list(map(int, input().split())) for _ in range(N)]

# matrix
for r in range(N):
    for c in range(r):
        #수를 한 곳에 모음.
        matrix[r][c] += matrix[c][r]

# members
members = list(range(N))
subsets = list(combinations(members, N//2))
min_a = 40001

# pop하면서 꺼내옴
for list_a in subsets:
    list_b = subsets.pop()
    sum_a = 0
    sum_b = 0
    for i in range(N//2):
        a = list_a[i]
        for j in range(i+1, N//2):
            b = list_a[j]
            sum_a += matrix[b][a]

    for i in range(N//2):
        a = list_b[i]
        for j in range(i+1, N//2):
            b = list_b[j]
            sum_b += matrix[b][a]
    if min_a > abs(sum_a - sum_b):
        min_a = abs(sum_a - sum_b)

print(min_a)