# "이것이 코딩 테스트다" / 챕터17 / 최단경로
# Q40. 숨바꼭질
# 난이도 : 2.0/3.0
# 시간 제한 : 1초 / 메모리 제한 : 128MB / 풀이 제한 시간 : 40분
# 문제 출처 : USACO

import heapq
import sys
sys = input.stdin.readline
INF = int(1e9)



n, m = map(int, input().split())


distance = [[INF] * (n + 1) for _ in range(n + 1)]

