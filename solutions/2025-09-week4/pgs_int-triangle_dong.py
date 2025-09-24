

def solution(triangle):
    a_len = len(triangle) + 1
    memo = [[0] * i for i in range(1, a_len)]
    memo[0][0] = triangle[0][0]

    #bottom-up
    for i in range(1, a_len - 1):
        for j in range(0, i + 1):
            if j == 0:
                memo[i][0] = memo[i - 1][0] + triangle[i][0]
            elif j == i:
                memo[i][j] = memo[i - 1][j - 1] + triangle[i][j]

            else:
                memo[i][j] = max(memo[i - 1][j - 1], memo[i - 1][j]) + triangle[i][j]

    answer = max(memo[a_len - 2])
    return answer