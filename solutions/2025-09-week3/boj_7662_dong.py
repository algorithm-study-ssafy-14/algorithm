import heapq, sys

input = sys.stdin.readline

#이름 사전등록
heappush = heapq.heappush
heappop = heapq.heappop



T = int(input())


#최소힙과 최대힙 둘 다 생성
#튜플로 생성해서 각자 인덱스를 넣어둠.
#해당 값이 있는지 없는지는 id저장소에 있는 True/False로 한 번 더 판별.
#최대힙에서 최소값을 빼내기 힘들고, 마찬가지로 최소힙에서 최대값을 뺴내기 힘들기 때문에
#반대쪽에 있는 수를 억지로 빼내지 않고 pop했을 때 False값이면 없는 값으로 생각하고 더 뽑음.
for _ in range(T):
    k = int(input())
    min_heap = []
    max_heap = []
    id_storage = [False] * k


    for i in range(k):
        key, value = input().split()

        #값 저장시
        if key == 'I':
            value = int(value)
            heappush(min_heap, (value, i))
            heappush(max_heap, (-value, i))
            id_storage[i] = True

        #값을 빼낼 시

        #1일 경우 최대값 추출
        #id 저장소에 값이 True일 경우가 존재할 때 까지 값을 빼냄.
        else:
            if value == '1':

                while max_heap:
                    value, vid = heappop(max_heap)

                    if id_storage[vid]:
                        id_storage[vid] = False
                        break

        #-1일 경우 최소값 추출
        #마찬가지로 id 저장소에 값이 True일 경우가 존재할 때 까지 값을 빼냄.
            else:
                while min_heap:
                    value, vid = heappop(min_heap)

                    if id_storage[vid]:
                        id_storage[vid] = False
                        break


    ans = []
    #남은 수 중에서 출력
    while max_heap:
        value, vid = heappop(max_heap)

        #id저장소에 아직 꺼내지지 않은 값이 있다면 꺼냄.
        if id_storage[vid]:
            ans.append(-value)
            break

    #트리안에 값이 없을 경우
    if not ans:
        print('EMPTY')

    #만약 max_heap에 값이 있었다면 min_heap도 값 존재
    else:
        while min_heap:
            value, vid = heappop(min_heap)

            if id_storage[vid]:
                ans.append(value)
                break

        print(*ans)
