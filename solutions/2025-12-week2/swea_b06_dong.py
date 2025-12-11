# 동아리실 관리하기

t = int(input())

for tc in range(1, t+1):
    
    # 날마다 꼭 포함되어야 하는 사람 => orders
    orders = input()

    # 사람 수 4명 => 총 16가지로 dp 진행
    # ex) a와 d만 참여 => 1001 => 9에 저장
    memo = [[0] * 16 for _ in range(len(orders))]
    if orders[0] == 'A':
        order = 3
    elif orders[0] == 'B':
        order = 2
    elif orders[0] == 'C':
        order = 1
    elif orders[0] == 'D':
        order = 0

    # 첫째 날, 키는 항상 'A'가 들고 있음.
    # A가 항상 방문해야하고 당번이 동시에 와야하기 때문에 해당 dp에 1을 입력.
    for i in range(16):
        if i & (1 << 3) and i & (1 << order):
            memo[0][i] = 1

    # 둘째날부터 마지막날까지 dp 진행
    for idx in range(1, len(orders)):

        #담당자를 비트index로 변환
        if orders[idx] == 'A':
            order = 3
        elif orders[idx] == 'B':
            order = 2
        elif orders[idx] == 'C':
            order = 1
        elif orders[idx] == 'D':
            order = 0

        # i: 어제의 출입자 dp를 순회
        for i in range(1, 16):

            #dp가 0일 때는 가지치기(더해도 0)
            if memo[idx-1][i] != 0:
                temp = memo[idx-1][i]

        # 조건1 => 오늘 담당자는 반드시 포함되어야 하고 ==> j & (1 << order)
        # 조건2 => 어제와 오늘의 출입자 집합이 최소 한 명 겹쳐야 함 ==> (i & j)
                for j in range(1, 16):
                    if j & (1 << order) and (i & j):
                        memo[idx][j] += temp
                        
        for i in range(1, 16):
            memo[idx][i] %= 1000000007

    #print(memo)
    result = sum(memo[-1]) % 1000000007

    print(f"#{tc} {result}")