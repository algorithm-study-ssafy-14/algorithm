from collections import deque

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())  # N 은 건물 개수, K 는 건설 순서 규칙의 총 개수

    bs = [[] for _ in range(N + 1)]
    deg = [0] * (N + 1)

    b_value = [0] + list(map(int, input().split()))  # 건설 속도

    for _ in range(K):
        x, y = map(int, input().split())

        bs[x].append(y)
        deg[y] += 1

    W = int(input())

    dist = [0] * (N + 1)

    q = deque()
    for i in range(1, N + 1):  # 1 ~ N 까지
        if deg[i] == 0:
            q.append(i)
            dist[i] = b_value[i]

    while q:
        cur = q.popleft()

        for nxt in bs[cur]:
            # 가장 큰 시간만 계산하기 위해 갱신
            if dist[nxt] < dist[cur] + b_value[nxt]:
                dist[nxt] = dist[cur] + b_value[nxt]

            deg[nxt] -= 1
            if deg[nxt] == 0:
                q.append(nxt)

    print(dist[W])