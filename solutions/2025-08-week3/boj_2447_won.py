N = int(input())
standard_list = ['***', '* *', '***']


def star(n, cnt=3, arr=standard_list):
    if cnt == N:
        return arr

    temp = []
    for i in range(cnt):
        temp.append(arr[i] * 3)
    for i in range(cnt):
        temp.append(arr[i] + ' ' * cnt + arr[i])
    for i in range(cnt):
        temp.append(arr[i] * 3)

    return star(n, cnt * 3, temp)


result_list = star(N, 3)
for s in result_list:
    print(s)
