# "이것이 코딩 테스트다" / 챕터13 / DFS BFS / 339p
# Q15. 특정 거리의 도시 찾기
# 풀이일 : 2023-10-24
# 난이도 : 1.5/3.0
# 시간 제한 : 2초
# 메모리 제한 256MB
# 풀이 제한 시간 : 30분
# 소요 시간 : 
# https://www.acmicpc.net/problem/18352

# 1) 나의 풀이

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)] # 인접리스트

# 주어진 데이터를 인접리스트로 변형
for _ in range(n) :
    data = list(map(int, input().split()))
    graph[data[0]].append(data[1])

