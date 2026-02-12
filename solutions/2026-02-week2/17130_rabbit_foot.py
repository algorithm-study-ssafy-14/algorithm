import sys
sys.stdin = open("input/17130_input.txt", 'r')
input = sys.stdin.readline

def main(n, m, arr):
    global _n, _m, _arr, dij, dp
    _n, _m, _arr = n, m, arr
    dij = [(1, 1), (0, 1), (-1, 1)]
    dp = [[-1] * _m for _ in range(_n)]
    max_carrot = -1

    start, end = find_rabbit_exit()

    find_max_val(start, end)

    if end == set():
        return -1

    max_carrot = max(dp[i][j] for i, j in end)

    return max_carrot


def find_rabbit_exit():
    exit_coord = set()
    
    for i in range(_n):
        for j in range(_m):
            if _arr[i][j] == 'R':
                start = (i, j)
            elif _arr[i][j] == 'O':
                exit_coord.add((i, j))

    return start, exit_coord


def find_max_val(start, end):
    si, sj = start
    dp[si][sj] = 0

    # [중요 1] 열(Column) 우선 순회
    # 토끼는 항상 오른쪽(열 번호 증가)으로만 이동합니다.
    # 따라서 왼쪽 열(sj)부터 오른쪽 끝(m-1)까지 순서대로 처리해야
    # 이전 열의 결과(dp값)를 다음 열 계산에 누적하여 사용할 수 있습니다.
    for cj in range(sj, _m-1):
        for ci in range(_n):
            # [중요 2] 도달 불가능한 칸 체크 (Reachability Check)
            # dp 값이 -1이라면, 시작점에서 현재 위치(ci, cj)로 올 수 없다는 의미이므로
            # 여기서 뻗어나가는 경로도 계산할 필요가 없습니다. (가지치기 효과)
            if dp[ci][cj] == -1:
                continue
            
            # [주의] 도착 지점('O') 처리
            # 문제 조건: "쪽지가 있는 칸에 도착하면 끝난다"
            # 즉, 'O'에 도착하면 더 이상 이동하지 않아야 합니다.
            # 만약 이 체크가 없다면 'O'를 지나쳐서 더 가는 경로가 생겨 오답이 될 수 있습니다.
            if _arr[ci][cj] == 'O':
                continue

            for di, dj in dij:
                ni, nj = ci + di, cj + dj
            
                # [중요 3] 범위 체크 (Boundary Check)
                if ni < 0 or ni >= _n or nj < 0 or nj >= _m:
                    continue

                # [중요 4] 벽 체크
                if _arr[ni][nj] == '#':
                    continue
                
                # [중요 5] 점화식 (State Transition)
                # 다음 칸(ni, nj)의 값은
                # "기존에 기록된 값" vs "현재 칸(ci, cj)에서 왔을 때의 값" 중 큰 값으로 갱신
                # 당근('C')이 있으면 +1을 해줍니다.
                if _arr[ni][nj] == 'C':
                    dp[ni][nj] = max(dp[ni][nj], dp[ci][cj] + 1)
                else:
                    dp[ni][nj] = max(dp[ni][nj], dp[ci][cj])


N, M = map(int, input().split())

Arr = [input().strip() for _ in range(N)]

print(main(N, M, Arr))