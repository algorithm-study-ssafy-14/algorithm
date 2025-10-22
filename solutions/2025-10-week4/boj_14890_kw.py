N, L = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

result = 0


def check_can_slope(li):
    used = [0] * N                      # 경사로를 놓는 칸이 중첩되면 안되기 때문에 사용

    for i in range(1, N):
        diff = li[i] - li[i-1]          # 인접 칸의 높이 차이
        if diff == 0:                   # 인접 칸의 높이가 같을 경우 패스
            continue

        if abs(diff) >= 2:              # 인접 칸의 높이가 2 이상이면 못감
            return 0

        if diff == 1:                   # 오르막
            for j in range(i - L, i):   # i - L 칸 부터 i - 1 칸까지 높이가 같은지 확인
                if j < 0 or li[j] != li[i - 1] or used[j]:  # 같지 않다면 return 0
                    return 0
            for j in range(i - L, i):
                used[j] = 1             # 높이가 같다면 (경사로를 놓을 수 있다면) used 갱신

        else:                           # 내리막
            for j in range(i, i + L):   # i 부터 i + L - 1 까지 높이가 같은지 확인
                if j >= N or li[j] != li[i] or used[j]:
                    return 0
            for j in range(i, i + L):
                used[j] = 1
    return 1


for row in arr:                         # 가로
    result += check_can_slope(row)

for col in zip(*arr):                   # 세로
    result += check_can_slope(col)

print(result)
