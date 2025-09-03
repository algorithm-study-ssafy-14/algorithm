# valid 확인
def isvalid(r, c, p, q):
    # 일종의 가지치기
    if a_max >= (p - r) * 2:
        return False
    # 대각선 (+,+), (-,-) 방향
    d = ((p + q) - (r + c)) // 2

    # 대각선 (+,-)/(-,+) 방향
    e = (p - r) - d

    # (0< x <n-1) 확인용 좌표
    r2 = r + d
    c2 = c + d
    p2 = p - d
    q2 = q - d
    if 0 <= r2 < N and 0 <= c2 < N and 0 <= p2 < N and 0 <= q2 < N:

        # 중복시 탈출용 집합
        a_set = set()

        # for문 순회하며 사각형 탐색 (+,+),(-,-) 방향
        for i in range(d):
            if matrix[r + i][c + i] not in a_set:
                a_set.add(matrix[r + i][c + i])
            else:
                return False

            if matrix[p - i][q - i] not in a_set:
                a_set.add(matrix[p - i][q - i])
            else:
                return False

        # for문 순회하며 사각형 탐색 (+,-),(-,+) 방향
        for i in range(1, e + 1):
            if matrix[r + i][c - i] not in a_set:
                a_set.add(matrix[r + i][c - i])
            else:
                return False
            if matrix[p - i][q + i] not in a_set:
                a_set.add(matrix[p - i][q + i])
            else:
                return False

        # 다 다른 번호일 때 대각선 크기 리턴
        return (p - r) * 2

    else:
        return False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 0,1 대각선
    a_max = -1
    for r in range(N):
        # 대각선 방향 sorting
        for c in range((r + 1) % 2, N, 2):
            # 대각선 방향 꼭짓점 탐색
            # r+2부터 시작, 불필요한 추가탐색 제거
            for p in range(r + 2, N):
                for q in range((p + 1) % 2, N, 2):
                    result = isvalid(r, c, p, q)
                    if result:
                        if a_max < result:
                            a_max = result
    # 0,0 대각선
    for r in range(N):
        # 대각선 방향 sorting
        for c in range(r % 2, N, 2):
            # 대각선 방향 꼭짓점 탐색
            # r+2부터 시작, 불필요한 추가탐색 제거
            # 두 대각선 꼭짓점이 완벽히 대각선 상에 일치 할 경우,
            # (사각형이 아닐 모양일 경우 값 중복으로 알아서 탈락)
            # 원한다면 추가적인 범위 탐색 지정 가능, 지금은 isvalid()에서 거르는 상태.
            for p in range(r + 2, N):
                # 대각선 방향 sorting
                for q in range(p % 2, N, 2):
                    result = isvalid(r, c, p, q)

                    # 값이 참이라면: 맥스값 확인
                    if result:
                        if a_max < result:
                            a_max = result

    print(f"#{tc} {a_max}")