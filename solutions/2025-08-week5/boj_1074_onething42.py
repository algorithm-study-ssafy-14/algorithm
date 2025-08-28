n, r, c = map(int, input().split())
N = 2 ** n
num = 0


def check(x, y, N):
    global num
    if N > 2:
        size = N // 2
        # 어느 사분면에 있는지 판단
        if r < x + size and c < y + size:  # 1사분면
            return check(x, y, size)
        elif r < x + size and c >= y + size:  # 2사분면
            num += size * size
            return check(x, y + size, size)
        elif r >= x + size and c < y + size:  # 3사분면
            num += 2 * size * size
            return check(x + size, y, size)
        else:  # 4사분면
            num += 3 * size * size
            return check(x + size, y + size, size)
    else:
        # 2x2 블록 직접 탐색
        for dx, dy in [(0, 0), (0, 1), (1, 0), (1, 1)]:
            if x + dx == r and y + dy == c:
                return num
            num += 1


print(check(0, 0, N))
