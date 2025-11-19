## 3번

for tc in range(1, 11):
    n = int(input())
    n_list = list(map(int, input().split()))
    m = int(input())
    input_orders = list(input().split())

    # 숫자는 type 변환
    orders = [int(x) if x.isdigit() else x for x in input_orders]

    # 포인터로 인덱싱
    pointer = 0
    for _ in range(m):
        order = orders[pointer]

        if order == 'I':
            x, y = orders[pointer+1], orders[pointer+2]
            sub_list = list(orders[pointer+3:pointer+3+y])
            pointer += 3 + y
            # 빈 공간에 넣기
            n_list[x+1:x+1] = sub_list

        elif order == 'D':
            x, y = orders[pointer+1], orders[pointer+2]
            pointer += 3
            # 값 제거
            n_list[x+1:x+1+y] = []

        elif order == 'A':
            x = orders[pointer+1]
            sub_list = list(orders[pointer+2:pointer+2+x])
            pointer += 2 + x
            # extend 활용
            n_list.extend(sub_list)


    print(f"#{tc}", end=' ')
    #처음부터 출력하면 계속 답이 달라지는데 왜그런지 모르겠음.(결국 n_list[0] 뺌)
    print(*n_list[1:11])