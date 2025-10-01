from collections import defaultdict
import heapq


def prim(graph, start):
    weight = 0
    visited = [False] * (len(graph) + 1)
    p_queue = [(0, start)]

    while p_queue:
        w, u = heapq.heappop(p_queue)
        if not visited[u]:
            visited[u] = True
            weight += w
            for a, b in graph[u]:
                if not visited[b]:
                    heapq.heappush(p_queue, (a, b))
    return weight


v, e = map(int, input().split())
graph = defaultdict(list)
for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

s_node = 1
print(prim(graph, s_node))