# Code-up 6098
# 시간 초과

maze = []
for _ in range(10):
    row = list(map(int, input().split()))
    maze.append(row)

x, y = 1, 1  # 개미의 출발 위치 (2, 2)
maze[x][y] = 9  # 개미의 출발 위치를 9로 표시

while True:
    if maze[x][y] == 2:  # 먹이를 찾은 경우 종료
        maze[x][y] = 9
        break

    if maze[x][y+1] != 1:  # 오른쪽으로 이동 가능한 경우
        y += 1
        if maze[x][y] != 2:  # 먹이가 아닌 경우
            maze[x][y] = 9

    elif maze[x+1][y] != 1:  # 오른쪽으로 이동할 수 없는 경우 아래쪽으로 이동
        x += 1
        if maze[x][y] != 2:  # 먹이가 아닌 경우
            maze[x][y] = 9

for row in maze:
    for num in row:
        print(num, end=' ')
    print()

