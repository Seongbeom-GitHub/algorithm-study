# 백준 10828번 "스택"
# 문제 분류 : 알고리즘 기초 1/2 (자료구조)
# 풀이 : 성공
# 이해도 : 상
# 소요 시간 : 학습목적 (측정하지 않음)

import sys
input = sys.stdin.readline

stack = []
result = []

n = int(input())

for i in range(n) :
    cmd = input().split()

    if cmd[0] == "push" :
        stack.append(cmd[1])
    elif cmd [0] == "pop" :
        if len(stack) == 0 :
            result.append(-1)
        else :
            result.append(stack[-1])
            stack.pop()
    elif cmd [0] == "size" :
        result.append(len(stack))
    elif cmd [0] == "empty" :
        if len(stack) < 1 : 
            result.append(1)
        else :
            result.append(0)
    elif cmd[0] == "top" :
        if len(stack) < 1 :
            result.append(-1)
        else :
            result.append(stack[-1])

for i in result :
    print(i)