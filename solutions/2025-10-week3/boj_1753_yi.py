import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        w, now = heapq.heappop(q)
        if dist[now] < w:
            continue
        for i in graph[now]:
            cost = w+i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
                    

V, E = map(int, input().split())
k = int(input())
graph = [[] for _ in range(V+1)]
dist = [int(1e9)] * (V + 1)
for i in range(E):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))

dijkstra(k)
for i in range(1, V + 1):
    if dist[i] == int(1e9):
        print("INF")
    else:
        print(dist[i])