T = int(input())
for tc in range(1, T + 1):
    num = [0] * 10
    n = int(input())
    mul = 1
    cnt = 0
    while True:
        if 0 not in num:
            break
        res = n * mul
        temp = set(list(str(res)))
        temp = {int(x) for x in temp}
        for i in range(10):
            if i in temp:
                num[i] += 1
        # print(temp)
        # print(num)
        # break
        mul += 1
        cnt += 1
    print(f"#{tc} {n * cnt}")
