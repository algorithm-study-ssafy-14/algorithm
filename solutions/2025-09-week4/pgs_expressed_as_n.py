def solution(N, number):
    if N == number:
        return 1

    dp = [set() for _ in range(9)]

    for i in range(1, 9):
        dp[i].add(int(str(N) * i))

        for a in range(1, i):
            b = i - a
            for x in dp[a]:
                for y in dp[b]:
                    dp[i].add(x + y)
                    dp[i].add(x - y)
                    dp[i].add(y - x)
                    dp[i].add(x * y)

                    if y != 0:
                        dp[i].add(x // y)
                    if x != 0:
                        dp[i].add(y // x)

            if number in dp[i]:
                return i
    return -1
