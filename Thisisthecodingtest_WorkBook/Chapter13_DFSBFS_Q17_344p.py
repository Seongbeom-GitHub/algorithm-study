# "이것이 코딩 테스트다" / 챕터13 / DFS BFS / 344p
# Q17. 경쟁적 전염
# 풀이일 : 2023-11-01
# 난이도 : 2.0/3.0
# 시간 제한 : 2초
# 메모리 제한 256MB
# 풀이 제한 시간 : 50분
# 소요 시간 : 실패(답안과 어느정도 근접함)
# https://www.acmicpc.net/problem/18405


# # 1) 나의 풀이
# from collections import deque

# n, k = map(int, input().split())    
# data = []
# for _ in range(n) :
#     data.append(list(map(int, input().split())))
# s, x, y = map(int, input().split())

# virus = [[] for _ in range(k + 1)]

# for i in range(n) :
#     for j in range(n) :
#         vNum = data[i][j]
#         if (vNum > 0) :
#             virus[vNum].append((i, j))

# def virusBFS() :
#     # 4가지 이동방향에 대한 리스트 (상, 하, 좌, 우)
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]

#     for row in range(1, k + 1) :
#         for position in virus[row] :
#             # 1번 바이러스 부터 k번 까지 BFS 실행
#             for _ in range(4) :
#                 position

# def search(x, y) :
#     return data[x - 1][y - 1]

# virusBFS()
# print(search(x, y))

# 2) 모범 답안
from collections import deque

n, k = map(int, input().split())

graph  = [] # 전체 보드 정보
data = [] # 바이러스에 대한 정보

for i in range(n) :
    # 보드 정보를 한 줄 단위로 입력
    graph.append(list(map(int, input().split())))
    for j in range(n) :
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0 :
            # (바이러스 번호, 시간, 위치x, 위치y) 삽입
            data.append((graph[i][j], 0, i, j))

# 낮은 번호 부터 정렬
data.sort()
# 큐에 대입
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

# 바이러스의 4가지 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# BFS 진행
while q :
    virus, s, x, y = q.popleft()
    # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
    if s == target_s : 
        break

    # 현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        # 해당 위치로 이동할 수 있는 경우
        if 0 <= nx and nx < n and 0 <= ny and ny < n :
            # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0 :
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])



