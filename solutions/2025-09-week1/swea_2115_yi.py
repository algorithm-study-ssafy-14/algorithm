T = int(input())
for test_case in range(1, T + 1):
    n, m, c = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    res = 0

    for i in range(n):
        for j in range(n):
            if j + m <= n:
                sub1 = arr[i][j:j + m]
                p1_val = 0
                for a in range(m):
                    if sub1[a] <= c:
                        p1_val = max(p1_val, sub1[a] ** 2)
                    for b in range(a + 1, m):
                        s = sub1[a] + sub1[b]
                        if s <= c:
                            p1_val = max(p1_val, sub1[a] ** 2 + sub1[b] ** 2)
                        for d in range(b + 1, m):
                            s2 = s + sub1[d]
                            if s2 <= c:
                                p1_val = max(p1_val, sub1[a] ** 2 + sub1[b] ** 2 + sub1[d] ** 2)
                            for e in range(d + 1, m):
                                s3 = s2 + sub1[e]
                                if s3 <= c:
                                    p1_val = max(p1_val, sub1[a] ** 2 + sub1[b] ** 2 + sub1[d] ** 2 + sub1[e] ** 2)

            for k in range(n):
                if k == i:
                    start_h = j + m
                else:
                    start_h = 0
                for h in range(start_h, n):
                    if h + m <= n:
                        sub2 = arr[k][h:h + m]
                        p2_val = 0
                        for a in range(m):
                            if sub2[a] <= c:
                                p2_val = max(p2_val, sub2[a] ** 2)
                            for b in range(a + 1, m):
                                s = sub2[a] + sub2[b]
                                if s <= c:
                                    p2_val = max(p2_val, sub2[a] ** 2 + sub2[b] ** 2)
                                for d in range(b + 1, m):
                                    s2 = s + sub2[d]
                                    if s2 <= c:
                                        p2_val = max(p2_val, sub2[a] ** 2 + sub2[b] ** 2 + sub2[d] ** 2)
                                    for e in range(d + 1, m):
                                        s3 = s2 + sub2[e]
                                        if s3 <= c:
                                            p2_val = max(p2_val, sub2[a] ** 2 + sub2[b] ** 2 + sub2[d] ** 2 + sub2[e] ** 2)

                        res = max(res, p1_val + p2_val)

    print(f"#{test_case} {res}")