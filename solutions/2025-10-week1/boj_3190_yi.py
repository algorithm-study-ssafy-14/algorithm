from collections import deque


n = int(input())
k = int(input())
graph = [[0]*n for _ in range(n)]
for i in range(k):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
l = int(input())
turn = dict()
for i in range(l):
    a, b = map(str, input().split())
    turn[int(a)] = b

snake = deque()
dir = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x, y = 0, 0
snake.append((0,0))
time = 0
while True:
    time += 1
    nx, ny = x + dx[dir], y + dy[dir]

    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        break

    if (nx, ny) in snake:
        break

    snake.appendleft((nx, ny))
    if graph[nx][ny] == 1:
        graph[nx][ny] = 0
    else:
        snake.pop()

    x, y = nx, ny

    if time in turn:
        if turn[time] == "D":
            dir = (dir + 1) % 4
        else:
            dir = (dir - 1) % 4
print(time)
