# Code-up 6097
# 2023-06-16
# 성공률 : 38.9%
# 풀이시간 : 약 50분
# 채점 : 정확한 풀이

w, h = list(map(int, input().split()))      # w 행, h 열
s = int(input())    # 막대의 개수
sticks = []   # 막대의 정보를 저장할 배열

for i in range(s) : 
    stick = list(map(int, input().split()))
    sticks.append(stick)

plate = [[0 for j in range(h)] for i in range(w)]     # 격자판을 0으로 초기화


# 막대기의 개수 만큼 반복
for i in range(s) :

    # 막대의 시작 좌표
    x = sticks[i][2] -1
    y = sticks[i][3] -1

    # 가로 막대기 일때
    if sticks[i][1] == 0 :
        for _ in range(sticks[i][0]) : 
            plate[x][y] = 1
            y += 1

    # 세로 막대기 일때
    if sticks[i][1] == 1 :
        for _ in range(sticks[i][0]) : 
            plate[x][y] = 1
            x += 1

# 격자판 출력
for i in plate :
    for j in i : print(j, end =' ')
    print()