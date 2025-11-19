# 공통조상 찾기
# 자신의 조상 나열
def find(me):
    a_list = []
    while True:
        # 꼭대기일 경우 종료
        if P[me] == 0:
            break
        # 꼭대기 전까지 계속 list에 기록
        else:
            a_list.append(P[me])
            me = P[me]
    return a_list

# bfs 탐색
def family(me):
    global count
    basket = [me]
    while basket:
        r = basket.pop()
        if L[r] != 0:
            basket.append(L[r])
            count += 1
        if R[r] != 0:
            basket.append(R[r])
            count += 1


T = int(input())
for tc in range(1, T + 1):
    #정점 수 , 간선 수, 공통조상을 찾는 2개의 정점 번호
    V, E, n, m = map(int, input().split())
    
    # P/L/R 풀이
    P = [0] * (V + 1)
    L = [0] * (V + 1)
    R = [0] * (V + 1)
    
    #연결노드 정보저장
    line_list = list(map(int, input().split()))
    
    #라인 연결
    for i in range(0, 2 * E, 2):
        i, j = line_list[i], line_list[i + 1]
        P[j] = i
        #왼쪽 자식이 비어있으면 왼쪽에 저장
        if L[i] == 0:
            L[i] = j
        #왼쪽 자식이 차있으면 오른쪽에.
        else:
            R[i] = j
    
    #조상 찾기
    a_ance = find(n)
    b_ance = find(m)
    
    # 역순으로 조상이 저장되어 있음 -> 역순으로 찾았을 때 같은 번호가 있으면 가장 가까운 공통조상
    for i in a_ance:
        if i in b_ance:
            common_p = i
            break

    # 공통조상 기준으로 노드의 갯수를 구함
    count = 1 # 자신의 노드 카운트
    family(common_p)

    print(f"#{tc} {common_p} {count}")