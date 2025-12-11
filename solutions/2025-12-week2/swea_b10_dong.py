from collections import deque

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    n_list = list(map(int, input().split()))

    # 자식 리스트(정방향 그래프), 부모 정보, 각 노드의 깊이(레벨)
    start_graph = [[] for _ in range(n+1)]
    parent_graph = [0] * (n+1)
    numbering = [0] * (n+1)

    # 2번 노드부터 n번 노드까지 부모 정보 입력
    for i in range(n-1):
        start_graph[n_list[i]].append(i+2)           # 부모 → 자식 연결
        parent_graph[i+2] = n_list[i]                # 자식의 부모 기록
        numbering[i+2] = numbering[n_list[i]] + 1    # 부모 깊이 + 1 로 깊이 저장

    # BFS 방문 순서(대화 순서) 기록
    dialog = []
    def bfs(start):
        basket = deque([start])
        while basket:
            node = basket.popleft()
            dialog.append(node)          # 방문 순서를 기록
            for i in start_graph[node]:
                basket.append(i)
    bfs(1)  # 루트에서 시작

    # node에서 cnt번 위로 올라간 조상 노드 반환
    def cutting(node, cnt):
        temp = node
        for _ in range(cnt):
            temp = parent_graph[temp]
        return temp

    # 두 노드 a, b가 같은 조상이 될 때까지
    # 동시에 한 칸씩 위로 올리며 이동 거리(간선 수)를 계산
    def find_parent(a, b):
        temp1 = a
        temp2 = b
        cnt = 0
        while temp1 != temp2:
            temp1 = parent_graph[temp1]
            temp2 = parent_graph[temp2]
            cnt += 2         # 두 노드가 동시에 한 칸씩 올라가므로 +2
        return cnt

    total = 0
    # BFS 방문 순서대로 인접한 두 노드 사이의 거리 합산
    for i in range(len(dialog)-1):
        p = dialog[i]
        q = dialog[i+1]

        # 깊이가 더 큰 노드를 a, 더 작은 쪽을 b로 설정
        a = max(numbering[p], numbering[q])
        b = min(numbering[p], numbering[q])

        # 깊이를 맞추기 위해 더 깊은 쪽을 위로 올림
        if numbering[p] > numbering[q]:
            p = cutting(p, a-b)
        elif numbering[p] < numbering[q]:
            q = cutting(q, a-b)

        # 깊이 차이(a-b) + 같은 조상이 될 때까지 이동 거리
        cnt = a - b + find_parent(p, q)
        total += cnt

    print(f"#{tc} {total}")
