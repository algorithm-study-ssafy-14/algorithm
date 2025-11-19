## 1번

t = int(input())

for tc in range(1, t+1):

    n = int(input())
    num_set = set()

    cnt = 0
    mul = 0
    while len(num_set) < 10:
        cnt += 1 ; mul += 1
        num_set |= set(list(str(n * mul)))


    print(f"#{tc} {n*cnt}")