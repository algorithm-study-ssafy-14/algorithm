import heapq
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    min_heap = []
    max_heap = []
    exist = dict()  # value: 남은 개수

    for _ in range(k):
        cmd, num = input().split()
        num = int(num)

        if cmd == 'I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            if num in exist:
                exist[num] += 1
            else:
                exist[num] = 1
        elif cmd == 'D':
            if exist:
                if num == 1:  # 최대값 삭제
                    while max_heap:
                        x = -heapq.heappop(max_heap)
                        if exist.get(x, 0) > 0:
                            exist[x] -= 1
                            if exist[x] == 0:
                                del exist[x]
                            break
                else:         # 최소값 삭제
                    while min_heap:
                        x = heapq.heappop(min_heap)
                        if exist.get(x, 0) > 0:
                            exist[x] -= 1
                            if exist[x] == 0:
                                del exist[x]
                            break

    # 힙 정리
    while min_heap and exist.get(min_heap[0], 0) == 0:
        heapq.heappop(min_heap)
    while max_heap and exist.get(-max_heap[0], 0) == 0:
        heapq.heappop(max_heap)

    if not exist:
        print("EMPTY")
    else:
        print(-max_heap[0], min_heap[0])
