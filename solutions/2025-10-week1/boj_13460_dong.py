
#상하좌우를 전부 구현, 바람직하지는 않은 것 같음.
#좌

#if문으로 앞에 있는 구슬을 먼저 옮긴 후 뒤에 있는 구슬을 옮김.
def left(balls):
    r1, r2, b1, b2 = balls

    if r2 < b2:
        check2 = True
    else:
        check2 = False

    check = False

    while True:
        if matrix[r1][r2-1] == '.':
            r2 -= 1
        elif matrix[r1][r2-1] == '#':
            break
        elif matrix[r1][r2-1] == 'O':
            check = True
            break

    while True:
        if matrix[b1][b2-1] == '.':
            b2 -= 1
        elif matrix[b1][b2-1] == '#':
            break
        elif matrix[b1][b2-1] == 'O':
            return 'fail'
        else:
            break
    if check:
        return 'success'

    if r1 == b1 and r2 == b2:
        if check2:
            b2 += 1
        else:
            r2 += 1


    return (r1, r2, b1, b2)

#우
def right(balls):
    r1, r2, b1, b2 = balls
    check = False

    if r2 > b2:
        check2 = True
    else:
        check2 = False

    while True:

        if matrix[r1][r2+1] == '.':
            r2 += 1
        elif matrix[r1][r2+1] == '#':
            break
        elif matrix[r1][r2+1] == 'O':
            check = True
            break


    while True:
        if matrix[b1][b2+1] == '.':
            b2 += 1
        elif matrix[b1][b2+1] == '#':
            break
        elif matrix[b1][b2+1] == 'O':
            return 'fail'
        else:
            break

    if check:
        return 'success'

    if r1 == b1 and r2 == b2:
        if check2:
            b2 -= 1
        else:
            r2 -= 1

    return (r1, r2, b1, b2)

#상
def up(balls):
    r1, r2, b1, b2 = balls
    check = False

    if r1 < b1:
        check2 = True
    else:
        check2 = False

    while True:

        if matrix[r1-1][r2] == '.':
            r1 -= 1
        elif matrix[r1-1][r2] == '#':
            break
        elif matrix[r1-1][r2] == 'O':
            check = True
            break
    while True:
        if matrix[b1-1][b2] == '.':
            b1 -= 1
        elif matrix[b1-1][b2] == '#':
            break
        elif matrix[b1-1][b2] == 'O':
            return 'fail'
        else:
            break

    if check:
        return 'success'

    if r1 == b1 and r2 == b2:
        if check2:
            b1 += 1
        else:
            r1 += 1

    return (r1, r2, b1, b2)

#하
def down(balls):
    r1, r2, b1, b2 = balls
    check = False

    if r1 > b1:
        check2 = True
    else:
        check2 = False


    while True:
        if matrix[r1+1][r2] == '.':
            r1 += 1
        elif matrix[r1+1][r2] == '#':
            break
        elif matrix[r1+1][r2] == 'O':
            check = True
            break
    while True:
        if matrix[b1+1][b2] == '.':
            b1 += 1
        elif matrix[b1+1][b2] == '#':
            break
        elif matrix[b1+1][b2] == 'O':
            return 'fail'

    if check:
        return 'success'

    if r1 == b1 and r2 == b2:
        if check2:
            b1 -= 1
        else:
            r1 -= 1

    return (r1,r2,b1,b2)

#dfs 구현 시작. 2**(n) = 충분(1000) * (상수)

def dfs(depth, balls, probability):

    global max_a
    if max_a <= depth:
        return

    if depth == 10:
        return 'fail'

    for i in probability:

        result = i(balls)

        if i in (up, down):
            if type(result) == tuple:
                dfs(depth+1, result,[left,right])

            elif result == 'fail':
                continue

            else:
                if max_a > depth+1:
                    max_a = depth+1
                return

        else:
            if type(result) == tuple:
                dfs(depth+1, result, [up, down])

            elif result == 'fail':
                continue

            else:
                if max_a > depth+1:
                    max_a = depth+1
                return

N, M = map(int, input().split())

matrix = [list(input()) for _ in range(N)]
# for i in matrix3:
#     print(*i)
for r in range(N):
    for c in range(M):
        if matrix[r][c] == 'R':
            matrix[r][c] = '.'
            red = (r,c)
        elif matrix[r][c] == 'B':
            matrix[r][c] = '.'
            blue = (r,c)

balls = (red[0],red[1],blue[0],blue[1])
max_a = 11
final_result = dfs(0, balls,[left, right, up, down])
if max_a == 11:
    max_a = -1
print(max_a)