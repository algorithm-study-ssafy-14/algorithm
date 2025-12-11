# 영준이의 진짜 bfs
from collections import deque

def solve():
    T = int(input())
    for tc in range(1, T + 1):
        n = int(input())
        n_list = list(map(int, input().split()))   # n-1개, i번째 = (i+2)의 부모

        # 1. 트리 구성 (부모 -> 자식) + 바로 위 부모(parent0)
        children = [[] for _ in range(n + 1)]
        parent0 = [0] * (n + 1)   # parent0[v] = v의 바로 위 부모

        for i in range(n - 1):
            child = i + 2
            p = n_list[i]
            children[p].append(child)
            parent0[child] = p

        # 2. BFS로 실제 BFS 순서와 depth 계산
        order = []               # BFS 순서대로 방문한 노드들
        depth = [0] * (n + 1)

        q = deque([1])
        while q:
            v = q.popleft()
            order.append(v)
            for nxt in children[v]:
                depth[nxt] = depth[v] + 1
                q.append(nxt)

        # 3. Binary Lifting 테이블 만들기
        LOG = (n + 1).bit_length()  # 2^LOG > n 이 되도록
        parent = [[0] * (n + 1) for _ in range(LOG)]

        # 1-step 부모 채우기
        for v in range(1, n + 1):
            parent[0][v] = parent0[v]

        # 2^k번째 부모 채우기
        for k in range(1, LOG):
            for v in range(1, n + 1):
                mid = parent[k-1][v]
                parent[k][v] = parent[k-1][mid]

        # 4. LCA 함수
        def lca(a, b):
            # 깊이 맞추기 (a를 더 깊은 쪽으로 맞춰서 시작)
            if depth[a] < depth[b]:
                a, b = b, a

            diff = depth[a] - depth[b]
            bit = 0
            while diff:
                if diff & 1:
                    a = parent[bit][a]
                diff >>= 1
                bit += 1

            if a == b:
                return a

            # 위에서부터 부모가 다를 때까지 같이 점프
            for k in range(LOG - 1, -1, -1):
                if parent[k][a] != parent[k][b]:
                    a = parent[k][a]
                    b = parent[k][b]

            return parent[0][a]

        # 5. BFS 순서대로 인접한 두 노드 사이의 거리 합산
        ans = 0
        for i in range(1, n):   # order[i-1] -> order[i]
            u = order[i - 1]
            v = order[i]
            w = lca(u, v)
            ans += depth[u] + depth[v] - 2 * depth[w]

        print(f"#{tc} {ans}")

solve()
