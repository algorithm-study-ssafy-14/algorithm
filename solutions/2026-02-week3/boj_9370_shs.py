import sys
sys.stdin = open('input/9370_input.txt', 'r')
input = sys.stdin.readline

from heapq import heappush, heappop


def main(n, s, g, h, w_gh):
    global _n
    _n = n

    result = []

    # [핵심 로직 1] 다익스트라 3번 실행
    # 매번 목적지마다 다익스트라를 돌리면 O(T * E log V)로 시간 초과가 발생할 수 있습니다.
    # 따라서 S, G, H를 시작점으로 하는 '모든 노드까지의 최단 거리'를 딱 3번만 구해서 재사용합니다.
    dist_s = dijkstra(s) # S에서 출발하는 전체 최단 거리
    dist_g = dijkstra(g) # G에서 출발하는 전체 최단 거리 (g-h 간선의 한쪽 끝)
    dist_h = dijkstra(h) # H에서 출발하는 전체 최단 거리 (g-h 간선의 다른쪽 끝)

    for e in exits:
        # [핵심 로직 2] 반드시 g-h 간선을 지나가는 두 가지 경로 계산
        # 1. S -> G -> H -> E (S에서 G까지 최단 + G-H 사이 거리 + H에서 E까지 최단)
        path_1 = dist_s[g] + w_gh + dist_h[e]
        # 2. S -> H -> G -> E (S에서 H까지 최단 + H-G 사이 거리 + G에서 E까지 최단)
        path_2 = dist_s[h] + w_gh + dist_g[e]

        # [주의사항 & 디버깅 포인트] 
        # 목적지 e까지 아예 갈 수 없는 경우(dist_s[e] == inf)를 반드시 체크해야 합니다.
        # 이를 체크하지 않으면 무한대끼리의 비교(inf == inf)가 True가 되어, 
        # 갈 수 없는 곳인데도 정답으로 처리되는 치명적인 오류가 발생합니다.
        if dist_s[e] != float('inf') and dist_s[e] == min(path_1, path_2):
            result.append(e)
            
    result.sort()
    return " ".join(map(str, result))


def dijkstra(start):
    distance = [float('inf')] * (_n + 1)
    distance[start] = 0
    pq = [(0, start)]
    while pq:
        d, curr = heappop(pq)
        if d > distance[curr]:
            continue
        for next_node, weight in info[curr]:
            if distance[next_node] > d + weight:
                distance[next_node] = d + weight
                heappush(pq, (distance[next_node], next_node))

    return distance
    

T = int(input())
for test_case in range(1, T + 1):
    N, M, T = map(int, input().split())
    S, G, H = map(int, input().split())
    info = [[] for _ in range(N + 1)]
    gh_weight = float('inf')
    for _ in range(M):
        a, b, d = map(int, input().split())
        info[a].append((b, d))
        info[b].append((a, d))
        if a == G and b == H or a == H and b == G:
            gh_weight = min(gh_weight, d)
    exits = [int(input()) for _ in range(T)]
    
    print(main(N, S, G, H, gh_weight))