import heapq
T = int(input().strip())

for _ in range(T):
    k = int(input().strip())

    min_heap = []
    max_heap = []
    visited = [False] * k

    for i in range(k):
        char, num = input().split()
        num = int(num)

        if char == 'I':
            heapq.heappush(min_heap, (num, i))

            heapq.heappush(max_heap, (-num, i))

        else:

            if num == 1:
                while max_heap and visited[min_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = True
                    heapq.heappop(max_heap)
            else:
                while min_heap and visited[max_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = True
                    heapq.heappop(min_heap)

        while max_heap and visited[max_heap[0][1]]:
            heapq.heappop(max_heap)
        while min_heap and visited[min_heap[0][1]]:
            heapq.heappop(min_heap)

    if not max_heap or not min_heap:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])