# "이것이 코딩 테스트다" / 챕터17 / 최단경로
# Q39. 화성 탐사
# 난이도 : 2.0/3.0
# 시간 제한 : 1초 / 메모리 제한 : 128MB / 풀이 제한 시간 : 40분
# 문제 출처 : ACM-ICPC

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for tc in range(int(input())) :
    # 노드의 개수
    n = int(input())

    # 전체 맵 정보
    graph = []
    for i in range(n) :
        graph.append(list(map(int, input().split())))

    # 최단거리 테이블 초기화
    distance = [[INF] * n for _ in range(n)]
    
    # 시작 위치는 (0,0)
    x,y = 0, 0
    # 시작 노드로 가기 위한 비용은 (0,0) 위치 값으로 설정하여, 큐에 삽입
    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]

    # 다익스트라 알고리즘 수행
    while q :
        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, x, y = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[x][y] < dist :
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            # 맵의 범위를 벗어나는지 체크
            if nx < 0 or nx >= n or ny < 0 or ny >= n :
                continue
            cost = dist + graph[nx][ny]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 겨우
            if cost < distance[nx][ny] :
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))

    print(distance[n - 1][n - 1])


