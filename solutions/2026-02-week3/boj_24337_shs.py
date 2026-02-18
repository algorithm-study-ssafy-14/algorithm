import sys
sys.stdin = open('input/24337_input.txt', 'r')
input = sys.stdin.readline


def main(n, a, b):
    # 중요: a + b - 1은 필요한 최소 건물의 수 (H가 중복되므로 -1)
    # 이 값이 N보다 크면 조건을 만족하는 건물을 지을 수 없음
    if a + b - 1 > n:
        return -1

    # L: 왼쪽에서 보이는 건물 리스트 (1부터 a-1까지 증가)
    L = [x for x in range(1, a)]
    # R: 오른쪽에서 보이는 건물 리스트 (b-1부터 1까지 감소)
    R = [y for y in range(b - 1, 0, -1)]
    # H: 가장 높은 건물 (a와 b 중 최댓값)
    H = max(a, b)

    # 기본 형태 구성
    core = L + [H] + R

    len_answer = len(core)

    # N보다 길이가 짧을 경우 1로 채워넣음 (사전순 최소를 위해)
    if len_answer < n:
        # 주의: a가 1인 경우, 가장 높은 건물이 맨 처음에 와야 함
        # 따라서 부족한 길이만큼의 1들을 H 뒤에 배치해야 함 (맨 앞에 두면 a가 늘어남)
        if a == 1:
            answer = [H] + [1] * (n - len_answer) + R
        # a > 1인 경우, 1들을 맨 앞에 배치
        # 맨 앞의 1 외에는 자신보다 앞의 1이나 뒤의 오름차순 건물에 의해 가려짐
        else:
            answer = [1] * (n - len_answer) + core
    else:
        answer = core

    result = ' '.join(map(str, answer))

    return result

N, a, b = map(int, input().split())

print(main(N, a, b))