#퇴사
#dfs로 모든 경우의 수 탐색 (복잡도 2^15 = 32768)
def dfs(day, pay):

    #기저조건
    if day > N:
        a_sum.add(pay)
        return

    #각 날짜마다 일을 할지 말지 결정
    for a_limit in range(day-1, len(a_list)):
        #일함.
        if a_list[a_limit][0] + a_list[a_limit][1] > N+1:
            a_sum.add(pay)

        #일 안함.
        else:
            dfs(a_list[a_limit][0] + a_list[a_limit][1],pay + a_list[a_limit][2])

#-------------------------
N = int(input())
a_list = []
#index에 날짜와 걸리는 기간, 페이를 넣어줌.
for i in range(1, N+1):
    t, p = map(int, input().split())
    a_list.append([i, t, p])

a_sum = {0}

dfs(1, 0)
print(max(a_sum))

