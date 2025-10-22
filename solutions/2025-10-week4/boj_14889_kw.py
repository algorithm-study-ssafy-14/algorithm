import itertools

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]


# 조합으로 시너지 계산
def team_synergy(team):
    total = 0
    for a, b in itertools.combinations(team, 2):
        total += arr[a][b] + arr[b][a]

    return total


# 1팀을 골랐을 때 2팀을 빠르게 계산하기 위한 set
people = set(range(N))
result = 1e10

# 조합 계산
for team_1 in itertools.combinations(range(N), N // 2):
    team_2 = people - set(team_1)

    # 1팀과 2팀의 시너지 차이
    score = abs(team_synergy(team_1) - team_synergy(team_2))

    # 갱신
    if score < result:
        result = score

print(result)