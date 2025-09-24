

# 2개로 만듦.
def solution(money):

    n = len(money)
    memo1 = [[0] * 2 for _ in range(n - 1)]
    memo2 = [[0] * 2 for _ in range(n - 1)]

    memo1[0][1] = money[0]
    memo2[0][1] = money[1]

    for i in range(1, len(money) - 1):
        memo1[i][0] = max(memo1[i - 1][0], memo1[i - 1][1])
        memo1[i][1] = memo1[i - 1][0] + money[i]

        memo2[i][0] = max(memo2[i - 1][0], memo2[i - 1][1])
        memo2[i][1] = memo2[i - 1][0] + money[i + 1]

    return max(memo1[n - 2][0], memo1[n - 2][1], memo2[n - 2][0], memo2[n - 2][1])