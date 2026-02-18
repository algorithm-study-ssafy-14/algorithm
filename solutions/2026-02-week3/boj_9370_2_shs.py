import sys
sys.stdin = open('input/9370_input.txt', 'r')
input = sys.stdin.readline

from heapq import heappush, heappop


def main(n, s, g, h):
    global _n
    _n = n

    result = []

    # [핵심 로직: 홀수/짝수 트릭]
    # 모든 간선의 가중치를 2배로 늘렸습니다. (모든 거리가 짝수가 됨)
    # 단, 반드시 지나야 하는 배꼽 간선(g-h)만 가중치를 '2*d - 1'로 홀수로 만들었습니다.
    
    # 1. 다익스트라 실행 (시작점 S)
    dist_s = dijkstra(s) 

    # 2. 결과 판별
    # 최단 경로의 총 합(dist_s[e])이
    # - 짝수라면? -> 홀수 가중치 간선(g-h)을 0번 또는 짝수 번 지났다는 뜻 (g-h 미포함)
    # - 홀수라면? -> 홀수 가중치 간선(g-h)을 홀수 번(1번) 지났다는 뜻 (g-h 포함!)
    # 따라서 dist_s[e] % 2 == 1 인 경우만 정답으로 채택하면 됩니다.
    for e in exits:
        if dist_s[e] != INF and dist_s[e] % 2 == 1:
            result.append(e)
            
    result.sort()
    return " ".join(map(str, result))


def dijkstra(start):
    distance = [INF] * (_n + 1)
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
INF = 10**18
for test_case in range(1, T + 1):
    N, M, T = map(int, input().split())
    S, G, H = map(int, input().split())
    info = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b, d = map(int, input().split())
        if a == G and b == H or a == H and b == G:
            info[a].append((b, 2*d - 1))
            info[b].append((a, 2*d - 1))
        else:
            info[a].append((b, 2*d))
            info[b].append((a, 2*d))
        
    exits = [int(input()) for _ in range(T)]
    
    print(main(N, S, G, H))