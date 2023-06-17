# Code-up 6096
# 2023-06-17
# 성공률 : 29%
# 풀이시간 : 약 30분
# 채점 : 정확한 풀이

# 행과 열의 개수
wh = 19

# 바둑판 배열
board = []

# 바둑판 배열 생성
for i in range(wh) : 
    row = list(map(int, input().split()))
    board.append(row)

# 뒤집기 입력 개수
n = int(input())
clip = []

# 십자 뒤집기 배열 입력
for i in range(n) :
    temp = list(map(int, input().split()))
    clip.append(temp)

# 십자 뒤집기 실행
for i in range(n) :
    x = clip[i][0] -1
    y = clip[i][1] -1

    for j in range(wh) :
        if board[j][y] == 0 :
            board[j][y] = 1
        elif board[j][y] == 1 :
            board[j][y] = 0
    
    for j in range(wh) :
        if board[x][j] == 0 :
            board[x][j] = 1
        elif board[x][j] == 1 :
            board[x][j] = 0

# 바둑판 출력
for i in board :
    for j in i : print(j, end =' ')
    print()