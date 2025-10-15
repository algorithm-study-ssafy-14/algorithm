from collections import deque

N, M = map(int, input().split())

students = [[] for _ in range(N + 1)]
deg = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    students[a].append(b)
    deg[b] += 1

q = deque()
for i in range(1, N + 1):
    if deg[i] == 0:
        q.append(i)

result = []
while q:
    cur = q.popleft()
    result.append(cur)
    for nxt in students[cur]:
        deg[nxt] -= 1
        if deg[nxt] == 0:
            q.append(nxt)

print(' '.join(map(str, result)))
