T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    temp = list(bin(m)[2:])
    temp = [int(x) for x in temp]
    while len(temp) < n:
        temp.insert(0, 0)
    cnt = 0
    flag = True
    for i in temp[::-1]:
        if cnt == n:
            break
        if i == 1:
            flag = True
            cnt += 1
        else:
            flag = False
            break
    if flag:
        print(f"#{tc} ON")
    else:
        print(f"#{tc} OFF")
