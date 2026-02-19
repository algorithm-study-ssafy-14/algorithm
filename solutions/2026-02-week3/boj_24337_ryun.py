# 가희와 탑
N, a, b = map(int, input().split())
ans = []

for i in range(1, a):
    ans.append(i)
ans.append(max(a, b))
for i in range(b-1, 0, -1):
    ans.append(i)

if len(ans) > N:
    print(-1)
else:
    print(ans[0], end=" ")
    for i in range(N-len(ans)):
        print(1, end=" ")
    for i in range(1, len(ans)):
        print(ans[i], end=" ")