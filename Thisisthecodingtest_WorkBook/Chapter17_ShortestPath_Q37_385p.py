# "이것이 코딩 테스트다" / 챕터17 / 최단경로
# Q37. 플로이드
# 난이도 : 1.5/3.0
# 시간 제한 : 1초 / 메모리 제한 : 256MB / 풀이 제한 시간 : 40분
# 문제 출처 : 기출 핵심 유형
# https://www.acmicpc.net/problem/11404

n = int(input()) # 도시의 수
m = int(input()) # 버스의 수

INF = int(1e9)

# 2차원 그래프를 무한값으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신의 도시로 가는 비용은 0으로 설정
for i in range(1, n + 1) :
    for j in range(1, n + 1) :
        if i == j :
            graph[i][j] = 0

# a에서 b로 가는 비용은 c로 설정
for _ in range(m) :
    a, b, c = map(int, input().split())
    if c < graph[a][b] :
        graph[a][b] = c

# 플로이드워셜 알고리즘 수행
for k in range(1, n + 1) :
    for a in range(1, n + 1) :
        for b in range(1, n + 1) :
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            
# 수행된 결과를 출력
for a in range(1, n + 1) :
    for b in range(1, n + 1) : 
        if graph[a][b] == INF :
            print("0", end = " ")
        else :
            print(graph[a][b], end=" ") 

    print()