#import time
#start_1 = time.time()

##한다면 deepcopy 대신 일반 copy()로 쓰는 것이 좋음.
from copy import deepcopy
from collections import deque

# 벽 세우기의 모든 조합 생성
def dfs(depth, start):
    #벽 3개를 세웠으면 total_set에 저장
    if depth == 3:
        total_set.append(subset.copy())

    else:
        #set_list 의 남은 좌표들을 선택
        for i in range(start, len(set_list)):
            subset.append(set_list[i])
            dfs(depth+1, i+1)
            subset.pop()
#-----------------------------------------------------------------------------
#연구소 크기 입력
n, m = map(int, input().split())

#연구소 지도 입력
matrix = [list(map(int, input().split())) for _ in range(n)]

set_list = []  # 벽을 세울 수 있는 빈칸 좌표
subset = []    # DFS에서 사용되는 현재 선택 좌표
total_set = [] # 벽 3개 조합 리스트
dirs = [[0,1], [1,0], [-1,0], [0,-1]]
# 0인 곳 찾기
for r in range(n):
    for c in range(m):
        if matrix[r][c] == 0:
            set_list.append([r,c])

# 전염 근원지 찾기
contaminated_zone = deque()
for r in range(n):
    for c in range(m):
        if matrix[r][c] == 2:
            contaminated_zone.append([r,c])

# 벽 세우기 조합 생성
dfs(0,0)

maximized = 0
#0 인 곳에서 벽이 세워진 수 만큼 빼기.(초기 안전영역 수)
counter = len(set_list) - 3

# 모든 벽 조합에 대해 바이러스 넣음 + 시뮬
for a_list in total_set:
    matrix2 = deepcopy(matrix)
    count = counter            #초기화
    check_mat = [[1] * m for _ in range(n)] #방문 체크
    cont2 = deepcopy(contaminated_zone)     #바이러스 위치 복제

    for i, j in a_list:
        matrix2[i][j] = 1
    while cont2:
        r, c = cont2.popleft()
        for dr, dc in dirs:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < n and 0 <= nc < m and matrix2[nr][nc] == 0 and check_mat[nr][nc] == 1:
                check_mat[nr][nc] = 0   #방문 처리
                count -= 1              # 안전 영역 감소
                cont2.append([nr,nc])   # 큐에 추가

    #안전영역 최대값 갱신
    if maximized < count:
        maximized = count

#결과 출력
print(maximized)

#end_1 = time.time()
#print(end_1 - start_1)