# 버블 소트

from heapq import heappush, heappop

n = int(input())
m = n - 1
depth = 1
while m:
    m //= 2
    depth += 1

n_list = list(map(int, input().split()))
temp = 2**(depth-1)
n_compressed = [temp] * n

#---------------------------------------------------좌표 압축
pq = []
for i in range(n):
    heappush(pq, (n_list[i], i))

pointer = -1
correction = -100000000000
calc = 1
while pq:
    num, temp = heappop(pq)

    if num != correction:
        pointer += calc
        calc = 1
    else:
        calc += 1

    n_compressed[temp] += pointer


    correction = num

#print(n_compressed)
seg_tree = [0] * (2**depth)

#------------------------------------------(세그트리)

ans = 0

def counting(num):
    cnt = 0
    while num > 1:
        if not num % 2:
            cnt += seg_tree[num+1]
        seg_tree[num] += 1
        num >>= 1

    return cnt


for i in range(n):
    ans += counting(n_compressed[i])
    #print(ans)
print(ans)
