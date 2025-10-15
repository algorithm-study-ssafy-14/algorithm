#주사위 굴리기
#발상이 어려웠음.

from collections import deque
N, M, x, y, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

order = list(map(int, input().split()))
dir_x = [0, 0, 0, -1, 1]
dir_y = [0,1, -1, 0, 0]
dice = [0,0,0,0,0,0]
ans_list = []

#시행 할 때 마다
for i in order:
    nx = x + dir_x[i]
    ny = y + dir_y[i]

    #범위 벗어나면 무시
    if nx >= N or ny >= M or nx < 0 or ny < 0:
        continue

    #범위 안이라면
    else:
        #바뀐 값을 다시 x, y 에 넣어줌. 약간 이상하게 한 듯.
        x, y = nx, ny

        #주사위 굴리기 : 각 방향마다 주사위의 전개도를 새로 설정해줌.
        if i == 1:
            dice = [dice[0],dice[2],dice[3],dice[5],dice[4],dice[1]]

        elif i == 2:
            dice = [dice[0],dice[5],dice[1],dice[2],dice[4],dice[3]]

        elif i == 3:
            dice = [dice[5],dice[1],dice[0],dice[3],dice[2],dice[4]]

        else:
            dice = [dice[2],dice[1],dice[4],dice[3],dice[5],dice[0]]

    #이제 주사위 바닥면과 지도 칸의 숫자 비교
    if matrix[x][y] == 0:
        
        #0 이면 주사위 바닥면 숫자가 칸에 복사
        matrix[x][y] = dice[2]

    #0이 아니면 칸의 숫자가 주사위 바닥면에 복사되고 칸은 0이 됨.
    else:
        dice[2] = matrix[x][y]
        matrix[x][y] = 0

    ans_list.append(str(dice[5]))
print('\n'.join(ans_list))