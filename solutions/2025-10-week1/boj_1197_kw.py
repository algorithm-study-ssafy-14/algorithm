# 크루스칼 알고리즘

def find_set(x):
    if x == parents[x]:
        return x

    while parents[x] != parents[parents[x]]:
        parents[x] = parents[parents[x]]

    return parents[x]


def union(x, y):
    rx = find_set(x)
    ry = find_set(y)

    if rx == ry:
        return

    if rx < ry:
        parents[ry] = rx
    else:
        parents[rx] = ry


V, E = map(int, input().split())

edges = []
for _ in range(E):
    s, e, w = map(int, input().split())

    edges.append([s, e, w])

edges.sort(key=lambda x: x[2])

cnt = 0
result = 0

# 정점이 1부터 시작하기 때문에 V + 1 개 만들어줌
parents = [i for i in range(V + 1)]

for s, e, w in edges:
    if find_set(s) != find_set(e):
        union(s, e)
        cnt += 1
        result += w

        if cnt == V - 1:
            break

print(result)
