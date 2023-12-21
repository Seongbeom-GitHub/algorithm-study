# "이것이 코딩 테스트다" / 챕터17 / 최단경로
# Q38. 정확한 순위
# 난이도 : 2.0/3.0
# 시간 제한 : 1초 / 메모리 제한 : 128MB / 풀이 제한 시간 : 40분
# 문제 출처 : K대회


INF = int(1e9)
# 학생수 n / 비교 횟수 m
n, m = map(int, input().split())
# 2차원 그래프
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신의 비용 0
for a in range(1, n + 1) :
    for b in range(1, n + 1) :
        if a == b :
            graph[a][b] = 0
        
# 각 간선에 대한 정보 입력
for _ in range(m) :
    a, b = map(int, input().split())
    graph[a][b] = 1

# 점화식에 따른 플로이드워셜 알고리즘 수행
for k in range(1, n + 1) :
    for a in range(1, n + 1) :
        for b in range(1, n + 1) :
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0
# 각 학생을 번호에 따라 한 명씩 확인하며 도달 가능한지 체크
for i in range(1, n + 1) :
    count = 0
    for j in range(1, n + 1) :
        if graph[i][j] != INF or graph[i][j] != INF :
            count += 1
    if count == n :
        result += 1

print(result)