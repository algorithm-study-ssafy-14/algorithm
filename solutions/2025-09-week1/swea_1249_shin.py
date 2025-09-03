#queue 구현 최적화를 위한 deque
from collections import deque

#단순 bfs
def bfs(r, c):
    basket = deque([(r, c)])
    
    while basket:
        p, q = basket.popleft()

        for i in range(4):
            np = p + dir_r[i]
            nq = q + dir_c[i]
            
            #visited값보다 기존값이 작을 시 새로 갱신하며 해당 노드 재탐색
            if 0 <= np < N and 0 <= nq < N and matrix[np][nq] + visited[p][q] < visited[np][nq]:
                visited[np][nq] = matrix[np][nq] + visited[p][q]

                #append 방향 분리
                #값이 0일시 appendleft : 조금이라도 적은 수를 먼저 탐색해보기 위함
                if matrix[np][nq] == 0:
                    basket.appendleft((np, nq))

                #아닐시 그냥 진행
                else:
                    basket.append((np, nq))

    return visited[N - 1][N - 1]


T = int(input())
dir_r = [1, -1, 0, 0]
dir_c = [0, 0, 1, -1]


for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, list(input()))) for _ in range(N)]

    #큰 값을 지정하여 값 탐색 유도
    visited = [[2500] * N for _ in range(N)]
    visited[0][0] = 0

    result = bfs(0, 0)

    print(f"#{tc} {result}")