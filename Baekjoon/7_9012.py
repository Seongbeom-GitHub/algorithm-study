# 백준 9012번 "괄호"
# 문제 분류 : 알고리즘 기초 1/2 (자료구조)
# 풀이 : 성공
# 이해도 : 상
# 소요 시간 : 학습목적 (측정하지 않음)

# 1. 나의 풀이
t = int(input())
result = []

for _ in range(t) : 
    
    sample = list(input())
    stack = []

    for i in sample :
        if i == '(' :
            stack.append('(')
        elif i == ')' :
            if len(stack) != 0 and stack[-1] == '(' :   # 스택이 비어있지 않고, 스택의 위에 열린 괄호가 있다면
                stack.pop()
            else :
                stack.append(')')

    if len(stack) == 0 :
        result.append("YES")
    else :
        result.append("NO")


for i in result :
    print(i)

