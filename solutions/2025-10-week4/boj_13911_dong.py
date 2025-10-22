import heapq, sys

input = sys.stdin.readline
heappop = heapq.heappop
heappush = heapq.heappush

#하나로 통합했어야 됐는데 귀찮았나봄.
def dijkstra_m():
    memo = [200000000] * (V+1)

    for i in m_set:
        memo[i] = 0
    basket = [(0,i) for i in m_set]


    while basket:
        cost, num = heappop(basket)

        # 계산했는데 또 하는 상황 컨티뉴로 패스
        if cost > dist_m:
            break

        if cost > memo[num]:
            continue

        # 값이 새로운 장소라면:
        for next_num, add_cost in link_dict[num].items():
            temp = cost + add_cost

            if temp > dist_m:
                continue

            if temp < memo[next_num]:
                memo[next_num] = temp
                heappush(basket, (temp, next_num))

    return memo

def dijkstra_n():

    memo = [200000000] * (V+1)
    for i in n_set:
        memo[i] = 0
    basket = [(0,i) for i in n_set]


    while basket:
        cost, num = heappop(basket)

        # 계산했는데 또 하는 상황 컨티뉴로 패스
        if cost > dist_n:
            break

        if cost > memo[num]:
            continue

        # 값이 새로운 장소라면:
        for next_num, add_cost in link_dict[num].items():
            temp = cost + add_cost

            if temp > dist_n:
                continue

            if temp < memo[next_num]:
                memo[next_num] = temp
                heappush(basket, (temp, next_num))

    return memo


V, E = map(int, input().split())

#인접리스트를 딕셔너리에.
link_dict = [{} for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int, input().split())
    link_dict[u][v] = w
    link_dict[v][u] = w

m, dist_m = map(int, input().split())
m_set = set(map(int, input().split()))

n, dist_n = map(int,input().split())
n_set = set(map(int, input().split()))

h_set = set(range(1,V+1)) - m_set - n_set

#각각 맥날, 스벅에서 멀티소스 다익스트라 시작.
m = dijkstra_m()
n = dijkstra_n()
a_max = 400000000
for i in range(1,V+1):
    if m[i] != 0 and m[i] != 200000000 and n[i] != 0 and n[i] != 200000000:
        if a_max > m[i] + n[i]:
            a_max = m[i] + n[i]
if a_max == 400000000:
    a_max = -1
print(a_max)