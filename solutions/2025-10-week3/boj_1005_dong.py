#ACM craft
import sys
input = sys.stdin.readline
from collections import deque

#위상정렬
def sorting():

    #도착노드가 없는 노드부터 deque에서 시작.
    while basket:
        p = basket.popleft()

        #이 노드에 도착한 노드들의 맥스값을 times(==dp)에 넣어줌.
        if end_graph[p]:
            times[p] = max(times[k] for k in end_graph[p]) + time_list[p-1]

        #도착노드가 없는 노드라면 그냥 자기자신의 시간.
        else:
            times[p] = time_list[p-1]

        #승리노드가 나올때까지 반복
        if times[to_win] >= 0:
            return times[to_win]

        #이 노드에서 도착하는 노드들의 visited 를  -1 해주고, 그렇게 0이 된 노드를 deque에 넣어줌.
        for j in graph[p]:
            visited[j] -= 1
            if not visited[j]:
                basket.append(j)


#testcase 수
t = int(input())

#각 테스트케이스마다
for _ in range(t):

    node, lines = map(int, input().split())
    time_list = list(map(int, input().split()))

    graph = [[] for _ in range(node+1)]
    end_graph = [[] for _ in range(node+1)]

    visited = [0] * (node+1)
    times = [-1] * (node+1)
    for _ in range(lines):
        start, end = map(int, input().split())

        #인접 리스트    
        graph[start].append(end)

        #역인접 리스트 ( dp 밑작업)
        end_graph[end].append(start)

        # 몇개가 이 노드에 들어오는지. 위상정렬 밑작업
        visited[end] += 1

    #이기기 위해서 지어야 하는 건물
    to_win = int(input())

    #bfs비슷하게 구현
    basket = deque()
    for i in range(1, node+1):
        if not visited[i]:
            basket.append(i)

    print(sorting())