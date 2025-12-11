# 공통 조상

from collections import deque

t = int(input())

# node에서 시작해서 루트(1번)까지 조상들을 리스트에 담는 함수
def find(node, data):
    # 부모가 있는 경우 (p[node] != 0 이면 아직 루트 아님)
    if p[node] != 0:
        data.append(node)          # 현재 노드를 기록하고
        return find(p[node], data) # 부모로 올라가면서 재귀

    else:
        # 부모가 없다는 건 루트라는 뜻(문제에서 루트는 1번 노드라고 가정)
        data.append(1)
        return data                # node ~ 1번까지의 경로 반환


for tc in range(1, t+1):

    # v: 정점 수, e: 간선 수, node1 / node2: 공통 조상을 찾을 두 노드
    v, e, node1, node2 = map(int, input().split())

    # plr로 진행(이진트리)
    p = [0] * (v+1)
    l = [0] * (v+1)
    r = [0] * (v+1)

    # 간선 정보 (부모 자식 순서로 e쌍이 들어옴)
    n_list = list(map(int, input().split()))

    # 간선 정보를 이용해 부모/자식 배열 채우기
    for i in range(e):
        s, e = n_list[2*i], n_list[2*i + 1]   # s: 부모, e: 자식

        # 왼쪽 자식이 비어있으면 왼쪽에 넣고
        if l[s] == 0:
            l[s] = e
            p[e] = s          # 자식의 부모 정보 기록

        # 이미 왼쪽이 차 있으면 오른쪽에 넣기
        else:
            r[s] = e
            p[e] = s

    # node1과 node2의 조상 경로(자기 자신 ~ 루트) 구하기
    p1 = find(node1, [])
    p2 = find(node2, [])
    # 예시: node1 = 8이면 [8, 4, 2, 1] 이런 식

    # 두 조상 리스트의 길이 중 더 짧은 쪽 기준으로만 비교
    temp = min(len(p1), len(p2))

    # 뒤에서부터(루트 방향) 비교하면서 처음으로 서로 다른 지점 직전이 LCA가 아니라,
    # **뒤에서부터 같은 지점 중 "가장 깊은" 공통 노드를 찾는 방식**
    # 인덱스: -1, -2, ... 이렇게 뒤에서부터 접근
    for idx in range(-temp, 0):
        if p1[idx] == p2[idx]:
            value = p1[idx]   # 가장 가까운 공통 조상(LCA)
            break

    # 이제 value(공통 조상)의 서브트리에 포함된 노드 개수를 세기
    basket = deque([value])
    count = 0
    while basket:
        k = basket.popleft()
        count += 1            # 방문한 노드 수 증가

        # 왼쪽 자식이 있으면 큐에 추가
        if l[k]:
            basket.append(l[k])
            # 오른쪽 자식도 있으면 큐에 추가
            if r[k]:
                basket.append(r[k])

    # value: 공통 조상, count: 그 정점을 루트로 하는 서브트리의 크기
    print(f"#{tc} {value} {count}")