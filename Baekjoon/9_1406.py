# 백준 1406번 "에디터"
# 문제 분류 : 알고리즘 기초 1/2 (자료구조)
# 풀이 : 성공
# 이해도 : 중상 (스택 사용 아이디어를 떠올리기 어려웠음)
# 소요 시간 : 학습목적 (측정하지 않음)

'''
(문자열)  / a / b /  c / d  /
(커서)    0   1   2    3    4

B : 커서 -1  인덱스 지우기
P : 커서 인덱스에 추가
'''
# 1. 초기 접근법 (시간초과)
# import sys
# input = sys.stdin.readline

# s = list(input()) # 초기 문자열 입력
# n = int(input()) # 명령어 수

# cursor = len(s)

# for _ in range(n) :
#     cmd = list(input().split())
#     if cmd[0] == 'L' :
#         if cursor > 0 :
#             cursor -= 1
#     elif cmd[0] == 'D' :
#         if cursor <= len(s) :
#             cursor += 1
#     elif cmd[0] == 'B' :
#         if cursor > 0 :
#             s.remove(s[cursor - 1])
#             cursor -= 1
#     elif cmd[0] == 'P' :
#         s.insert(cursor, cmd[1])
#         cursor += 1

# print(''.join(s))

# 2. 모범답안 (큐사용, 스택으로도 구현 가능)
import sys
input = sys.stdin.readline

s = list(input().strip())  # 초기 문자열 입력
n = int(input())  # 명령어 수

left_stack = s  # 커서 왼쪽의 문자열을 스택으로 관리
right_stack = []  # 커서 오른쪽의 문자열을 스택으로 관리

for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'L':
        if left_stack:
            right_stack.append(left_stack.pop())
    elif cmd[0] == 'D':
        if right_stack:
            left_stack.append(right_stack.pop())
    elif cmd[0] == 'B':
        if left_stack:
            left_stack.pop()
    elif cmd[0] == 'P':
        left_stack.append(cmd[1])

# 결과 출력
print(''.join(left_stack) + ''.join(reversed(right_stack)))

