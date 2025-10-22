def rows(r):
    num = matrix[r][0]
    n_count = p_count = 0
    for c in range(N):
        p = matrix[r][c]
        #같을 때
        if num == p:
            if p_count > 0:
                return False

            n_count += 1
            continue
        #내려갈 때
        elif num == p + 1:
            p_count += 1
            if p_count >= L:
                num = p
                p_count = 0
            n_count = 0
        # 올라갈 때
        elif num == p - 1:
            if p_count > 0:
                return False
            # 누적길이 넘으면 통과
            if n_count >= L:
                n_count = 1
                num = p
            else:
                return False

        else:
            return False

    if p_count > 0:
        return False
    else:
        return True

def cols(c):
    num = matrix[0][c]
    n_count = p_count = 0
    for r in range(N):
        p = matrix[r][c]
        #같을 때
        if num == p:
            if p_count > 0:
                return False

            n_count += 1
            continue
        #내려갈 때
        elif num == p + 1:
            p_count += 1
            if p_count >= L:
                num = p
                p_count = 0
            n_count = 0
        # 올라갈 때
        elif num == p - 1:
            if p_count > 0:
                return False
            # 누적길이 넘으면 통과
            if n_count >= L:
                n_count = 1
                num = p
            else:
                return False

        else:
            return False

    if p_count > 0:
        return False
    else:
        return True

N, L = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
count = 0
for i in range(N):
    if rows(i):
        count += 1

for j in range(N):
    if cols(j):
        count += 1

print(count)