# "이것이 코딩 테스트다" / 챕터13 / DFS BFS / 341p
# Q16. 연구소
# 풀이일 : 2023-10-27
# 난이도 : 2.0/3.0
# 시간 제한 : 2초
# 메모리 제한 512MB
# 풀이 제한 시간 : 40분
# 소요 시간 : 실패
# https://www.acmicpc.net/problem/14502

import sys

n, m = map(int, input().split())
mapData = [] # 초기맵
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트

for _ in range(n) :
    data = list(map(int, sys.stdin.readline().split()))
    mapData.append(data)

# 4가지 이동방향에 대한 리스트 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

# DFS 탐색으로 바이러스 퍼트리기
def virus(x, y) :
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m :
            if temp[nx][ny] == 0 :
                temp[nx][ny] = 2
                virus(nx, ny)

# 현재 맵에서 안전 영역의 크기 계산하는 메서드
def get_score() :
    score = 0
    for i in range(n) :
        for j in range(m) :
            if temp[i][j] == 0 :
                score += 1
    return score

# 깊이 우선 탐색(DFS)을 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산
def dfs(count) :
    global result
    # 울타리가 3개 설치된 경우
    if count == 3 :
        for i in range(n) :
            for j in range(m) :
                temp[i][j] = data[i][j]

                # 각 바이러스의 위치에서 전파 진행
                for i in range(n) :
                    for j in range(m) :
                        if temp[i][j] == 2 :
                            virus(i, j)
                
                # 안전 영역 최댓값 계산
                result = max(result, get_score())
                return
    
    # 빈 공간에 울타리 설치
    for i in range(n) :
        for j in range(m) :
            if data[i][j] == 0 :
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)


