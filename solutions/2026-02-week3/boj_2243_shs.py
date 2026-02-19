import sys
# [주의] 백준 제출 시에는 아래 경로 설정을 주석 처리하거나 삭제해야 런타임 에러를 방지할 수 있습니다.
sys.stdin = open('input/2243_input.txt', 'r')
input = sys.stdin.buffer.readline  # 대량의 입력을 빠르게 처리하기 위해 buffer.readline 사용

MAX_CANDY = 1_000_001

class SegTree:
    __slots__ = ('n', 'size', 'tree')

    def __init__(self, n):
        self.n = n
        size = 1
        # n보다 크거나 같은 2의 거듭제곱 중 가장 작은 값을 size로 설정
        # 이렇게 하면 트리를 완전 이진 트리 형태로 관리하기 편함
        while size < n:
            size *= 2
        self.size = size
        self.tree = [0] * (2 * size)

    def total(self):
        return self.tree[1]

    def update(self, idx, delta):
        self._update(idx, delta)

    def _update(self, idx, delta):
        # 리프 노드의 인덱스를 찾음. idx는 1부터 시작하므로 1을 빼줌.
        i = self.size + (idx - 1)
        self.tree[i] += delta
        i >>= 1
        # 리프 노드부터 루트까지 거슬러 올라가며 합 갱신
        while i:
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]
            i >>= 1
    
    def kth(self, k):
        return self._kth(k)

    def _kth(self, k):
        node = 1
        # 리프 노드에 도달할 때까지 탐색
        while node < self.size:
            left = node * 2
            right = node * 2 + 1
            # 왼쪽 자식 노드에 있는 사탕 개수가 k보다 크거나 같다면 왼쪽으로 이동
            if k <= self.tree[left]:
                node = left
            else:
                # 왼쪽 자식 노드에 충분하지 않다면, 왼쪽 개수만큼 k에서 빼고 오른쪽으로 이동
                k -= self.tree[left]
                node = right
        # 최종 도달한 리프 노드의 인덱스를 맛의 번호(1-based)로 변환하여 반환
        return (node - self.size) + 1


def main():
    try:
        line = input()
        if not line:
            return
        N = int(line)
    except ValueError:
        return

    # 맛의 종류가 최대 1,000,000번까지 있음
    seg_tree = SegTree(MAX_CANDY)

    result = []
    for _ in range(N):
        query = list(map(int, input().split()))
        
        # 1 B: 사탕상자에서 맛의 순위가 B번째인 사탕을 꺼낸다.
        if query[0] == 1:
            B = query[1]
            # [중요] B번째 사탕의 '맛'을 찾음
            taste = seg_tree.kth(B)
            result.append(str(taste))
            # 사탕을 꺼냈으므로 해당 맛의 개수를 1 줄임
            # (최적화 포인트: kth 구하는 과정에서 바로 감소시킬 수도 있지만, 분리하는 것이 로직 이해에 좋음)
            seg_tree.update(taste, -1)

        # 2 B C: 맛이 B인 사탕을 C개 넣거나 뺀다.
        else:
            B, C = query[1], query[2]
            seg_tree.update(B, C)


    answer = '\n'.join(result)
    sys.stdout.write(answer)

if __name__ == '__main__':
    main()