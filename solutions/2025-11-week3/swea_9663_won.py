N = int(input())
count = 0
visited = [-1] * N


def check(n_r):
    for r in range(n_r):  # 0부터 new r 까지 순회하면서 비교
        # 같은 라인이거나, 대각선이면 False, 대각선은 가로의 차이와 세로의 차이가 같음.
        if visited[n_r] == visited[r] or n_r - r == abs(visited[n_r] - visited[r]):
            return False
    return True


def dfs(r):
    global count

    if r == N:      # r == N 이면 모든 행에 퀸이 들어간 것이기 때문에 count++
        count += 1
        return

    for c in range(N):
        visited[r] = c  # visited 를 c 로 갱신. visited 의 인덱스가 행, 값이 열
        if check(r):
            dfs(r + 1)


dfs(0)
print(count)