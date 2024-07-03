# 백준 10845번 "큐"
# 문제 분류 : 알고리즘 기초 1/2 (자료구조)
# 풀이 : 성공
# 이해도 : 상
# 소요 시간 : 학습목적 (측정하지 않음)

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
result = []
q = deque()

for _ in range(n):
    cmd = input().split()

    if cmd[0] == "push":
        q.append(cmd[1]) # 큐에 추가

    elif cmd[0] == "pop":
        if q:
            result.append(q.popleft()) # 큐의 POP
        else:
            result.append(-1)

    elif cmd[0] == "size":
        result.append(len(q)) # 큐의 길이

    elif cmd[0] == "empty":
        if q: # 큐의 요소 존재 여부
            result.append(0)
        else:
            result.append(1)

    elif cmd[0] == "front":
        if q:
            result.append(q[0]) # 큐의 첫번째 요소 접근
        else:
            result.append(-1)

    elif cmd[0] == "back":
        if q:
            result.append(q[-1]) # 큐의 마지막 요소 접근
        else:
            result.append(-1)

for i in result:
    print(i)
