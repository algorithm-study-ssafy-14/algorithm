from collections import Counter
import sys

# 입력 처리
try:
    r, c, k = map(int, sys.stdin.readline().split())
except:
    exit()

r -= 1
c -= 1

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
row = 3
col = 3

for t in range(101):
    
    if r < row and c < col and matrix[r][c] == k:
        print(t)
        break
        
    if row >= col:
        is_transposed = False
        
    else:
        matrix = [list(item) for item in zip(*matrix)]
        row, col = col, row
        is_transposed = True


    a_max = 0
    new_matrix = []

    for lst in matrix:
        temp_counter = Counter(lst)
        temp = [(num, count) for num, count in temp_counter.items() if num != 0]

        temp.sort(key=lambda x: (x[1], x[0]))

        new_row = []
        for num, count in temp:
            new_row.extend([num, count])

        new_row = new_row[:100]

        new_matrix.append(new_row)

        # 최대 열 길이 업데이트
        a_max = max(a_max, len(new_row))

    col = a_max

    # 0으로 패딩
    for i in range(len(new_matrix)):
        new_matrix[i].extend([0] * (a_max - len(new_matrix[i])))
    matrix = new_matrix

    if is_transposed:
        matrix = [list(item) for item in zip(*matrix)]
        row, col = col, row 

else:
    print(-1)