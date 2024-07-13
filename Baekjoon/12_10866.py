# 백준 10866번 "덱"
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

for _ in range(n) :
    cmd = input().split()

    if cmd[0] == "push_front" :
        q.appendleft(int(cmd[1]))

    elif cmd[0] == "push_back" :
        q.append(int(cmd[1]))

    elif cmd[0] == "pop_front" :
        if q :
            result.append(q.popleft())
        else :
            result.append(-1)

    elif cmd[0] == "pop_back" :
        if q :
            result.append(q.pop())
        else :
            result.append(-1)

    elif cmd[0] == "size" :
        result.append(len(q))

    elif cmd[0] == "empty" :
        if q :
            result.append(0)
        else :
            result.append(1)

    elif cmd[0] == "front" :
        if q :
            result.append(q[0])
        else :
            result.append(-1)

    elif cmd[0] == "back" :
        if q :
            result.append(q[-1])
        else :
            result.append(-1)

for i in result :
    print(i)
