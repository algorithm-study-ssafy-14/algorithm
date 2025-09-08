N = int(input().strip())

my_list = [0] * int(N + 2)  # N + 2 만큼 만들어두기

for i in range(2, N+1):               # 1 은 어처피 0 이므로 2부터 순회
    my_list[i] = my_list[i-1] + 1     # 먼저 1을 빼는 경우로 갱신

    if i % 2 == 0:
        my_list[i] = min(my_list[i], my_list[i//2] + 1)  # 2로 나누는 경우와 1을 빼는 경우를 비교
    if i % 3 == 0:
        my_list[i] = min(my_list[i], my_list[i//3] + 1)  # 3으로 나누는 경우와 1을 빼는 경우, 2로 나누는 경우를 비교

print(my_list[N])
