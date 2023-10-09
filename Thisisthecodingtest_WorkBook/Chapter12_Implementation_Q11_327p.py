# "이것이 코딩 테스트다" / 챕터12 / 구현 / 327p
# Q11. 뱀
# 풀이일 : 2023-10-08
# 난이도 : 2.0/3.0
# 시간 제한 : 1초
# 메모리 제한 128MB
# 풀이 제한 시간 : 40분
# 소요 시간 : (실패)
# https://www.acmicpc.net/problem/3190

# 1) 나의 풀이 (실패)
# appleArray = []     # 사과의 위치 배열
# rotateArray = []    # (초, 회전방향) 배열
# logArray = []       # 이동한 위치 기록 배열
# maxSecond = 0       # 최대 시간(초)
# snakePositionX = 0  # 뱀 x좌표
# snakePositionY = 0  # 뱀 y좌표

# # 이동 방향 배열 (상,하,좌,우) 순서
# direction = [[-1,1,0,0], 
#              [0,0,-1,1]]

# n = int(input()) # 정사각 보드판의 길이

# appleNum = int(input()) # 사과의 개수

# # 사과의 위치를 배열에 저장
# for i in range(appleNum) :
#     appleArray.append(list(map(int, input().split())))

# rotateNum = int(input()) # 뱀의 회전 횟수

# # 회전 정보를 배열에 저장
# for i in range(rotateNum) :
#     rotateArray.append(list(input().split()))

# # 최대 시간 구하기
# for x in range(len(rotateArray)) :
#     maxSecond += int(rotateArray[0][x])

# # 뱀을 가장먼저 오른쪽으로 이동
# snakePositionX += direction[0][3]
# snakePositionY += direction[1][3]
# # 이동한 위치를 배열에 저장
# logArray.append([snakePositionX,snakePositionY])
# count = 1

# for i in range(len(rotateArray)) :
#     for j in range(rotateArray[i][0]) :



# # 게임 오버 체크
# def checkGameOver(x, y) :



# 2) 모범 답안
n = int(input()) # 맵의 크기
k = int(input()) # 사과의 개수
data = [[0] * (n + 1) for _ in range(n + 1)] # 맵 정보
info = [] # 방향 회전 정보

# 맵 정보(사과가 있는 곳은 1로 표시)
for _ in range(k) : 
    a, b = map(int, input().split())
    data[a][b] = 1

# 방향 회전 정보 입력
l = int(input())
for _ in range(l) :
    x, c = intput().split()
    
