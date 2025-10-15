from collections import deque

T = int(input())
for i in range(1, T + 1):
    n, k = map(int, input().split())
    time = list(map(int, input().split()))
    indegree = [0] * (n + 1)
    indegree[0] = -1
    graph = [[] for _ in range(n + 1)]
    q = deque()
    res = []

    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    w = int(input())

    for i in range(1, n  + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        res.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in res:
        print(i, sep=' ')