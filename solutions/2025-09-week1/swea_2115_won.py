T = int(input())
 
 
def find_val(arr, c):
    if sum(arr) <= c:
        res = 0
        for num in arr:
            res += num * num
        return res
 
    best = 0
    l = len(arr)
    for mask in range(1 << l):
        s = v = 0
        ok = True
        for i in range(l):
            if mask & (1 << i):
                x = arr[i]
                s += x
                if s > c:
                    ok = False
                    break
                v += x * x
        if ok and best < v:
            best = v
    return best
 
 
for test_case in range(1, T + 1):
 
    N, M, C = map(int, input().split())
 
    my_list = [list(map(int, input().split())) for _ in range(N)]
 
    sub_list = []
    val_list = [[] for _ in range(N)]
 
    for i in range(N):
        for j in range(N - M + 1):
            sub_list = my_list[i][j:j+M]
            val_list[i].append(find_val(sub_list, C))
 
    best_v = result = 0
    r1 = c1 = 0
    for i in range(N):
        for j in range(N - M + 1):
            if best_v < val_list[i][j]:
                best_v = val_list[i][j]
                r1, c1 = i, j
    result += best_v
    best_v = 0
 
    r2, c2 = 0, 0
    for i in range(N):
        for j in range(N - M + 1):
            if i == r1 and abs(j - c1) < M:
                continue
            if best_v < val_list[i][j]:
                best_v = val_list[i][j]
                r2, c2 = i, j
 
    result += best_v
 
    print(f"#{test_case} {result}")
