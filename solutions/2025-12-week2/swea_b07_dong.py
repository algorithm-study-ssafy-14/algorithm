# 중위 순회

# p/l/r 로 구현했지만 여기서 p는 노드의 value를 표현.
for tc in range(1, 11):
    n = int(input())
    p = [0] * (n+1)
    l = [0] * (n+1)
    r = [0] * (n+1)

    for _ in range(n):
        n_list = list(input().split())

        #숫자만 int로 변환
        n_list = [int(i) if i.isdigit() else i for i in n_list]

        # 자식이 2개
        if len(n_list) == 4:
            p[n_list[0]] = n_list[1]
            l[n_list[0]] = n_list[2]
            r[n_list[0]] = n_list[3]

        # 자식이 하나
        elif len(n_list) == 3:
            p[n_list[0]] = n_list[1]
            l[n_list[0]] = n_list[2]

        # 자식 없음
        else:
            p[n_list[0]] = n_list[1]

    result = []
    
    # 중위순회 재귀
    def recursion(start):

        if l[start]:
            recursion(l[start])

        result.append(p[start])

        if r[start]:
            recursion(r[start])

    recursion(1)
    result = ''.join(result)

    print(f"#{tc} {result}")