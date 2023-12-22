# "이것이 코딩 테스트다" / 챕터17 / 최단경로
# Q40. 숨바꼭질
# 난이도 : 2.0/3.0
# 시간 제한 : 1초 / 메모리 제한 : 128MB / 풀이 제한 시간 : 40분
# 문제 출처 : USACO

import heapq
import sys
sys = input.stdin.readline
INF = int(1e9)


# 노드와 간선의 개수 입력
n, m = map(int, input().split())
# 시작노드를 1번 헛간으로 설정
start = 1
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for i in range(n + 1)]
# 최단거리 테이블 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력
for _ in range(m) :
    a, b = map(int, input().split())
    # a번 노드와 b번 노드의 이동 비용은 1 (양방향)
    graph[a].append((b, 1))
    graph[b].append((a, 1))

def dijkstra(start) :
    q = []
    # 시작노드로 가기 위한 최단경로는 0으로 설정, 큐 삽입
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q :
        # 가장 최단거리가 짧은 노드 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 노드라면 무시
        if distance[now] < dist :
            continue
        # 현재 노드와 연결된 다른 인접노드 확인
        for i in graph[now] :
            cost += dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

max_node = 0
max_distance = 0
result = []

for i in range(1, n + 1) :
    if max_distance < distance[i] :
        max_node = i
        max_distance = distance[i]
        result = [max_node]
    elif max_distance == distance[i] :
        result.append(i)

print(max_node, max_distance, len(result))
