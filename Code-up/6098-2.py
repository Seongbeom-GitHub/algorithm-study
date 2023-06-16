# Code-up 6098
# 정확한 풀이

maze = []
for _ in range(10):
    row = list(map(int, input().split()))
    maze.append(row)

x = 1
y = 1
while True :
    if maze[x][y] == 0 :
        maze[x][y] = 9
    elif maze[x][y] == 2 :
        maze[x][y] = 9
        break

    if (maze[x][y+1]==1 and maze[x+1][y]==1) or (x==9 and y==9) :
        break

    if maze[x][y+1] != 1 :
        y += 1
    elif maze[x+1][y] != 1 :
        x += 1


for row in maze:
    for num in row:
        print(num, end=' ')
    print()

