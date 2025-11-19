T = int(input())

for test_case in range(1, T + 1):

    V, E, s1, s2 = map(int, input().split())

    graph = [[] for _ in range(V + 1)]              # 그래프

    input_list = list(map(int, input().split()))    # 입력을 받을 리스트

    parent = [0] * (V + 1)                          # 부모를 확인할 리스트

    for i in range(0, len(input_list), 2):          # 그래프, 부모 확인
        a, b = input_list[i], input_list[i+1]

        graph[a].append(b)
        parent[b] = a

    s1_parent = set()                               # s1 의 부모들, 본인 포함

    x = s1

    while x:
        s1_parent.add(x)                            # 넣기
        x = parent[x]

    common_parent = 1                               # 공통 조상

    y = s2

    while y:
        if y in s1_parent:                          # y 가 s1_parent 에 있으면, y 가 공통 조상임
            common_parent = y
            break
        y = parent[y]

    stack = [common_parent]                         # 크기 파악을 위한 리스트
    size = 0

    while stack:
        cur = stack.pop()
        size += 1
        for nxt in graph[cur]:
            stack.append(nxt)

    print(f"#{test_case} {common_parent} {size}")