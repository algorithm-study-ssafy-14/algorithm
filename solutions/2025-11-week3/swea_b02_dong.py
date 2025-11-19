## 2번

t = int(input())

for tc in range(1, t+1):

    n, m = map(int, input().split())
    bin_m = bin(m)

    mask = (1 << n) - 1
    if (mask & m) == mask:
        result = 'ON'
    else:
        result = 'OFF'

    print(f"#{tc} {result}")