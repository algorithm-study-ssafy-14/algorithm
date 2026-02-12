# 폴더 정리

from collections import deque

a, b = map(int, input().split())

# tree[idx] = 해당 폴더(idx)가 직접 포함하는 "이름"들의 집합 (폴더/파일 모두 이름 문자열)
tree = [set() for _ in range(a + 1)]

# pointer_storage[folder_name] = (parent_idx, my_idx)
# 폴더 이름은 유일하다고 가정하므로, 이름으로 인덱스를 바로 찾는다.
pointer_storage = {'main': (-1, 0)}
pointer = 0

# idx_to_name[idx] = 폴더 이름 (후에 postorder 결과를 "이름"으로 저장하기 위해 필요)
idx_to_name = [''] * (a + 1)
idx_to_name[0] = 'main'

# ------------------------------------------------------------
# 1) 입력을 먼저 children에 모아두기
#    org(부모)가 아직 인덱스가 없을 수도 있으므로, 바로 tree를 채우지 않고
#    org -> [(name, isfolder), ...] 형태로 저장해둔다. (KeyError 방지)
# ------------------------------------------------------------
children = {}  # org_name -> list of (name, isfolder)
for _ in range(a + b):
    org, name, isfolder = input().split()
    children.setdefault(org, []).append((name, isfolder))

# ------------------------------------------------------------
# 2) main부터 BFS로 내려가며 폴더에 인덱스 부여 + tree 채우기
#    - org 폴더에 속한 자식 이름들은 tree[org_idx]에 추가
#    - 자식이 폴더(isfolder=='1')라면 pointer_storage에 등록하고 큐에 넣어 확장
# ------------------------------------------------------------
q = deque(['main'])
while q:
    org = q.popleft()
    org_idx = pointer_storage[org][1]

    for name, isfolder in children.get(org, []):
        # org 폴더의 "직접 자식"으로 name을 추가 (파일/폴더 공통)
        tree[org_idx].add(name)

        # 폴더만 인덱스 생성 + 다음 탐색 대상으로 추가
        if isfolder == '1' and name not in pointer_storage:
            pointer += 1
            pointer_storage[name] = (org_idx, pointer)
            idx_to_name[pointer] = name
            q.append(name)

# ------------------------------------------------------------
# 3) 이동 연산 처리
#    parent 경로에서 p 폴더를 찾아, p 내부의 모든 자식을 child 경로의 ch 폴더로 "합치기"
#    - p 자체는 ance(부모)에서 제거(삭제)
#    - p의 자식 폴더들은 부모 idx를 ch_idx로 갱신
# ------------------------------------------------------------
c = int(input())
for _ in range(c):
    parent, child = input().split()
    ance = parent.split('/')[-2]  # parent 경로의 상위 폴더 이름
    p = parent.split('/')[-1]     # 이동 대상 폴더 이름
    ch = child.split('/')[-1]     # 목적지 폴더 이름

    p_idx = pointer_storage[p][1]
    ch_idx = pointer_storage[ch][1]

    # p 안의 모든 자식(파일/폴더)을 ch로 옮김 (set union과 유사한 "합치기")
    # tree[p_idx]를 순회하면서 동시에 수정하면 위험하므로 list로 복사해 순회
    for j in list(tree[p_idx]):
        if j in pointer_storage:  # j가 폴더라면 부모 인덱스도 ch로 갱신
            pointer_storage[j] = (ch_idx, pointer_storage[j][1])
        tree[ch_idx].add(j)

    # p는 비워지고, 상위 폴더(ance)에서 p 이름을 제거 (폴더 삭제 효과)
    tree[p_idx].clear()
    tree[pointer_storage[ance][1]].discard(p)  # discard: 없으면 에러 없이 무시

# ------------------------------------------------------------
# 4) 이동 후 최종 트리 기준으로 postorder 재생성
#    DP를 "자식 -> 부모" 순서로 누적해야 하므로 postorder가 필요.
#    재귀 대신 스택으로 (enter/exit) 상태를 둬서 postorder를 만든다.
# ------------------------------------------------------------
orders = deque()
root = 0  # main idx

# state: 0이면 enter(자식 먼저 push), 1이면 exit(지금 노드를 orders에 추가)
stack = [(root, 0)]
while stack:
    idx, state = stack.pop()
    if state == 0:
        stack.append((idx, 1))
        # 현재 폴더의 자식들 중 "폴더"만 내려간다 (파일은 DP 단계에서 처리)
        for name in tree[idx]:
            if name in pointer_storage:
                stack.append((pointer_storage[name][1], 0))
    else:
        # 자식이 모두 처리된 뒤(후위), 현재 노드 이름을 기록
        orders.append(idx_to_name[idx])

# ------------------------------------------------------------
# 5) DP: 폴더별 (서브트리 내 파일 종류 수 / 전체 파일 수) 계산
#    - set_counter[idx] : idx 폴더 서브트리에 존재하는 "파일 이름 종류" 집합
#    - total_counter[idx]: idx 폴더 서브트리에 존재하는 "전체 파일 개수"
#    postorder로 돌면 자식 결과를 부모에 누적할 수 있다.
# ------------------------------------------------------------
set_counter = [set() for _ in range(a + 1)]
total_counter = [0] * (a + 1)

d = int(input())

for folder_name in orders:
    idx = pointer_storage[folder_name][1]

    # 현재 폴더의 직접 자식들을 훑으며 누적
    for name in tree[idx]:
        if name in pointer_storage:  # 자식이 폴더면: 그 폴더의 DP 결과를 가져와 합침
            cidx = pointer_storage[name][1]
            set_counter[idx] |= set_counter[cidx]
            total_counter[idx] += total_counter[cidx]
        else:
            # 자식이 파일이면: 종류 set에 추가, 총 개수 +1
            set_counter[idx].add(name)
            total_counter[idx] += 1

# ------------------------------------------------------------
# 6) 질의 처리
#    입력 경로의 마지막 토큰이 폴더 이름이고, 폴더 이름은 유일하다고 가정
#    출력: (파일 종류 개수, 전체 파일 개수)
# ------------------------------------------------------------
for _ in range(d):
    target = input().split('/')[-1]
    t = pointer_storage[target][1]
    print(len(set_counter[t]), total_counter[t])
