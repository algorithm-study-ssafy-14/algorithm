def find_parent(cur, k):
    if cur == 1:
        return 1
    return (cur - 2) // k + 1


N, K, Q = map(int, input().split())

for _ in range(Q):
    start, end = map(int, input().split())

    if K == 1:
        print(abs(start - end))
        continue

    result = 0

    while start != end:
        if start < end:
            end = find_parent(end, K)
        else:
            start = find_parent(start, K)
        result += 1

    print(result)