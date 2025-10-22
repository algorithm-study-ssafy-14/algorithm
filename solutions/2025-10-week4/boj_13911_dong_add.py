#최적화 풀이

import heapq

class UserSolution:
    def __init__(self):
        self.edges = []
        self.nodeNum = 0

    def init(self, N, K, sBuilding, eBuilding, mDistance):
        self.nodeNum = N
        self.edges = [[] for _ in range(N + 1)]

        for i in range(K):
            a = sBuilding[i]
            b = eBuilding[i]
            dist = mDistance[i]
            self.edges[a].append((b, dist))
            self.edges[b].append((a, dist))

    def add(self, sBuilding, eBuilding, mDistance):
        self.edges[sBuilding].append((eBuilding, mDistance))
        self.edges[eBuilding].append((sBuilding, mDistance))

    def calculate(self, M, mCoffee, P, mBakery, R):
        INF = float('inf')
        pq = []  # (dist, kind, pos)
        info = [0] * (self.nodeNum + 1)
        dp = [[INF] * (self.nodeNum + 1) for _ in range(2)]

        # 커피집 초기화
        for idx in mCoffee:
            info[idx] = 1
            heapq.heappush(pq, (0, 1, idx))
            dp[0][idx] = 0

        # 빵집 초기화
        for idx in mBakery:
            info[idx] = 2
            heapq.heappush(pq, (0, 2, idx))
            dp[1][idx] = 0

        answer = INF

        while pq:
            dist, kind, pos = heapq.heappop(pq)

            if dist > dp[kind - 1][pos] or dist >= answer:
                continue

            # 교차점 후보 (커피와 빵집 모두 도달 가능)
            if dp[0][pos] != INF and dp[1][pos] != INF and info[pos] == 0:
                answer = min(answer, dp[0][pos] + dp[1][pos])

            for nxt, d in self.edges[pos]:
                newDist = dist + d
                if newDist >= answer or newDist > R:
                    continue
                if dp[kind - 1][nxt] > newDist:
                    dp[kind - 1][nxt] = newDist
                    heapq.heappush(pq, (newDist, kind, nxt))

        return -1 if answer == INF else answer
