import sys
from collections import defaultdict
sys.stdin = open('input/22861_input.txt', 'r')
input = sys.stdin.readline

def solve(move, check):
    move_dir(move)
    answer = []
    for path in check:
        kind, total = count_files(find_node(path))
        answer.append(f'{kind} {total}')

    return '\n'.join(answer)


# [핵심 로직] 폴더 이동 및 병합
# 주의: 여기서 A의 내용물을 B로 옮기는 것이지, A 폴더 자체를 B의 하위 폴더로 넣는 게 아님!
# 문제 조건에 따라 "이름이 겹치면 합친다"는 점이 중요함.
def move_dir(move):
    for A, B in move:
        # 1. A의 부모 경로와 A의 이름을 분리 (오른쪽에서 1번만 자름)
        parrent_path, name_A = A.rsplit('/', 1)
        
        # 2. 부모 폴더 노드를 찾아서, A 폴더를 통째로 떼어냄(pop)
        parrent_node = find_node(parrent_path)
        subtree_A = parrent_node['folders'].pop(name_A) # A 폴더 객체(딕셔너리) 획득

        # 3. B 폴더 노드를 찾음
        target_node = find_node(B)
        
        # 4. B 폴더에 A 폴더의 내용물을 병합(Merge)
        # target_node['folders'][name_A] = subtree_A 처럼 그냥 붙이면 안 됨!
        # B 내부에 이미 같은 파일/폴더가 있을 수 있으므로 재귀적으로 합쳐야 함.
        merge_tree(target_node, subtree_A)
    

# [재귀] 두 폴더 트리를 합치는 함수
# destination: 합쳐질 대상 폴더 (B)
# src: 옮겨올 폴더 (A)
def merge_tree(destination, src):
    # 1. 파일 합치기 (Set 자료구조를 쓰므로 중복 자동 제거됨)
    destination['files'].update(src['files'])

    # 2. 하위 폴더 합치기
    for folder_name, src_folder in src['folders'].items():
        # 만약 B에도 같은 이름의 폴더가 있다면 -> 그 안으로 또 들어가서 합쳐야 함 (재귀)
        if folder_name in destination['folders']:
            merge_tree(destination['folders'][folder_name], src_folder)
        # 없다면 -> 그냥 통째로 이동시키면 됨
        else:
            destination['folders'][folder_name] = src_folder     


# 경로 문자열을 따라가서 실제 폴더 노드(딕셔너리)를 반환하는 함수
def find_node(path_str):
    curr = root # 루트부터 탐색 시작

    # 'main'은 루트이므로 제외하고 그 다음부터 경로를 따라감
    # 'main'만 들어오는 경우도 있으므로 예외처리 필요할 수 있으나 문제 조건상 괜찮음
    path = path_str.split('/')[1:]
    
    for name in path:
        curr = curr['folders'][name] # 딕셔너리 안으로 계속 파고 들어감

    return curr


# [BFS/DFS] 하위 폴더까지 싹 뒤져서 파일 개수 세는 함수
def count_files(start_node):
    total_files = 0
    unique_files = set() # 파일 종류는 중복 제거해야 하므로 Set 사용

    stack = [start_node]
    while stack:
        curr = stack.pop()
        
        # 현재 폴더에 있는 파일들 집계
        total_files += len(curr['files'])
        unique_files.update(curr['files']) # Set 합집합

        # 자식 폴더들도 탐색하기 위해 스택에 추가
        for folder_node in curr['folders'].values():
            stack.append(folder_node)

    return total_files, len(unique_files)


def build_tree(current_name):
    # 내 노드 생성
    node = {
        'files': set(), 
        'folders': {}
    }
    
    # 내 자식들을 찾아서 채워넣기
    for child_name, type in temp_info[current_name]:
        if type == '1': # 폴더면
            # 재귀적으로 자식 폴더 생성해서 연결
            node['folders'][child_name] = build_tree(child_name)
        else: # 파일이면
            node['files'].add(child_name)
            
    return node

# -------------------------------------------------------------------------------------
N, M = map(int, input().split())
temp_info = defaultdict(list)

for _ in range(N + M):
    P, F, C = input().split()
    temp_info[P].append((F, C))

root = build_tree('main')

K = int(input())
move = [input().split() for _ in range(K)]
Q = int(input())
check = [input().strip() for _ in range(Q)]

print(solve(move, check))