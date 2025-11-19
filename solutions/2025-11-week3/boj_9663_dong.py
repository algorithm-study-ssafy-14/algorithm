# n-queen

def dfs(depth):
    global total_count
    
    # 다 놓았을 때 경우의 수 중 하나로 등록
    if depth == n:
        total_count += 1
        return

    # dfs 본문
    # i값을 고정시키면서 가로값의 가능성을 동시에 제거
    for i in range(len(num_list)):
        # 인자 하나 선택
        p = num_list[i]
        #대각선 검증
        if depth + p not in plus_dir and depth - p not in minus_dir:
            # 대각선(+,+)
            plus_dir.add(depth + p)
            # 대각선(+,-) / (-, +)
            minus_dir.add(depth - p)
            # 세로 방향 가능성 제거
            temp = num_list.pop(i)
            dfs(depth + 1)
            # 원상복구
            num_list.insert(i, temp)
            plus_dir.remove(depth + p)
            minus_dir.remove(depth - p)



# matrix 크기
n = int(input())
# 답
total_count = 0
# 남을 때 까지 꺼내기
num_list = list(range(0, n))
# 대각선 방향(+, + 방향)
plus_dir = set()
# 대각선 방향(+, -)
minus_dir = set()
dfs(0)

    print(f"#{tc} {total_count}")