from heapq import heappush, heappop

V, E = map(int, input().split())

start = int(input())

graph = [[] for _ in range(V + 1)]

d = [1e9] * (V + 1)

d[start] = 0
pq = [(d[start], start)]

for _ in range(E):
    u, v, w = map(int, input().split())

    graph[u].append((v, w))

while pq:
    cw, cv = heappop(pq)

    if d[cv] != cw:
        continue

    for nv, nw in graph[cv]:
        if d[nv] <= cw + nw:
            continue
        d[nv] = cw + nw
        heappush(pq, (d[nv], nv))

for i in range(1, len(d)):
    print("INF" if d[i] == 1e9 else d[i])
