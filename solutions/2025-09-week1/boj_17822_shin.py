#앞 뒤 양쪽에서 빼기 위함
from collections import deque

#입력값 받아오기
N, M, T = map(int, input().split())
matrix = [0] + [deque(map(int, input().split())) for _ in range(N)]

#후에 평균값을 계산하기 위한 변수
counter = N * M

#입력값 받으며 횟수만큼 순회
for _ in range(T):

    x, d, k = map(int, input().split())

    # 배수 찾아서 원판 돌리기
    i = 1
    while x * i <= N:
        #배수
        t = x * i
        #방향
        if d == 0:
            for j in range(k):
                h = matrix[t].pop()
                matrix[t].appendleft(h)

        if d == 1:
            for j in range(k):
                h = matrix[t].popleft()
                matrix[t].append(h)
        i += 1


    # 인접한 값 제거할 자리값 색출
    remover = set()
    for r in range(1, N + 1):
        for c in range(M):
            #인접한 값 같을 시 뽑아옴.
            #굳이 집합이 아니라 다른 형태로 가져온 후 지정된 값(r,c)만 가져오면 될 것 같음.
            if matrix[r][c] == 0:
                continue

            if matrix[r][c] == matrix[r][(c - 1) % M]:
                remover |= {(r, c), (r, (c - 1) % M)}

            if matrix[r][c] == matrix[r][(c + 1) % M]:
                remover |= {(r, c), (r, (c + 1) % M)}

            if r < N:
                if matrix[r][c] == matrix[r + 1][c]:
                    remover |= {(r, c), (r + 1, c)}

            if r > 1:
                if matrix[r][c] == matrix[r - 1][c]:
                    remover |= {(r, c), (r - 1, c)}
    
    #평균값 계산용
    counter -= len(remover)
    
    # remover에 등록된 값이 있다면 값 제거
    if remover:
        for r, c in remover:
            matrix[r][c] = 0

    #remover가 없다면 평균 구한 후 +1/-1
    else:
        #zero division error 방지
        if counter == 0:
            break

        else:
            a_sum = 0
            for r in range(1, N + 1):
                a_sum += sum(matrix[r])
                a_avg = a_sum / counter

            for r in range(1, N + 1):
                for c in range(M):
                    if matrix[r][c] != 0:
                        if matrix[r][c] > a_avg:
                            matrix[r][c] -= 1
                        elif matrix[r][c] < a_avg:
                            matrix[r][c] += 1

#결과
total = 0
for r in range(1, N + 1):
    total += sum(matrix[r])

print(total)