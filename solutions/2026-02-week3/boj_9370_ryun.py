# 경로 찾기

from heapq import heappop, heappush
import sys

input = sys.stdin.readline

test_case = int(input())
for _ in range(test_case):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    inf = 1e8

    graph = [[] for _ in range(n + 1)]
    dp = [inf] * (n + 1)
    dp_2 = [inf] * (n + 1)
    dp[s] = 0

    # 그래프
    for _ in range(m):
        start, end, weight = map(int, input().split())
        graph[start].append((end, weight))
        graph[end].append((start, weight))

    goal_2 = {}
    for _ in range(t):
        goal_2[int(input())] = 1

    # (있어도 되고 없어도 됨) 정렬
    for i in graph:
        i.sort(key=lambda x: x[1])

    # 1) s에서 다익스트라
    heap_q = []
    heappush(heap_q, (0, s))

    while heap_q:
        weight, node = heappop(heap_q)
        if weight != dp[node]:
            continue

        for e_node, e_weight in graph[node]:
            total_weight = weight + e_weight
            if total_weight < dp[e_node]:
                dp[e_node] = total_weight
                heappush(heap_q, (total_weight, e_node))

    # g-h 간선 가중치
    dist = None
    for e_node, e_weight in graph[g]:
        if e_node == h:
            dist = e_weight
            break

    # 2) g-h를 "지난 뒤" 상태의 멀티소스 다익스트라
    heap_q.clear()

    dp_2[g] = dp[h] + dist
    dp_2[h] = dp[g] + dist
    heappush(heap_q, (dp_2[g], g))
    heappush(heap_q, (dp_2[h], h))

    while heap_q:
        weight, node = heappop(heap_q)
        if weight != dp_2[node]:
            continue

        for e_node, e_weight in graph[node]:
            total_weight = weight + e_weight
            if total_weight < dp_2[e_node]:
                dp_2[e_node] = total_weight
                heappush(heap_q, (total_weight, e_node))

    # 3) 정답 후보 판정
    ans_arr = []
    for x in goal_2:
        if dp[x] < inf and dp_2[x] == dp[x]:
            ans_arr.append(x)

    ans_arr.sort()
    print(*ans_arr)
