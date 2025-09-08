

N = int(input())

#1일시 바로 출력
if N == 1:
    print(input())


#아닐시 DP 시작
else:
    #beverage => 0넣고 1부터 시작, 포도주의 양을 나타냄

    beverage = [0]

    for _ in range(N):
        i = int(input())
        beverage.append(i)


    #memo => 누적 포도주의 양
    #memo에 초반 포도주 양을 적어놓음, 초반 오류 방지
    memo = [[0,0] for _ in range(N+1)]
    memo[1][0] = beverage[1]
    memo[2][0] = beverage[2]
    memo[2][1] = beverage[1] + beverage[2]
    
    #DP 시작, 2잔째로 가는 경우의 수는 단 하나, 1잔째의 경우의 수는 밑에 나열된 경우의 수
    #[0] 이 연속 한 잔, [1] 은 연속 두 잔
    for i in range(3,N+1):
        memo[i][0] = max(memo[i-2][0], memo[i-2][1], memo[i-3][1]) + beverage[i]
        memo[i][1] = memo[i-1][0] + beverage[i]

    print(max(memo[N][0],memo[N][1], memo[N-1][0], memo[N-1][1]))
