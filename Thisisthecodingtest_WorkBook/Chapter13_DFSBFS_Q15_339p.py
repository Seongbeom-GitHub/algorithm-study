# "이것이 코딩 테스트다" / 챕터13 / DFS BFS / 339p
# Q15. 특정 거리의 도시 찾기
# 풀이일 : 2023-10-24
# 난이도 : 1.5/3.0
# 시간 제한 : 2초
# 메모리 제한 256MB
# 풀이 제한 시간 : 30분
# 소요 시간 : 
# https://www.acmicpc.net/problem/18352

# 1) 나의 풀이 + 모범답안
from collections import deque
import sys

n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)] # 인접리스트

# 주어진 데이터를 인접리스트로 변형
for _ in range(m) :
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

distance = [-1] * (n + 1)
distance[x] = 0

# BFS 탐색
q = deque([x])

while q :
    now = q.popleft()

    for next_node in graph[now] :
        if distance[next_node] == -1 :
            distance[next_node] = distance[now] + 1
            q.append(next_node)

check = False
for i in range(1, n + 1) :
    if distance[i] == k :
        print(i)
        check = True

if check == False :
    print(-1)