import sys
# 로컬 테스트용 입력 파일 설정 (제출 시 주석 처리 또는 제거 필요)
sys.stdin = open('input/16566_input.txt', 'r')
input = sys.stdin.buffer.readline
from bisect import bisect_right

def main(Red, Blue):
    global parent
    # parent 배열 초기화: 0부터 M까지의 인덱스 생성
    # Disjoint Set(유니온 파인드)의 parent 배열 역할을 함
    # parent[i]는 i번 인덱스 카드가 사용되었을 때, 다음으로 확인해야 할 인덱스를 가리킴
    parent = [i for i in range(M + 1)]
    answer = []

    for a in Blue:
        # 이분 탐색(bisect_right): 민수(Blue)의 카드 a보다 큰 카드 중 가장 작은 카드의 위치(인덱스)를 찾음
        # Red 리스트는 정렬되어 있어야 함
        idx = bisect_right(Red, a)
        
        # find 함수를 통해 실제로 사용 가능한 카드의 인덱스(draw)를 찾음
        # 만약 idx 위치의 카드가 이미 사용되었다면, parent 포인터를 따라 다음 사용 가능한 카드를 찾게 됨
        draw = find(idx)
        
        # 찾은 카드를 정답 리스트에 추가
        answer.append(str(Red[draw]))
        
        # 중요: 사용한 카드(draw) 처리
        # 현재 사용한 인덱스(draw)를 다음 인덱스(draw + 1)와 연결(Union 연산과 유사)
        # 즉, 다음에 다시 draw 인덱스가나오면 바로 draw + 1 (혹은 그 뒤의 가용 카드)로 이동하게 됨
        parent[draw] = find(draw + 1)
        
    return '\n'.join(answer)


# 경로 압축(Path Compression)을 적용한 Find 함수
# 재귀 대신 반복문을 사용하여 스택 오버플로우 방지 및 효율성 증대
def find(x):
    # 자기 자신이 부모가 아닐 때(즉, 이미 다른 노드를 가리키고 있을 때)
    while parent[x] != x:
        # 경로 압축: 현재 노드의 부모를 '부모의 부모'로 바로 갱신
        # 이렇게 하면 다음에 find(x)를 호출할 때 탐색 경로가 절반으로 줄어듬
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

# 입력 처리
# N: 카드의 수, M: 철수가 가진 카드의 수, K: 게임 턴 수
N, M, K = map(int, input().split())
Red = list(map(int, input().split()))
Blue = list(map(int, input().split()))

# 이분 탐색을 사용하기 위해 Red 리스트 정렬 필수
Red.sort()

# 결과 출력
sys.stdout.write(main(Red, Blue))