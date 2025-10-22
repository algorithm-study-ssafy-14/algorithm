from itertools import combinations

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
res = float('inf')
for i in combinations(range(n), n//2):
    start_sum = 0
    link_sum = 0
    link = [j for j in range(n) if j not in i]
    #print(f"start:{i}, link:{link}")
    for a,b in combinations(i, 2):
        start_sum += s[a][b] + s[b][a]
    for a,b in combinations(link, 2):
        link_sum += s[a][b] + s[b][a]
    #print(f"start_sum:{start_sum}, link_sum:{link_sum}")
    res = min(res, abs(start_sum-link_sum))
print(res)