

from heapq import heappush, heappop

#다익스트라
def dijk():

    pq = []
    #pq 첫 번째 값을 대상으로 최소값 정렬, 2번째, 3번째 정렬은 안하기 위함
    
    # 첫 번째 노드를 기준으로 시작, 시작 노드는 자유
    heappush(pq, (0, 1))

    #최단거리 합
    full_cost = 0

    while pq:
        #visited 방문 표시 되었을 시 continue
        cost, node = heappop(pq)
        if not visited[node]:
            full_cost += cost
            visited[node] = True

            for (new_cost, new_node) in lines[node]:
                if not visited[new_node]:
                    heappush(pq, (new_cost, new_node))


    return full_cost


v, e = map(int, input().split())


lines = [[] for _ in range(v+1)]
for _ in range(e):

    # 양방향
    s, e, value = map(int, input().split())
    lines[s].append((value, e))
    lines[e].append((value, s))


visited = [False] * (v+1)
visited[0] =True
print(dijk())