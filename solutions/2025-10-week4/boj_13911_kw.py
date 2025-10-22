from heapq import heappop, heappush


def dijkstra(starts):                           # 다익스트라 템플릿
    dist = [1e10] * (V + 1)
    hq = []

    for s in starts:
        dist[s] = 0
        heappush(hq, (0, s))

    while hq:
        d, v = heappop(hq)

        if dist[v] != d:
            continue

        for u, w in graph[v]:
            n_d = d + w

            if n_d < dist[u]:
                dist[u] = n_d
                heappush(hq, (n_d, u))

    return dist


V, E = map(int, input().split())

graph = [[] for _ in range(V + 1)]

for _ in range(E):
    a, b, w = map(int, input().split())

    graph[a].append((b, w))
    graph[b].append((a, w))

mc_cnt, mc_weight = map(int, input().split())       # 맥도날드 수, 맥세권 조건
mc_list = list(map(int, input().split()))           # 맥도날드 리스트

sb_cnt, sb_weight = map(int, input().split())       # 스벅 수, 스세권 조건
sb_list = list(map(int, input().split()))           # 스벅 리스트

mc_dist_list = dijkstra(mc_list)                    # 각 정점에서 가장 가까운 맥날까지의 거리
sb_dist_list = dijkstra(sb_list)                    # 가장 가까운 스벅까지의 거리

result = 1e10
pass_node = set(mc_list) | set(sb_list)             # 합집합

for node in range(1, V + 1):
    if node in pass_node:                           # 스벅과 맥날이 존재하는 정점은 정답이 될 수 없음
        continue

    if mc_dist_list[node] <= mc_weight and sb_dist_list[node] <= sb_weight:  # 맥세권, 스세권 조건에 맞으면 result 와 비교해서 갱신
        result = min(result, mc_dist_list[node] + sb_dist_list[node])

print(result if result < 1e10 else -1)