# "이것이 코딩 테스트다" / 챕터13 / DFS BFS / 351p
# Q20. 감시 피하기
# 풀이일 : 2023-11-22
# 난이도 : 2.5/3.0
# 시간 제한 : 2초
# 메모리 제한 256MB
# 풀이 제한 시간 : 60분
# 소요 시간 : 실패
# https://acmicpc.net/problem/18428

from itertools import combinations

n = int(input())
tlist = []
space = []
map =[]

for i in range(n) :
    map.append(list(input().split()))
    for j in range(n) :
        # 선생님의 위치 정보 저장
        if map[i][j] == 'T' :
            tlist.append((i,j))
        # 빈공간의 위치 저장
        if map[i][j] == 'X' :
            space.append((i,j))

# 특정 방향으로 감시 진행 (학생 발견시 True)
def watch(x, y, direction) :
    # 왼쪽 방향으로 감시
    if direction == 0 :
        while y >= 0 :
            if map[x][y] == 'S' :
                return True
            if map[x][y] == 'O' :
                return False
            y -= 1

    # 오른쪽 방향으로 감시
    if direction == 1 :
        while y < n :
            if map[x][y] == 'S' :
                return True
            if map[x][y] == 'O' :
                return False
            y += 1

    # 위쪽 방향으로 감시
    if direction == 2 :
        while x >= 0 :
            if map[x][y] == 'S' :
                return True
            if map[x][y] == 'O' :
                return False
            x -= 1
    
    # 아래쪽 방향으로 감시
    if direction == 3 :
        while x < n :
            if map[x][y] == 'S' :
                return True
            if map[x][y] == 'O' :
                return False
            x += 1

# 장애물 설치 이후에, 한 명이라도 학생이 감지되는지 검사
def process() :
    # 모든 선생님의 위치를 하나씩 확인
    for x, y in tlist :
        # 4가지 방향으로 학생을 감지할 수 있는지 확인
        for i in range(4) :
            if watch(x, y, i) :
                return True
            
    return False

find = False # 학생이 한 명도 감지되지 않도록 설치할 수 있는지의 여부

# 빈 공간에서 3개를 뽑는 모든 조합을 확인
for data in combinations(space, 3) :
    # 장애물 설치해보기
    for x, y in data :
        map[x][y] = 'O'
    
    # 학생이 한 명도 감지되지 않는 경우
    if not process() :
        # 원하는 경우를 발견한 것임
        find = True
        break

    # 설치된 장애물을 다시 없애기
    for x,y in data :
        map[x][y] = 'X'
    
if find : 
    print('YES')
else :
    print('NO')

