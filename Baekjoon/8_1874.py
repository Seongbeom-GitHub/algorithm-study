# 백준 1874번 "스택 수열"
# 문제 분류 : 알고리즘 기초 1/2 (자료구조)
# 풀이 : 성공
# 이해도 : 상
# 소요 시간 : 학습목적 (측정하지 않음)

# 1. 나의 접근법
# n = int(input())

# a = [] # 1 ~ n 까지순서로 담을 리스트
# targetList = [] # 만들어야 하는 수열
# stack = [] 
# result = [] 

# for i in range(1, n + 1) :
#     a.append(i)

# for _ in range(n) :
#     targetList.append(int(input()))

# targetIndex = 0

# for i in a :
#     target = targetList[targetIndex]

#     if stack and stack[-1] == target :
#         stack.pop()
#         result.append('+')

#         targetIndex += 1

#     elif i == target :
#         stack.append(i)
#         result.append('+')

#         stack.pop()
#         result.append('-')

#         targetIndex += 1

#     else :
#         stack.append(i)


# 2. 모범 답안
n = int(input())

targetList = [int(input()) for _ in range(n)]  # 만들어야 하는 수열

stack = []
result = []
current = 1  # 스택에 넣을 다음 숫자

for target in targetList:
    # target에 도달할 때까지 숫자를 스택에 push
    while current <= target:
        stack.append(current)
        result.append('+')
        current += 1
    
    # 스택의 가장 위에 있는 숫자가 target과 같다면 pop
    if stack[-1] == target:
        stack.pop()
        result.append('-')
    else:
        # 스택의 가장 위에 있는 숫자가 target과 다르다면 불가능
        print("NO")
        break
else:
    # 모든 수열을 만들 수 있다면 연산 순서 출력
    for op in result:
        print(op)



