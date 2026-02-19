from bisect import bisect_right

N, M, K = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort()
queries = list(map(int, input().split()))

# parent[i] : i번째 카드가 막혔을 때 다음 후보 인덱스를 가리키는 DSU
parent = list(range(M + 1))  # 0..M, M은 sentinel(더 이상 없음)

# union find
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

out = []
for x in queries:
    idx = bisect_right(cards, x)   # first index with cards[idx] > x
    real = find(idx)              # skip used cards
    out.append(str(cards[real]))
    parent[real] = find(real + 1) # union 과정

print("\n".join(out))
