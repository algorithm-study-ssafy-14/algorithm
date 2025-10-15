#줄 세우기

from collections import deque
import sys

input = sys.stdin.readline

#위상정렬
def sorting():

    basket = deque()
    
    #노착노드가 없는 노드들부터 순회하며 시작.
    for i in range(1, n+1):
        if not num_of_line[i]:
            basket.append(i)

    #위상정렬 시작.
    while basket:
        p = basket.popleft()
        sorted_list.append(p)

        #이 노드에서 도착하는 노드들의 진입차수를 -1 해주고, 그렇게 0이 된 노드를 deque에 넣어줌.
        for j in graph[p]:
            num_of_line[j] -= 1

            #이 노드에 남아있는 도착노드가 없다면 deque에 넣어줌.
            if not num_of_line[j]:
                basket.append(j)


n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
num_of_line = [0] * (n+1)
sorted_list = []

#인접리스트 생성
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)

    #도착노드의 수를 적어둠.
    num_of_line[end] += 1

sorting()
print(*sorted_list)
